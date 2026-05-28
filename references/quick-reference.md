# Flux quick reference

Canonical site: https://flux.kaptio.com  
Token source (GitLab): `kaptio1/platform-and-services/edge/kaptio-flux` → `src/tokens/flux.json`

## Design principles

1. **Professional & approachable** — business sophistication with warmth.
2. **Clean & purposeful** — no decorative noise or gratuitous gradients.
3. **Data-driven** — dense information must be scannable and actionable.
4. **Modern** — intentional interactions; contemporary aesthetics.

## Typography

| Role | Size | Weight | Line height | Use |
|------|------|--------|-------------|-----|
| Display | 3rem | 700 | 1.1 | Hero headlines |
| H1 | 2.25rem | 700 | 1.2 | Page titles |
| H2 | 1.875rem | 700 | 1.25 | Section headers |
| H3 | 1.5rem | 700 | 1.3 | Subsection headers |
| H4 | 1.25rem | 600 | 1.4 | Card titles |
| H5 | 1.125rem | 600 | 1.4 | Small headings |
| Body Large | 1rem | 400 | 1.6 | Primary content |
| Body | 0.875rem | 300 | 1.6 | Secondary content |
| Small | 0.75rem | 300 | 1.5 | Captions, labels |
| Mono | 0.875rem | 400 | 1.6 | Code, tokens |

- **Fonts:** Lexend (`--flux-font-sans`) for UI; JetBrains Mono for code.
- **Body text on light backgrounds:** `#212121` only — not light grey or yellow for body copy.
- **Emphasis:** underline or Seagreen (`#034955` / `--flux-primary-600`), not rainbow heading colors.

## Brand colors (marketing palette)

| Name | HEX |
|------|-----|
| Kaptio Seagreen | `#034955` |
| Fandango Pink | `#DE37A4` |
| Bumble-Me Yellow | `#FFBC42` |
| Poison Green | `#2BA711` |
| Puffin Beak Orange | `#FF6F59` |
| Blue | `#4285FF` |
| Purple | `#6F59FF` |
| The Dark Side (text) | `#212121` |

## Interactive primary scale (teal)

Prefer CSS variables, not raw hex, in product UI:

| Token | HEX | Notes |
|-------|-----|-------|
| `--flux-primary-600` | `#034955` | Brand seagreen |
| `--flux-primary-400` | `#056F82` | Links, icons, interactive (AA on white) |
| `--flux-primary-300` | `#69A9B4` | |
| `--flux-primary-800` | `#032E36` | Dark surfaces |

## Semantic colors

| Role | HEX |
|------|-----|
| Success | `#10B981` |
| Error | `#C1121F` |
| Warning | `#F59E0B` |
| Info | `#056F82` |

## Product layer accents

Use only in the scoped product context — not globally:

| Product / layer | Accent | CSS variable |
|-----------------|--------|--------------|
| Core | `#056F82` | `--flux-layer-core` |
| Product Experience (Quest, Voyage, Circle) | `#F18525` | — |
| Edge | `#DE37A4` | — |
| Agents | `#8B5CF6` | — |

## Spacing (4px grid)

| Token | Value |
|-------|-------|
| `--flux-space-1` | 0.25rem (4px) |
| `--flux-space-2` | 0.5rem (8px) |
| `--flux-space-4` | 1rem (16px) — default gap |
| `--flux-space-6` | 1.5rem (24px) — card padding |
| `--flux-space-8` | 2rem (32px) — section gap |
| `--flux-space-12` | 3rem (48px) |
| `--flux-space-16` | 4rem (64px) — page section |

## Shadows & radius

- Shadows: `--flux-shadow-sm`, `--flux-shadow-md` (default cards), `--flux-shadow-lg`, `--flux-shadow-xl`
- Radius: `sm` 0.25rem, `md` 0.5rem, `lg` 0.75rem, `xl` 1rem, `2xl` 1.5rem, `full` 9999px

## Documented components

Inputs: Button, Checkbox, Date Picker, Input, Multi Select, Radio, Select, Switch, Textarea  
Display: Avatar, Badge, Code Block, Journey, Note, Table  
Feedback: Progress, Skeleton, Spinner  
Layout: Accordion, Card, Hero, Modal, Tabs, Tooltip  
Outcome patterns: Outcome Header, Flow Entry, Outcome Complete

## Patterns

- **Salesforce ↔ Edge transitions:** `references/patterns-edge-transitions.md` — entering/leaving focused outcomes across Salesforce and Edge.

## Hard don'ts (summary)

See `references/donts.md` for full list. Never:

- Invent colors, token names, or hex values outside `flux.json` / Colours page
- Add single-edge accent borders, decorative dots beside headings, or stacked heavy shadows
- Use marketing site layout as default product app shell
- Substitute typefaces or use emoji as primary icons
- Apply product accent colors globally
