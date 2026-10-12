# Flux — /components/timeline/

Source: https://flux.kaptio.com/components/timeline/

Component

# Timeline
Events in time order on a hairline rail. A booking history, a day’s schedule, a workflow’s progress.

Plain-text source, for agents and clipboard use: [/components/source/timeline.txt](/components/source/timeline.txt)

## When to use it
Shows things that happen in sequence — what has happened to a booking, what runs when on a departure day — so the order and the gaps between them can be read at a glance. Each event has a time, a title and optionally one line of detail and a status. The marker says whether the event is done, current or still ahead.

Not thisNot for steps a person fills in one after another; that is a form split into sections. Not for comparing many records on the same attributes; that is a Table. Not for a slide; decks have their own timeline in flux-deck.css.
## Examples

### Booking history
Time above the title. Done events are filled, the current one is larger with its time in brand text, and the future ones are hollow.

2 Sep 2026, 10:14

Booking created

Sigrún Halldórsdóttir · Direct

2 Sep 2026, 10:21

Deposit received

ISK 120,000 · Card

4 Sep 2026, 16:02

Glacier walk requested

Mountain Guides

Awaiting supplier

8 Sep 2026

Balance due

ISK 366,000

htmlCopy`

2 Sep 2026, 10:14

Booking created
Sigrún Halldórsdóttir · Direct

2 Sep 2026, 10:21

Deposit received
ISK 120,000 · Card

4 Sep 2026, 16:02

Glacier walk requested
Mountain Guides
Awaiting supplier

8 Sep 2026

Balance due
ISK 366,000

`
### Schedule
flux-timeline--schedule puts the time in its own column, for a day read as a timetable.

08:30

Pick-up at Hotel Borg

Coach 18 · Guide Anna Jónsdóttir

10:15

Seljalandsfoss

45 minutes

13:00

Glacier walk

Sólheimajökull · Mountain Guides

Awaiting supplier

17:30

Check-in at Hotel Kría

Vík

htmlCopy`

08:30

Pick-up at Hotel Borg
Coach 18 · Guide Anna Jónsdóttir

10:15

Seljalandsfoss
45 minutes

13:00

Glacier walk
Sólheimajökull · Mountain Guides
Awaiting supplier

17:30

Check-in at Hotel Kría
Vík

`
## Anatomy
PartDescriptionListAn ol, because order is the meaning. A hairline rail in border-default joins the markers.TimeA time element with a machine-readable datetime, in text-secondary and tabular figures.MarkerA small square at radius-sm, decorative and hidden from assistive technology. Hollow ahead, filled when done, larger when current.TitleWhat happened or will happen, in bold text-primary.BodyOptional: one line of detail such as the supplier, the person or the vehicle, in text-secondary.AsideOptional: a status badge or a single action, on the title’s line. It wraps below the title when the title would drop under --flux-timeline-title-min-width.
## API
NameKindDescription`flux-timeline`classThe ol. Time sits above each title.`flux-timeline--schedule`classPuts the time in a column before the rail, --flux-timeline-time-width wide.`flux-timeline__item`classOne li, holding the time, the marker and the content, in that order.`data-state="done"`attributeOn the item: the event has happened. Fills the marker.`aria-current="step"`attributeOn the item that is happening now or needs attention next. At most one per timeline. Use "time" or "date" when the list is a schedule rather than a process.`flux-timeline__time`classA time element with a datetime attribute.`flux-timeline__marker`classAn empty span with aria-hidden="true".`flux-timeline__content`classWraps the title, body and aside.`flux-timeline__title`classA p naming the event. Use a heading only when events are sections of the page.`flux-timeline__body`classOptional p with one line of detail.`flux-timeline__aside`classOptional span holding one badge or one action.
## States
StateTreatmentUpcomingThe default. Hollow marker with a border-strong edge.Donedata-state="done". Filled marker in icon-brand.Currentaria-current. Larger filled marker, and the time in bold text-brand. Size and weight carry it, not colour alone.
## Keyboard
KeysAction`—`Not interactive. Links and buttons inside an event take focus in reading order.
## Accessibility

- Use an ol, so the count and order are announced.
- Give every time element a datetime attribute.
- Mark the current event with aria-current; the marker itself is hidden, so the state must not live only in its fill.
- Name a timeline with aria-label or aria-labelledby when the page has more than one.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-timeline-rail | -rail-width
- --flux-timeline-marker-size | -marker-current-size | -marker-radius
- --flux-timeline-marker-done | -marker-upcoming | -marker-bg
- --flux-timeline-item-gap | -column-gap | -time-width | -title-min-width
- --flux-timeline-font-size
- --flux-timeline-time-color | -time-current | -title-color | -body-color
## Do and don’t
Do

- Order events by time. Oldest first for a history of a process, earliest first for a schedule.
- Use the status badge only where the event has a status that someone acts on.
- Keep each event to a title and one line. Put the full record behind a link.Don’t

- Do not number the events. The time already orders them.
- Do not colour markers by status. The badge carries status; the marker carries done, current and upcoming.
- Do not put each event in its own card. The rail is the grouping.
- Do not use the timeline as a stepper for a form.[PreviousChart](/components/chart/)[NextItinerary](/components/itinerary/)
