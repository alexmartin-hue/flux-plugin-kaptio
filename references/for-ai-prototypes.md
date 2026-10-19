# Flux — /for-ai/prototypes/

Source: https://flux.kaptio.com/for-ai/prototypes/

For AI

# Prototype prompt
Importing the stylesheet gives a prototype Flux values. Giving the agent this brief makes it use those values as a system: documented components, readable density, one hierarchy and a check before handoff.

## Set up the repository
Persistent rules carry more authority than a paragraph pasted once.

Add the Flux rule file from [Repository rules](/for-ai/rules/) to the prototype repository first. It is always applied to UI files, so later prompts cannot silently drop the design contract when the conversation grows.

If the repository already has agent instructions, append the Flux contract rather than replacing them. Product context and engineering conventions still apply.

CarefulA CSS import supplies tokens; it does not choose hierarchy, density or component semantics. The repository rule and prototype brief are both required for consistent generated work.
## Copy the prompt
Fill the five context fields, then give the whole prompt to the agent.

Also available as plain text at [/prototypes/brief.txt](/prototypes/brief.txt).

textCopy`Build a Kaptio product prototype using Flux 2.0.

Before writing UI:
1. Read and follow https://flux.kaptio.com/llms.txt.
2. For every component you use, copy its markup from https://flux.kaptio.com/components/source/.txt. Do not write component markup from memory.
3. Reuse existing repository components only when they are built from Flux components.
4. This is product UI, not a presentation. Never import flux-deck.css.

Composition contract — this is not optional:
- Every view is a layout of documented Flux components. Every surface, control, status, message, table, chart and overlay on screen is one of the components listed below, used as documented.
- Your own CSS only places components: display, grid, flex, gap, padding, margin and size, using space tokens. It never draws: no background, box border, radius or shadow, no font family, and no restyling of a .flux-* class or redefining of a --flux-* token. A divider between regions is a single-side border with var(--flux-border-subtle).
- Never name a class after a component (booking-card, status-pill, side-drawer, kpi-tile). If you are about to, use that Flux component instead.
- If the task needs something no component covers, stop and say which component is missing and what it must do. Do not build a stand-in.

Components — choose from this list before writing any markup:
- Button (button): Triggers an action. Six variants, three sizes.
- Input (input): Single-line text entry, with the label, help and error pattern that goes with it.
- Select (select): Choice from a known, closed set of options.
- Date picker (date-picker): Single-date and date-range selection from a keyboard-operable calendar.
- Checkbox and radio (checkbox): On-or-off choices and one-of-many choices, each with its label beside it.
- Switch (switch): An on or off setting that takes effect the moment it changes.
- Slider (slider): A duration, count or amount chosen by dragging along a bounded scale, as one value or a range.
- Search (search): A search field with its icon, a clear button and the number of results.
- Card (card): Groups related content into one surface on the layer above.
- Description list (description-list): Labelled values in a row or a stack. The summary block at the top of a record.
- Metric (metric): Headline figures with a label and a change, aligned on one surface. The top of a dashboard.
- Chart (chart): Columns, stacked columns, lines, areas, two scales, ranked bars and a donut, drawn from theme roles, with a readout on hover or focus.
- Heatmap (heatmap): A matrix of values on one sequential scale, where every cell can be focused and opened for its detail.
- Timeline (timeline): Events in time order on a hairline rail. A booking history, a day’s schedule, a workflow’s progress.
- Itinerary (itinerary): A trip, day by day: where each day goes, what runs when, and where everyone sleeps.
- Calendar view (calendar): A month of departures, bookings or deadlines laid out on the days they fall.
- Map (map): A route and its stops drawn on a map, with a numbered marker for each stop.
- Flow diagram (flow): Steps and the connections between them on a pannable canvas, for automations and process maps.
- App shell (app-shell): The frame of a product: a rail of destinations, a top bar and the main column.
- Spinner (spinner): An arc that turns while something loads, with the status written beside it.
- Progress and meter (progress): Segmented bars for how far a task has got, and where a measurement sits in its range.
- Skeleton (skeleton): Flat placeholder shapes that hold the layout of content that is still loading.
- Accordion (accordion): Page sections that open and close under their own headings.
- Toast (toast): A short confirmation that an action worked, with a way to undo it.
- Reorderable list (reorder): A list whose order is the meaning, rearranged by dragging a handle or with the keyboard.
- Board (board): Records as cards in columns by stage, moved between stages by drag or keyboard.
- Editable cell (editable-cell): A table value that is edited where it is shown, with saving and error states.
- Tooltip and popover (tooltip): A short label on hover or focus, and a small panel opened by a button.
- Empty state (empty-state): What a region shows when it has nothing in it: why, and the one thing to do next.
- Breadcrumbs (breadcrumbs): The path from a section to the current page, as a list of links.
- Pagination (pagination): Range text and page links for a long list that is served one page at a time.
- Segmented control (segmented-control): Two to five joined options, exactly one selected, that switch a view or a setting in place.
- Stepper and wizard (stepper): Numbered steps that show progress through a task, and the wizard recipe that validates each one.
- Walkthrough and storyboard (walkthrough): Numbered steps beside the interface they describe, and a strip of screens that tells a flow frame by frame.
- List and detail (split-view): A list of records beside the detail of the selected one, each pane scrolling on its own.
- File upload (file-upload): A dropzone over a native file input, and a list of the chosen files with their progress and errors.
- Assistant panel (assistant-panel): A side panel for conversing with Runa: messages, cited sources, suggestions and a prompt.
- Rich text editor (rich-text-editor): A field with a formatting toolbar for short structured text, and the prose styles it produces.
- Badge (badge): A short status label. Four status colours, shared with tables.
- Table (table): Quiet data table with sorting, selection, expandable rows, row actions, a toolbar and sticky columns.
- Action menu (menu): A short list of actions behind one button, for a record or a toolbar.
- Keyboard shortcut (kbd): A key or key combination, shown inline, in a control, or in a list of shortcuts.
- Command palette (command-palette): A searchable list of actions, pages and records, opened over the page with ⌘K.
- Modal (modal): A focused, interrupting dialog built on the native dialog element.
- Drawer (drawer): A full-height panel over the page, from its end edge, to read or edit one record without leaving the list.
- Note (note): Inline contextual message in one of four semantic tones.
- Tabs (tabs): Switches between sibling views within one context.
- Avatar (avatar): Represents a person or account, as an image or initials.

Prototype context:
- Product or feature: [name]
- Primary user: [user]
- Task they must complete: [task]
- Required screens and states: [screens and states]
- Data and business constraints: [constraints]

Design requirements:
- Import https://flux.kaptio.com/tokens/v2/flux.css, https://flux.kaptio.com/tokens/v2/flux-components.css and then https://flux.kaptio.com/tokens/v2/flux-prototype.css, from that URL or the @kaptio/flux-tokens package. Never copy a Flux file into the repository; a copy stops receiving fixes and new components.
- Typography comes from flux-prototype.css: Google Sans Flex Medium for headings and card titles, Bold in text-brand for KPI values (.flux-kpi); Manrope for everything else — body, tables and inputs, .flux-description for descriptions, labels in Medium, buttons and .flux-kpi-change in Semi Bold, .flux-meta for small metadata. The layer changes typefaces and weights only: size headings from the scale exactly as in the Lexend product, and keep the sizes components set. No Lexend and no mono in a prototype. Never write a literal font-weight; use --flux-prototype-weight-regular, -medium or -semibold.
- Load https://flux.kaptio.com/tokens/v2/flux-components.js with defer on every page. Select, Date picker, info bubbles, menus, drawers, toasts, tables, the app shell, the command palette, boards, maps and flow diagrams all depend on it, and it does nothing where none of them appear. Markup a framework renders after the page loads is wired when it is inserted.
- Reference Tier 2 semantic tokens for every interface role.
- Use at least --flux-text-sm for controls, table cells and compact secondary copy.
- Use --flux-text-base for sentences intended to be read.
- Reserve --flux-text-xs for badges, help text and short metadata.
- Preserve readable type and spacing. Let the page scroll.
- Keep text, notes and controls inside the documented padding of their surface. Never let content touch a card or panel edge.
- Keep action rows inside the same inline inset as the content above, with a token gap between actions; wrap or stack them on narrow screens.
- Reflow layouts on narrow screens; never use CSS zoom or transform to scale the application.
- Wrap wide tables in their horizontal scrolling container.
- Group related metrics on one surface instead of making every value a card: copy the Metric row from https://flux.kaptio.com/components/source/metric.txt, and for a dashboard follow https://flux.kaptio.com/patterns/dashboards/ — page header, one metric row, then the records that need action as a table.
- Establish one clear primary action and use at most one yellow CTA per view.
- Map each domain status to the documented Badge semantics before rendering it. Do not leave every status on the neutral base style when the states have different consequences.
- Use yellow status styling only when waiting, delay or required attention is part of the meaning.
- Use eyebrows and numbering sparingly: an eyebrow only when it adds context the heading does not, and numbers only when order is the meaning. Never label or number every section.
- Use native semantic elements, visible labels and documented keyboard behaviour.
- Never use a native select, datalist or date-type input element; their menus and calendars draw in the operating system style. For single choice copy the Select markup from https://flux.kaptio.com/components/source/select.txt, its searchable variant for lists longer than about ten options, its grouped variant when options fall into categories, its flux-multiselect variant for several choices, and for dates https://flux.kaptio.com/components/source/date-picker.txt. With four or fewer options use radio buttons instead.
- Put explanatory field text in the info bubble beside the label, using the markup in https://flux.kaptio.com/components/source/input.txt. Never place help or explanation text below a field; that space is only for error messages.
- Support light and dark themes. Do not use deep for dense product UI.
- Do not invent colours, dimensions, components, statuses or interactions.

Workflow:
1. Inspect the repository and its existing components.
2. State the proposed screen hierarchy as the Flux components in each region, for example: app shell; page header; metric row; table of bookings; drawer for a booking.
3. Implement only the requested workflow, copying each component's markup from its source file.
4. Verify responsive reflow and keyboard interaction.
5. Test light and dark themes.
6. Run the Flux check from the prototype's folder and fix every finding: npx flux-check --prototype . where @kaptio/flux-tokens is installed, otherwise curl -fsSL https://flux.kaptio.com/tokens/v2/check.mjs -o /tmp/flux-check.mjs && node /tmp/flux-check.mjs --prototype . It fails on hand-built surfaces, restyled components, component-like class names and Flux not loaded from the published URL, as well as on every raw value. A finding is fixed by using the component, never by renaming a class or moving a style somewhere the check does not look. If one is genuinely correct, annotate it with the reason as described in llms.txt.

Do not optimise the prototype to fit into one screenshot. Optimise it for the user completing the task.`
## Fill the context
Flux controls the interface language. These fields tell the agent what the interface must accomplish.

Do

- Name one primary user and the task they need to complete.
- List required empty, loading, error and success states when they matter.
- Provide representative data shapes and real business constraints.
- Keep the requested workflow narrow enough to verify.Don’t

- Do not ask for a generic dashboard without naming the user’s task.
- Do not use a screenshot as the only statement of hierarchy.
- Do not ask the agent to fit the whole workflow into one viewport.
- Do not add a second visual taste system on top of Flux.
## Product or deck
Choose one contract. The two surfaces deliberately use different composition rules.

This prompt is for product interfaces and operational prototypes. For a presentation, use the [deck brief](/decks/brief.txt) instead. Never paste both contracts into the same request: the agent will average rules that are intentionally different.

[PreviousRepository rules](/for-ai/rules/)[NextSlack teammates](/for-ai/slack/)
