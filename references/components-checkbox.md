# Flux — /components/checkbox/

Source: https://flux.kaptio.com/components/checkbox/

Component

# Checkbox and radio
On-or-off choices and one-of-many choices, each with its label beside it.

Plain-text source, for agents and clipboard use: [/components/source/checkbox.txt](/components/source/checkbox.txt)

## When to use it
A checkbox turns one thing on or off, or picks any number from a short list. A radio picks exactly one from a short list where every option should be visible at once. Both are drawn by Flux from tokens, so they follow every theme, and both sit inside a label so the whole line is the target.

Not thisNot for a setting that takes effect immediately; that is a switch. Not for more than about seven options, or options that need searching; use Select. Not for a choice between two actions; use two buttons.
## Examples

### Checkbox

Send the manifest to the guide
htmlCopy`

Send the manifest to the guide
`
### Checkbox group
Any number of the options. One is disabled because the departure has no driver assigned yet.

Send confirmation to
Lead passenger
Booking agent
Guide
Driver
htmlCopy`
Send confirmation to
Lead passenger
Booking agent
Guide
Driver
`
### Radio group

Room type
Double
Twin
Single
htmlCopy`
Room type
Double
Twin
Single
`
### Inline, with an error
Short options can sit on one line and wrap when space runs out. The error is bound to the fieldset, and each radio carries aria-invalid.

Payment terms *
30% deposit
Full payment
Invoice, 30 days
Choose how the agent pays.

htmlCopy`
Payment terms *
30% deposit
Full payment
Invoice, 30 days
Choose how the agent pays.
`
## Anatomy
PartDescriptionChoiceA label wrapping the control and its text, so a click anywhere on the line toggles it.Controlflux-checkbox, square with a check, or flux-radio, round with a dot. Filled in surface-brand when on.GroupA fieldset with a legend, holding related choices. The legend is the question; each label is an answer.ErrorOne message below the group, bound to it with aria-describedby.
## API
NameKindDescription`flux-choice`classThe label wrapping a control and its text.`flux-checkbox`classOn an input type="checkbox". Supports checked, indeterminate (set in script), disabled and aria-invalid.`flux-radio`classOn an input type="radio". Give every radio in a group the same name.`flux-choice-group`classOn a fieldset. Its legend is the group label, set like a field label.`flux-choice-group--inline`classOptions in a row that wraps. For short labels only.
## States
StateTreatmentUncheckedborder-strong outline on field-bg, so the boundary clears 3:1.CheckedFilled in surface-brand with a check or a dot in icon-on-color.IndeterminateCheckbox only: a bar instead of a check, for a select-all that covers some of its rows.Disabledsurface-disabled fill and border-disabled outline; the label turns text-disabled.Invalidborder-error outline, with the message below the group.
## Keyboard
KeysAction`Space`Toggles a checkbox, or checks the focused radio.`Tab`Moves to each checkbox, and into a radio group once, landing on the checked radio.`↑ ↓ ← →`Within a radio group, moves to and checks the previous or next radio.
## Accessibility

- Wrap the control in its label, so the label names it and enlarges the target.
- Group related choices in a fieldset with a legend. The legend is announced with the first option, so "Room type, Double, radio button, 1 of 3".
- A required radio group puts required on each radio. The error goes on the fieldset with aria-describedby, and each radio takes aria-invalid.
- Set indeterminate from script; there is no attribute for it.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-control-size | -label-gap | -radio-dot
- --flux-control-checked-bg | -unchecked-border | -check
- --flux-choice-group-gap | -group-inline-gap
## Do and don’t
Do

- Write the label as the thing that becomes true when it is checked: "Send the manifest to the guide".
- Pre-select the safest or most common radio option, so a group never starts with nothing chosen unless the choice must be deliberate.
- Order options by how often they are chosen, or by their natural order, such as smallest to largest.Don’t

- Do not use a single checkbox for a choice between two named options. Use two radios.
- Do not put a radio group inside a table cell. A row holds one value; edit it in a form or an editable cell.
- Do not explain an option in text below it. Put explanation in the info bubble beside the legend.[PreviousDate picker](/components/date-picker/)[NextSwitch](/components/switch/)
