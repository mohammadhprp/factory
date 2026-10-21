"""Regression checks for workflow boundaries, local evidence, and import integrity."""

import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]


def load_script(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class LocalWorkflowTests(unittest.TestCase):
    def test_local_entrypoints_have_no_provider_commands(self):
        names = (
            "to-spec", "to-tickets", "implement-spec", "setup-matt-pocock-skills",
            "code-review", "triage", "review", "walkthrough", "new-feature",
            "handoff", "before-and-after", "maintain-verification-skill",
            "write-product-spec", "write-tech-spec", "differential-review",
        )
        commands = re.compile(r"\b(?:gh|glab|jira|ntn)\s+(?:pr|mr|issue|api|pages|label)\b|git\s+(?:fetch|push)\b")
        for name in names:
            with self.subTest(skill=name):
                text = (ROOT / name / "SKILL.md").read_text()
                self.assertIsNone(commands.search(text))
        self.assertFalse((ROOT / "review/scripts/resolve_spec_context.py").exists())
        self.assertTrue((ROOT / "implement/scripts/resolve_external_spec_context.py").is_file())

    def test_adapters_cannot_trigger_as_independent_workflows(self):
        for name in ("gh", "glab", "jira-cli", "merge-request"):
            meta = yaml.safe_load((ROOT / name / "SKILL.md").read_text().split("---", 2)[1])
            with self.subTest(adapter=name):
                self.assertTrue(meta["disable-model-invocation"])
                self.assertIn("implement", meta["description"])

    def test_upload_requires_explicit_gate_and_destination(self):
        script = ROOT / "implement/scripts/evidence-upload/upload-and-copy.sh"
        result = subprocess.run(["bash", str(script)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn("External upload disabled", result.stderr)
        environment = dict(os.environ)
        environment.pop("IMAGE_ADAPTER", None)
        result = subprocess.run(["bash", str(script), "--upload"], capture_output=True, text=True, env=environment)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Set the explicitly selected upload adapter", result.stderr)
        self.assertFalse((ROOT / "before-and-after/scripts/upload-and-copy.sh").exists())

    def test_walkthrough_renders_offline_inside_project(self):
        script_dir = ROOT / "walkthrough/scripts"
        sys.path.insert(0, str(script_dir))
        try:
            renderer = load_script("local_walkthrough_renderer", script_dir / "render_walkthrough.py")
        finally:
            sys.path.remove(str(script_dir))
        with tempfile.TemporaryDirectory() as directory:
            self.assertEqual(renderer.default_output_dir(directory), Path(directory) / ".factory/review/walkthrough")
        schema = (ROOT / "walkthrough/references/schema.md").read_text()
        data = json.loads(re.search(r"```json\n(.*?)\n```", schema, re.S).group(1))
        html = renderer.render_html(data)
        self.assertIn("flowchart TD", html)
        self.assertIn("offline viewing", html)
        self.assertNotIn("<script", html)
        self.assertNotIn("cdn.jsdelivr.net", html)
        self.assertNotRegex(html, r"(?:src|href)=[\"']https?://")

    def test_recorded_adaptations_do_not_hide_later_edits(self):
        validator = load_script("local_collection_validator", ROOT / "scripts/validate_collection.py")
        with tempfile.TemporaryDirectory() as directory:
            copy = Path(directory) / "factory"
            shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns(".git", "__pycache__"))
            validator.ROOT = copy
            path = copy / "to-spec/SKILL.md"
            path.write_text(path.read_text() + "\nUnrecorded behavior change\n")
            with self.assertRaisesRegex(ValueError, "checksum mismatch"):
                validator.validate()


if __name__ == "__main__":
    unittest.main()
