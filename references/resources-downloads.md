# Flux — /resources/downloads/

Source: https://flux.kaptio.com/resources/downloads/

Resources

# Downloads
Everything the system publishes, at a URL that will not move. Generated on every release from one source, so no two artifacts can disagree.

## Token artifacts
FileSizeContents`/tokens/v2/flux.css`50.5 kBFonts, all three tiers, all three themes, base rules. The usual import.`/tokens/v2/flux-tokens.css`48.7 kBThe same tokens without font imports or base rules.`/tokens/v2/flux.json`137.2 kBEvery token as structured data, grouped by tier and theme.`/tokens/v2/flux-tailwind.css`17.6 kBTailwind v4 theme block. Clears the defaults, remaps the names.`/tokens/v2/flux-components.css`148.7 kBThe 47 documented components, as framework-agnostic CSS.`/tokens/v2/flux-components.js`90.3 kBComponent behaviour for Select and Date picker, including keyboard handling and form-value syncing.`/tokens/v2/flux-prototype.css`4.1 kBPrototype typography: Google Sans Flex and Manrope. Product prototypes only — never decks.`/tokens/v2/flux-deck.css`41.4 kBThe presentation layer. Slide canvas and layouts. Decks only — it overrides the fluid root.`/tokens/v2/flux-deck.js`7.0 kBDeck navigation: previous and next arrows, click to advance, and the keys. Optional — snapping is CSS.Direct links: [flux.css](/tokens/v2/flux.css) ·[flux-tokens.css](/tokens/v2/flux-tokens.css) ·[flux.json](/tokens/v2/flux.json) ·[flux-tailwind.css](/tokens/v2/flux-tailwind.css) ·[flux-components.css](/tokens/v2/flux-components.css) ·[flux-components.js](/tokens/v2/flux-components.js) ·[flux-prototype.css](/tokens/v2/flux-prototype.css) ·[flux-deck.css](/tokens/v2/flux-deck.css) ·[flux-deck.js](/tokens/v2/flux-deck.js)

Not this path`/tokens/flux.css`, without the version, is Flux 1.x and stays that way. It is a live runtime dependency of applications that cannot redeploy to follow a change. Six tokens differ between the two — see [Upgrading](/get-started/upgrading/).
## Machine contract
FileFor`/llms.txt`The complete contract: tokens, rules, and every component’s markup.`/rules/flux.mdc`Cursor project rule. Drop into .cursor/rules/.`/rules/AGENTS.md`Portable agent brief. Works for Claude Code and Copilot.`/prototypes/brief.txt`Reusable product-prototype prompt with context fields, composition constraints and verification.`/decks/llms.txt`The deck contract. Separate on purpose — slide rules and product rules disagree.bashCopy`curl -o .cursor/rules/flux.mdc https://flux.kaptio.com/rules/flux.mdc
curl -o AGENTS.md                https://flux.kaptio.com/rules/AGENTS.md`
## Component sources
One plain-text file per component: markup, API, states, keyboard, accessibility and tokens.

- [button.txt

Triggers an action. Six variants, three sizes.](/components/source/button.txt)
- [input.txt

Single-line text entry, with the label, help and error pattern that goes with it.](/components/source/input.txt)
- [select.txt

Choice from a known, closed set of options.](/components/source/select.txt)
- [date-picker.txt

Single-date and date-range selection from a keyboard-operable calendar.](/components/source/date-picker.txt)
- [checkbox.txt

On-or-off choices and one-of-many choices, each with its label beside it.](/components/source/checkbox.txt)
- [switch.txt

An on or off setting that takes effect the moment it changes.](/components/source/switch.txt)
- [slider.txt

A duration, count or amount chosen by dragging along a bounded scale, as one value or a range.](/components/source/slider.txt)
- [search.txt

A search field with its icon, a clear button and the number of results.](/components/source/search.txt)
- [card.txt

Groups related content into one surface on the layer above.](/components/source/card.txt)
- [description-list.txt

Labelled values in a row or a stack. The summary block at the top of a record.](/components/source/description-list.txt)
- [metric.txt

Headline figures with a label and a change, aligned on one surface. The top of a dashboard.](/components/source/metric.txt)
- [chart.txt

Columns, lines, ranked bars and a donut, drawn from theme roles with a title, a takeaway and a legend.](/components/source/chart.txt)
- [timeline.txt

Events in time order on a hairline rail. A booking history, a day’s schedule, a workflow’s progress.](/components/source/timeline.txt)
- [itinerary.txt

A trip, day by day: where each day goes, what runs when, and where everyone sleeps.](/components/source/itinerary.txt)
- [calendar.txt

A month of departures, bookings or deadlines laid out on the days they fall.](/components/source/calendar.txt)
- [map.txt

A route and its stops drawn on a map, with a numbered marker for each stop.](/components/source/map.txt)
- [flow.txt

Steps and the connections between them on a pannable canvas, for automations and process maps.](/components/source/flow.txt)
- [app-shell.txt

The frame of a product: a rail of destinations, a top bar and the main column.](/components/source/app-shell.txt)
- [spinner.txt

An arc that turns while something loads, with the status written beside it.](/components/source/spinner.txt)
- [progress.txt

Segmented bars for how far a task has got, and where a measurement sits in its range.](/components/source/progress.txt)
- [skeleton.txt

Flat placeholder shapes that hold the layout of content that is still loading.](/components/source/skeleton.txt)
- [accordion.txt

Page sections that open and close under their own headings.](/components/source/accordion.txt)
- [toast.txt

A short confirmation that an action worked, with a way to undo it.](/components/source/toast.txt)
- [reorder.txt

A list whose order is the meaning, rearranged by dragging a handle or with the keyboard.](/components/source/reorder.txt)
- [board.txt

Records as cards in columns by stage, moved between stages by drag or keyboard.](/components/source/board.txt)
- [editable-cell.txt

A table value that is edited where it is shown, with saving and error states.](/components/source/editable-cell.txt)
- [tooltip.txt

A short label on hover or focus, and a small panel opened by a button.](/components/source/tooltip.txt)
- [empty-state.txt

What a region shows when it has nothing in it: why, and the one thing to do next.](/components/source/empty-state.txt)
- [breadcrumbs.txt

The path from a section to the current page, as a list of links.](/components/source/breadcrumbs.txt)
- [pagination.txt

Range text and page links for a long list that is served one page at a time.](/components/source/pagination.txt)
- [segmented-control.txt

Two to five joined options, exactly one selected, that switch a view or a setting in place.](/components/source/segmented-control.txt)
- [stepper.txt

Numbered steps that show progress through a task, and the wizard recipe that validates each one.](/components/source/stepper.txt)
- [walkthrough.txt

Numbered steps beside the interface they describe, and a strip of screens that tells a flow frame by frame.](/components/source/walkthrough.txt)
- [split-view.txt

A list of records beside the detail of the selected one, each pane scrolling on its own.](/components/source/split-view.txt)
- [file-upload.txt

A dropzone over a native file input, and a list of the chosen files with their progress and errors.](/components/source/file-upload.txt)
- [assistant-panel.txt

A side panel for conversing with Runa: messages, cited sources, suggestions and a prompt.](/components/source/assistant-panel.txt)
- [rich-text-editor.txt

A field with a formatting toolbar for short structured text, and the prose styles it produces.](/components/source/rich-text-editor.txt)
- [badge.txt

A short status label. Four status colours, shared with tables.](/components/source/badge.txt)
- [table.txt

Quiet data table with sorting, selection, expandable rows, row actions, a toolbar and sticky columns.](/components/source/table.txt)
- [menu.txt

A short list of actions behind one button, for a record or a toolbar.](/components/source/menu.txt)
- [kbd.txt

A key or key combination, shown inline, in a control, or in a list of shortcuts.](/components/source/kbd.txt)
- [command-palette.txt

A searchable list of actions, pages and records, opened over the page with ⌘K.](/components/source/command-palette.txt)
- [modal.txt

A focused, interrupting dialog built on the native dialog element.](/components/source/modal.txt)
- [drawer.txt

A full-height panel over the page, from its end edge, to read or edit one record without leaving the list.](/components/source/drawer.txt)
- [note.txt

Inline contextual message in one of four semantic tones.](/components/source/note.txt)
- [tabs.txt

Switches between sibling views within one context.](/components/source/tabs.txt)
- [avatar.txt

Represents a person or account, as an image or initials.](/components/source/avatar.txt)
## Package
bashCopy`npm config set @kaptio:registry https://gitlab.com/api/v4/packages/npm/
npm install @kaptio/flux-tokens`Published to the Kaptio GitLab registry. Pin it for anything you ship — see [Install](/get-started/install/).

## URL stability
GuaranteedEvery URL on this page is permanent. Artifacts are updated in place on each 2.x release, and no path will be moved or removed within the 2.x line. A 3.0 would take a new prefix rather than these.Hosted artifacts track the current release, which is right for prototypes and wrong for production. Pin the package where a change underneath you would matter.

[PreviousSlack teammates](/for-ai/slack/)[NextChangelog](/resources/changelog/)
