# Flux — /for-ai

Source: https://flux.kaptio.com/for-ai

[Flux](/)
For AI Tools

# Building with Flux + AI

Copy-paste guidance for any AI coding tool building prototypes, slides, or UI on top of
Flux. The goal: stop agents from leaking generic Tailwind defaults and keep generated
output on-brand. These are consumer-facing rules for your repo — not for
maintaining this site.

Machine-readable sources

Agent context lives at [/llms.txt](/llms.txt),
tokens at [/tokens/flux.css](/tokens/flux.css)
and [/tokens/flux.json](/tokens/flux.json).
The full do/don't list is on the [Don'ts](/donts) page.

## 1. Import the tokens first

Put this on the first line of your global stylesheet. It defines every
`--flux-*` custom property.

@import url("https://flux.kaptio.com/tokens/flux.css");
## 2. The rules

- Use only `--flux-*` tokens for color, spacing, radius, shadow, and type. If it isn't a token, it isn't Flux.
- Never use Tailwind default palette names (`gray-*`, `slate-*`, `blue-*`, `red-*`, …) as design decisions.
- No one-off hex / rgb values for brand UI. Never invent token names.
- Font is Lexend, weights 300 and 700 only (no 400/500/600). Mono is JetBrains Mono.
- Text is `--flux-black` (#212121) on light backgrounds. No colored heading text.
- `--flux-yellow-400` is for CTAs and key highlights only.
- Don't mix in another design system (Bootstrap, MUI, Spotlight). Flux is not Spotlight.
## 3. Canonical token names

Reference the names, not the hex values. Full list at
[Token Reference](/foundations/tokens).

/* Radius  */ --flux-radius-sm  --flux-radius-md  --flux-radius-lg  --flux-radius-xl  --flux-radius-2xl  --flux-radius-full
/* Shadow  */ --flux-shadow-sm  --flux-shadow-md  --flux-shadow-lg  --flux-shadow-xl
/* Spacing */ --flux-space-1 … --flux-space-24   (4px grid)
/* Type    */ --flux-text-xs … --flux-text-5xl
/* Weight  */ --flux-weight-light (300)  --flux-weight-bold (700)
/* Font    */ --flux-font-sans (Lexend)  --flux-font-mono (JetBrains Mono)
## 4. Drop-in Cursor rule

Save this as `.cursor/rules/flux.mdc` in your repo so Cursor applies Flux
rules automatically.

---
description: Kaptio Flux design system — use for all UI, prototypes, and slides
alwaysApply: true
---

# Flux by Kaptio

Flux is the single source of truth for all Kaptio UI. Canonical reference:
https://flux.kaptio.com (full context: https://flux.kaptio.com/llms.txt).

## Setup
- Import the tokens on line one of the global stylesheet:
@import url("https://flux.kaptio.com/tokens/flux.css");
- Raw token JSON: https://flux.kaptio.com/tokens/flux.json

## Rules
- Use ONLY --flux-* tokens for color, spacing, radius, shadow, and type.
- Never use Tailwind default palette names (gray-*, slate-*, blue-*, red-*, ...) as design decisions.
- No one-off hex / rgb values for brand UI. Never invent token names.
- Font: Lexend, weights 300 and 700 ONLY (no 400/500/600). Mono: JetBrains Mono.
- Body and heading text is --flux-black (#212121) on light backgrounds. No colored heading text.
- --flux-yellow-400 is for CTAs and key highlights only.
- Do not mix in another design system (Bootstrap, MUI, Spotlight). Flux is not Spotlight.

## Don't
- No single-edge colored borders / top accent bars on cards.
- No solid colored dots beside headings inside cards or panels.
- No arbitrary radii or spacing outside the Flux scales.
- No stacking of competing outlines, glows, and heavy shadows — follow the shadow scale.
## 5. AGENTS.md

For tools that read `AGENTS.md` (Codex, Claude Code, and others), drop an
`AGENTS.md` at your repo root with the same rules. A ready-made version lives in
the Flux repo root, and the canonical agent context is always at
[/llms.txt](/llms.txt).
