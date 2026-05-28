#!/usr/bin/env python3
"""Fetch flux.kaptio.com pages and write markdown references for the Flux skill."""

from __future__ import annotations

import html as html_lib
import re
import sys
import time
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

BASE = "https://flux.kaptio.com"
USER_AGENT = "Kaptio-Flux-Skill-Scraper/1.0"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "references"

PATHS = [
    "/",
    "/brand",
    "/brand/story",
    "/brand/voice",
    "/brand/logo",
    "/foundations",
    "/foundations/colors",
    "/foundations/typography",
    "/foundations/spacing",
    "/foundations/shadows",
    "/foundations/tokens",
    "/foundations/iconography",
    "/products",
    "/products/core",
    "/products/quest",
    "/products/voyage",
    "/products/circle",
    "/products/edge",
    "/products/agents",
    "/components",
    "/components/button",
    "/components/checkbox",
    "/components/date-picker",
    "/components/input",
    "/components/multi-select",
    "/components/radio",
    "/components/select",
    "/components/switch",
    "/components/textarea",
    "/components/avatar",
    "/components/badge",
    "/components/code-block",
    "/components/journey",
    "/components/note",
    "/components/table",
    "/components/progress",
    "/components/skeleton",
    "/components/spinner",
    "/components/accordion",
    "/components/card",
    "/components/hero",
    "/components/modal",
    "/components/tabs",
    "/components/tooltip",
    "/components/outcome-header",
    "/components/flow-entry",
    "/components/outcome-complete",
    "/patterns",
    "/assets",
    "/changelog",
    "/donts",
]

VALID_PATH = re.compile(r"^/[a-z0-9][a-z0-9/-]*$")


class LinkExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        for key, value in attrs:
            if key == "href" and value and value.startswith("/"):
                path = value.split("#")[0].split("?")[0]
                if VALID_PATH.match(path):
                    self.links.add(path)


def fetch(url: str) -> tuple[str | None, int | None]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=45) as response:
            return response.read().decode("utf-8", errors="replace"), response.status
    except urllib.error.HTTPError as exc:
        return None, exc.code
    except urllib.error.URLError:
        return None, None


def strip_tags(fragment: str) -> str:
    fragment = re.sub(r"<[^>]+>", "", fragment)
    return html_lib.unescape(fragment).strip()


def extract_main_html(raw: str) -> str:
    match = re.search(r"<main[^>]*>(.*)</main>", raw, flags=re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1)
    match = re.search(r'<article[^>]*>(.*)</article>', raw, flags=re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1)
    return raw


def html_to_markdown(raw: str) -> str:
    raw = extract_main_html(raw)
    text = re.sub(r"<script[^>]*>.*?</script>", "", raw, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<style[^>]*>.*?</style>", "", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<noscript[^>]*>.*?</noscript>", "", text, flags=re.DOTALL | re.IGNORECASE)

    for level in range(1, 7):
        text = re.sub(
            rf"<h{level}[^>]*>(.*?)</h{level}>",
            lambda m, lv=level: "\n" + "#" * lv + " " + strip_tags(m.group(1)) + "\n",
            text,
            flags=re.DOTALL | re.IGNORECASE,
        )

    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"</p>", "\n\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<p[^>]*>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"<li[^>]*>", "\n- ", text, flags=re.IGNORECASE)
    text = re.sub(r"</li>", "", text, flags=re.IGNORECASE)
    text = re.sub(
        r'<a[^>]+href="([^"]*)"[^>]*>(.*?)</a>',
        lambda m: f"[{strip_tags(m.group(2))}]({m.group(1)})",
        text,
        flags=re.DOTALL | re.IGNORECASE,
    )
    text = re.sub(
        r"<code[^>]*>(.*?)</code>",
        lambda m: "`" + strip_tags(m.group(1)) + "`",
        text,
        flags=re.DOTALL | re.IGNORECASE,
    )
    text = re.sub(
        r"<pre[^>]*>(.*?)</pre>",
        lambda m: "\n```\n" + strip_tags(m.group(1)) + "\n```\n",
        text,
        flags=re.DOTALL | re.IGNORECASE,
    )

    text = strip_tags(text)
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            lines.append("")
            continue
        if stripped in {"-", "⌘K"}:
            continue
        if stripped.startswith("Flux") and "Foundations" in stripped and len(stripped) > 40:
            continue
        if re.match(r"^v\d+\.\d+ —", stripped):
            continue
        lines.append(stripped)
    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def path_to_slug(path: str) -> str:
    if path == "/":
        return "home"
    return path.strip("/").replace("/", "-")


def discover_extra_paths(paths: list[str]) -> list[str]:
    known = set(paths)
    extra: list[str] = []
    for path in list(paths):
        raw, status = fetch(BASE + path)
        if not raw or status != 200:
            continue
        parser = LinkExtractor()
        parser.feed(raw)
        for link in sorted(parser.links):
            if link not in known:
                known.add(link)
                extra.append(link)
        time.sleep(0.1)
    return paths + extra


def main() -> int:
    all_paths = discover_extra_paths(list(PATHS))
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    index_lines = [
        "# Flux reference index",
        "",
        f"Scraped from {BASE}. Regenerate: `python scripts/scrape_flux.py`",
        "",
        "## Start here",
        "",
        "- [Quick reference](quick-reference.md) — curated tokens, colors, typography, don'ts summary",
        "",
        "## Pages",
        "",
    ]
    ok = 0
    for path in sorted(set(all_paths)):
        url = BASE + path
        raw, status = fetch(url)
        if not raw or status != 200:
            print(f"SKIP {path} status={status}", file=sys.stderr)
            continue
        md = html_to_markdown(raw)
        slug = path_to_slug(path)
        title = "Home" if path == "/" else path
        body = f"# Flux — {title}\n\nSource: {url}\n\n{md}\n"
        (OUTPUT_DIR / f"{slug}.md").write_text(body, encoding="utf-8")
        index_lines.append(f"- [{title}]({slug}.md)")
        print(f"OK {path} ({len(md)} chars)", file=sys.stderr)
        ok += 1
        time.sleep(0.12)

    (OUTPUT_DIR / "index.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    print(f"Wrote {ok} pages to {OUTPUT_DIR}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
