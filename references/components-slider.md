# Flux — /components/slider/

Source: https://flux.kaptio.com/components/slider/

Component

# Slider
A duration, count or amount chosen by dragging along a bounded scale, as one value or a range.

Plain-text source, for agents and clipboard use: [/components/source/slider.txt](/components/source/slider.txt)

## When to use it
A slider sets a number where the position within its bounds matters more than the exact figure: the length of a stay, a tour duration filter, a cancellation window. It is a native range input, so arrow keys, Home and End, form submission and the slider role come from the platform. Two inputs over one track make a range, such as tours of 7 to 14 days, and the handles never cross. The value is always shown as text beside the label, with its unit, so it is never read from the handle position alone.

Not thisNot when the exact number matters or the range is wide, such as a price or a passenger count above twenty; use an Input with type="number", which is faster to type and to correct. Not for a few named options; use a Segmented control. Not for dates; use the Date picker.
## Examples

### Value
One handle. The fill runs from the minimum to the value.

Nights
4 nights

1 night14 nights
htmlCopy`

Nights
4 nights

1 night14 nights
`
### Duration range
Two handles on one track filter by a minimum and a maximum. The group is labelled once; each handle is named Minimum or Maximum. When both meet, the reading collapses to one value.

Tour length
7–14 days

1 day21 days
htmlCopy`

Tour length
7–14 days

1 day21 days
`
### With an explanation
What the value means goes in the info bubble beside the label, never as text below the track. The input references the bubble with aria-describedby.

Full refund window

Bookings cancelled at least this many days before departure are refunded in full.

30 days

0 days60 days
htmlCopy`

Full refund window

Bookings cancelled at least this many days before departure are refunded in full.

30 days

0 days60 days
`
### Disabled

Minimum stay
2 nights

1 night7 nights
htmlCopy`

Minimum stay
2 nights

1 night7 nights
`
## Anatomy
PartDescriptionLabelVisible, above the track, naming the quantity: "Tour length", not "Days".ValueThe current value or range with its unit, at the end of the label line. Hidden from assistive technology, which hears aria-valuetext instead.TrackThe rail in layer-03, and the fill in icon-brand from the start, or between the two handles of a range.HandleA ringed circle per input. It fills while focused or dragged, so a range says which handle is active.ScaleThe minimum and maximum, with their units, under each end of the track.
## API
NameKindDescription`flux-slider`classThe wrapper. Holds the label line, the control and the scale.`data-flux-slider`attributeBinds the fill, the visible value and aria-valuetext to the inputs. Requires flux-components.js.`data-flux-slider-unit | -units`attributeThe unit for one and for every other number: "night" and "nights". Used in the value text and in aria-valuetext.`flux-slider__value`classThe value text at the end of the label line, with aria-hidden="true". Write the initial value into it.`flux-slider__control`classThe track. Contains one input for a value or two for a range.`flux-slider__input`classOn each input type="range", with min, max, step, value and an initial aria-valuetext.`flux-slider__scale`classThe minimum and maximum under the track, aria-hidden because the input already exposes its bounds.`role="group"`attributeOn the wrapper of a range, with aria-labelledby pointing at its label. Each input then takes aria-label="Minimum …" or "Maximum …".
## States
StateTreatmentDefaultHandle ringed in icon-brand on surface; fill in icon-brand on a layer-03 rail.HoverThe handle fills with surface-brand-subtle.FocusThe focused handle fills in icon-brand, and keyboard focus adds the Flux focus ring around the input.DraggingDragging focuses the input, so the handle fills in icon-brand.DisabledHandle and fill in icon-disabled; the label, value and scale turn text-disabled.
## Keyboard
KeysAction`Arrow Right / Arrow Up`Increases the focused handle by one step.`Arrow Left / Arrow Down`Decreases the focused handle by one step.`Page Up / Page Down`Moves by a larger step, as the browser defines it.`Home / End`Moves the focused handle to the minimum or maximum, or to the other handle of a range.`Tab`Moves from the minimum handle to the maximum handle, then on.
## Accessibility

- A native input type="range" carries the slider role, its bounds and keyboard support. Do not rebuild it from a div.
- Set aria-valuetext with the unit, "7 nights" rather than "7"; flux-components.js keeps it current as the value changes.
- The visible value is aria-hidden so it is not announced twice while dragging; the input announces aria-valuetext.
- A range is a group named by its visible label, and each handle says whether it is the minimum or the maximum.
- The value is shown as text, so it is never conveyed by handle position or fill alone.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-slider-thumb-size | -thumb-border-width | -thumb-bg | -thumb-bg-hover | -thumb-border
- --flux-slider-track-height | -track | -fill
- --flux-slider-value | -scale | -scale-gap
## Do and don’t
Do

- Name the quantity in the label and the unit in data-flux-slider-unit, so every reading says what it measures.
- Choose a step that matches the decision: whole nights, whole days, five-minute intervals.
- Write the initial value and aria-valuetext into the markup, so the page reads correctly before the script runs.Don’t

- Do not use a slider for a value people need exactly, such as a price; use a number Input.
- Do not hide the value text and leave the handle position to say it.
- Do not explain the value in text below the track. Use the info bubble.
- Do not put two independent sliders on one track. A shared track is only for a minimum and maximum of the same quantity.[PreviousSwitch](/components/switch/)[NextSearch](/components/search/)
