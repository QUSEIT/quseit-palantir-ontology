"""
Palantir Ontology skill integration tests.

Tests the skill's ability to produce well-formed Decision System Specs
across the four working modes (A: Ontology, B: +Ingest, C: +GUI, D: E2E).

Each test case corresponds to one of the canonical use cases from
references/use-cases.md.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

SKILL_DIR = Path(__file__).resolve().parents[2]
SCRIPT_PATH = SKILL_DIR / "scripts" / "bootstrap_decision_spec.py"
REFERENCES_DIR = SKILL_DIR / "references"
ASSETS_DIR = SKILL_DIR / "assets"

# Required top-level sections in a Decision System Spec
REQUIRED_SECTIONS = [
    "## 1. Decision",
    "## 2. Objects",
    "## 3. Signals",
    "## 4. Actions",
    "## 5. Permissions and Review",
    "## 6. Workflow",
    "## 7. Failure Cases",
    "## 8. Evaluation Plan",
    "## 9. Missing Data",
    "## 10. MVP Build Plan",
]

# Required elements within a well-formed spec
REQUIRED_IN_SPEC = [
    "Business question:",
    "Key properties",
    "States",
    "Execution class",
    "Human approval points",
    "Escalation triggers",
    "Success metrics",
    "First delivery milestone",
]

# Execution class labels that must appear in the Actions section
EXEC_CLASSES = ["auto", "recommend", "review", "forbidden"]


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def spec_dir(tmp_path):
    """Temporary directory for generated spec files."""
    d = tmp_path / "specs"
    d.mkdir()
    return d


def run_bootstrap(goal: str, context_files: list[str] | None = None, cwd=None):
    """
    Run the bootstrap script and return the path to the generated file.
    Raises if the script exits non-zero.
    """
    output = tmp_path_factory.get_local_path() / "spec.md" if False else None

    if output is None:
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            output_path = Path(tmp) / "spec.md"
            cmd = [
                sys.executable,
                str(SCRIPT_PATH),
                "--goal", goal,
                "--output", str(output_path),
            ]
            for f in (context_files or []):
                cmd += ["--context-file", f]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return output_path, result
    # Make mypy happy
    return output, None


# ---------------------------------------------------------------------------
# Test 1: Script smoke test
# ---------------------------------------------------------------------------

def test_bootstrap_script_runs_without_error(tmp_path):
    """Bootstrap script exits 0 and writes a file."""
    output = tmp_path / "spec.md"
    result = subprocess.run(
        [sys.executable, str(SCRIPT_PATH),
         "--goal", "Test goal",
         "--output", str(output)],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"stderr: {result.stderr}"
    assert output.exists()


# ---------------------------------------------------------------------------
# Test 2: Required sections present
# ---------------------------------------------------------------------------

def _read_spec(path: Path) -> str:
    assert path.exists(), f"Spec not written: {path}"
    return path.read_text(encoding="utf-8")


def test_spec_has_all_required_sections(tmp_path):
    """Every generated spec includes the 10 required sections."""
    output = tmp_path / "spec.md"
    subprocess.run(
        [sys.executable, str(SCRIPT_PATH),
         "--goal", "Prioritize incidents for production release",
         "--output", str(output)],
        check=True,
    )
    content = _read_spec(output)
    missing = [s for s in REQUIRED_SECTIONS if s not in content]
    assert not missing, f"Missing sections: {missing}"


# ---------------------------------------------------------------------------
# Test 3: Required elements within sections
# ---------------------------------------------------------------------------

def test_spec_has_required_elements(tmp_path):
    """Spec contains all expected sub-elements (Business question, etc.)."""
    output = tmp_path / "spec.md"
    subprocess.run(
        [sys.executable, str(SCRIPT_PATH),
         "--goal", "Route customer support tickets to the right team",
         "--output", str(output)],
        check=True,
    )
    content = _read_spec(output)
    missing = [e for e in REQUIRED_IN_SPEC if e not in content]
    assert not missing, f"Missing elements: {missing}"


# ---------------------------------------------------------------------------
# Test 4: Context file list is rendered
# ---------------------------------------------------------------------------

def test_context_files_rendered_correctly(tmp_path):
    """Multiple --context-file args appear in the output."""
    output = tmp_path / "spec.md"
    subprocess.run(
        [sys.executable, str(SCRIPT_PATH),
         "--goal", "Claims review routing",
         "--context-file", "data/claims.csv",
         "--context-file", "docs/policy.md",
         "--output", str(output)],
        check=True,
    )
    content = _read_spec(output)
    assert "- data/claims.csv" in content
    assert "- docs/policy.md" in content
    assert "- None supplied" not in content


def test_no_context_shows_placeholder(tmp_path):
    """When no context files are supplied, '- None supplied' appears."""
    output = tmp_path / "spec.md"
    subprocess.run(
        [sys.executable, str(SCRIPT_PATH),
         "--goal", "Inventory allocation",
         "--output", str(output)],
        check=True,
    )
    content = _read_spec(output)
    assert "- None supplied" in content


# ---------------------------------------------------------------------------
# Test 5: Reference files are readable (not corrupted)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "ref_file",
    [
        "methodology.md",
        "ontology-patterns.md",
        "action-guardrails.md",
        "use-cases.md",
        "gui-patterns.md",
        "gui-principles.md",
        "industry-packs.md",
        "framework.md",
    ],
)
def test_reference_files_exist_and_nonempty(ref_file):
    """Every listed reference file exists and has content."""
    path = REFERENCES_DIR / ref_file
    assert path.exists(), f"Missing: {ref_file}"
    text = path.read_text(encoding="utf-8").strip()
    assert len(text) > 100, f"{ref_file} is too short ({len(text)} chars)"


# ---------------------------------------------------------------------------
# Test 6: Asset files are readable
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "asset_file",
    [
        "decision-system-spec-template.md",
        "palantir-html-mock-starter.html",
        "palantir-queue-detail-action.html",
        "palantir-plan-tracker.html",
    ],
)
def test_asset_files_exist_and_nonempty(asset_file):
    """Every asset file exists and has content."""
    path = ASSETS_DIR / asset_file
    assert path.exists(), f"Missing: {asset_file}"
    text = path.read_text(encoding="utf-8").strip()
    assert len(text) > 50, f"{asset_file} is too short ({len(text)} chars)"


# ---------------------------------------------------------------------------
# Test 7: HTML assets contain expected Palantir UI patterns
# ---------------------------------------------------------------------------

def test_html_mock_contains_queue_and_detail_elements():
    """palantir-html-mock-starter.html has queue + detail DOM structure."""
    path = ASSETS_DIR / "palantir-html-mock-starter.html"
    content = path.read_text(encoding="utf-8").lower()
    assert "queue" in content or "table" in content, "Missing queue/table element"
    assert "detail" in content or "panel" in content, "Missing detail/panel element"


def test_queue_detail_action_has_filter_and_action_elements():
    """palantir-queue-detail-action.html has filters and action buttons."""
    path = ASSETS_DIR / "palantir-queue-detail-action.html"
    content = path.read_text(encoding="utf-8").lower()
    assert "filter" in content, "Missing filter element"
    assert "action" in content or "btn" in content, "Missing action button element"


def test_plan_tracker_has_kpi_or_metric_elements():
    """palantir-plan-tracker.html has KPI/metric tracking elements."""
    path = ASSETS_DIR / "palantir-plan-tracker.html"
    content = path.read_text(encoding="utf-8").lower()
    assert "kpi" in content or "metric" in content or "plan" in content, \
        "Missing KPI/metric element"


# ---------------------------------------------------------------------------
# Test 8: SKILL.md frontmatter is valid
# ---------------------------------------------------------------------------

def test_skill_md_has_valid_frontmatter():
    """SKILL.md has required name and description fields."""
    skill_md = SKILL_DIR / "SKILL.md"
    content = skill_md.read_text(encoding="utf-8")
    assert content.startswith("---"), "Missing YAML frontmatter"
    frontmatter, _, _ = content[3:].partition("---")
    assert "name: palantir-ontology" in frontmatter, "Missing 'name' in frontmatter"
    assert "description:" in frontmatter, "Missing 'description' in frontmatter"


# ---------------------------------------------------------------------------
# Test 9: Bootstrap output is valid Markdown (rough check)
# ---------------------------------------------------------------------------

def test_bootstrap_output_is_markdown(tmp_path):
    """Output contains markdown heading markers, not raw HTML or JSON."""
    output = tmp_path / "spec.md"
    subprocess.run(
        [sys.executable, str(SCRIPT_PATH),
         "--goal", "Incident triage for release readiness",
         "--output", str(output)],
        check=True,
    )
    content = _read_spec(output)
    # Should have at least 5 markdown headings
    heading_count = content.count("## ")
    assert heading_count >= 5, f"Expected ≥5 headings, got {heading_count}"
    # Should not be empty JSON or HTML
    assert not content.strip().startswith("{")
    assert not content.strip().startswith("<!DOCTYPE")


# ---------------------------------------------------------------------------
# Test 10: Goal is preserved verbatim in output
# ---------------------------------------------------------------------------

def test_goal_preserved_in_output(tmp_path):
    """The --goal argument appears verbatim in the generated spec."""
    goal = "Which claims should be auto-approved vs held for review?"
    output = tmp_path / "spec.md"
    subprocess.run(
        [sys.executable, str(SCRIPT_PATH),
         "--goal", goal,
         "--output", str(output)],
        check=True,
    )
    content = _read_spec(output)
    assert goal in content, "Goal not preserved verbatim in output"


# ---------------------------------------------------------------------------
# Test 11: Multiple context files in mixed order
# ---------------------------------------------------------------------------

def test_multiple_context_files_preserve_order(tmp_path):
    """Context files appear in the output in the same order they were passed."""
    output = tmp_path / "spec.md"
    ctx = ["a.md", "b.md", "c.md"]
    subprocess.run(
        [sys.executable, str(SCRIPT_PATH),
         "--goal", "Test",
         "--context-file", ctx[0],
         "--context-file", ctx[1],
         "--context-file", ctx[2],
         "--output", str(output)],
        check=True,
    )
    content = _read_spec(output)
    i0 = content.find(ctx[0])
    i1 = content.find(ctx[1])
    i2 = content.find(ctx[2])
    assert i0 < i1 < i2, "Context file order not preserved"


# ---------------------------------------------------------------------------
# Test 12: Long goal text is handled
# ---------------------------------------------------------------------------

def test_long_goal_text_does_not_crash(tmp_path):
    """A very long goal string completes without error."""
    output = tmp_path / "spec.md"
    long_goal = "Design a decision system for " + "x" * 2000 + " related workflows"
    result = subprocess.run(
        [sys.executable, str(SCRIPT_PATH),
         "--goal", long_goal,
         "--output", str(output)],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"Crashed on long goal: {result.stderr}"
    assert _read_spec(output).__len__() > 2000  # goal text is in there
