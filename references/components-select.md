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

Choose a region

- Iceland

- Nordics

- United Kingdom

Determines which price rules apply.

htmlCopy`
Region

Choose a region

Iceland
Nordics
United Kingdom

Determines which price rules apply.
`
### Multi-select
When several values from a closed set may be chosen at once and the list is too long for a visible checkbox group. Checkbox options inside a dropdown panel; the trigger matches Select geometry.

Markets

Choose markets

Iceland

Nordics

United Kingdom

DACH

Price rules apply to every selected market.

htmlCopy`
Markets

Choose markets

Iceland

Nordics

United Kingdom

DACH

Price rules apply to every selected market.
`
## Anatomy
PartDescriptionLabelAbove the control, matching Input exactly.TriggerA button with the same height, radius and border as Input, so a mixed form stays level.IndicatorA line chevron in icon-subtle at the trailing edge. Stroke only, not a filled triangle.ListboxA Flux surface containing keyboard-focusable options and the selected checkmark.ValueA hidden input carrying the selected value into ordinary form submission.
## API
NameKindDescription`flux-select`classPositions the styled trigger and its floating listbox.`data-flux-select`attributeInitialises listbox selection, focus management and form-value syncing.`flux-select__control`classButton trigger. Matches Input geometry exactly.`flux-select__value`classVisible selected option inside the trigger.`flux-select__chevron`classLine chevron indicator. Stroke inherits icon-subtle via currentColor.`flux-select__panel`classFloating Flux surface containing the listbox.`flux-select__option`classFocus-managed option. Set aria-selected on exactly one option.`flux-multiselect`classDropdown multi-select built on details. Checkbox options inside the panel.`flux-multiselect__control`classThe trigger summary. Same field geometry as flux-select.`flux-multiselect__value`classTrigger label. Update to show the selection count or chosen values.`flux-field`classSame wrapper as Input.`aria-invalid`attributeError state on select or multiselect trigger.
## States
StateTreatmentDefaultIdentical to Input at rest.Hoverborder-interactive.FocusGlobal teal focus outline.Disabledsurface-disabled fill at 60% opacity.
## Keyboard
KeysAction`Space, Enter`Opens the listbox from the trigger or selects the focused option.`Up, Down`Opens the listbox, then moves focus through its options.`Home, End`Moves to the first or last option.`Type-ahead`Moves to the first option matching the typed characters.`Escape`Closes the listbox and returns focus to the trigger.`Space, Enter`Opens or closes the multi-select panel.`Tab`Moves through checkbox options inside an open multi-select panel.
## Accessibility

- The trigger exposes aria-haspopup="listbox", its expanded state and the panel it controls. Its accessible name includes the visible field label and current value.
- Every option exposes aria-selected, and selection moves back to the trigger so the new value is announced in context.
- The hidden input carries the value into form submission. Validate required values in the form logic and bind any error with aria-describedby and aria-invalid.
- The line chevron and selected checkmarks are decorative and aria-hidden; selected state is also exposed programmatically.
- Multi-select uses a details panel with labelled checkboxes. Each option is a native checkbox so selection state is announced correctly.
- Update flux-multiselect__value when selections change so screen-reader users hear the current count, not only the placeholder.
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
- Use multi-select when the list is long but only some values apply; use a visible checkbox group when the full set should stay in view.Don’t

- Do not use a select for two options — that is a switch or a pair of radios.
- Do not omit flux-components.js. The styled select requires its focus and form-value behaviour.[PreviousInput](/components/input/)[NextDate picker](/components/date-picker/)
