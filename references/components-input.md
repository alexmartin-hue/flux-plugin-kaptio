# Flux — /components/input/

Source: https://flux.kaptio.com/components/input/

Component

# Input
Single-line text entry, with the label, help and error pattern that goes with it.

Plain-text source, for agents and clipboard use: [/components/source/input.txt](/components/source/input.txt)

## When to use it
Collects a short, free-form value. The field, its label, and its help or error text are one unit and should be built together — a bare input is almost always a bug.

Not thisFor a value from a known, closed set use Select. For a long-form value use Textarea. For a boolean use Switch or Checkbox.
## Examples

### Default

Booking reference

Six digits, prefixed with KB.

htmlCopy`
Booking reference

Six digits, prefixed with KB.
`
### Error
Bind the message to the field with aria-describedby so a screen reader announces it, and set aria-invalid so the state is not conveyed by colour alone.

Email *

Add the part after the @, for example kaptio.com.

htmlCopy`

Email *

Add the part after the @, for example kaptio.com.
`
### Disabled

Currency

Set by the departure, and not editable here.

htmlCopy`
Currency

Set by the departure, and not editable here.
`
## Anatomy
PartDescriptionLabelAlways present and always visible, above the field. Bold, small.Control36px tall, 4px radius, border-strong outline so the boundary clears 3:1.Help textBelow the field. Explains format or constraints before the user gets them wrong.Error textReplaces help text. Says what to do, not that something failed.
## API
NameKindDescription`flux-field`classWrapper binding label, control and message into one unit.`flux-field__label`classThe visible label. Required on every field.`flux-input`classThe control. Also applies to type=email, number, search, tel, url.`flux-field__help`classHelp text. Add data-tone="error" to switch it to the error style.`aria-invalid`attributeMarks the field invalid. Drives the error border.
## States
StateTreatmentDefaultborder-strong outline on field-bg.Hoverborder-interactive.Focus2px teal outline at 2px offset, from the global focus rule.Invalidborder-error, plus error text bound with aria-describedby.Disabledsurface-disabled fill at 60% opacity.
## Keyboard
KeysAction`Tab`Moves focus into and out of the field.`Escape`Where the field is a search or filter, clears it.
## Accessibility

- Every input needs a programmatically associated label. A placeholder is not a label — it disappears on focus and fails 4.5:1 by design.
- Error text must be referenced by aria-describedby, or a screen reader user will hear the field is invalid without hearing why.
- Never signal validity with colour alone; pair the border with aria-invalid and a message.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-field-height
- --flux-field-radius
- --flux-field-padding-x
- --flux-field-border
- --flux-field-border-hover
- --flux-field-border-error
- --flux-field-placeholder
## Do and don’t
Do

- Keep one field height and one radius across an entire form.
- Write help text before the user makes the mistake, not only after.
- Size the field to the expected content where it aids scanning — a postcode field need not be full width.Don’t

- Do not use the placeholder as the label.
- Do not use a blue focus ring. Focus is Flux teal in every theme.
- Do not mark a field required with colour alone; use the asterisk and the required attribute.[PreviousButton](/components/button/)[NextSelect](/components/select/)
