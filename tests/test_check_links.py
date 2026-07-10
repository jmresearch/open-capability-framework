import urllib.error
from unittest import mock

import pytest

from check_links import (
    BROKEN,
    OK,
    SUSPECT,
    check_url,
    format_report,
    load_links,
    write_report,
)


def _write_bib(path, rows):
    lines = ["key,type,citation,link,notes"]
    lines.extend(rows)
    path.write_text("\n".join(lines) + "\n")


def _http_error(url, code):
    return urllib.error.HTTPError(url, code, "boom", hdrs=None, fp=None)


def test_load_links_skips_empty_and_dedupes_urls(tmp_path):
    bib = tmp_path / "bibliography.csv"
    _write_bib(
        bib,
        [
            'a1,theory,"Author, Title (2020)",https://example.com/x,notes',
            'a2,theory,"Author, Other (2021)",,no link here',
            'a3,standard,"Body, Std (2019)",https://example.com/x,same url again',
            'a4,study,"Author, Study (2022)",https://example.com/y,distinct',
        ],
    )
    links = load_links(bib)
    assert links == [
        ("a1, a3", "https://example.com/x"),
        ("a4", "https://example.com/y"),
    ]


def test_check_url_ok_on_head_200():
    resp = mock.Mock(status=200)
    resp.__enter__ = lambda s: s
    resp.__exit__ = lambda s, *a: False
    with mock.patch("check_links.urlopen", return_value=resp) as opened:
        status, detail = check_url("https://example.com/x", timeout=5)
    assert status == OK
    assert detail == "200"
    assert opened.call_count == 1


def test_check_url_falls_back_to_get_when_head_rejected():
    resp = mock.Mock(status=200)
    resp.__enter__ = lambda s: s
    resp.__exit__ = lambda s, *a: False
    calls = []

    def fake_urlopen(req, timeout):
        calls.append(req.get_method())
        if req.get_method() == "HEAD":
            raise _http_error(req.full_url, 405)
        return resp

    with mock.patch("check_links.urlopen", side_effect=fake_urlopen):
        status, detail = check_url("https://example.com/x", timeout=5)
    assert status == OK
    assert calls == ["HEAD", "GET"]


def test_check_url_404_is_broken():
    with mock.patch(
        "check_links.urlopen", side_effect=lambda req, timeout: (_ for _ in ()).throw(_http_error(req.full_url, 404))
    ):
        status, detail = check_url("https://example.com/gone", timeout=5)
    assert status == BROKEN
    assert detail == "404"


def test_check_url_403_is_suspect_not_broken():
    with mock.patch(
        "check_links.urlopen", side_effect=lambda req, timeout: (_ for _ in ()).throw(_http_error(req.full_url, 403))
    ):
        status, detail = check_url("https://example.com/blocked", timeout=5)
    assert status == SUSPECT
    assert detail == "403"


def test_check_url_network_error_broken_after_retries():
    err = urllib.error.URLError("name or service not known")
    with mock.patch("check_links.urlopen", side_effect=err) as opened, mock.patch(
        "check_links.time.sleep"
    ):
        status, detail = check_url("https://no-such-host.example", timeout=5, retries=2)
    assert status == BROKEN
    assert "name or service not known" in detail
    # 2 attempts; GET fallback only applies to HTTP rejections, not network errors
    assert opened.call_count == 2


def test_format_report_lists_broken_but_not_suspect_urls():
    # Suspect links are counted but never listed: bot-blocking 403/429s
    # flap between runs, and listing them would churn the report (and the
    # PR opened from it) forever. The full suspect list goes to stdout.
    results = [
        ("a1", "https://example.com/gone", BROKEN, "404"),
        ("a2", "https://example.com/blocked", SUSPECT, "403"),
        ("a3", "https://example.com/fine", OK, "200"),
    ]
    md = format_report(results, checked_on="2026-07-10")
    assert "https://example.com/gone" in md
    assert "404" in md
    assert "https://example.com/blocked" not in md
    assert "https://example.com/fine" not in md
    assert "2026-07-10" in md
    assert "1 broken" in md
    assert "1 suspect" in md
    assert "3 checked" in md


def test_write_report_creates_file_when_broken(tmp_path):
    out = tmp_path / "report.md"
    results = [("a1", "https://example.com/gone", BROKEN, "404")]
    changed = write_report(results, out, checked_on="2026-07-10")
    assert changed
    assert "example.com/gone" in out.read_text()


def test_write_report_suspect_only_writes_nothing(tmp_path):
    out = tmp_path / "report.md"
    results = [("a1", "https://example.com/blocked", SUSPECT, "403")]
    changed = write_report(results, out, checked_on="2026-07-10")
    assert not changed
    assert not out.exists()


def test_write_report_removes_stale_file_when_no_broken(tmp_path):
    out = tmp_path / "report.md"
    out.write_text("old report")
    results = [("a1", "https://example.com/blocked", SUSPECT, "403")]
    changed = write_report(results, out, checked_on="2026-07-10")
    assert changed
    assert not out.exists()


def test_write_report_noop_when_all_ok_and_no_file(tmp_path):
    out = tmp_path / "report.md"
    results = [("a1", "https://example.com/fine", OK, "200")]
    changed = write_report(results, out, checked_on="2026-07-10")
    assert not changed
    assert not out.exists()
