# Flux — /components/metric/

Source: https://flux.kaptio.com/components/metric/

Component

# Metric
Headline figures with a label and a change, aligned on one surface. The top of a dashboard.

Plain-text source, for agents and clipboard use: [/components/source/metric.txt](/components/source/metric.txt)

## When to use it
Shows the few numbers that say how something is going — berths sold, revenue booked, bookings waiting on a supplier — with how each has moved. Related metrics share one surface and one grid, so their labels, values and changes line up and read as a set rather than as separate cards competing for attention.

Not thisNot for the attributes of one record; that is a Description list. Not for comparing many rows; that is a Table. If a figure has no comparison and nobody acts on it, it probably does not belong at the top of the page.
## Examples

### Metric row
Four related figures on one surface. Bookings on request rising is bad news, so its upward change is negative; cancellations falling is neutral because nobody needs to act.

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

htmlCopy`

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

`
### Without changes
When there is no meaningful comparison period, leave the change out. The values still align.

Departures this week
23

Travellers
412

Guides assigned
19 of 23

htmlCopy`

Departures this week
23

Travellers
412

Guides assigned
19 of 23

`
## Anatomy
PartDescriptionRowA dl on layer-01 with a hairline border and card padding. Columns fit the width and wrap.LabelA dt naming the figure, in text-secondary. Short enough to stay on one line.ValueA dd with the figure and its unit, in tabular figures and text-brand. Lexend Bold at text-4xl; Google Sans Flex Bold in a prototype.ChangeOptional dd: an arrow, the signed change and its comparison period. Coloured by what the change means, not by its direction.
## API
NameKindDescription`flux-metrics`classThe dl and its surface. Lays out metrics in columns of at least --flux-metric-min-width that wrap. Inside a flux-card it drops its border, fill and padding, because the card is already the surface.`flux-metric`classOne metric: a div holding one dt and one or two dd. Spans three subgrid rows so parts align across the row.`flux-metric__label`classThe dt naming the figure.`flux-metric__value`classThe dd holding the figure, on one line. Include the unit: a symbol such as % inline, a currency code or unit word in flux-metric__unit before the figure.`flux-metric__unit`classA span inside the value for a currency code or unit word, set at label size so the figure keeps the weight.`flux-metric__change`classOptional dd: an aria-hidden arrow svg, the signed change in a span, then flux-metric__context.`data-tone`attributeOn the change: positive or negative, by meaning. Leave it off for a neutral change.`flux-metric__context`classThe comparison period, such as "vs last week". Required whenever there is a change.
## States
StateTreatmentNeutral changetext-secondary. The default; most changes need no colour.Positivetext-success, for a change that is good news.Negativetext-error, for a change that needs someone to act.
## Keyboard
KeysAction`—`Not interactive. If a metric opens a report, put a link in the label rather than making the whole tile a button.
## Accessibility

- Use dl, dt and dd so each figure is announced with its label.
- Colour is never the only signal: the arrow shows direction and the signed text states it, so a change reads correctly without the tint.
- Write the sign and unit into the text, as "+3.2 pts" or "−1". A bare number gives no direction to a screen reader.
- Name the row with a heading above it when the page has more than one set of metrics.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-metric-min-width
- --flux-metric-padding
- --flux-metric-gap-x | -gap-y | -part-gap
- --flux-metric-bg | -border | -radius
- --flux-metric-label-color | -label-size
- --flux-metric-value-color | -value-size | -value-tracking
- --flux-metric-change-size | -neutral | -positive | -negative
- --flux-metric-icon-size
## Do and don’t
Do

- Show three to five metrics. More than that and none of them is headline.
- Use one comparison period across the row, so the changes can be compared.
- Decide the tone from the consequence: rising cancellations are negative even though the arrow points up.
- Keep related metrics on one surface, and put the work they point to — the exceptions table — directly below.Don’t

- Do not give every metric its own card. One surface groups them; the important change carries the emphasis.
- Do not wrap the row in a second bordered box. Inside a card it drops its own surface and uses the card’s; do not add vertical dividers between metrics either.
- Do not colour a change just because it moved. Neutral is the default.
- Do not add a coloured bar, icon tile or sparkline to each metric as decoration.
- Do not shrink the value to fit more metrics in a row. Let the row wrap.[PreviousDescription list](/components/description-list/)[NextChart](/components/chart/)
