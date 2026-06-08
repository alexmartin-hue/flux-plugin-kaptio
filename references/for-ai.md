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

@import url("https://flux.kaptio.com/tokens/flux.css");               Tailwind v4 projects should also import the enforcement layer
after `@import "tailwindcss";`. It resets Tailwind's built-in
color palette and remaps the common names onto Flux, so generic defaults mechanically
degrade to on-brand: `bg-gray-300` → Flux grey, `bg-blue-500` → Flux
primary teal, `rounded-lg` → Flux radius, `text-xl` → Flux type scale.
Non-Tailwind projects don't need it — use `flux.css` alone.

@import "tailwindcss";
@import url("https://flux.kaptio.com/tokens/flux.css");
@import url("https://flux.kaptio.com/tokens/flux-tailwind.css"); /* must come last */
## 2. The rules

- Use only `--flux-*` tokens for color, spacing, radius, shadow, and type. If it isn't a token, it isn't Flux.
- Never use Tailwind default palette names (`gray-*`, `slate-*`, `blue-*`, `red-*`, …) as design decisions.
- No one-off hex / rgb values for brand UI. Never invent token names.
- Font is Lexend, weights 300 and 700 only — the only weights loaded (`wght@300;700`). Body / default text is Light (300); headings are Bold (700). 400 (Regular) and 500 (Medium) are not loaded — never use them (nor 600). Mono is JetBrains Mono.
- Root font-size is fluid, not a fixed 16px — every rem-based size (e.g. `text-sm` = `0.875rem`) scales from a 16–19px root, so it renders larger on wide screens. Reproduce the clamp or your rem text comes out too small.
- Text is `--flux-black` (#212121) on light backgrounds. No colored heading text.
- `--flux-yellow-400` is for CTAs and key highlights only.
- Don't mix in another design system (Bootstrap, MUI, Spotlight). Flux is not Spotlight.   html {
font-size: clamp(16px, 0.875rem + 0.4vw, 19px); /* fluid root — rem scales 16→19px */
font-weight: 300;                                /* Lexend Light is the body default */
}
h1, h2, h3, h4, h5, h6 { font-weight: 700; }       /* Lexend Bold */
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

## 6. Tables

Flux tables are quiet: a standard surface, horizontal row dividers only (no full gridlines),
and the [Badge](/components/badge)
component for status. See [Table](/components/table)
for the live reference. The cell classes:

/* Header cell — left-aligned; numeric columns add text-right */
text-xs font-bold uppercase tracking-wider
text-[var(--flux-grey-300)] border-b border-[var(--flux-grey-100)]

/* Body cell — row divider is a bottom border only */
py-3 border-b border-[var(--flux-grey-100)] text-[var(--flux-black)]

/* Numeric / price / quantity — right-aligned, figures line up */
text-right [font-variant-numeric:tabular-nums]   /* header right too */
- Wrap the table in a Flux surface — `bg-[var(--flux-surface)]`, `border-[var(--flux-grey-100)]`, rounded.
- Last row: drop the bottom divider. Reference/code columns use Lexend Light (300).
- Status uses Badge semantics: confirmed/completed = green, pending/action required/on request = amber, awaiting supplier = blue, cancelled/rejected/expired = red.
- Don't add heavy gridlines, per-cell or vertical borders, or invent per-status colors — dividers are horizontal-only via `--flux-grey-100`.
## 7. Forms & inputs

Inputs are the #1 place agents leak generic Tailwind. The focus state is
always Flux primary teal, never `focus:ring-blue-*`, and a form
keeps one field height and one radius throughout. The canonical field — shared by
[Input](/components/input),
[Textarea](/components/textarea), and the
[Select](/components/select) trigger:

/* Text field / select trigger / textarea */
w-full px-3 py-2 rounded border border-[var(--flux-grey-200)]
bg-[var(--flux-surface)] text-sm text-[var(--flux-black)]
focus:border-[var(--flux-primary-400)] focus:ring-1 focus:ring-[var(--flux-primary-300)]
outline-none transition-colors
/* Textarea adds */ min-h-[100px] resize-y
/* Label    */ block text-sm font-medium text-[var(--flux-black)] mb-1
/* Disabled */ opacity-50 cursor-not-allowed bg-[var(--flux-grey-50)]
/* Error    */ border-[var(--flux-error)] focus:ring-[var(--flux-error)]   /* helper text: text-xs text-[var(--flux-error)] */
- Focus is Flux primary — border `--flux-primary-400` + ring `--flux-primary-300`. Placeholder is `--flux-grey-300`; never use it as the only label.
- [Select](/components/select) /
[Multi-select](/components/input):
trigger matches the field; chevron `text-[var(--flux-grey-500)]` rotates open; option list is a `--flux-surface` panel with `--flux-shadow-lg`, selected option `bg-[var(--flux-primary-50)] text-[var(--flux-primary-800)]`, hover `bg-[var(--flux-grey-50)]`.
- [Checkbox](/components/checkbox),
[Radio](/components/radio), and
[Switch](/components/switch):
checked / active color is always `--flux-primary-400`; unchecked borders are `--flux-grey-200`; label gap `gap-2.5`.
- Don't use `border-gray-*` / `focus:ring-blue-*` defaults, placeholder-as-label, mixed field heights or radii, or a non-primary checked/focus color.
## 8. Buttons

Buttons are Lexend Bold, radius `--flux-radius-sm` (4px), and focus with a
`--flux-primary-300` ring (never a blue ring). Five variants, three sizes.
See [Button](/components/button).

/* Base — every variant */
font-bold rounded-[4px] focus:outline-none focus:ring-2 focus:ring-[var(--flux-primary-300)]

/* Primary   */ bg-[var(--flux-primary-600)] hover:bg-[var(--flux-primary-500)] active:bg-[var(--flux-primary-700)] text-white
/* Secondary */ bg-[var(--flux-grey-100)] hover:bg-[var(--flux-grey-200)] text-[var(--flux-black)]
/* Outline   */ border border-[var(--flux-primary-600)] text-[var(--flux-primary-600)] bg-transparent hover:bg-[var(--flux-primary-50)]
/* Ghost     */ bg-transparent text-[var(--flux-primary-600)] hover:bg-[var(--flux-primary-50)]
/* Danger    */ bg-[var(--flux-error)] text-white hover:opacity-90

/* Sizes */ sm: text-xs px-3 py-1.5   md: text-sm px-4 py-2   lg: text-base px-6 py-2.5
- Disabled is `opacity-50 cursor-not-allowed`; loading keeps the label and adds an inline spinner (`gap-2`).
- Compact inline actions inside cards, modals, and toolbars may use the lighter `bg-[var(--flux-primary-400)] text-white hover:opacity-90` fill — still Flux primary, never a raw Tailwind blue/indigo.
- Don't use `bg-blue-*`/`bg-indigo-*`, arbitrary radii, or font weights other than 700.
## 9. Badges & status colors

Badges are pills — `rounded-full`, `--flux-text-xs`, bold (700), tight padding
(`px-2.5 py-0.5`). Solid status badges use the tint tokens (the `-200`/`-300` steps)
with dark text for AAA contrast. See [Badge](/components/badge).

/* Pill base */ inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-bold

/* Canonical status tints (solid bg + --flux-black text) */
confirmed / completed          → bg --flux-green-200
pending / action required / on request → bg --flux-yellow-300
awaiting supplier              → bg --flux-blue-200
cancelled / rejected           → bg --flux-orange-300

/* Outline variant */ bg-transparent border + text in the colour token
/* Neutral / default */ bg-[var(--flux-primary-100)] text-[var(--flux-primary-400)]
- These are the same semantics tables use for status cells — stay consistent across the app.
- Don't invent per-status hexes or use Tailwind `bg-green-500`/`bg-red-500`; map every status to a Flux tint token.
## 10. Cards

A card is a quiet surface: `--flux-surface` background, a single `--flux-grey-100` hairline border,
rounded, no decorative chrome. See [Card](/components/card).

/* Card surface */ rounded border border-[var(--flux-grey-100)] bg-[var(--flux-surface)] p-5
/* Header / footer divider */ border-b / border-t border-[var(--flux-grey-100)]
/* Interactive (hover)  */ hover:border-[var(--flux-primary-300)] hover:shadow-md transition-all
/* Muted / archived     */ bg-[var(--flux-grey-50)] opacity-60
- Elevation follows the shadow scale — at most `--flux-shadow-md` on hover. Don't stack borders, glows, and heavy shadows.
- Don't add a single-edge accent bar (“stroke top”) or a colored dot beside the title.
## 11. Modals & tooltips

Overlays share the card surface with stronger elevation. See
[Modal](/components/modal) and
[Tooltip](/components/tooltip).

/* Modal backdrop */ fixed inset-0 bg-black/50 z-50 flex items-center justify-center
/* Modal dialog   */ bg-[var(--flux-surface)] rounded shadow-xl max-w-md w-full mx-4
/* Header / footer */ p-5 border-b / border-t border-[var(--flux-grey-100)]; footer actions justify-end gap-3

/* Tooltip */ bg-[var(--flux-primary-800)] text-white text-xs px-2.5 py-1.5 rounded shadow-lg
/*          arrow matches the bubble (--flux-primary-800); positions top/right/bottom/left */
- Modal uses `--flux-shadow-xl`; footer pairs a ghost Cancel with a primary Confirm. The close X is `--flux-grey-300` → `--flux-black` on hover.
- Don't tint the backdrop with a brand color or give the dialog a colored border.
## 12. Notes, progress & loading

Feedback components pair a semantic tint background with a matching semantic icon. See
[Note](/components/note),
[Progress](/components/progress),
[Spinner](/components/spinner), and
[Skeleton](/components/skeleton).

/* Note — rounded p-4, tint bg + semantic icon stroke, --flux-black text */
info    → bg --flux-primary-100  (icon --flux-info)
success → bg --flux-green-100     (icon --flux-success)
warning → bg --flux-yellow-100    (icon --flux-warning)
error   → bg --flux-orange-100    (icon --flux-error)

/* Progress */ track bg-[var(--flux-grey-100)] rounded-full; fill bg-[var(--flux-primary-400)]
/* Spinner  */ track --flux-grey-200, arc --flux-primary-400, animate-spin
/* Skeleton */ shimmer --flux-grey-100 → --flux-grey-50 → --flux-grey-100
- Use semantic tokens (`--flux-success/warning/error/info`) for status — not Tailwind `green-500`/`amber-500`.
- Don't color note body text; it stays `--flux-black`. The tint carries the meaning.
## 13. Tabs & accordions

Disclosure components signal state with Flux primary, never an underline color leak. See
[Tabs](/components/tabs) and
[Accordion](/components/accordion).

/* Tab bar  */ flex border-b border-[var(--flux-grey-100)]; tab px-4 py-2.5 text-sm font-bold
/* Active   */ text-[var(--flux-primary-400)] border-b-2 border-[var(--flux-primary-400)]
/* Inactive */ text-[var(--flux-grey-300)] hover:text-[var(--flux-black)]

/* Accordion row */ border-b border-[var(--flux-grey-100)] (none on last)
/*   title bold --flux-heading; chevron --flux-grey-300 rotates 180 when open
disabled item opacity-40 cursor-not-allowed */
- Active tab indicator is always `--flux-primary-400`. Dividers are `--flux-grey-100` only.
## 14. Avatars

Always circular. Initials fall back to a Flux primary tint. See
[Avatar](/components/avatar).

/* Image    */ rounded-full object-cover
/* Initials */ rounded-full bg-[var(--flux-primary-100)] text-[var(--flux-primary-400)] font-bold
/* Sizes    */ sm w-8 h-8 · md w-10 h-10 · lg w-14 h-14
/* Status dot */ w-2.5 h-2.5 rounded-full bg-[var(--flux-success)] ring-2 ring-white
/* Group    */ overlap with -ml-2 and ring-2 ring-[var(--flux-surface)]
- Don't use square avatars or a non-primary tint for initials. The presence dot is `--flux-success`.
## 15. Date picker

A trigger that opens a calendar popover. The trigger follows the field convention; the calendar uses Flux primary
for selection. See [Date Picker](/components/date-picker).

/* Trigger */ border --flux-grey-200, radius-md, calendar icon + chevron --flux-grey-300
/*   open: border --flux-primary-400 + a --flux-primary-100 focus ring; chevron rotates */
/* Popover */ bg --flux-surface, border --flux-grey-100, --flux-radius-lg, --flux-shadow-lg
/* Day cells */ selected/range ends bg --flux-primary-400 white (rounded-full)
/*   in-range bg --flux-primary-100; today text --flux-primary-400 w/ --flux-primary-200 ring */
## 16. Hero, Journey & Code Block

Display components for marketing and documentation surfaces. See
[Hero](/components/hero),
[Journey](/components/journey), and
[Code Block](/components/code-block).

- Hero: dark variants use a `--flux-primary-800` ground (or a photo with a teal overlay); eyebrow/subtitle are `--flux-yellow-400`, headline white, body white at ~85%. Light variant is `--flux-background` with `--flux-black` heading. CTA buttons reuse the Button variants.
- Journey: horizontal steps with rounded icon tiles (`--flux-radius-sm`) filled with a brand/product accent, connected by `--flux-grey-200` arrows; step detail opens in a Modal.
- Code Block: dark ground `--flux-primary-800`, code text `--flux-primary-100`, JetBrains Mono. Inline code is `--flux-primary-100` bg + `--flux-primary-400` text. This site's wrapper adds a copy button.
- Don't treat the marketing hero layout as the default app shell for product UI.
## 17. Outcome patterns

Patterns for embedded outcome flows (e.g. a focused task launched from Salesforce). See
[Outcome Header](/components/outcome-header),
[Flow Entry](/components/flow-entry), and
[Outcome Complete](/components/outcome-complete).
They share the `--flux-flow-*` tokens.

- Outcome Header: a `--flux-flow-header-height` bar on `--flux-flow-header-bg` with a `--flux-flow-header-border` bottom border. Bold `--flux-heading` outcome label, a `--flux-grey-500` → `--flux-primary-400` return action. An optional 2px top accent bar in a product color is part of this pattern (the only sanctioned single-edge accent).
- Flow Entry: the arriving state — Skeleton placeholders during load, an `--flux-orange-100`/`--flux-orange-400` error block with a retry, and a `--flux-green-100`/`--flux-green-400` resolved tick that fades in over `--flux-flow-entry-duration`.
- Outcome Complete: a centered `--flux-green-100` tick, bold achievement line, a primary return button (with optional `--flux-flow-return-countdown` auto-return), and outline next-step buttons.
