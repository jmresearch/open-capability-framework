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
    # R3 complete (all role records retrofitted): no sourcing-gap REPORT lines remain.
    assert "REPORT" not in res.stdout
    # R2 complete: the catalog itself must have zero unsourced levels
    assert "unsourced capability levels" not in res.stdout


def test_strict_mode_fails_on_gaps():
    res = run("--strict")
    # R3 complete: every role record is fully sourced, so strict mode now also passes.
    assert res.returncode == 0, res.stdout
    assert "sourcing issue" not in res.stdout


def test_em13_is_not_reported_unsourced():
    from check_consistency import sourcing_issues
    assert not any("EM-13" in issue for issue in sourcing_issues())


def test_evidence_warnings_handles_none_evidence():
    import shutil
    import yaml
    d = os.path.join(ROOT, "roles", "zz-fixture-none-evidence")
    os.makedirs(d, exist_ok=True)
    role = {
        "role": "Fixture None Evidence", "slug": "zz-fixture-none-evidence", "variant": "manager",
        "minted": "2026-07-09", "derived": True,
        "levels": [{"code": "M1", "title": "Manager", "scope": "one team", "focus": "one team"}],
        "competencies": [{
            "theme": "Test theme", "capability": "EM-13",
            "key_area": "People", "key_attribute": "Team Composition",
            "mappings": {"M1": {"p": "P2", "sources": [], "why": "test"}},
            "evidence": {"M1": None},  # `M1:` with no value in yaml
        }],
    }
    try:
        with open(os.path.join(d, "role.yaml"), "w") as f:
            yaml.safe_dump(role, f, sort_keys=False)
        from check_consistency import evidence_warnings
        evidence_warnings()  # must not raise AttributeError
    finally:
        shutil.rmtree(d)
