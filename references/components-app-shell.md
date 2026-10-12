# Flux — /components/app-shell/

Source: https://flux.kaptio.com/components/app-shell/

Component

# App shell
The frame of a product: a rail of destinations, a top bar and the main column.

Plain-text source, for agents and clipboard use: [/components/source/app-shell.txt](/components/source/app-shell.txt)

## When to use it
Holds every screen of an application in one frame, so moving between areas changes the main column and nothing else. The rail lists destinations in labelled sections and marks the current one; it collapses to its icons on a wide screen and opens as a sheet from the top bar on a narrow one. The top bar carries the search entry point, reached with ⌘K, and the session context. One shell replaces the per-product sidebars that each grew their own width, colour and active state.

Not thisNot for a single task with a start and an end, such as a booking or a setup wizard; give that the Flow header so nothing pulls attention away from finishing it. Not for a marketing page or a deck. Not for switching views of one object; that is Tabs. Not for steps in order; a rail is a set of places, not a sequence.
## Examples

### Shell with sectioned rail
Property mapping is the current destination. Collapse the rail from its foot; at 48rem and below the rail moves behind the menu button in the top bar. The contained modifier frames the shell for this preview; an application leaves it off and fills the viewport.

[Skip to content](#shell-main)

[Connect SetupKaptio Edge](#)

Connectors

- [New connector](#)

- [Requests3](#)

Setup

- [Property mapping](#)

- [Content import](#)

- [Network import](#)

Workspace

- [Plans12](#)

- [Credentials](#)

Collapse

Search requests, properties and plans⌘K

demo / staging
OG

# Property mapping

Match each supplier property to its Kaptio service before content is imported.

htmlCopy`
Skip to content

Connect SetupKaptio Edge

Connectors

New connector
Requests3

Setup

Property mapping
Content import
Network import

Workspace

Plans12
Credentials

Collapse

Search requests, properties and plans⌘K

demo / staging
OG

Property mapping
Match each supplier property to its Kaptio service before content is imported.

`
## Anatomy
PartDescriptionSkip linkThe first focusable element. Hidden until focused, then jumps to the main column.RailA nav labelled with the product name, on layer-01 with a hairline against the main column.ProductThe product mark, filled with its --flux-product-* accent, and the product name. Links to the product home.SectionsGroups of destinations, each with a short mono label. Three or four sections at most.ItemAn icon, a label and an optional count. The current destination carries aria-current="page".CollapseAt the foot of the rail. Reduces the rail to its icons on a wide screen.Top barThe menu button on a narrow screen, the search entry point, and the session context with the avatar.MainThe page itself: its h1, then its content. It scrolls beneath the sticky top bar.
## API
NameKindDescription`flux-shell`classThe grid. Fills the viewport and holds the rail, the top bar and the main column.`data-flux-shell`attributeWires collapse, the narrow sheet and the search shortcut. Requires flux-components.js.`flux-shell--contained`classFrames the shell at --flux-shell-contained-height for previews and documentation. The search shortcut is not bound, so the host page keeps its own.`data-collapsed`attributeOn flux-shell. Set it at render time to start collapsed, for example from a saved preference.`flux-shell__skip`classThe skip link. Its href names the main column.`flux-shell__rail`classThe nav element. Give it an id for the menu button’s aria-controls and an aria-label with the product name.`flux-shell__product`classThe product link, with flux-shell__mark and flux-shell__product-name inside.`flux-shell__mark`classThe square mark. Set --flux-shell-mark to the product’s accent, such as var(--flux-product-edge).`flux-shell__product-meta`classOptional span inside the product name, such as Kaptio Edge.`flux-shell__nav`classThe scrolling list of sections.`flux-shell__section`classOne group: a flux-shell__section-label span and a flux-shell__list ul labelled by it.`flux-shell__item`classA link with an svg icon, a flux-shell__label span and an optional flux-shell__count span.`aria-current="page"`attributeOn the item for the current destination. Fills the item and sets its label in bold.`flux-shell__footer`classHolds the collapse button, a flux-shell__item with flux-shell__collapse and data-flux-shell-collapse.`flux-shell__topbar`classThe header element.`data-flux-shell-menu`attributeOn a ghost Button with flux-shell__menu, aria-controls and aria-expanded. Shown at 48rem and below.`data-flux-shell-search`attributeOn the flux-shell__search button. Click and ⌘K or Ctrl K dispatch a bubbling flux-shell-search event; open the product’s search in a Modal from it.`flux-shell__actions`classThe end of the top bar: flux-shell__context in mono and an Avatar.`flux-shell__main`classThe main element, with the id the skip link names and tabindex="-1".
## States
StateTreatmentCurrentaria-current="page" fills the item in surface-selected, sets the label in bold text-brand and the icon in icon-brand. Weight and fill change, so colour is not the only signal.HoverBackground layer-hover-01 and text-primary. Colour only; nothing moves.CollapsedThe rail narrows to --flux-shell-rail-collapsed-width. Labels, counts and section labels stay in the accessibility tree; each item gains a title with its label, and a hairline separates the sections.NarrowAt 48rem and below the rail leaves the grid. The menu button opens it as a sheet over a backdrop, with --flux-shell-sheet-shadow because it floats. The top bar and main column become inert while it is open.
## Keyboard
KeysAction`Tab`Skip link first, then the rail, the top bar and the main column, in that order.`Enter`On the skip link, moves focus to the main column.`⌘K / Ctrl K`Activates the search entry point from anywhere on the page.`Escape`Closes the narrow sheet and returns focus to the menu button.
## Accessibility

- Use nav, header and main, so each region is a landmark. Label the nav with the product name.
- Set aria-current="page" on exactly one item, and update it on every client-side navigation.
- Label each list by its section label with aria-labelledby, so "Setup, list, 3 items" is announced.
- Keep labels in the accessibility tree when collapsed. The rail hides them visually, never with display: none.
- Opening the sheet moves focus to the current item; closing it returns focus to the menu button.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-shell-rail-width | -rail-collapsed-width | -topbar-height | -search-width | -contained-height
- --flux-shell-rail-bg | -topbar-bg | -main-bg | -divider | -backdrop | -sheet-shadow
- --flux-shell-padding | -content-padding | -section-gap | -section-label
- --flux-shell-item-height | -item-gap | -item-padding-x | -item-radius | -icon-size
- --flux-shell-item-text | -item-hover | -item-hover-text | -item-current-bg | -item-current-text | -item-icon | -item-current-icon
- --flux-shell-mark | -mark-size
## Do and don’t
Do

- Name destinations by what the user finds there, such as Requests or Plans, not by the team that owns them.
- Remember the collapsed state per user, and render data-collapsed on the server or before first paint so the rail does not jump.
- Show a count only when it is work waiting for the user, such as open requests.
- Put the page title in the main column’s h1, where it scrolls with the page, and keep the top bar for search and context.Don’t

- Do not number rail items. A rail is a set of places; a sequence belongs in a Flow.
- Do not set the rail on a dark or brand ground. It is layer-01, like every other surface around content.
- Do not put a count in a pill or a badge. A count is not a status.
- Do not hide items for a role by greying them out. Leave them out, or keep them and explain on the destination why it is locked.
- Do not animate the rail’s width when it collapses. It changes in one step.[PreviousFlow diagram](/components/flow/)[NextSpinner](/components/spinner/)
