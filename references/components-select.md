# Flux — /components/select/

Source: https://flux.kaptio.com/components/select/

Component

# Select
Choice from a known, closed set of options.

Plain-text source, for agents and clipboard use: [/components/source/select.txt](/components/source/select.txt)

## When to use it
Use when the value must come from a fixed list the user cannot extend, and the list is long enough that radios would crowd the layout — roughly five options or more.

Not thisWith four or fewer options, radio buttons are faster and show every choice at once. For an open-ended value use Input.
## Examples

### Default

Sales channel

Direct B2C

- Direct B2C

- Trade partner

- Agent network

- Corporate

htmlCopy`
Sales channel

Direct B2C

Direct B2C
Trade partner
Agent network
Corporate

`
### With a placeholder option
Where no value is preselected, the first option states the choice rather than reading as a value.

Region

Determines which price rules apply.

Choose a region

- Iceland

- Nordics

- United Kingdom

htmlCopy`

Region

Determines which price rules apply.

Choose a region

Iceland
Nordics
United Kingdom

`
### Grouped options
When the options fall into categories people scan by. Each group is labelled, and the labels are not selectable. Keep groups to a handful; if every group holds one option, drop the grouping.

Service

Choose a service

Accommodation

- Hotel room

- Cabin

- Guesthouse

Transport

- Coach transfer

- Domestic flight

- Ferry crossing

Activities

- Glacier walk

- Whale watching

- Lagoon entry

htmlCopy`
Service

Choose a service

Accommodation

Hotel room
Cabin
Guesthouse

Transport

Coach transfer
Domestic flight
Ferry crossing

Activities

Glacier walk
Whale watching
Lagoon entry

`
### Searchable
For lists longer than about ten options. The list opens with focus in a search field; typing narrows the options, Arrow Down moves into them and Enter picks the best match. Groups work here too, and a group with no matches is hidden.

Supplier

Choose a supplier

- Arctic Adventures

- Blue Lagoon

- Eagle Air

- Elding Whale Watching

- Fosshotel Hekla

- Gray Line Iceland

- Hotel Kea

- Hótel Búðir

- Icelandair

- Reykjavik Excursions

- Sky Lagoon

- Smyril Line

No suppliers match.

htmlCopy`
Supplier

Choose a supplier

Arctic Adventures
Blue Lagoon
Eagle Air
Elding Whale Watching
Fosshotel Hekla
Gray Line Iceland
Hotel Kea
Hótel Búðir
Icelandair
Reykjavik Excursions
Sky Lagoon
Smyril Line

No suppliers match.

`
### Multi-select
When several values from a closed set may be chosen at once and the list is too long for a visible checkbox group. Checkbox options inside a dropdown panel; the trigger matches Select geometry. flux-components.js keeps the trigger label in step: the placeholder, up to two chosen labels, then a count.

Markets

Price rules apply to every selected market.

United Kingdom

Iceland

Nordics

United Kingdom

DACH

htmlCopy`

Markets

Price rules apply to every selected market.

United Kingdom

Iceland

Nordics

United Kingdom

DACH

`
## Anatomy
PartDescriptionLabelAbove the control, matching Input exactly.TriggerA button with the same height, radius and border as Input, so a mixed form stays level.IndicatorA line chevron in icon-subtle at the trailing edge. Stroke only, not a filled triangle.ListboxA Flux surface containing keyboard-focusable options and the selected checkmark, optionally in labelled groups.Search fieldOptional, for long lists. Sits above the options and stays in view while they scroll.ValueA hidden input carrying the selected value into ordinary form submission.
## API
NameKindDescription`flux-select`classPositions the styled trigger and its floating listbox.`data-flux-select`attributeInitialises listbox selection, focus management and form-value syncing.`flux-select-change`elementCancelable event dispatched on the select when an option is chosen, with detail.value, detail.label and detail.option. A framework that renders the value cancels it and renders the selection from detail; the select then leaves the value, aria-selected and the hidden input to it.`flux-select__control`classButton trigger. Matches Input geometry exactly.`flux-select__value`classVisible selected option inside the trigger.`flux-select__chevron`classLine chevron indicator. Stroke inherits icon-subtle via currentColor.`flux-select__panel`classFloating Flux surface containing the listbox.`flux-select__option`classFocus-managed option. Set aria-selected on exactly one option.`flux-select__group`classAn li with role="none" holding a flux-select__group-label and a nested ul with role="group" and aria-labelledby pointing at that label.`flux-select__panel--search`classSearchable panel. The panel itself has no role; role="listbox" moves to the flux-select__options list, which the trigger’s aria-controls points at.`flux-select__search`classText input inside flux-select__search-row at the top of a searchable panel, with flux-input, an aria-label and aria-controls naming the listbox.`flux-select__empty`classHidden message after the list, shown when the search matches nothing.`flux-multiselect`classDropdown multi-select built on details. Checkbox options, each with flux-checkbox, inside the panel.`data-flux-multiselect`attributeOn the details element. Keeps the trigger label in step with the checked options and closes the panel on Escape or a click outside. data-placeholder is the label when nothing is checked.`flux-multiselect__control`classThe trigger summary. Same field geometry as flux-select.`flux-multiselect__value`classTrigger label. Written by the script; set its initial text to match the options checked in the markup.`flux-field`classSame wrapper as Input.`aria-invalid`attributeError state on select or multiselect trigger.
## States
StateTreatmentDefaultIdentical to Input at rest.Hoverborder-interactive.FocusGlobal teal focus outline.Disabledsurface-disabled fill at 60% opacity.
## Keyboard
KeysAction`Space, Enter`Opens the listbox from the trigger or selects the focused option.`Up, Down`Opens the listbox, then moves focus through its options.`Home, End`Moves to the first or last option.`Type-ahead`Moves to the first option matching the typed characters. In a searchable select, typing goes to the search field instead.`Escape`Closes the listbox and returns focus to the trigger.`Down (in search)`Moves from the search field to the first matching option. Up from the first option returns to the field.`Enter (in search)`Selects the first option that starts with the search text, or else the first match.`Space, Enter`Opens or closes the multi-select panel.`Tab`Moves through checkbox options inside an open multi-select panel.`Escape (multi-select)`Closes the panel and returns focus to the trigger.
## Accessibility

- The trigger exposes aria-haspopup="listbox", its expanded state and the panel it controls. Its accessible name includes the visible field label and current value.
- Every option exposes aria-selected, and selection moves back to the trigger so the new value is announced in context.
- The hidden input carries the value into form submission. Validate required values in the form logic and bind any error with aria-describedby and aria-invalid.
- The line chevron and selected checkmarks are decorative and aria-hidden; selected state is also exposed programmatically.
- Multi-select uses a details panel with labelled checkboxes. Each option is a native checkbox so selection state is announced correctly.
- flux-components.js updates flux-multiselect__value as boxes change, so screen-reader users hear the current choice or count, not only the placeholder.
- Group labels are named by aria-labelledby on their group, so each option is announced with its category. They are not options and cannot be selected.
- The search field has its own aria-label; it narrows the list and never becomes the value. Options it hides are skipped by every key.
- Option text must stand alone; "Yes" and "No" mean nothing when read out of context.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-field-height
- --flux-field-radius
- --flux-field-border
- --flux-icon-subtle
- --flux-select-chevron-size
- --flux-select-panel-max-height
- --flux-multiselect-panel-max-height
## Do and don’t
Do

- Order options by expected frequency, or alphabetically when frequency is unknown.
- Keep the trigger the same height as neighbouring inputs.
- Use multi-select when the list is long but only some values apply; use a visible checkbox group when the full set should stay in view.
- Add the search field once a list passes about ten options, so nobody scrolls to find a known name.Don’t

- Do not use a select for two options — that is a switch or a pair of radios.
- Do not omit flux-components.js. The styled select requires its focus and form-value behaviour.[PreviousInput](/components/input/)[NextDate picker](/components/date-picker/)
