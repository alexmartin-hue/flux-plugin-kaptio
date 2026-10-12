# Flux — /components/switch/

Source: https://flux.kaptio.com/components/switch/

Component

# Switch
An on or off setting that takes effect the moment it changes.

Plain-text source, for agents and clipboard use: [/components/source/switch.txt](/components/source/switch.txt)

## When to use it
A switch turns a setting on or off immediately, with no Save button: automatic confirmation, a notification, a feature for one account. It is a native checkbox with role="switch", so Space, form state and the label come from the platform, drawn as a round track whose thumb moves to the end when on. Position carries the state as well as colour.

Not thisNot inside a form that is submitted later; there, a checkbox says "this will be true when you save". Not for a choice between two named options; use a Segmented control or radios. Not for an action such as Send or Archive; use a Button.
## Examples

### Default

Confirm bookings automatically
htmlCopy`

Confirm bookings automatically
`
### Settings list
flux-choice--end puts the text first and the switch at the end of the line, so a column of settings aligns on the controls. A setting the account cannot change stays visible and disabled.

Email me when
A supplier answers a request
A balance becomes overdue
A manifest is sent
An invoice is issued
htmlCopy`
Email me when
A supplier answers a request
A balance becomes overdue
A manifest is sent
An invoice is issued
`
### With an explanation
What the setting does goes in the info bubble beside it, never as text below. The switch references the bubble with aria-describedby.

Hold seats for unpaid bookings

Unpaid bookings keep their seats for 48 hours, then release them to the next request.

htmlCopy`

Hold seats for unpaid bookings

Unpaid bookings keep their seats for 48 hours, then release them to the next request.

`
## Anatomy
PartDescriptionChoiceThe same flux-choice label as a checkbox, wrapping the switch and its text.TrackThe input itself: a border-strong outline when off, filled in surface-brand when on.ThumbA circle at the start when off and at the end when on.
## API
NameKindDescription`flux-switch`classOn an input type="checkbox" with role="switch". checked and disabled work as usual.`flux-choice`classThe label wrapping the switch and its text, shared with Checkbox.`flux-choice--end`classText first and the control at the end of the line, for a list of settings.`role="switch"`attributeRequired. Announces on and off rather than checked and not checked.
## States
StateTreatmentOffborder-strong outline on field-bg, thumb in icon-secondary at the start.OnFilled in surface-brand, thumb in icon-on-color at the end.HoverThe outline turns border-interactive.FocusThe Flux focus ring around the track.Disabledsurface-disabled fill and border-disabled outline; the text turns text-disabled.
## Keyboard
KeysAction`Space`Turns the focused switch on or off.`Tab`Moves to the next switch.
## Accessibility

- role="switch" on the native checkbox makes it announce as on or off, and keeps Space and the label click.
- Wrap the switch in its label, so the label names it and the whole line is the target.
- Apply the change at once and confirm it if the result is not visible, with a toast or a status message. If saving fails, turn the switch back and say why.
- Group related switches in a fieldset with a legend.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-switch-track-width | -track-height | -thumb-inset | -thumb
- --flux-control-checked-bg | -unchecked-border | -check
## Do and don’t
Do

- Label the setting so that "on" reads as true: "Confirm bookings automatically".
- Apply the change immediately.Don’t

- Do not put a switch in a form that waits for a Save button. Use a checkbox.
- Do not add On and Off text beside the switch; the label and the thumb already say it.
- Do not explain the setting in text below it. Use the info bubble.[PreviousCheckbox and radio](/components/checkbox/)[NextSlider](/components/slider/)
