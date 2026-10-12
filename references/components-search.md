# Flux — /components/search/

Source: https://flux.kaptio.com/components/search/

Component

# Search
A search field with its icon, a clear button and the number of results.

Plain-text source, for agents and clipboard use: [/components/source/search.txt](/components/source/search.txt)

## When to use it
Narrows a list or finds a record by typing. The field keeps its visible label, shows a magnifier so it reads as search at a glance, offers a clear button once it holds text, and says how many results match below it, so the effect of each keystroke is visible and announced.

Not thisNot for the application-wide search entry point; that is the App shell top bar, opened with ⌘K. Not for choosing one value from a list; that is the searchable Select.
## Examples

### Search with a result count
The product updates the count as results change. Escape or the clear button empties the field and returns focus to it.

Search bookings

248 bookings

htmlCopy`
Search bookings

248 bookings
`
## Anatomy
PartDescriptionLabelVisible, above the field, naming what is searched: "Search bookings", not "Search".IconA magnifier at the start of the field, decorative.FieldAn Input with type="search". The platform’s own clear control is replaced.ClearAn icon button at the end, shown only while the field holds text.CountThe number of matching results below the field, in a role="status" element so it is announced as it changes.
## API
NameKindDescription`flux-search`classWraps the icon, the input and the clear button.`data-flux-search`attributeShows the clear button while the field has a value, and clears on Escape. Requires flux-components.js.`flux-search__icon`classThe magnifier svg, aria-hidden.`flux-search__clear`classButton with aria-label="Clear search", hidden until there is a value. Clearing dispatches an input event.`flux-search__count`classA p with role="status", referenced from the input with aria-describedby. Not explanation: the result count only.
## States
StateTreatmentEmptyIcon and field; the clear button is hidden.With a queryThe clear button appears; the count shows matches, such as "12 of 248 bookings".No resultsThe count says so and suggests the next step: "No bookings match. Check the reference or clear the search."
## Keyboard
KeysAction`Escape`Clears the field and keeps focus in it.`Tab`From the field to the clear button, when it is shown.
## Accessibility

- Keep the visible label. A magnifier and a placeholder are not a label.
- Wrap the search and its results in a search element, or a form with role="search", where it is the main way into the page.
- Reference the count from the input with aria-describedby, and keep it in a role="status" element so changes are announced without moving focus.
- Announce the count after the user pauses typing, not on every keystroke.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-search-icon | -icon-size | -clear-size | -count
- All --flux-field-* tokens, for the input.
## Do and don’t
Do

- Search as the user types when results are local; on submit when each search is a server request.
- Match on the identifiers people paste, such as booking references, as well as names.
- Keep the query when the user navigates away and comes back.Don’t

- Do not hide the label to save space. Put the search in the table toolbar, where its label fits.
- Do not clear the query when results are empty. The user needs it to correct the typo.[PreviousSlider](/components/slider/)[NextCard](/components/card/)
