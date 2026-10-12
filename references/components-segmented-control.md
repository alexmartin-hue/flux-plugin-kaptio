# Flux — /components/segmented-control/

Source: https://flux.kaptio.com/components/segmented-control/

Component

# Segmented control
Two to five joined options, exactly one selected, that switch a view or a setting in place.

Plain-text source, for agents and clipboard use: [/components/source/segmented-control.txt](/components/source/segmented-control.txt)

## When to use it
Chooses between a few short, mutually exclusive options that are all worth seeing at once: list, calendar or map; gross or net. It is a set of native radio buttons styled as one joined control, so arrow keys, form submission and the group label come from the platform. The selected option fills with surface-selected and its text turns teal.

Not thisNot for switching between panels of different content; use Tabs. Not for more than five options or long labels; use a Select. Not for an on or off setting; use a Switch, or a Checkbox in a form. Not for actions; use Buttons.
## Examples

### Default
The legend is hidden because the options say what they switch. Arrow keys move the selection.

View
List
Calendar
Map
htmlCopy`
View
List
Calendar
Map
`
### With a visible label
As a setting in a form, the group takes a field label.

Show prices

Gross
Net

htmlCopy`
Show prices

Gross
Net

`
### Small, with a disabled option
flux-segmented--sm matches small buttons in a toolbar. A disabled option stays visible so the set does not change shape.

Period
Day
Week
Month
Season
htmlCopy`
Period
Day
Week
Month
Season
`
## Anatomy
PartDescriptionGroupA fieldset with a legend, visually hidden when the purpose is clear from the context.OptionA label wrapping a radio input that is invisible but still receives focus and clicks.
## API
NameKindDescription`flux-segmented`classOn the fieldset.`flux-segmented__option`classOn each label. Put the radio first inside it, then the text.`flux-segmented--sm`classThe small height, for toolbars.`input type="radio"`elementOne per option, sharing a name. checked and disabled work as usual.
## States
StateTreatmentDefaulttext-secondary on the field background, inside a border-strong outline.Hovertext-primary.Selectedsurface-selected fill and text-brand. The radio’s checked state, not colour alone, carries it to assistive technology.FocusThe Flux focus ring around the focused option.Disabledtext-disabled and not selectable.
## Keyboard
KeysAction`Tab`Moves focus to the selected option, then out of the group.`← → ↑ ↓`Selects the previous or next option.
## Accessibility

- Native radios provide the group role, the checked state and arrow-key selection.
- Give the fieldset a legend, or aria-labelledby pointing at a visible label.
- The change takes effect on selection; announce any resulting change in content with a live region.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-segmented-height | -height-sm | -padding-x
- --flux-segmented-bg | -border | -text | -text-hover
- --flux-segmented-selected-bg | -selected-text
## Do and don’t
Do

- Keep labels to one or two words.
- Apply the change immediately when the selection changes.Don’t

- Do not use it in place of Tabs to switch between different panels of content.
- Do not put more than five options in one control.
- Do not leave the group with nothing selected.[PreviousPagination](/components/pagination/)[NextStepper and wizard](/components/stepper/)
