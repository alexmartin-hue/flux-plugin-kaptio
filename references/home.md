# Flux — Home

Source: https://flux.kaptio.com/

Flux 2.0

# Flux
The Kaptio design system. One import gives you the tokens, the typography, the focus states and the accessibility floor — in light, dark or deep, without a component knowing which.

## Install
One line for a prototype. Everything below inherits from it.

cssCopy`@import url("https://flux.kaptio.com/tokens/v2/flux.css");`That loads Lexend and JetBrains Mono, defines every token in all three themes, sets the fluid root size, and applies the focus ring. For an application, pin the package instead — see [Install](/get-started/install/).

## The shape of the system
Three tiers. Your code should almost always touch the middle one.

A primitive is a raw value with no opinion — `--flux-primary-400`is a teal, and nothing more. A semantic token is a role —`--flux-text-link` is what a link is, whichever theme is active. A component token is a decision about one part —`--flux-button-height-md`.

Reference semantic tokens. They are the only tier that changes with the theme, so anything built on them themes automatically and anything built on primitives does not.

cssCopy`/* Themes. Survives a redefinition of the teal ramp. */
.panel {
background: var(--flux-layer-01);
color: var(--flux-text-primary);
border: 1px solid var(--flux-border-subtle);
}

/* Does not theme. Locks a light-mode value into a dark-mode surface. */
.panel {
background: var(--flux-white);
color: var(--flux-black);
border: 1px solid #E3E8E8;
}`
## What 2.0 adds
Almost all of the Flux 1.x surface carries over under the same name and the same value, so an upgrade is close to an import swap.

- [Three token tiers

Primitives hold raw values, semantic tokens hold roles, component tokens hold dimensions. Reference tier two and your work themes for free.](/foundations/tokens/)
- [Three themes

Light, dark and deep, switched with one attribute on the root element. No component knows which one is active.](/get-started/themes/)
- [A layer model

Nested surfaces stay legible without anyone hand-picking greys, in every theme.](/foundations/elevation/)
- [A second voice

JetBrains Mono Variable at three weights, for the metadata, identifiers and structural labels Lexend was never meant to carry.](/foundations/typography/)
- [Verified contrast

Every text and non-text pairing is checked against WCAG 2.2 AA on every build, with body and primary text held to AAA. The build fails before the site does.](/foundations/accessibility/)
- [A machine contract

llms.txt, per-component plain-text sources and drop-in repository rules, so agents build in Flux by default.](/for-ai/)CompatibleFlux 1.x names such as `--flux-background`, `--flux-surface` and`--flux-heading` are published forever, with their original light-theme values. Six tokens do differ, and 1.x keeps serving at its own URL until you move — see[Upgrading from 1.x](/get-started/upgrading/).
## If you are an agent
Read the contract, not the marketing.

Flux is designed to be consumed by language models as much as by people. The whole system is available as plain text at [/llms.txt](/llms.txt) — every token name, every rule, every component’s markup, in one file with no HTML to parse.

Individual components are at `/components/source/.txt`. Repository rules for Cursor, Claude Code and Copilot are at [For AI → Repository rules](/for-ai/rules/).

## Components
Twelve, documented to one shape. Each one shows a live specimen above the exact markup that produced it.

- [Button

Triggers an action. Six variants, three sizes.](/components/button/)
- [Input

Single-line text entry, with the label, help and error pattern that goes with it.](/components/input/)
- [Select

Choice from a known, closed set of options.](/components/select/)
- [Date picker

Single-date and date-range selection from a keyboard-operable calendar.](/components/date-picker/)
- [Card

Groups related content into one surface on the layer above.](/components/card/)
- [Description list

Labelled values in a row or a stack. The summary block at the top of a record.](/components/description-list/)
- [Badge

A short status label. Four status colours, shared with tables.](/components/badge/)
- [Table

Quiet data table. Horizontal dividers only, tabular figures, badge status cells.](/components/table/)
- [Modal

A focused, interrupting dialog built on the native dialog element.](/components/modal/)
- [Note

Inline contextual message in one of four semantic tones.](/components/note/)
- [Tabs

Switches between sibling views within one context.](/components/tabs/)
- [Avatar

Represents a person or account, as an image or initials.](/components/avatar/)[NextInstall](/get-started/install/)
