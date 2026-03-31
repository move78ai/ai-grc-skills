#!/usr/bin/env python3
"""
ai_grc_repo_audit.py

Lightweight local audit for the ai-grc-skills repository.

Checks:
- required root files
- required skill files (README.md, SKILL.md, agents/openai.yaml)
- README section structure
- scaffold residue / weak phrases
- basic markdown link validation for relative links
- YAML validity and required metadata keys
- instructions_file existence
- optional SKILL.md style markers

Usage:
    python ai_grc_repo_audit.py . --write-report
    python ai_grc_repo_audit.py D:\\Github\\ai-grc-skills --write-report --fail-on-warnings
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

try:
    import yaml
except Exception:
    print("ERROR: PyYAML is required. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

ROOT_REQUIRED = [
    "README.md",
    "SKILLS-CATALOG.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
]

DOCS_REQUIRED = [
    "docs/repo-map.md",
    "docs/how-to-use-the-library.md",
    "docs/skill-installation.md",
    "docs/release-policy.md",
    "docs/naming-conventions.md",
    "docs/release-assets.md",
]

README_REQUIRED_HEADINGS = [
    "What this skill does",
    "Who it is for",
    "Use this skill when",
    "Typical inputs",
    "Typical outputs",
    "How it works",
    "Related skills",
    "Notes / source boundaries",
]

BANNED_PATTERNS = [
    r"\bTODO\b",
    r"\bTBD\b",
    r"\bFIXME\b",
    r"use when chatgpt needs",
    r"normalized repository copy",
]

MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.*)\s*$")


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def add_issue(store: Dict[str, List[dict]], severity: str, path: str, message: str) -> None:
    store[severity].append({"path": path, "message": message})


def is_skill_dir(path: Path) -> bool:
    return path.is_dir() and (path / "SKILL.md").exists()


def find_skill_dirs(repo_root: Path) -> List[Path]:
    skill_dirs = []
    skills_root = repo_root / "skills"
    umbrella_root = repo_root / "umbrella"
    if skills_root.exists():
        for p in skills_root.rglob("*"):
            if is_skill_dir(p):
                skill_dirs.append(p)
    if umbrella_root.exists():
        for p in umbrella_root.rglob("*"):
            if is_skill_dir(p):
                skill_dirs.append(p)
    return sorted(set(skill_dirs))


def validate_root(repo_root: Path, results: Dict[str, List[dict]]) -> None:
    for rel in ROOT_REQUIRED + DOCS_REQUIRED:
        p = repo_root / rel
        if not p.exists():
            add_issue(results, "errors", rel, "Required root/doc file is missing.")


def extract_headings(md: str) -> List[str]:
    headings = []
    for line in md.splitlines():
        m = HEADING_RE.match(line)
        if m:
            headings.append(m.group(1).strip())
    return headings


def validate_markdown_links(md_path: Path, text: str, results: Dict[str, List[dict]]) -> None:
    for _, target in MARKDOWN_LINK_RE.findall(text):
        target = target.strip()
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target_path = target.split("#", 1)[0].split("?", 1)[0]
        if not target_path:
            continue
        resolved = (md_path.parent / target_path).resolve()
        if not resolved.exists():
            add_issue(results, "warnings", str(md_path), f"Broken relative markdown link: {target}")


def audit_readme(skill_dir: Path, results: Dict[str, List[dict]]) -> None:
    readme = skill_dir / "README.md"
    if not readme.exists():
        add_issue(results, "errors", str(readme), "README.md is missing.")
        return
    text = load_text(readme)
    headings = extract_headings(text)
    for required in README_REQUIRED_HEADINGS:
        if required not in headings:
            add_issue(results, "errors", str(readme), f'Missing README section heading: "{required}".')
    first_nonempty = next((ln.strip() for ln in text.splitlines() if ln.strip()), "")
    if first_nonempty and not first_nonempty.startswith("#"):
        add_issue(results, "warnings", str(readme), "README does not start with a markdown title heading.")
    if text.lstrip().startswith('"'):
        add_issue(results, "warnings", str(readme), "README appears to start with a stray leading quote (possible clipped opener).")
    if re.search(r'^\s*#\s+.+\n+\s*"use this skill when', text, flags=re.I | re.M):
        add_issue(results, "warnings", str(readme), "README opener still contains old clipped scaffold phrasing.")
    for pat in BANNED_PATTERNS:
        if re.search(pat, text, flags=re.I):
            add_issue(results, "errors", str(readme), f'Found banned/scaffold residue pattern: "{pat}".')
    validate_markdown_links(readme, text, results)


def audit_skill_md(skill_dir: Path, results: Dict[str, List[dict]]) -> None:
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        add_issue(results, "errors", str(skill_md), "SKILL.md is missing.")
        return
    text = load_text(skill_md)
    if not text.startswith("---"):
        add_issue(results, "errors", str(skill_md), "SKILL.md is missing YAML frontmatter.")
        return
    parts = text.split("---", 2)
    if len(parts) < 3:
        add_issue(results, "errors", str(skill_md), "SKILL.md frontmatter is malformed.")
        return
    frontmatter = parts[1]
    body = parts[2]
    try:
        meta = yaml.safe_load(frontmatter) or {}
    except Exception as e:
        add_issue(results, "errors", str(skill_md), f"YAML frontmatter invalid: {e}")
        return
    allowed_keys = {"name", "description"}
    extra_keys = set(meta.keys()) - allowed_keys
    missing_keys = [k for k in ("name", "description") if not meta.get(k)]
    if missing_keys:
        add_issue(results, "errors", str(skill_md), f"Missing frontmatter keys: {', '.join(missing_keys)}")
    if extra_keys:
        add_issue(results, "warnings", str(skill_md), f"Unexpected frontmatter keys: {', '.join(sorted(extra_keys))}")
    if meta.get("name") and meta["name"] != str(meta["name"]).lower():
        add_issue(results, "warnings", str(skill_md), "Frontmatter name should be lowercase.")

    desc = str(meta.get("description", "")).strip()
    if not desc:
        add_issue(results, "errors", str(skill_md), "Missing frontmatter description.")
    elif re.search(r"chatgpt needs|todo|tbd|fixme", desc, flags=re.I):
        add_issue(results, "warnings", str(skill_md), "Frontmatter description contains weak or scaffold phrasing.")

    if "Default audience" not in body:
        add_issue(results, "warnings", str(skill_md), "Missing 'Default audience' block.")
    if "Default style" not in body:
        add_issue(results, "warnings", str(skill_md), "Missing 'Default style' block.")
    for pat in BANNED_PATTERNS:
        if re.search(pat, body, flags=re.I):
            add_issue(results, "errors", str(skill_md), f'Found banned/scaffold residue pattern: "{pat}".')


def audit_yaml(skill_dir: Path, results: Dict[str, List[dict]]) -> None:
    yml = skill_dir / "agents" / "openai.yaml"
    if not yml.exists():
        add_issue(results, "errors", str(yml), "agents/openai.yaml is missing.")
        return
    try:
        data = yaml.safe_load(load_text(yml)) or {}
    except Exception as e:
        add_issue(results, "errors", str(yml), f"YAML invalid: {e}")
        return
    required_top = ["version", "name", "description", "instructions_file", "interface"]
    for key in required_top:
        if key not in data:
            add_issue(results, "errors", str(yml), f'Missing required YAML key: "{key}".')
    if isinstance(data.get("interface"), dict):
        if "display_name" not in data["interface"]:
            add_issue(results, "errors", str(yml), 'Missing required YAML key: "interface.display_name".')
    else:
        add_issue(results, "errors", str(yml), 'Key "interface" must be a mapping.')

    instructions_file = data.get("instructions_file")
    if instructions_file:
        candidates = [
            (yml.parent / instructions_file).resolve(),         # relative to agents/openai.yaml
            (yml.parent.parent / instructions_file).resolve(),  # fallback relative to skill root
        ]
        if not any(p.exists() for p in candidates):
            add_issue(results, "errors", str(yml), f'instructions_file target not found: "{instructions_file}".')

    desc = str(data.get("description", ""))
    if re.search(r"chatgpt needs", desc, flags=re.I):
        add_issue(results, "warnings", str(yml), 'Description still contains "chatgpt needs" phrasing.')


def audit_repo(repo_root: Path) -> Dict[str, object]:
    results: Dict[str, List[dict]] = {"errors": [], "warnings": [], "info": []}
    validate_root(repo_root, results)
    skill_dirs = find_skill_dirs(repo_root)
    if not skill_dirs:
        add_issue(results, "errors", str(repo_root), "No skill directories found under skills/ or umbrella/.")
    for skill_dir in skill_dirs:
        audit_readme(skill_dir, results)
        audit_skill_md(skill_dir, results)
        audit_yaml(skill_dir, results)
    return {
        "repo_root": str(repo_root.resolve()),
        "skill_dir_count": len(skill_dirs),
        "error_count": len(results["errors"]),
        "warning_count": len(results["warnings"]),
        "results": results,
    }


def write_report(repo_root: Path, summary: Dict[str, object]) -> Tuple[Path, Path]:
    json_path = repo_root / "audit_results.json"
    md_path = repo_root / "audit_report.md"
    json_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    lines = [
        "# Repository Audit Report",
        "",
        f"- Repo root: `{summary['repo_root']}`",
        f"- Skill directories found: **{summary['skill_dir_count']}**",
        f"- Errors: **{summary['error_count']}**",
        f"- Warnings: **{summary['warning_count']}**",
        "",
    ]
    for severity in ("errors", "warnings"):
        items = summary["results"][severity]
        lines.append(f"## {severity.title()}")
        lines.append("")
        if not items:
            lines.append("_None_")
            lines.append("")
            continue
        current_path = None
        for item in items:
            if item["path"] != current_path:
                current_path = item["path"]
                lines.append(f"### `{current_path}`")
            lines.append(f"- {item['message']}")
        lines.append("")
    md_path.write_text("\n".join(lines), encoding="utf-8")
    return md_path, json_path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo_root", nargs="?", default=".", help="Path to repo root")
    parser.add_argument("--write-report", action="store_true", help="Write audit_report.md and audit_results.json")
    parser.add_argument("--fail-on-warnings", action="store_true", help="Exit 1 if warnings exist")
    args = parser.parse_args()
    repo_root = Path(args.repo_root).resolve()
    if not repo_root.exists():
        print(f"ERROR: Repo root does not exist: {repo_root}", file=sys.stderr)
        return 2
    summary = audit_repo(repo_root)
    print(f"Repo root       : {summary['repo_root']}")
    print(f"Skill dirs      : {summary['skill_dir_count']}")
    print(f"Errors          : {summary['error_count']}")
    print(f"Warnings        : {summary['warning_count']}")
    if args.write_report:
        md_path, json_path = write_report(repo_root, summary)
        print(f"Markdown report : {md_path}")
        print(f"JSON report     : {json_path}")
    if summary["error_count"] > 0:
        return 1
    if args.fail_on_warnings and summary["warning_count"] > 0:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
