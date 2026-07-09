import csv
import os

from render_catalog import load_sourcing, render_capabilities_md, read_csv

ROOT = os.path.join(os.path.dirname(__file__), "..")


def test_sourced_level_renders_why_and_citation():
    caps = read_csv("capabilities.csv")
    scale = read_csv("proficiency_scale.csv")
    domains = read_csv("domains.csv")
    bib, levels = load_sourcing()
    md = render_capabilities_md(caps, scale, domains, bib, levels)
    em13 = md.split('id="em-13"')[1].split('id="em-14"')[0]
    assert "30/60/90 onboarding with named buddies" in em13          # bar text unchanged
    assert "Watkins' standard line-manager transition toolkit" in em13  # why rendered
    assert "Tuckman, Developmental Sequence in Small Groups" in em13    # citation rendered


def test_unsourced_level_renders_without_why():
    # unit-level: a capability with no capability_levels rows renders bare profile lines
    caps = read_csv("capabilities.csv")
    scale = read_csv("proficiency_scale.csv")
    domains = read_csv("domains.csv")
    bib, _ = load_sourcing()
    md = render_capabilities_md(caps[:1], scale, domains, bib, {})  # empty sourcing table
    assert "Why this level" not in md


def test_catalog_fully_sourced():
    # R2 gate: every capability × P1-P6 carries a sourced why line
    caps = read_csv("capabilities.csv")
    scale = read_csv("proficiency_scale.csv")
    domains = read_csv("domains.csv")
    bib, levels = load_sourcing()
    md = render_capabilities_md(caps, scale, domains, bib, levels)
    assert md.count("Why this level") == len(caps) * 6
