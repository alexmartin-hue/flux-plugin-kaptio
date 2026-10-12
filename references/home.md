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
47, documented to one shape. Each one shows a live specimen above the exact markup that produced it.

- [Button

Triggers an action. Six variants, three sizes.](/components/button/)
- [Input

Single-line text entry, with the label, help and error pattern that goes with it.](/components/input/)
- [Select

Choice from a known, closed set of options.](/components/select/)
- [Date picker

Single-date and date-range selection from a keyboard-operable calendar.](/components/date-picker/)
- [Checkbox and radio

On-or-off choices and one-of-many choices, each with its label beside it.](/components/checkbox/)
- [Switch

An on or off setting that takes effect the moment it changes.](/components/switch/)
- [Slider

A duration, count or amount chosen by dragging along a bounded scale, as one value or a range.](/components/slider/)
- [Search

A search field with its icon, a clear button and the number of results.](/components/search/)
- [Card

Groups related content into one surface on the layer above.](/components/card/)
- [Description list

Labelled values in a row or a stack. The summary block at the top of a record.](/components/description-list/)
- [Metric

Headline figures with a label and a change, aligned on one surface. The top of a dashboard.](/components/metric/)
- [Chart

Columns, lines, ranked bars and a donut, drawn from theme roles with a title, a takeaway and a legend.](/components/chart/)
- [Timeline

Events in time order on a hairline rail. A booking history, a day’s schedule, a workflow’s progress.](/components/timeline/)
- [Itinerary

A trip, day by day: where each day goes, what runs when, and where everyone sleeps.](/components/itinerary/)
- [Calendar view

A month of departures, bookings or deadlines laid out on the days they fall.](/components/calendar/)
- [Map

A route and its stops drawn on a map, with a numbered marker for each stop.](/components/map/)
- [Flow diagram

Steps and the connections between them on a pannable canvas, for automations and process maps.](/components/flow/)
- [App shell

The frame of a product: a rail of destinations, a top bar and the main column.](/components/app-shell/)
- [Spinner

An arc that turns while something loads, with the status written beside it.](/components/spinner/)
- [Progress and meter

Segmented bars for how far a task has got, and where a measurement sits in its range.](/components/progress/)
- [Skeleton

Flat placeholder shapes that hold the layout of content that is still loading.](/components/skeleton/)
- [Accordion

Page sections that open and close under their own headings.](/components/accordion/)
- [Toast

A short confirmation that an action worked, with a way to undo it.](/components/toast/)
- [Reorderable list

A list whose order is the meaning, rearranged by dragging a handle or with the keyboard.](/components/reorder/)
- [Board

Records as cards in columns by stage, moved between stages by drag or keyboard.](/components/board/)
- [Editable cell

A table value that is edited where it is shown, with saving and error states.](/components/editable-cell/)
- [Tooltip and popover

A short label on hover or focus, and a small panel opened by a button.](/components/tooltip/)
- [Empty state

What a region shows when it has nothing in it: why, and the one thing to do next.](/components/empty-state/)
- [Breadcrumbs

The path from a section to the current page, as a list of links.](/components/breadcrumbs/)
- [Pagination

Range text and page links for a long list that is served one page at a time.](/components/pagination/)
- [Segmented control

Two to five joined options, exactly one selected, that switch a view or a setting in place.](/components/segmented-control/)
- [Stepper and wizard

Numbered steps that show progress through a task, and the wizard recipe that validates each one.](/components/stepper/)
- [Walkthrough and storyboard

Numbered steps beside the interface they describe, and a strip of screens that tells a flow frame by frame.](/components/walkthrough/)
- [List and detail

A list of records beside the detail of the selected one, each pane scrolling on its own.](/components/split-view/)
- [File upload

A dropzone over a native file input, and a list of the chosen files with their progress and errors.](/components/file-upload/)
- [Assistant panel

A side panel for conversing with Runa: messages, cited sources, suggestions and a prompt.](/components/assistant-panel/)
- [Rich text editor

A field with a formatting toolbar for short structured text, and the prose styles it produces.](/components/rich-text-editor/)
- [Badge

A short status label. Four status colours, shared with tables.](/components/badge/)
- [Table

Quiet data table with sorting, selection, expandable rows, row actions, a toolbar and sticky columns.](/components/table/)
- [Action menu

A short list of actions behind one button, for a record or a toolbar.](/components/menu/)
- [Keyboard shortcut

A key or key combination, shown inline, in a control, or in a list of shortcuts.](/components/kbd/)
- [Command palette

A searchable list of actions, pages and records, opened over the page with ⌘K.](/components/command-palette/)
- [Modal

A focused, interrupting dialog built on the native dialog element.](/components/modal/)
- [Drawer

A full-height panel over the page, from its end edge, to read or edit one record without leaving the list.](/components/drawer/)
- [Note

Inline contextual message in one of four semantic tones.](/components/note/)
- [Tabs

Switches between sibling views within one context.](/components/tabs/)
- [Avatar

Represents a person or account, as an image or initials.](/components/avatar/)[NextInstall](/get-started/install/)
