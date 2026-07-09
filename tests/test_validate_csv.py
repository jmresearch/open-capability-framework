import csv
import os
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCRIPT = os.path.join(ROOT, "skills", "career-ladder", "scripts", "validate_csv.py")


def _write_ladder(path, cell):
    """Minimal single-skill-row ladder CSV with `cell` as the sole M1 value."""
    rows = [
        ["type", "key_area", "key_attribute", "theme", "M1"],
        ["meta_name", "Test Ladder", "", "", ""],
        ["level_title", "", "", "", "Manager"],
        ["skill", "People", "Team Composition", "Test Theme", cell],
    ]
    with open(path, "w", encoding="utf-8", newline="") as f:
        csv.writer(f).writerows(rows)


def _validate(path, *flags):
    return subprocess.run(
        [sys.executable, SCRIPT, path, "--allow-single-theme", *flags],
        capture_output=True, text=True)


def test_assembled_cell_bar_only_passes_manager(tmp_path):
    csv_path = tmp_path / "ladder.csv"
    _write_ladder(
        str(csv_path),
        "Depth: Documents current roles, handoffs, and reporting lines under direction. Scope: one team.")
    res = _validate(str(csv_path), "--manager")
    assert res.returncode == 0, res.stdout


def test_assembled_cell_position_locked_evidence_fails_manager(tmp_path):
    csv_path = tmp_path / "ladder.csv"
    _write_ladder(
        str(csv_path),
        "Depth: Documents current roles, handoffs, and reporting lines under direction. "
        "Evidenced by: owns the reporting line for the team. Scope: one team.")
    res = _validate(str(csv_path), "--manager")
    assert res.returncode == 1
    assert "reporting line" in res.stdout


def test_legacy_authored_cell_position_locked_fails_manager(tmp_path):
    csv_path = tmp_path / "ladder.csv"
    _write_ladder(
        str(csv_path),
        "Owns headcount planning and manages managers across three teams.")
    res = _validate(str(csv_path), "--manager")
    assert res.returncode == 1
    assert "manages managers" in res.stdout
