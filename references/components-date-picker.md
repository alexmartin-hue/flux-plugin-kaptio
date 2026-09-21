# Flux — /components/date-picker/

Source: https://flux.kaptio.com/components/date-picker/

Component

# Date picker
Single-date and date-range selection from a keyboard-operable calendar.

Plain-text source, for agents and clipboard use: [/components/source/date-picker.txt](/components/source/date-picker.txt)

## When to use it
Use when a user needs to choose a date and the surrounding days help them decide — departures, arrivals, deadlines and booking ranges. The trigger matches every other Flux field, while the calendar exposes the same ISO values an ordinary form expects.

Not thisFor a date the user already knows and can type faster, use a labelled text input with explicit format help. For a month, quarter or recurring schedule, use a control designed for that unit rather than making users select an arbitrary day.
## Examples

### Single date
Selecting a date updates the hidden ISO value and closes the calendar. The visible value follows the familiar day / month / year order.

Departure date

DD / MM / YYYY

Choose a date

###

MoTuWeThFrSaSu

Clear

htmlCopy`
Departure date

DD / MM / YYYY

Choose a date

MoTuWeThFrSaSu

Clear

`
### Date range
The first selection sets the start. The second completes and orders the range, then closes the calendar.

Travel dates

Select dates

Choose a start date

###

MoTuWeThFrSaSu

Clear

htmlCopy`
Travel dates

Select dates

Choose a start date

MoTuWeThFrSaSu

Clear

`
## Anatomy
PartDescriptionLabelVisible above the trigger and included in its accessible name.TriggerField-height button showing the current value or format placeholder.Calendar dialogA floating overlay with month navigation, weekday headings and a date grid.Date gridRoving-tabindex grid. One date is tabbable; arrow keys move by day or week.Form valueOne hidden ISO date for single selection; start and end ISO dates for a range.
## API
NameKindDescription`flux-date-picker`classPositions the field trigger and floating calendar.`data-flux-date-picker`attributeInitialises a single picker. Set it to "range" for start-and-end selection.`flux-date-picker__control`classButton trigger with standard Flux field geometry.`flux-date-picker__panel`classCalendar dialog surface. Hidden until the trigger opens it.`flux-date-picker__grid`classGenerated calendar grid with roving keyboard focus.`data-flux-date-input`attributeMarks hidden start and optional end inputs that receive YYYY-MM-DD values.`data-placeholder`attributeVisible trigger text before a date has been selected.`aria-invalid`attributeError state on the date-picker wrapper. Bind an adjacent message with aria-describedby.
## States
StateTreatmentEmptyFormat or selection prompt shown with text-placeholder.OpenCalendar dialog visible; focus moves to the selected date, today or the first date.Selectedsurface-brand date with text-on-color; hidden input carries its ISO value.RangeStart and end use the selected treatment; days between use surface-selected.Todayborder-interactive outline, independent of selection.Invalidborder-error on the trigger plus a bound error message.
## Keyboard
KeysAction`Enter, Space, Down`Opens the calendar from the trigger.`Left, Right`Moves focus by one day.`Up, Down`Moves focus by one week.`Home, End`Moves to the first or last day of the current week.`Page Up, Page Down`Moves to the same day in the previous or next month.`Shift + Page Up, Page Down`Moves to the same day in the previous or next year.`Enter, Space`Selects the focused date.`Escape`Closes the calendar and returns focus to the trigger.
## Accessibility

- The trigger exposes aria-haspopup="dialog", aria-expanded and aria-controls. Its accessible name combines the visible field label and value.
- The month heading labels the grid and announces month changes through aria-live.
- Today uses aria-current="date"; selected endpoints use aria-selected. Range colour is supplementary and never the only programmatic selection state.
- Only one date has tabindex="0". Arrow, Home, End and Page keys follow the WAI-ARIA date-picker keyboard pattern.
- Hidden values use ISO YYYY-MM-DD so display formatting never changes submitted data.
- Include flux-components.js. Without it the grid cannot be generated or operated.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-field-height
- --flux-field-border
- --flux-datepicker-panel-width
- --flux-datepicker-panel-bg
- --flux-datepicker-day-size
- --flux-datepicker-selected-bg
- --flux-datepicker-selected-text
- --flux-datepicker-range-bg
- --flux-datepicker-today-border
## Do and don’t
Do

- Use a single picker for one deadline or departure date, and range only when both endpoints belong to one decision.
- Keep submitted values in ISO format even when visible dates use a local format.
- Provide nearby constraints such as earliest departure or maximum stay before the user opens the calendar.Don’t

- Do not use colour alone to identify today, selection or errors.
- Do not close a range picker after the first date; announce that the end date is now required.
- Do not omit flux-components.js or replace the visible label with the placeholder.[PreviousSelect](/components/select/)[NextCard](/components/card/)
