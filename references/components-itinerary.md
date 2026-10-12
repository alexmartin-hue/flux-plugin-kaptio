# Flux — /components/itinerary/

Source: https://flux.kaptio.com/components/itinerary/

Component

# Itinerary
A trip, day by day: where each day goes, what runs when, and where everyone sleeps.

Plain-text source, for agents and clipboard use: [/components/source/itinerary.txt](/components/source/itinerary.txt)

## When to use it
Lays out a booking or a departure as days. Each day has its number and date, a title naming the route, a schedule of services with their supplier and status, and the overnight. It is the view an operator checks before confirming a booking and the view a guide reads before a departure, so status sits next to every service that can fail.

Not thisNot for a list of departures or bookings; that is a Table. Not for a single day’s schedule on its own; that is a Timeline with the schedule modifier. Not for a customer-facing brochure, where photography and copy lead and operational status does not belong.
## Examples

### Departure itinerary
Three days. Day 2’s glacier walk awaits its supplier and Day 3’s boat tour is on request, so the open work is visible where it happens rather than in a separate list.

Day 1
Sat 12 Sep

### Keflavík → Reykjavik

15:40

Arrival transfer

Private car · Reykjavik Transfers

Confirmed

19:30

Welcome dinner

Harbour Kitchen · 4 guests

Confirmed

OvernightHotel Borg, Reykjavik · Superior double

Day 2
Sun 13 Sep

### Reykjavik → Vík

08:30

South Coast day tour

Coach 18 · Guide Anna Jónsdóttir

Confirmed

13:00

Glacier walk

Sólheimajökull · Mountain Guides

Awaiting supplier

OvernightHotel Kría, Vík · Standard double

Day 3
Mon 14 Sep

### Vík → Jökulsárlón

09:00

Glacier lagoon boat tour

Jökulsárlón · Lagoon Boats

On request

OvernightFosshotel Glacier Lagoon · Room not yet allocated

htmlCopy`

Day 1
Sat 12 Sep

Keflavík → Reykjavik

15:40

Arrival transfer
Private car · Reykjavik Transfers
Confirmed

19:30

Welcome dinner
Harbour Kitchen · 4 guests
Confirmed

OvernightHotel Borg, Reykjavik · Superior double

Day 2
Sun 13 Sep

Reykjavik → Vík

08:30

South Coast day tour
Coach 18 · Guide Anna Jónsdóttir
Confirmed

13:00

Glacier walk
Sólheimajökull · Mountain Guides
Awaiting supplier

OvernightHotel Kría, Vík · Standard double

Day 3
Mon 14 Sep

Vík → Jökulsárlón

09:00

Glacier lagoon boat tour
Jökulsárlón · Lagoon Boats
On request

OvernightFosshotel Glacier Lagoon · Room not yet allocated

`
## Anatomy
PartDescriptionListAn ol of days, separated by hairlines in border-subtle rather than cards.WhenThe day number in bold and the date below it. The column wraps above the day when the content would drop below its minimum width.TitleAn h3 naming the route or the theme of the day, such as Reykjavik → Vík.ServicesA Timeline with the schedule modifier: time, service, supplier and status.OvernightOptional: the accommodation and room type, after a hairline.
## API
NameKindDescription`flux-itinerary`classThe ol of days.`flux-itinerary__day`classOne li, labelled by its title with aria-labelledby.`flux-itinerary__when`classHolds the number and the date. --flux-itinerary-when-width wide.`flux-itinerary__number`classThe day number, as "Day 1". Numbering is correct here: the order of days is the meaning.`flux-itinerary__date`classA time element with a datetime attribute.`flux-itinerary__body`classHolds the title, the services and the overnight. Never narrower than --flux-itinerary-body-min-width.`flux-itinerary__title`classThe h3. Choose the level for the page outline; the size comes from the token.`flux-itinerary__overnight`classOptional p with the accommodation.`flux-itinerary__overnight-label`classThe span reading "Overnight".
## States
StateTreatmentService statusA badge in each service’s aside: confirmed, on request, awaiting supplier or cancelled.TodayOn a departure in progress, aria-current="time" on the running service marks where the day is.NarrowThe when column wraps above the day. Nothing is hidden or truncated.
## Keyboard
KeysAction`—`Not interactive. Links and buttons inside a service take focus in reading order.
## Accessibility

- Use an ol for the days, and label each day with its title so it is announced as "Reykjavik → Vík" rather than as list item 2.
- Give each service timeline an aria-label naming its day.
- Write status in the badge text, never only in its colour.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-itinerary-when-width | -body-min-width
- --flux-itinerary-day-padding | -column-gap | -divider
- --flux-itinerary-number-color | -date-color | -title-size
- All --flux-timeline-* tokens, for the services.
## Do and don’t
Do

- Show every service’s status, so an operator can see what is still open without opening each one.
- Name the supplier on the service line. It is the first thing someone chasing a confirmation needs.
- Keep the overnight on every day that has one, including the last night before departure.Don’t

- Do not put each day in a card. Hairlines separate days; cards would compete with the badges.
- Do not hide services behind an expander by default. Collapse past days only on a long departure in progress.
- Do not colour the day by its worst status. The badges already say it, where it applies.[PreviousTimeline](/components/timeline/)[NextCalendar view](/components/calendar/)
