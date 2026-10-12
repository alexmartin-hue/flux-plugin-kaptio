# Flux — /patterns/dashboards/

Source: https://flux.kaptio.com/patterns/dashboards/

Patterns

# Dashboards
A dashboard answers two questions in order: how are things going, and what needs me now. Everything on the page serves one of those, and the second is usually the one people came for.

## The recipe
Page header, one metric row, then the exceptions as a table.

# September operations

Capacity, revenue and the departures that need someone today.

Export report

## At a glance

Berths sold
79.7%
+3.2 pts vs last week

Revenue booked
ISK48.2m
+6.1% vs last week

Bookings on request
14
+5 since Monday

Cancellations
3
−1 vs last week

## Needs attention

Reference
Departure
Issue
Status
Pax

KB-104931
Golden Circle, 14 Sep
Guide not assigned
On request
12

KB-104940
South Coast, 19 Sep
Hotel Kea has not confirmed
Awaiting supplier
2

KB-104963
Diamond Circle, 28 Sep
Balance overdue
On request
8

htmlCopy`

September operations
Capacity, revenue and the departures that need someone today.

Export report

At a glance

Berths sold
79.7%
+3.2 pts vs last week

Revenue booked
ISK48.2m
+6.1% vs last week

Bookings on request
14
+5 since Monday

Cancellations
3
−1 vs last week

Needs attention

Reference
Departure
Issue
Status
Pax

KB-104931
Golden Circle, 14 Sep
Guide not assigned
On request
12

KB-104940
South Coast, 19 Sep
Hotel Kea has not confirmed
Awaiting supplier
2

KB-104963
Diamond Circle, 28 Sep
Balance overdue
On request
8

`Every part is a documented component: the [Metric](/components/metric/) row, the [Table](/components/table/) and the [Badge](/components/badge/). The only layout is a grid with `--flux-seam-gap` between sections. Copy it, replace the figures, and keep the order.

## Order of the page
Status first, work second, detail on demand.

- Page header. A title that names the scope and period — "September operations", not "Dashboard" — and one line saying what the page is for. Page-level actions such as export sit at the end of the header row.
- Metric row. Three to five figures on one surface, each with the same comparison period. This is the only place for headline numbers.
- The exceptions. The records someone has to act on, as a table with a status badge and the reason in words. If nothing needs attention, say so in the table’s empty state rather than hiding the section.
- Everything else. Full lists and reports belong on their own pages, linked from the metric or the section heading, not stacked below.cssCopy`.dashboard {
display: grid;
gap: var(--flux-seam-gap);
}`
## Choosing metrics
A metric earns its place if someone would act differently when it moves.

- Three to five. Past five, none of them is headline and the row wraps into a grid nobody reads.
- One comparison period. "vs last week" on every change, so the changes can be compared with each other.
- Units in the value. "ISK 48.2m", "79.7%", "19 of 23". A bare number makes the reader guess.
- Counts that lead to work. "Bookings on request: 14" is useful because the table below lists them.
## Tone of a change
Colour follows the consequence, not the arrow.

An arrow shows direction; the tone says whether that direction is good. More bookings on request is an upward arrow and negative news. Fewer cancellations is a downward arrow, and usually needs no colour at all because nobody has to act. Leave a change neutral unless the colour tells someone something.

CarefulIf every change on the row is green or red, the colour has stopped meaning anything. Most changes should be neutral, so the one that is not is seen.
## Charts
Below the metrics, at full width, saying what it shows.

If a dashboard needs a trend or a share, use the [Chart](/components/chart/)component below the metric row, at full width. Its caption states the takeaway in a sentence, and its series take the --flux-chart-* roles, so it re-colours with the theme. Do not bring in a chart library’s default palette.

## Do and don’t
Do

- Name the scope and period in the page title.
- Keep headline figures in one Metric row on one surface.
- Put the records that need action directly below the metrics.
- State the reason for each exception in words, beside its status badge.
- Leave changes neutral unless the colour tells someone to act.Don’t

- Do not give every figure its own card.
- Do not show more than five metrics at the top.
- Do not add icon tiles, coloured bars or sparklines to metrics as decoration.
- Do not stack full reports below the exceptions. Link to them.
- Do not shrink type or spacing to fit the whole dashboard above the fold.[PreviousForms](/patterns/forms/)[NextDecks](/patterns/decks/)
