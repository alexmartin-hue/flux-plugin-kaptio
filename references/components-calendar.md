# Flux — /components/calendar/

Source: https://flux.kaptio.com/components/calendar/

Component

# Calendar view
A month of departures, bookings or deadlines laid out on the days they fall.

Plain-text source, for agents and clipboard use: [/components/source/calendar.txt](/components/source/calendar.txt)

## When to use it
Shows when things happen across a month, so a planner can see the busy weeks, the gaps and the departure that needs attention. It is a table: weekdays are column headers, each cell is a day, and each event is a link to its record. Days outside the month are muted, today is marked, and events that need action carry the warning tone, an icon and hidden text, never colour alone.

Not thisNot for choosing a date in a form; use the Date picker. Not for a sequence of days in one trip; use the Itinerary. Not when the dates matter less than the records; use a Table sorted by date, which also reads better on a phone.
## Examples

### Month
Departures in October. The glacier walk on the 7th has no guide, so it carries the attention tone.

## October 2026

Today

Departures, October 2026

MonTueWedThuFriSatSun

28293012
- [Golden Circle](#)34
5
- [South Coast](#)67
- [Northern Lights](#)
- [Glacier walk, needs a guide](#)
- [+2 more](#)89
- [Ring Road, 8 days](#)1011
121314
- [Golden Circle](#)
- [Whale watching, below minimum numbers](#)1516
- [South Coast](#)1718
192021
- [Golden Circle](#)2223
- [Northern Lights](#)2425
262728
- [Golden Circle](#)2930
- [Snæfellsnes, needs a guide](#)311

htmlCopy`

October 2026
Today

Departures, October 2026

MonTueWedThuFriSatSun

28293012Golden Circle34
5South Coast67Northern LightsGlacier walk, needs a guide+2 more89Ring Road, 8 days1011
121314Golden CircleWhale watching, below minimum numbers1516South Coast1718
192021Golden Circle2223Northern Lights2425
262728Golden Circle2930Snæfellsnes, needs a guide311

`
## Anatomy
PartDescriptionHeaderThe month as a heading, then Today and the previous and next month buttons.GridA table with one column per weekday, scope="col" headers and a visually hidden caption. It scrolls sideways below 48rem.DayA cell with its date in mono. Outside days sit on layer-02; today has aria-current="date" and a brand date chip.EventA link on layer-02 that truncates to one line, with the full text in its title. flux-calendar__event--attention adds the warning tone and an icon.More linkPast three events a day shows two and a link to the rest, named with the count and the date.
## API
NameKindDescription`flux-calendar`classThe wrapper for the header and the grid.`flux-calendar__header | __title | __nav`classThe month heading, a ghost small Button for Today, and the icon-only previous and next buttons.`flux-calendar__scroll`classThe horizontal scroll container. Give it role="region", a name and tabindex="0".`flux-calendar__grid`classOn the table.`data-outside`attributeOn a td for a day in the previous or next month.`aria-current="date"`attributeOn today’s td.`flux-calendar__date`classThe day number, ideally a time element with datetime.`flux-calendar__events | __event | __event-label`classThe list of events in a day, each event link and its truncating label.`flux-calendar__event--attention`classAn event that needs action. Add the alert icon and visually hidden text saying why.`flux-calendar__more`classThe link to the rest of a day’s events.
## States
StateTreatmentTodayBrand date chip and aria-current="date".Outside the monthlayer-02 ground and a subtle date.Event hoverThe chip steps to layer-hover-02.Needs attentionWarning-subtle ground, the alert icon and hidden text.NarrowThe grid keeps 48rem and the scroll container scrolls sideways.
## Keyboard
KeysAction`Tab`Moves through the month buttons, the scroll region and each event link in reading order.`Arrow keys`Scroll the grid when the scroll region has focus.
## Accessibility

- It is a table, so screen readers announce the weekday with each cell. Keep the caption naming what the calendar holds.
- Give each event link its full text: truncation is visual only, and the title attribute shows the rest on hover.
- The attention state carries an icon and hidden text, so it is not signalled by colour alone.
- Name the more link with the count and the date; “+2 more” alone does not say of what.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-calendar-bg | -border | -outside-bg | -min-width
- --flux-calendar-day-min-height | -day-padding | -date
- --flux-calendar-today-bg | -today-text
- --flux-calendar-event-bg | -event-hover | -event-attention
## Do and don’t
Do

- Start weeks on the day the market expects; Monday in Europe.
- Link every event to its record.Don’t

- Do not colour events by product or by agent; the chart palette is for charts. Use the attention variant for the one thing that needs action.
- Do not shrink the grid to fit a phone. Let it scroll, or offer a list view.[PreviousItinerary](/components/itinerary/)[NextMap](/components/map/)
