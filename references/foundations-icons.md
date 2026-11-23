# Flux — /foundations/icons/

Source: https://flux.kaptio.com/foundations/icons/

Foundations

# Icons
Every icon in Flux is Phosphor Regular. One set at one weight, so an icon never has to explain which family it came from, and its line sits at the same weight as Lexend Light beside it.

## One set, one weight
Phosphor is MIT licensed, has more than a thousand icons on one 256-unit grid, and ships six weights. Product UI uses exactly one of them.

WeightWhereRegularEverywhere: product UI, prototypes, the docs and decks.DuotoneDecks only, with flux-slide__icon. See Duotone in decks below.Thin, Light, Bold, FillNowhere. Light is too faint at 16px; Bold and Fill shout over the type.Browse the set at [phosphoricons.com](https://phosphoricons.com), or install the package `@phosphor-icons/core` and read the SVG files from `assets/regular/`.

## Using an icon
Inline SVG, pasted as Phosphor ships it. No icon font, no sprite and no component library.

htmlCopy`

Export
`Keep the `viewBox="0 0 256 256"` and `fill="currentColor"` Phosphor ships with, and add `aria-hidden="true"`. Do not set a width, a height or a colour on the icon: the component it sits in does both.

Every documented component already contains its icons. Copy the component markup and the icons come with it.

## Size and colour
PropertyComes fromSizeThe component’s icon-size token, for example --flux-shell-icon-size or --flux-toast-icon-size. Most controls use --flux-space-4 (16px).ColourcurrentColor, so an icon follows the text of its control. Where an icon stands alone it takes an icon-* role: icon-primary, icon-secondary, icon-subtle, icon-brand or icon-disabled.ThemeNothing to do. Roles resolve per theme, so an icon is correct in light, dark and deep.NoteAn icon is never a product accent, a status hue or a primitive. If none of the icon-* roles fits, a role is missing: say which, rather than writing a colour.
## Accessibility
CaseDoIcon beside a labelaria-hidden="true" on the svg. The label is the name.Icon-only controlaria-label on the button or link, naming the action: “Remove filter”, not “X”.Contrasticon-* roles clear 3:1 against their grounds in every theme, and the build checks them.MeaningNever an icon alone for a state. Pair it with text, as Badge and Toast do.
## Icons in Flux
The 100 Phosphor icons the components and these docs use. Any other Phosphor Regular icon is equally allowed.

- app-window
- arrow-down
- arrow-left
- arrow-up
- arrows-down-up
- arrows-left-right
- article
- bell
- brackets-curly
- buildings
- calendar-blank
- calendar-check
- calendar-dots
- cards
- caret-circle-down
- caret-double-right
- caret-down
- caret-left
- caret-right
- caret-up
- caret-up-down
- chart-bar
- chart-bar-horizontal
- chart-line
- chat-teardrop-text
- check
- check-circle
- check-square
- clipboard-text
- clock-counter-clockwise
- columns
- command
- cursor-click
- dots-six-vertical
- dots-three
- dots-three-circle
- download-simple
- exclamation-mark
- file
- file-text
- flow-arrow
- funnel
- gauge
- graph
- grid-nine
- image
- info
- kanban
- key
- keyboard
- list
- list-bullets
- list-checks
- list-dashes
- list-numbers
- magic-wand
- magnifying-glass
- map-trifold
- minus-circle
- note
- palette
- path
- pen-nib
- pencil-simple-line
- person-arms-spread
- plus
- plus-circle
- plus-minus
- presentation
- printer
- quotes
- rectangle
- rows
- shapes
- sidebar
- sidebar-simple
- signpost
- slack-logo
- sliders-horizontal
- sparkle
- spinner
- square-split-horizontal
- squares-four
- stack
- steps
- table
- tabs
- tag
- terminal-window
- text-aa
- text-b
- text-h
- text-italic
- textbox
- toggle-right
- tray
- upload-simple
- user-circle
- wave-sine
- x
## Duotone in decks
A slide may use Phosphor Duotone. The line takes the ground’s icon colour and the tone layer takes one light Flux colour.

- Light Seagreen`--flux-slide-icon-tone`The default on a light slide.
- Light yellow`--flux-slide-icon-tone-yellow`data-tone="yellow". Always used on dark and deep slides.
- Light Kaptio Teal`--flux-slide-icon-tone-kaptio-teal`data-tone="kaptio-teal".htmlCopy`

`Paste the SVG from `assets/duotone/` as it comes. Never set a fill or an opacity yourself, never mix tones or weights on one slide, and never use Duotone in product UI. On dark and deep slides the tone is always yellow, because the pale tones merge with the white line.

## Do and don’t
Do

- Use Phosphor Regular, inline, with fill="currentColor".
- Let the component set the size and the colour.
- Name every icon-only control with aria-label.
- Pair an icon with text whenever it marks a state.Don’t

- Do not use another icon set, an icon font or emoji as icons.
- Do not use Thin, Light, Bold or Fill.
- Do not colour an icon with a primitive, a product accent or a status hue.
- Do not use Duotone outside a deck.[PreviousTypography](/foundations/typography/)[NextLayout & spacing](/foundations/layout/)
