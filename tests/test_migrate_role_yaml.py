import yaml

from migrate_role_yaml import migrate_lines

SRC = """\
competencies:
  # ---- People ----
  - theme: Onboarding & team formation
    capability: EM-13
    anchor: "Tuckman, Developmental Sequence in Small Groups (1965)"
    proficiency: {M1: P2, M2: P3, M3: P4, M4: P4, M5: P5, M6: P6}
"""


def test_migrates_proficiency_to_mappings():
    out = "".join(migrate_lines(SRC.splitlines(keepends=True)))
    assert "proficiency:" not in out
    data = yaml.safe_load(out)
    m = data["competencies"][0]["mappings"]
    assert m["M1"] == {"p": "P2", "sources": [], "why": ""}
    assert m["M6"] == {"p": "P6", "sources": [], "why": ""}
    assert "# ---- People ----" in out  # comments preserved


def test_idempotent_and_untouched_lines():
    lines = SRC.splitlines(keepends=True)
    once = migrate_lines(lines)
    twice = migrate_lines(once)
    assert once == twice
    assert "  - theme: Onboarding & team formation\n" in once
