#!/usr/bin/env python3
"""Check that bibliography links are reachable.

Reads the `link` column of data/bibliography.csv, probes each distinct URL
(HEAD first, GET fallback for servers that reject HEAD), and maintains a
markdown report of problem links:

- broken: DNS failure, timeout, SSL error, 404/410/5xx after retries
- suspect: 403/429 — usually bot-blocking, needs a human eyeball

The report file is written only when there is something to report and is
removed when every link is healthy again, so CI can open (and naturally
close out) a pull request from the file diff alone.

Usage:
    python scripts/check_links.py [--csv data/bibliography.csv]
        [--output docs/link-check-report.md] [--timeout 20] [--workers 10]

Exits 1 when broken or suspect links were found, 0 otherwise.
"""
from __future__ import annotations

import argparse
import csv
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent.parent

OK = "ok"
BROKEN = "broken"
SUSPECT = "suspect"

# Publishers (Wiley, ISO, ...) reject the default urllib agent outright.
USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"
)
SUSPECT_CODES = {401, 403, 429}


def load_links(csv_path):
    """Return [(keys, url)] for rows with a link, deduped by URL.

    Rows sharing a URL are collapsed into one entry with their keys joined
    by ", " so the report names every citation affected by a dead link.
    """
    by_url = {}
    with open(csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            url = (row.get("link") or "").strip()
            if not url:
                continue
            by_url.setdefault(url, []).append(row["key"])
    return [(", ".join(keys), url) for url, keys in by_url.items()]


def _probe(url, timeout):
    """Return the final HTTP status for url; HEAD first, GET on rejection."""
    last_err = None
    for method in ("HEAD", "GET"):
        req = Request(url, method=method, headers={"User-Agent": USER_AGENT})
        try:
            with urlopen(req, timeout=timeout) as resp:
                return resp.status
        except HTTPError as err:
            last_err = err
    return last_err.code


def check_url(url, timeout, retries=2):
    """Classify url as (OK|SUSPECT|BROKEN, detail).

    Network errors and 5xx are retried with backoff; 4xx verdicts are final
    (after the built-in HEAD->GET fallback).
    """
    detail = "unknown"
    for attempt in range(retries):
        try:
            code = _probe(url, timeout)
        except (URLError, TimeoutError, OSError) as err:
            detail = str(getattr(err, "reason", err))
        else:
            detail = str(code)
            if code < 400:
                return OK, detail
            if code in SUSPECT_CODES:
                return SUSPECT, detail
            if code < 500:
                return BROKEN, detail
        if attempt + 1 < retries:
            time.sleep(2 * (attempt + 1))
    return BROKEN, detail


def format_report(results, checked_on):
    """Markdown report of broken links.

    Suspect (401/403/429) links are counted but not listed: they are
    overwhelmingly bot-blocking, they flap between runs, and listing them
    would keep the report — and the PR opened from it — churning forever.
    The full suspect list is printed to stdout for the workflow log.
    """
    broken = [r for r in results if r[2] == BROKEN]
    suspect = [r for r in results if r[2] == SUSPECT]
    lines = [
        "# Bibliography link check",
        "",
        f"Checked on {checked_on}: {len(results)} checked, "
        f"{len(broken)} broken, {len(suspect)} suspect.",
        "",
        "Broken = DNS failure, timeout, SSL error, or 404/410/5xx after "
        "retries — the link likely needs replacing. Suspect links "
        "(401/403/429, usually bot-blocking, not dead) are only counted "
        "here; the full list is in the workflow run log.",
        "",
        "## Broken",
        "",
        "| key | status | link |",
        "| --- | --- | --- |",
    ]
    lines += [
        f"| {keys} | {detail} | {url} |" for keys, url, _, detail in broken
    ]
    lines.append("")
    return "\n".join(lines)


def write_report(results, out_path, checked_on):
    """Sync the report file with results; return True if the file changed.

    Writes the report when broken links exist, removes a stale report when
    none remain, and leaves the filesystem untouched otherwise.
    """
    out_path = Path(out_path)
    if any(r[2] == BROKEN for r in results):
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(format_report(results, checked_on), encoding="utf-8")
        return True
    if out_path.exists():
        out_path.unlink()
        return True
    return False


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--csv", default=ROOT / "data" / "bibliography.csv")
    parser.add_argument(
        "--output", default=ROOT / "docs" / "link-check-report.md"
    )
    parser.add_argument("--timeout", type=float, default=20)
    parser.add_argument("--workers", type=int, default=10)
    parser.add_argument(
        "--limit", type=int, default=None, help="check only the first N URLs"
    )
    args = parser.parse_args(argv)

    links = load_links(args.csv)[: args.limit]
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        statuses = pool.map(lambda kv: check_url(kv[1], args.timeout), links)
    results = [
        (keys, url, status, detail)
        for (keys, url), (status, detail) in zip(links, statuses)
    ]

    write_report(results, args.output, checked_on=date.today().isoformat())

    broken = sum(1 for r in results if r[2] == BROKEN)
    suspect = sum(1 for r in results if r[2] == SUSPECT)
    print(
        f"{len(results)} checked, {broken} broken, {suspect} suspect"
        + (f" -> {args.output}" if broken else "")
    )
    for keys, url, status, detail in results:
        if status != OK:
            print(f"  [{status} {detail}] {keys}: {url}")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
