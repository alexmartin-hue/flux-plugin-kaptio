# Flux — /components/table/

Source: https://flux.kaptio.com/components/table/

Component

# Table
Quiet data table. Horizontal dividers only, tabular figures, badge status cells.

Plain-text source, for agents and clipboard use: [/components/source/table.txt](/components/source/table.txt)

## When to use it
Presents rows of comparable records. Flux tables are deliberately quiet — the data carries the visual weight, and the chrome recedes to horizontal hairlines.

Not thisDo not use a table for layout. For a small number of records with heterogeneous content, a list of cards reads better and adapts to narrow screens.
## Examples

### Default

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
## Anatomy
PartDescriptionWrapperBordered, rounded surface that also provides horizontal scroll.HeaderMono, uppercase, extra-small, letter-spaced, in text-subtle.RowsDivided by a single hairline. The last row has none.Numeric columnsRight-aligned with tabular figures so digits line up.
## API
NameKindDescription`flux-table-wrap`classBordered surface and scroll container. Always wrap the table.`flux-table`classThe table element itself.`data-numeric`attributeRight-aligns and applies tabular figures. Put it on both th and td.`scope`attributeRequired on every header cell so the header/data relationship is programmatic.
## States
StateTreatmentRow hoverlayer-hover-01 fill across the row.Last rowBottom divider removed.
## Keyboard
KeysAction`Tab`Moves through interactive cells only. A static table is not a tab stop.
## Accessibility

- Every header cell needs scope="col" or scope="row"; without it the table is a grid of unrelated cells to a screen reader.
- Give the table a caption or an aria-label when its purpose is not obvious from surrounding copy.
- Status is announced from the badge text, not inferred from the tint.
- The wrapper scrolls horizontally on narrow screens rather than shrinking text below the minimum readable size.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-table-cell-padding-y
- --flux-table-cell-padding-x
- --flux-table-divider
- --flux-table-header-text
- --flux-table-row-hover
## Do and don’t
Do

- Right-align money, quantities and dates that are compared down a column.
- Use the Badge component for status cells.
- Keep reference codes in Lexend Light so they do not compete with the data.Don’t

- Do not add vertical column borders or a border on every cell.
- Do not zebra-stripe and divide at the same time; choose one.
- Do not invent status colours that differ from the badge set.[PreviousBadge](/components/badge/)[NextModal](/components/modal/)
