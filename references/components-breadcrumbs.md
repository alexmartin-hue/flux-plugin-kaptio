# Flux — /components/breadcrumbs/

Source: https://flux.kaptio.com/components/breadcrumbs/

Component

# Breadcrumbs
The path from a section to the current page, as a list of links.

Plain-text source, for agents and clipboard use: [/components/source/breadcrumbs.txt](/components/source/breadcrumbs.txt)

## When to use it
Shows where a page sits in a hierarchy and gives one-step access to each level above it: Bookings, then a booking, then its passengers. The trail is an ordered list inside a labelled nav. The current page closes the trail in bold and is not a link. Long names truncate with an ellipsis rather than wrapping the trail onto a second line.

Not thisNot for a flat site with one level. Not as the only navigation; it complements the app shell. Not for steps in a process; use the Stepper.
## Examples

### Default

- [Bookings](#)

- [Golden Circle Classic, 14 Sep](#)

- Passengers

htmlCopy`

Bookings
Golden Circle Classic, 14 Sep
Passengers

`
## Anatomy
PartDescriptionNavigationA nav with aria-label="Breadcrumb".TrailAn ordered list. The order is the meaning.LinkEach level above the current page, in text-secondary.SeparatorA chevron drawn by CSS between items, so screen readers do not read it.Current pageThe last item, bold, with aria-current="page".
## API
NameKindDescription`nav aria-label="Breadcrumb"`elementThe landmark. One per page.`flux-breadcrumbs`classOn the ol.`flux-breadcrumbs__item`classOn each li. Every item after the first draws a separator.`flux-breadcrumbs__link`classOn each link above the current page.`aria-current="page"`attributeOn the span that names the current page.
## States
StateTreatmentLinktext-secondary, no underline.Hovertext-brand and underlined.FocusThe Flux focus ring.Currenttext-primary, bold, truncated with an ellipsis when long.
## Keyboard
KeysAction`Tab`Moves through the links. The current page is not a stop.`Enter`Follows the link.
## Accessibility

- Label the nav "Breadcrumb" so it is distinct from the main navigation.
- Use an ordered list: the position of each level is part of its meaning.
- The separators are CSS, so they are not read out between items.
- Mark the last item with aria-current="page".
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-breadcrumbs-gap
- --flux-breadcrumbs-link | -link-hover | -current
- --flux-breadcrumbs-separator | -separator-size
## Do and don’t
Do

- Start the trail at the section, not at a home link the app shell already provides.
- Use the same names as the pages they link to.Don’t

- Do not make the current page a link.
- Do not type separators into the markup.
- Do not use breadcrumbs to show the steps of a process.[PreviousEmpty state](/components/empty-state/)[NextPagination](/components/pagination/)
