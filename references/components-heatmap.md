# Flux — /components/heatmap/

Source: https://flux.kaptio.com/components/heatmap/

Component

# Heatmap
A matrix of values on one sequential scale, where every cell can be focused and opened for its detail.

Plain-text source, for agents and clipboard use: [/components/source/heatmap.txt](/components/source/heatmap.txt)

## When to use it
Shows where values run high or low across two dimensions at once: occupancy by tour and month, a P&L line by period, a slice of usage by team and week. It is a real table, so the row and column headers name every cell, and each value is a button filled with one step of a five-step teal ramp and printed in the cell, so the colour is never the only way to read it. The grid is one tab stop: the arrow keys move between cells, and activating one opens its detail, typically in a Drawer.

Not thisNot for a single series over time; use a Chart. Not for values that are categories rather than amounts, such as a status per day; use a Table with Badges. Not when people need to edit the values; use Editable cells in a Table. Not for more than about twelve columns at once; aggregate, or let the table scroll horizontally.
## Examples

### Occupancy by tour and month
Tab into the grid, move with the arrow keys and press Enter, or click a cell: the drawer opens on that tour and month. Empty cells are tours that do not run that month.

### Occupancy by tour and month

Every tour peaks in July and August. Westfjords and the Highlands stay below 80% outside them.

AprMayJunJulAugSep

Golden Circle72%81%88%94%96%85%
South Coast64%75%86%91%93%79%
Snæfellsnes48%62%77%85%88%66%
Westfjords–No departures41%58%73%76%52%
Highlands–No departures–No departures69%82%87%54%

- Under 50%

- 50–64%

- 65–79%

- 80–89%

- 90% and over

## Golden Circle

Apr · 72% occupancy

TourGolden Circle
MonthApr
Occupancy72%

Close
[Open departures](#)

htmlCopy`

Occupancy by tour and month
Every tour peaks in July and August. Westfjords and the Highlands stay below 80% outside them.

AprMayJunJulAugSep

Golden Circle72%81%88%94%96%85%
South Coast64%75%86%91%93%79%
Snæfellsnes48%62%77%85%88%66%
Westfjords–No departures41%58%73%76%52%
Highlands–No departures–No departures69%82%87%54%

Under 50%
50–64%
65–79%
80–89%
90% and over

Golden Circle
Apr · 72% occupancy

TourGolden Circle
MonthApr
Occupancy72%

Close
Open departures

`
## Anatomy
PartDescriptionCaptionA heading naming what is measured and a sentence stating the pattern, as on a Chart.TableA table labelled by the heading. Column headers with scope="col" in mono, row headers with scope="row".CellA button per value with data-step from 1 to 5, filled with chart-sequential-<step> and printed in chart-sequential-text-<step>, audited at 4.5:1 in every theme.Empty cellA span with no fill, a dash and hidden text, for a combination with no value, so it never reads as a low one. It is skipped by the arrow keys.KeyBelow the table, a swatch and the range of each step, such as "80–89%".DetailA Drawer the cells open with commandfor. Elements in it with data-flux-heatmap-field="row", "column" or "value" are filled from the cell before it opens.
## API
NameKindDescription`flux-heatmap`classOn a figure, with data-flux-heatmap. It has no surface of its own; place it in a card or a section.`data-flux-heatmap`attributeBinds the arrow keys, the roving tabindex and the detail fields. Requires flux-components.js.`flux-heatmap__header | __title | __summary`classThe figcaption, its heading and the pattern in words.`flux-heatmap__scroll | __table`classThe horizontal scroll container and the table, labelled with aria-labelledby.`flux-heatmap__cell`classA button per value with data-step, an aria-label naming the row, the column and the value, and tabindex="0" on the first cell and "-1" on the rest.`data-step`attribute1 to 5, on a cell or a key swatch: the step of the sequential scale.`flux-heatmap__empty`classA span in a cell with no value.`flux-heatmap__key | __swatch`classThe scale key and its swatches.`data-flux-heatmap-field`attribute"row", "column" or "value", on elements in the dialog a cell opens.`flux-heatmap-select`elementEvent dispatched from the heatmap when a cell is activated, with detail.row, detail.column, detail.value and detail.cell, for loading the record behind it.
## States
StateTreatmentStepschart-sequential-1 to -5, lightest to darkest in light and darkest to lightest in dark and deep, so a high value always stands out most from the page. On deep the ramp steps around the teal ground.HoverAn inset ring in border-strong.FocusThe Flux focus ring, raised over the neighbouring cells.EmptyNo fill, a dash in text-secondary, and "No departures" or similar in hidden text.
## Keyboard
KeysAction`Tab`Moves into the grid, to the last cell used, and out again.`Arrow keys`Move one cell in that direction, skipping empty cells.`Home / End`Move to the first or last cell in the row.`Ctrl + Home / Ctrl + End`Move to the first or last cell in the grid. ⌘ on macOS.`Enter / Space`Opens the cell’s detail.
## Accessibility

- A native table with scoped headers, so screen readers can also move by row and column with their own table commands.
- Each cell button names its row, column and value in its aria-label: "Golden Circle, Jul: 94%".
- The value is printed in every cell; the colour is a second signal, never the only one.
- The detail opens in a Drawer on the native dialog, so focus moves into it and returns to the cell when it closes.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-chart-sequential-1 to -5 and --flux-chart-sequential-text-1 to -5 (Tier 2)
- --flux-heatmap-cell-height | -cell-min-width | -cell-gap | -cell-padding-x
- --flux-heatmap-header | -row-header | -empty-text | -hover-ring | -key-swatch
## Do and don’t
Do

- State the pattern in the summary sentence, so nobody has to scan the grid to find it.
- Choose step boundaries that mean something to the reader, and say them in the key.
- Open the detail with the cell’s context in its title: the row, then the column.Don’t

- Do not use status or product colours as steps. The ramp is one teal, low to high.
- Do not hide the values to make the grid look cleaner.
- Do not put two measures in one heatmap. Make two.[PreviousChart](/components/chart/)[NextTimeline](/components/timeline/)
