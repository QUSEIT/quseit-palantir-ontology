from pathlib import Path
import subprocess
import sys


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "bootstrap_decision_spec.py"


def run_script(tmp_path, *extra_args):
    output = tmp_path / "spec.md"
    cmd = [
        sys.executable,
        str(SCRIPT_PATH),
        "--goal",
        "Prioritize incidents for production release",
        "--output",
        str(output),
        *extra_args,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return output, result


def test_creates_output_file(tmp_path):
    output, result = run_script(tmp_path)
    assert output.exists()
    assert str(output) in result.stdout


def test_writes_goal_and_default_context(tmp_path):
    output, _ = run_script(tmp_path)
    content = output.read_text(encoding="utf-8")
    assert "Prioritize incidents for production release" in content
    assert "- None supplied" in content


def test_writes_multiple_context_files(tmp_path):
    output, _ = run_script(
        tmp_path,
        "--context-file",
        "docs/runbook.md",
        "--context-file",
        "data/incidents.csv",
    )
    content = output.read_text(encoding="utf-8")
    assert "- docs/runbook.md" in content
    assert "- data/incidents.csv" in content
