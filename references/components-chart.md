# Flux — /components/chart/

Source: https://flux.kaptio.com/components/chart/

Component

# Chart
Columns, lines, ranked bars and a donut, drawn from theme roles with a title, a takeaway and a legend.

Plain-text source, for agents and clipboard use: [/components/source/chart.txt](/components/source/chart.txt)

## When to use it
Shows a trend, a comparison or a share that a table of numbers would make someone work out. Each chart is built from lists and inline SVG rather than a library, so every mark takes a theme role and re-colours with the theme. Series take --flux-chart-1 to -4 in order, and --flux-chart-muted for the comparison, such as last year. The caption states the takeaway in words, so the chart is evidence for a sentence rather than a puzzle.

Not thisNot for one figure; use a Metric. Not for exact values someone will copy or act on; use a Table, or put one beside the chart. Not for more than four series; split the chart or rank the values as bars. Not for decoration on a metric, such as a sparkline in every tile.
## Examples

### Columns, compared with last year
Two series per month. The values are in visually hidden text inside each column, so a screen reader hears "Jul, 2026: 281, 2025: 248".

### Bookings by month

Every month is ahead of last year. July is the peak, at 281.

- 0

- 100

- 200

- 300

Apr

2026: 142
2025: 128

May

2026: 188
2025: 171

Jun

2026: 236
2025: 219

Jul

2026: 281
2025: 248

Aug

2026: 264
2025: 259

Sep

2026: 212
2025: 189

- 2026

- 2025

htmlCopy`

Bookings by month
Every month is ahead of last year. July is the peak, at 281.

0
100
200
300

Apr

2026: 142
2025: 128

May

2026: 188
2025: 171

Jun

2026: 236
2025: 219

Jul

2026: 281
2025: 248

Aug

2026: 264
2025: 259

Sep

2026: 212
2025: 189

2026
2025

`
### Line
A trend over time, on the same frame. Points sit at the centre of each month, with y as a share of the scale. The comparison is dashed as well as muted, so it does not depend on colour.

### Occupancy

Seats sold as a share of seats offered. August peaked at 91%, five points above last year.

- 0%

- 25%

- 50%

- 75%

- 100%

- Apr

- May

- Jun

- Jul

- Aug

- Sep

- 2026

- 2025

htmlCopy`

Occupancy
Seats sold as a share of seats offered. August peaked at 91%, five points above last year.

0%
25%
50%
75%
100%

Apr
May
Jun
Jul
Aug
Sep

2026
2025

`
### Ranked bars
One series, largest first, each value labelled at the end of its row. The bars scale to the largest value, so no axis is needed.

### Revenue by tour, September

Golden Circle earns more than the two smallest tours together.

Golden Circle

€412k

South Coast

€318k

Snæfellsnes

€196k

Westfjords

€88k

htmlCopy`

Revenue by tour, September
Golden Circle earns more than the two smallest tours together.

Golden Circle

€412k

South Coast

€318k

Snæfellsnes

€196k

Westfjords

€88k

`
### Donut
Shares of one whole. The ring’s circumference is 100, so each segment’s dash is its percentage and its offset is the total of the segments before it. The legend carries the values.

### Bookings by channel

Almost half of this season’s 1,322 bookings came direct.

- Direct48%

- Agents27%

- Online travel agencies15%

- Other10%

htmlCopy`

Bookings by channel
Almost half of this season’s 1,322 bookings came direct.

Direct48%
Agents27%
Online travel agencies15%
Other10%

`
## Anatomy
PartDescriptionFigureflux-chart on a figure. It has no surface of its own; place it in a card or a section.CaptionA heading naming what is measured, and a summary sentence stating the takeaway.FrameThe scale at the start side, gridlines across the plot, a baseline in border-strong, and the category labels below.LegendBelow the plot, a swatch and name per series. Beside the ring on a donut, with the values. Omit it for a single series the title already names.MarksColumns, lines, bars or ring segments. data-series picks the colour; the value arrives as --flux-value, a percentage of the scale.
## API
NameKindDescription`flux-chart`classOn the figure.`flux-chart__header | __title | __summary`classThe figcaption, its heading and the takeaway sentence.`flux-chart__legend | __swatch | __swatch--line | __legend-value`classThe legend list, a square or line key, and a value beside a legend name.`flux-chart__frame | __scale | __categories`classThe plot frame, its tick list (lowest first, aria-hidden) and the category labels below.`flux-chart__columns | __bars | __column | __category`classColumns: one list item per category, holding its label and its columns.`flux-chart__lines`classAn SVG with viewBox="0 0 100 100" and preserveAspectRatio="none", holding one polyline per series, role="img" and an aria-label with the values.`flux-chart__rows | __label | __bar | __value`classRanked bars: one list item per row, with its label, bar and value.`flux-chart__donut | __ring | __track`classThe donut and its legend, the SVG ring, and the empty ring under the segments.`data-series`attribute1, 2, 3, 4 or muted, on every mark and swatch.`--flux-value`attributeInline, on a column or bar: its value as a percentage of the scale’s top tick.
## States
StateTreatmentSeries colourschart-1 teal, chart-2 purple, chart-3 magenta, chart-4 ochre, and chart-muted grey for the comparison. Each clears 3:1 against every layer in light, dark and deep.Comparisonchart-muted, drawn after the current series in each group, and dashed on a line.EmptyReplace the plot with an Empty state that says what is missing; never draw an empty frame.
## Keyboard
KeysAction`None`A chart is not interactive. Put any controls, such as a period picker, beside it as ordinary fields.
## Accessibility

- The summary sentence states the takeaway, so nobody has to read the shape to get the point.
- Every value is available as text: hidden text in columns, visible labels on bars and in the donut legend, and the aria-label on a line chart. Scales are aria-hidden, because the values are already read.
- Colour is never the only signal: series are named in the legend, ordered the same way in every group, and the comparison line is dashed.
- Chart roles clear 3:1 against every layer, as WCAG 1.4.11 requires for graphics needed to understand the content.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-chart-1 | -2 | -3 | -4 | -muted (Tier 2)
- --flux-chart-gap | -plot-height | -scale-width | -headroom | -column-gap | -bar-width | -row-bar-height
- --flux-chart-grid | -axis | -label | -track | -legend-gap | -swatch-size
- --flux-chart-line-width | -line-dash | -donut-size | -donut-stroke
## Do and don’t
Do

- State the takeaway in the summary sentence.
- Start column and bar scales at zero.
- Use series colours in order, and the muted colour for the comparison.
- Place a chart below the metric row at full width, as the Dashboards pattern describes.Don’t

- Do not bring in a chart library’s palette, gradients or animations.
- Do not use product accents or status colours as series; a red series reads as an error.
- Do not draw more than four series, or a donut with more than five segments.
- Do not use a chart for a single number. Use a Metric.[PreviousMetric](/components/metric/)[NextTimeline](/components/timeline/)
