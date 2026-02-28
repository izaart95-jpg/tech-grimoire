#!/usr/bin/env python3
"""Validate links in the tech-grimoire knowledge base.

Checks, in order:

  1. Relative file links   — every `](path/to/file.md)` target must exist
  2. Intra-doc anchors     — every `](#anchor)` must match a heading in that file
  3. README coverage       — every .md file must be linked from README.md
  4. External URLs         — optional (`--external`), HEAD/GET each unique URL

Usage:
    python3 tools/check-links.py              # offline checks only (fast)
    python3 tools/check-links.py --external   # also probe external URLs (slow)
    python3 tools/check-links.py --external --timeout 15

Exit code is 0 when everything passes, 1 otherwise.
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from collections import Counter
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# GitHub renders headings to anchors by lowercasing, dropping punctuation, and
# turning every space into a hyphen (each space, so "a — b" becomes "a--b").
SLUG_STRIP = re.compile(r"[^\w\- ]")
HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
FENCE = re.compile(r"^\s*```")
LINK = re.compile(r"\]\(([^)]+)\)")
ANCHOR_LINK = re.compile(r"\]\(#([^)]+)\)")
EXTERNAL = re.compile(r"https?://[^\s)\]<>\"']+")
PLACEHOLDER = re.compile(r"https?://(www\.)?(example\.(com|org)|user|you|username|repo|localhost)\b")


def slug(text: str) -> str:
    """GitHub's heading -> anchor conversion."""
    text = text.strip().lower()
    text = SLUG_STRIP.sub("", text)
    return text.replace(" ", "-")


def markdown_files() -> list[str]:
    out = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in {".git", "node_modules", "tools"}]
        for name in filenames:
            if name.endswith(".md"):
                out.append(os.path.join(dirpath, name))
    return sorted(out)


def read(path: str) -> list[str]:
    with open(path, encoding="utf-8") as fh:
        return fh.read().split("\n")


def headings(lines: list[str]) -> set[str]:
    """Anchor slugs for a document, with GitHub's duplicate-name suffixes."""
    slugs: set[str] = set()
    counts: Counter[str] = Counter()
    in_fence = False
    for line in lines:
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = HEADING.match(line)
        if not m:
            continue
        base = slug(m.group(2))
        n = counts[base]
        counts[base] += 1
        slugs.add(base if n == 0 else f"{base}-{n}")
    return slugs


def check_relative(files: list[str], lines_of: dict[str, list[str]]) -> list[str]:
    problems = []
    for path in files:
        rel = os.path.relpath(path, ROOT)
        for i, line in enumerate(lines_of[path], 1):
            for target in LINK.findall(line):
                if target.startswith(("http://", "https://", "#", "mailto:")):
                    continue
                target = target.split("#", 1)[0]
                if not target:
                    continue
                resolved = os.path.normpath(os.path.join(os.path.dirname(path), target))
                if not os.path.exists(resolved):
                    problems.append(f"{rel}:{i}  missing file: {target}")
    return problems


def check_anchors(files: list[str], lines_of: dict[str, list[str]]) -> list[str]:
    problems = []
    for path in files:
        rel = os.path.relpath(path, ROOT)
        valid = headings(lines_of[path])
        for i, line in enumerate(lines_of[path], 1):
            for anchor in ANCHOR_LINK.findall(line):
                if anchor.strip().lower() not in valid:
                    problems.append(f"{rel}:{i}  missing anchor: #{anchor}")
    return problems


def check_readme(files: list[str], lines_of: dict[str, list[str]]) -> list[str]:
    readme = os.path.join(ROOT, "README.md")
    if not os.path.exists(readme):
        return ["README.md is missing"]
    linked = set()
    for target in LINK.findall("\n".join(lines_of[readme])):
        if target.startswith(("http://", "https://", "#")):
            continue
        linked.add(os.path.normpath(os.path.join(ROOT, target.split("#", 1)[0])))
    problems = []
    for path in files:
        if path == readme:
            continue
        if path not in linked:
            problems.append(
                f"{os.path.relpath(path, ROOT)}  not linked from README.md"
            )
    return problems


def collect_external(files: list[str], lines_of: dict[str, list[str]]) -> list[str]:
    urls = set()
    for path in files:
        for url in EXTERNAL.findall("\n".join(lines_of[path])):
            urls.add(url.rstrip(".,;:)"))
    return sorted(urls)


def check_external(urls: list[str], timeout: int, workers: int) -> list[str]:
    problems = []

    def probe(url: str) -> str | None:
        try:
            proc = subprocess.run(
                [
                    "curl", "-s", "-o", "/dev/null", "-w", "%{http_code}",
                    "-L", "--max-time", str(timeout),
                    "-A", "Mozilla/5.0 (X11; Linux x86_64) tech-grimoire-linkcheck",
                    url,
                ],
                capture_output=True,
                text=True,
                timeout=timeout + 5,
            )
            code = proc.stdout.strip()
        except subprocess.TimeoutExpired:
            code = "timeout"
        if code in {"200", "204", "301", "302", "307", "308", "403", "429"}:
            return None
        return f"{code or 'error':>7}  {url}"

    with ThreadPoolExecutor(max_workers=workers) as pool:
        for result in pool.map(probe, urls):
            if result:
                problems.append(result)
    return problems


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--external", action="store_true", help="also probe external URLs")
    ap.add_argument("--timeout", type=int, default=12, help="per-URL timeout in seconds")
    ap.add_argument("--workers", type=int, default=12, help="parallel URL probes")
    args = ap.parse_args()

    files = markdown_files()
    lines_of = {p: read(p) for p in files}

    problems = []
    problems += check_relative(files, lines_of)
    problems += check_anchors(files, lines_of)
    problems += check_readme(files, lines_of)

    if args.external:
        urls = collect_external(files, lines_of)
        print(f"Probing {len(urls)} external URLs ...", file=sys.stderr)
        problems += check_external(urls, args.timeout, args.workers)

    if problems:
        print(f"\n{len(problems)} problem(s):\n", file=sys.stderr)
        for p in problems:
            print(f"  {p}", file=sys.stderr)
        return 1

    print(f"OK - {len(files)} markdown files, all links and anchors valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
