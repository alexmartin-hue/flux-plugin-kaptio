# Flux — /donts

Source: https://flux.kaptio.com/donts

[Flux](/)
Guidelines

# Don'ts

Flux documents what we do use. This page lists common mistakes, legacy ideas, and
invented details that sometimes appear in mockups, AI output, or ad hoc designs. If something
is not defined in Foundations, Components, or Patterns, treat it as out of scope unless
design explicitly adds it here or in Figma.

For implementations and tooling

Prefer tokens from [Token Reference](/foundations/tokens)
and documented components. Do not infer extra chrome (accent borders on one edge only, novel
colour names, or layout blocks that are not in this site) as part of Flux.

## Colours and tokens

Do not introduce colours that are not defined in
[Colours](/foundations/colors)
or the token source. No one-off hex or RGB values for brand UI unless they map to an existing token.

Do not use made-up token names (for example invented semantic keys) in code or copy. Use the
names and CSS variables from the published token list.

Do not assume product accents from marketing screenshots apply globally; product colours are
scoped per product in [Products](/products).

## Containers, cards, and borders

Do not add decorative treatments that are not described in Flux, such as a thick or coloured
border on only one edge of a box (for example a “stroke top” or top accent bar on
cards). Standard surfaces use the patterns in
[Card](/components/card)
and related components unless design ships an explicit pattern.

Do not use small solid coloured dots or circles beside headings or labels inside cards, panels,
or other boxed content (for example a teal marker next to a section title). Rely on typography
hierarchy and spacing from
[Typography](/foundations/typography)
instead of decorative bullets that look like ad hoc status indicators.

Do not stack multiple competing outlines, inner glows, and heavy shadows on the same container;
elevation should follow [Shadows](/foundations/shadows).

Do not use arbitrary corner radii or spacing; use the spacing scale and component specs in Foundations.

## Layout and page sections

Do not invent new section types, hero variants, or navigation models that are not documented
under Components or Patterns.

Do not treat the marketing Flux site layout (for example showcase sections on this documentation
site) as the default app shell for product UIs unless product design specifies it.

## Typography and iconography

Do not substitute typefaces outside the scale in
[Typography](/foundations/typography).

Do not mix ad hoc icon styles or emoji as the primary icon system in product UI; follow
[Iconography](/foundations/iconography).

Do not use light grey, yellow, or any colour other than Kaptio dark for text on light backgrounds.

## Tables

Do not add heavy gridlines, a border on every cell, or vertical column borders. Flux tables
use horizontal row dividers only — a bottom border in
[--flux-grey-100](/foundations/colors)
— and drop the divider on the last row. See
[Table](/components/table).

Do not left-align numeric, price, or quantity columns or use proportional figures. Right-align them
(headers too) and set `font-variant-numeric: tabular-nums` so values line up.

Do not invent per-status colours or styles for status cells. Use the
[Badge](/components/badge)
component and its documented semantics (confirmed/completed green, pending/on request amber, awaiting
supplier blue, cancelled/rejected/expired red).

## Forms and inputs

Do not use Tailwind's default focus styles (`focus:ring-blue-500`, blue outlines). Input,
select, checkbox, radio, and switch focus and checked states are Flux primary —
border `--flux-primary-400` with a `--flux-primary-300` ring. See
[Input](/components/input).

Do not use `border-gray-*`, `border-slate-*`, or one-off greys for field
borders. Field borders are `--flux-grey-200`; placeholders are `--flux-grey-300`.

Do not mix field heights or corner radii within one form, and do not pick arbitrary radii. Keep a
single height and radius across inputs, selects, and the
[Textarea](/components/textarea).

Do not use the placeholder as the only label. Pair every field with a real
`text-sm font-medium text-[var(--flux-black)]` label, and surface errors with
`--flux-error` text and border — see
[Select](/components/select)
and [Checkbox](/components/checkbox).

## Buttons

Do not fill buttons with Tailwind blues or indigos (`bg-blue-600`, `bg-indigo-500`). The
primary button is `--flux-primary-600`; the danger button is `--flux-error`. See
[Button](/components/button).

Do not give buttons a blue focus ring. The focus ring is `--flux-primary-300`, and the corner
radius is `--flux-radius-sm` (4px) — not arbitrary pill or large radii.

Do not use font weights other than 700 for button labels, and do not invent extra variants beyond primary,
secondary, outline, ghost, and danger.

## Badges and status colours

Do not invent per-status hexes or reach for Tailwind `bg-green-500` / `bg-red-500`. Map
each status to a Flux tint token — confirmed/completed `--flux-green-200`, pending/on request
`--flux-yellow-300`, awaiting supplier `--flux-blue-200`, cancelled/rejected
`--flux-orange-300`. See [Badge](/components/badge).

Do not change the pill shape or weight: badges are `rounded-full`, `--flux-text-xs`, bold.
Keep the same status colours in tables and badges — do not maintain two palettes.

## Cards, modals, and tooltips

Do not give a [Modal](/components/modal)
a coloured border or tint its backdrop with a brand colour. The dialog is a `--flux-surface` panel with
`--flux-shadow-xl`; the backdrop is a neutral `bg-black/50`.

Do not style a [Tooltip](/components/tooltip)
on a light surface. Tooltips are dark — `--flux-primary-800` background, white text — with an arrow in the same colour.

Do not cap elevation above `--flux-shadow-md` for interactive cards, and do not combine a hover border,
glow, and heavy shadow at once.

## Notes, progress, and loading

Do not colour [Note](/components/note)
body text to match the variant. The tint background (`--flux-primary-100`, `--flux-green-100`,
`--flux-yellow-100`, `--flux-orange-100`) and the semantic icon carry the meaning; text stays `--flux-black`.

Do not fill [Progress](/components/progress)
bars or [Spinner](/components/spinner)
arcs with raw Tailwind greens/blues. The fill is `--flux-primary-400` on a `--flux-grey-100`/`--flux-grey-200` track;
use semantic tokens (`--flux-success`, etc.) for status colours.

## Tabs, accordions, and avatars

Do not use a non-primary colour for the active
[Tab](/components/tabs) indicator. The
active tab is `--flux-primary-400` text with a 2px `--flux-primary-400` underline; the tab strip
divider is `--flux-grey-100`.

Do not box each [Accordion](/components/accordion)
item in its own border. Items are separated by a single `--flux-grey-100` bottom divider (dropped on the last row).

Do not use square avatars or a non-primary initials tint. [Avatars](/components/avatar)
are `rounded-full`; initials are `--flux-primary-100` on `--flux-primary-400`; the presence dot is `--flux-success`.

## Outcome patterns

Do not hardcode the outcome bar's height, background, or border. Use the `--flux-flow-*` tokens
(`--flux-flow-header-height`, `--flux-flow-header-bg`, `--flux-flow-header-border`). See
[Outcome Header](/components/outcome-header).

Do not show a raw spinner with no context for the arriving state. Use
[Flow Entry](/components/flow-entry)
skeletons, and reserve the `--flux-orange-*` error and `--flux-green-*` resolved treatments for those states.

Note: the optional 2px top accent bar on the Outcome Header is a sanctioned pattern detail — it is the one
exception to the “no single-edge accent” rule, and applies only here, not to ordinary cards.

## Keeping this list current

When review or tooling keeps proposing the same incorrect pattern, add a short bullet under the
right heading above so humans and assistants share one source of truth. For new allowed patterns,
add or update the relevant Foundations, Component, or Pattern page instead of only listing a
negative here.
