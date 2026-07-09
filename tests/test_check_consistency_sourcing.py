import os
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCRIPT = os.path.join(ROOT, "scripts", "check_consistency.py")


def run(*flags):
    return subprocess.run([sys.executable, SCRIPT, *flags], capture_output=True, text=True)


def test_default_mode_reports_gaps_but_passes():
    res = run()
    assert res.returncode == 0, res.stdout
    assert "REPORT" in res.stdout            # ~2,724 unsourced catalog levels exist
    assert "unsourced capability levels" in res.stdout


def test_strict_mode_fails_on_gaps():
    res = run("--strict")
    assert res.returncode == 1
    assert "unsourced capability levels" in res.stdout


def test_em13_is_not_reported_unsourced():
    from check_consistency import sourcing_issues
    assert not any("EM-13" in issue for issue in sourcing_issues())
