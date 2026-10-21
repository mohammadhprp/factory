#!/usr/bin/env python3
"""Validate collection metadata and the integrity of pinned upstream imports."""

import ast
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote

import yaml


ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def contained_file(relative):
    path = ROOT / relative
    if path.is_symlink() or not path.resolve().is_relative_to(ROOT):
        raise ValueError(f"Unsafe import path: {relative}")
    if not path.is_file():
        raise ValueError(f"Missing file: {relative}")
    return path


def validate():
    errors = []
    manifest = json.loads((ROOT / "upstream-skills.json").read_text())
    if manifest.get("version") != 1:
        raise ValueError("Unsupported upstream manifest version")
    names = set()
    for skill in sorted(ROOT.glob("*/SKILL.md")):
        content = skill.read_text()
        match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", content, re.S)
        if not match:
            errors.append(f"{skill.parent.name}: missing frontmatter")
            continue
        metadata = yaml.safe_load(match.group(1))
        if not isinstance(metadata, dict):
            errors.append(f"{skill.parent.name}: metadata must be a mapping")
            continue
        name = metadata.get("name")
        if name != skill.parent.name or name in names:
            errors.append(f"{skill.parent.name}: duplicate or mismatched name {name!r}")
        names.add(name)
        if not isinstance(metadata.get("description"), str) or not metadata["description"].strip():
            errors.append(f"{skill.parent.name}: missing description")
    imported = set()
    files_checked = 0
    for entry in manifest["imports"]:
        name = entry["name"]
        if name not in names or name in imported:
            errors.append(f"{name}: missing or duplicate import")
        imported.add(name)
        if not re.fullmatch(r"[0-9a-f]{40}", entry["commit"]):
            errors.append(f"{name}: source must be pinned to a commit")
        expected_files = set(entry["files"])
        expected_files.add(Path(entry["license_path"]).relative_to(name).as_posix())
        actual_files = {
            p.relative_to(ROOT / name).as_posix()
            for p in (ROOT / name).rglob("*")
            if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc"
        }
        if expected_files != actual_files:
            errors.append(f"{name}: untracked import files {sorted(expected_files ^ actual_files)}")
        for relative, expected in entry["files"].items():
            path = contained_file(f"{name}/{relative}")
            if digest(path) != expected:
                errors.append(f"{name}/{relative}: upstream checksum mismatch")
            if path.suffix == ".py":
                ast.parse(path.read_text(), filename=str(path))
            if path.suffix == ".sh":
                subprocess.run(["bash", "-n", str(path)], check=True)
            files_checked += 1
        license_file = contained_file(entry["license_path"])
        if digest(license_file) != entry["license_sha256"]:
            errors.append(f"{name}: license checksum mismatch")
        skill = ROOT / name / "SKILL.md"
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", skill.read_text()):
            target = unquote(target.split("#", 1)[0])
            if not target or re.match(r"[a-zA-Z][\w+.-]*:|/|<", target):
                continue
            if not (skill.parent / target).exists():
                errors.append(f"{name}: missing entry-point link {target}")
    lock = json.loads((ROOT / "skills-lock.json").read_text())
    for name in lock["skills"]:
        if name not in names:
            errors.append(f"skills-lock.json references missing skill {name}")
    if errors:
        raise ValueError("\n".join(errors))
    print(f"Validated {len(names)} skills, {len(imported)} pinned imports, {files_checked} upstream files")


if __name__ == "__main__":
    try:
        validate()
    except (ValueError, OSError, SyntaxError, subprocess.CalledProcessError, yaml.YAMLError) as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
