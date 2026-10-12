# Flux — /components/pagination/

Source: https://flux.kaptio.com/components/pagination/

Component

# Pagination
Range text and page links for a long list that is served one page at a time.

Plain-text source, for agents and clipboard use: [/components/source/pagination.txt](/components/source/pagination.txt)

## When to use it
Splits a long, server-side result into pages and says which part is showing: 26–50 of 312. The page links are real links, so a page can be bookmarked, opened in a new tab and reached with the back button. Previous and Next stay in place and disable at the ends rather than disappearing, and a long run of pages collapses around the current one with gaps.

Not thisNot for a list short enough to show in full. Not for a feed read top to bottom; load more on request instead. Not for client-side tables of a few hundred rows, which can scroll.
## Examples

### Below a table
The pagination sits after the table wrapper, which spaces it automatically. Pages near the current one are shown, with the first and last.

Bookings, page 2 of 13

Reference
Departure
Pax

KB-104953Golden Circle, 21 Sep6
KB-104954South Coast, 22 Sep2
KB-104957Snæfellsnes, 22 Sep11

26–50 of 312

- [Previous](#)

- [1](#)

- [2](#)

- [3](#)

- …

- [13](#)

- [Next](#)

htmlCopy`

Bookings, page 2 of 13

Reference
Departure
Pax

KB-104953Golden Circle, 21 Sep6
KB-104954South Coast, 22 Sep2
KB-104957Snæfellsnes, 22 Sep11

26–50 of 312

Previous
1
2
3
…
13
Next

`
### Previous and next only
For results served by cursor, where the total is unknown or expensive to count. On the first page, Previous is disabled rather than removed, so Next does not move.

1–25

- Previous

- [Next](#)

htmlCopy`
1–25

Previous
Next

`
## Anatomy
PartDescriptionNavigationA nav with aria-label="Pagination" and the flux-pagination class.RangeWhich records are showing and how many there are, in text-secondary with tabular figures.Previous and NextLinks with an arrow and a word. At an end they become disabled spans.PageA link per page in mono. The current page is selected and carries aria-current="page".GapAn ellipsis standing for the pages left out.
## API
NameKindDescription`flux-pagination`classOn the nav. Give it aria-label="Pagination".`flux-pagination__range`classThe range text.`flux-pagination__list`classOn the ul of links.`flux-pagination__link`classOn every link, and on the span that replaces a disabled Previous or Next.`flux-pagination__page`classAdds mono figures to a page number link. Label it "Page n".`flux-pagination__gap`classThe ellipsis for omitted pages, with aria-hidden.`aria-current="page"`attributeOn the current page’s link.`aria-disabled="true"`attributeOn the span for Previous or Next at an end.
## States
StateTreatmentDefaulttext-primary on no fill.Hoversurface-hover fill.Currentsurface-selected fill, text-brand, mono bold.Disabledtext-disabled, not focusable, not a link.
## Keyboard
KeysAction`Tab`Moves through the links. Disabled ends and gaps are skipped.`Enter`Opens the page.
## Accessibility

- Label the nav "Pagination", and each number "Page n", so a list of links reads as pages.
- The current page carries aria-current="page", so it is not conveyed by fill alone.
- Update the table caption with the page number, so the change is clear after the page loads.
- Move focus to the top of the results after a page change that does not reload the page.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-pagination-gap | -item-size | -item-text | -item-hover
- --flux-pagination-current-bg | -current-text
- --flux-pagination-range
## Do and don’t
Do

- Show the first page, the last page and the pages either side of the current one.
- Keep the page in the URL so the back button returns to it.Don’t

- Do not hide Previous or Next at an end: disable it.
- Do not use buttons for pages when a URL can identify each one.
- Do not shrink row height to fit more rows on a page.[PreviousBreadcrumbs](/components/breadcrumbs/)[NextSegmented control](/components/segmented-control/)
