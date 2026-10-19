# Flux — /components/table/

Source: https://flux.kaptio.com/components/table/

Component

# Table
Quiet data table with sorting, selection, expandable rows, row actions, a toolbar and sticky columns.

Plain-text source, for agents and clipboard use: [/components/source/table.txt](/components/source/table.txt)

## When to use it
Presents rows of comparable records. Flux tables are deliberately quiet — the data carries the visual weight, and the chrome recedes to horizontal hairlines. The same markup scales from a static list to a working data table: add the toolbar, sort buttons, selection and row actions you need, and flux-components.js wires them together.

Not thisDo not use a table for layout. For a small number of records with heterogeneous content, a list of cards reads better and adapts to narrow screens. For a spreadsheet where every cell is editable, a grid with role="grid" is a different component.
## Examples

### Default
A static table. No script is needed.

Bookings departing in September

Reference
Departure
Status
Pax
Total

KB-104928
Reykjavik → Akureyri, 12 Sep
Confirmed
4
486,000

KB-104931
Golden Circle, 14 Sep
On request
12
1,240,500

KB-104940
South Coast, 19 Sep
Awaiting supplier
2
198,000

htmlCopy`

Bookings departing in September

Reference
Departure
Status
Pax
Total

KB-104928
Reykjavik → Akureyri, 12 Sep
Confirmed
4
486,000

KB-104931
Golden Circle, 14 Sep
On request
12
1,240,500

KB-104940
South Coast, 19 Sep
Awaiting supplier
2
198,000

`
### Compact
40px rows for dense operational views. Type stays at the same size; only the row height and vertical padding change.

Supplier confirmations

Supplier
Service
Status
Rooms

Hotel Kea
Twin, half board
Confirmed
8

Fosshotel Hekla
Double, breakfast
Awaiting supplier
6

Hótel Búðir
Single, breakfast
Unavailable
2

htmlCopy`

Supplier confirmations

Supplier
Service
Status
Rooms

Hotel Kea
Twin, half board
Confirmed
8

Fosshotel Hekla
Double, breakfast
Awaiting supplier
6

Hótel Búðir
Single, breakfast
Unavailable
2

`
### Data table
Everything together: search, a status filter, a More filters panel, removable filter chips with Clear all, a column menu, sortable headers, selection with a bulk-action bar, expandable rows, one visible row action with an overflow menu, and a sticky header and leading columns. Requires flux-components.js. Remove any part you do not need; the rest keeps working.

## September departures

6 of 6 departures

0 selected

Send manifests
Clear selection

Search departures

Status

All statuses

- All statuses

- Confirmed

- On request

- Awaiting supplier

- Cancelled

More filters

### More filters

Route

All routes

- All routes

- Reykjavik → Akureyri

- Golden Circle

- South Coast

- Snæfellsnes

- Westfjords

- Diamond Circle

Guide

All guides

- All guides

- Anna Jónsdóttir

- Unassigned

- Kári Pétursson

- Sara Björk

Columns

Route
Departure
Status
Pax
Total

Clear all

Details
Reference
Route
Departure
Status
Pax
Total
Actions

KB-104928
Reykjavik → Akureyri
12 Sep 2026
Confirmed
4
486,000

Manage

Duplicate
Send manifest
Cancel departure

GuideAnna Jónsdóttir
VehicleCoach 18
Balance due0

KB-104931
Golden Circle
14 Sep 2026
On request
12
1,240,500

Manage

Duplicate
Send manifest
Cancel departure

GuideUnassigned
VehicleCoach 32
Balance due620,250

KB-104940
South Coast
19 Sep 2026
Awaiting supplier
2
198,000

Manage

Duplicate
Send manifest
Cancel departure

GuideKári Pétursson
VehicleMinibus 9
Balance due99,000

KB-104952
Snæfellsnes
21 Sep 2026
Confirmed
16
1,612,000

Manage

Duplicate
Send manifest
Cancel departure

GuideSara Björk
VehicleCoach 18
Balance due0

KB-104957
Westfjords
26 Sep 2026
Cancelled
0
0

Manage

Duplicate
Send manifest
Cancel departure

Guide—
Vehicle—
Balance due0

KB-104963
Diamond Circle
28 Sep 2026
On request
8
904,000

Manage

Duplicate
Send manifest
Cancel departure

GuideUnassigned
VehicleMinibus 16
Balance due452,000

No departures match the search and filters.

htmlCopy`

September departures
6 of 6 departures

0 selected
Send manifests
Clear selection

Search departures

Status

All statuses

All statuses
Confirmed
On request
Awaiting supplier
Cancelled

More filters

More filters

Route

All routes

All routes
Reykjavik → Akureyri
Golden Circle
South Coast
Snæfellsnes
Westfjords
Diamond Circle

Guide

All guides

All guides
Anna Jónsdóttir
Unassigned
Kári Pétursson
Sara Björk

Columns

Route
Departure
Status
Pax
Total

Clear all

Details
Reference
Route
Departure
Status
Pax
Total
Actions

KB-104928
Reykjavik → Akureyri
12 Sep 2026
Confirmed
4
486,000

Manage

Duplicate
Send manifest
Cancel departure

GuideAnna Jónsdóttir
VehicleCoach 18
Balance due0

KB-104931
Golden Circle
14 Sep 2026
On request
12
1,240,500

Manage

Duplicate
Send manifest
Cancel departure

GuideUnassigned
VehicleCoach 32
Balance due620,250

KB-104940
South Coast
19 Sep 2026
Awaiting supplier
2
198,000

Manage

Duplicate
Send manifest
Cancel departure

GuideKári Pétursson
VehicleMinibus 9
Balance due99,000

KB-104952
Snæfellsnes
21 Sep 2026
Confirmed
16
1,612,000

Manage

Duplicate
Send manifest
Cancel departure

GuideSara Björk
VehicleCoach 18
Balance due0

KB-104957
Westfjords
26 Sep 2026
Cancelled
0
0

Manage

Duplicate
Send manifest
Cancel departure

Guide—
Vehicle—
Balance due0

KB-104963
Diamond Circle
28 Sep 2026
On request
8
904,000

Manage

Duplicate
Send manifest
Cancel departure

GuideUnassigned
VehicleMinibus 16
Balance due452,000

No departures match the search and filters.

`
## Anatomy
PartDescriptionWrapperBordered, rounded surface that also provides horizontal scroll. With --sticky it bounds the height so the header can stay in view.ToolbarTitle and live count on the left; search, the most-used filters, a More filters panel and the column menu on the right. Replaced by the bulk-action bar while rows are selected.Filter chipsOne removable chip per active filter, below the toolbar, then Clear all. Hidden while no filter is active.HeaderMono, uppercase, extra-small, letter-spaced, in text-subtle. Sortable headers hold a button and an arrow.Row headerThe cell that names the record, usually its reference: th scope="row", body type, bold.Control columnsSelection checkbox and expand chevron, before the row header.Rows48px, divided by a single hairline. 40px with --compact.Detail rowHidden until expanded. Shares a tbody with its row so they sort and filter together.Row actionsOne visible action and an overflow menu for the rest, in the last column.
## API
NameKindDescription`flux-table-wrap`classBordered surface and scroll container. Always wrap the table.`flux-table-wrap--sticky`classBounds the wrapper height so a sticky header has something to stick within.`flux-table`classThe table element itself.`flux-table--compact`class40px rows instead of 48px. Type size is unchanged.`flux-table--sticky-header`classKeeps the header row in view while the wrapper scrolls. Pair with flux-table-wrap--sticky.`flux-table--sticky-first`classPins every column up to and including the row header during horizontal scroll. Offsets are measured by flux-components.js.`scope`attributeRequired on every header cell: scope="col" in the head, scope="row" on the cell that names each record.`data-numeric`attributeRight-aligns and applies tabular figures. Put it on both th and td. A sortable numeric column sorts by number.`caption`elementNames the table. Add flux-visually-hidden when a visible heading already does, or use aria-labelledby.`data-flux-table`attributeOn the element wrapping the toolbar and table. Initialises every behaviour below.`flux-table__sort`classButton inside a sortable th. The th carries aria-sort="none", which the script updates to ascending or descending.`flux-sort`elementCancelable event dispatched on the data-flux-table element before a sort, with detail.column (the th’s data-column), detail.index and detail.direction. A framework that renders the rows cancels it and renders the order and aria-sort from detail; the table still announces the sort.`data-wrap`attributeLets a prose cell wrap. Body cells are single-line by default so rows keep their height and the wrapper scrolls instead.`data-sort-value`attributeOn a cell whose text does not sort correctly, such as a formatted date. Use an ISO date or a plain number.`data-column`attributeNames a header so filters and the column menu can find its column.`flux-table__control`classNarrow cell for the selection checkbox or the expand toggle.`flux-checkbox`classFlux-sized native checkbox. Add flux-table__select on row checkboxes.`data-flux-table-select-all`attributeHeader checkbox. Selects visible rows and shows a mixed state when some are selected.`flux-table__toggle`classExpand button with aria-expanded and aria-controls pointing at the detail row.`flux-table__detail`classHidden detail row with one cell spanning every column. Put it in the same tbody as its row.`flux-table__actions`classLast cell, holding flux-table__action-group: one ghost small button and the overflow trigger.`flux-table__icon-button`classIcon-only table control for the toggle and overflow trigger. Always give it an aria-label naming the row.`flux-menu`classPopover menu with role="menu", opened by a button with popovertarget, aria-haspopup="menu" and aria-expanded. A text trigger ends in flux-button__chevron.`flux-menu__item`classA button with role="menuitem", or role="menuitemcheckbox" with aria-checked and a flux-menu__check icon.`flux-table-toolbar`classRow above the wrapper: __summary (title and count), __bulk (selection actions, hidden until rows are selected) and __controls.`data-flux-table-count`attributeOn the count element. Its value is the noun, as in "4 of 6 departures".`data-flux-table-search`attributeSearch input. Matches against the text of each record row.`data-flux-table-filter`attributeOn a Flux select whose value filters the column named by the attribute. An empty value means all. A name with no matching column filters on that data attribute of the record row instead, as data-flux-table-filter="guide" matches data-guide.`flux-filter-panel`classPopover with role="dialog" for filters used less often, opened by a secondary button with popovertarget, aria-haspopup="dialog" and aria-expanded. Holds a flux-filter-panel__title and Flux selects with data-flux-table-filter. Filters apply as they change; there is no Apply button.`data-flux-table-chips`attributeOn flux-filter-chips, placed below the toolbar and hidden. Holds an empty flux-filter-chips__list with aria-label="Active filters" and the Clear all button. The script writes one flux-chip per active filter.`flux-chip`classA removable filter chip: a button reading "Label: value" with a cross. Written by the script; use it by hand only for filters the table script does not own.`data-flux-table-clear-filters`attributeClear all button inside the chips row. Resets search and every filter.`data-flux-table-column`attributeOn a menuitemcheckbox. Shows or hides the column with the matching data-column.`data-flux-table-status`attributeVisually hidden live region. Announces sorting, filtering and selection changes.`data-flux-table-empty`attributeA hidden tbody shown when search and filters leave no rows.`flux-visually-hidden`classRead by assistive technology, not drawn. For captions, header names and icon labels.
## States
StateTreatmentRow hoverlayer-hover-01 fill across the row.Selectedsurface-selected fill across the row, driven by its checkbox. The checkbox carries the state; the fill only echoes it.SortedThe header text darkens and a single arrow in icon-brand shows the direction. Unsorted headers show both arrows.ExpandedThe chevron turns down and the detail row appears on layer-02.Bulk selectionThe toolbar summary is replaced by the selection count and bulk actions.FilteredEach active search or filter shows as a chip on surface-selected below the toolbar; the border turns border-interactive on hover. Removing a chip resets that control.No resultsThe empty tbody replaces the rows, in text-secondary.
## Keyboard
KeysAction`Tab`Moves through interactive cells only: checkboxes, toggles, sort buttons, row actions. A static table is not a tab stop.`Enter / Space`Sorts by the focused header, toggles the focused checkbox or expands the focused row.`Arrow Up / Down, Home, End`Move between items in an open menu.`Escape`Closes an open menu or the More filters panel and returns focus to its trigger.`Enter / Space on a chip`Removes that filter and moves focus to the next chip, or to search when none remain.
## Accessibility

- Every header cell needs scope="col" or scope="row"; without it the table is a grid of unrelated cells to a screen reader.
- Name the table with a caption or aria-labelledby pointing at the toolbar title.
- Sort state is aria-sort on the th, not the arrow. Only sortable headers carry it.
- Icon-only controls name their row: "Details for KB-104928", "More actions for KB-104928".
- Selection is the checkbox state. The row fill is a second signal, never the only one.
- The live region announces sort order, result counts and selection, so changes that happen away from focus are heard.
- Each chip is named "Remove filter Status: Confirmed", so its purpose is clear without the cross. Removing one never drops focus to the page.
- Status is announced from the badge text, not inferred from the tint.
- The wrapper scrolls horizontally on narrow screens rather than shrinking text below the minimum readable size.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-table-cell-padding-y
- --flux-table-cell-padding-x
- --flux-table-row-height | -compact
- --flux-table-divider
- --flux-table-header-text
- --flux-table-header-bg
- --flux-table-row-hover
- --flux-table-row-selected
- --flux-table-detail-bg
- --flux-table-control-width
- --flux-table-icon | -hover | -hover-bg
- --flux-table-sort-icon-active
- --flux-table-sticky-max-height
- --flux-menu-bg | -border | -shadow | -item-hover
- --flux-chip-height | -bg | -text | -border | -border-hover | -icon
- --flux-filter-panel-width | -padding | -gap
## Do and don’t
Do

- Right-align money, quantities and dates that are compared down a column.
- Use the Badge component for status cells.
- Make the reference a row header, so every cell in the row is announced with it.
- Keep one visible action per row and put the rest in the overflow menu, so action columns line up.
- Make only the columns people actually compare sortable.
- Keep the one or two filters people use most in the toolbar and put the rest in More filters; the chips show what is active either way.Don’t

- Do not add vertical column borders or a border on every cell.
- Do not zebra-stripe and divide at the same time; choose one.
- Do not invent status colours that differ from the badge set.
- Do not shrink type to fit more columns. Use compact rows, hide columns or let the wrapper scroll.
- Do not offer the row header in the column menu; a row must always say what it is.[PreviousBadge](/components/badge/)[NextAction menu](/components/menu/)
