# Flux — /components/map/

Source: https://flux.kaptio.com/components/map/

Component

# Map
A route and its stops drawn on a map, with a numbered marker for each stop.

Plain-text source, for agents and clipboard use: [/components/source/map.txt](/components/source/map.txt)

## When to use it
Shows where a trip goes. The confirmed route is a solid line in chart-1, the part still being planned is dashed in chart-muted, and each stop is a numbered marker that opens a popup with the night and the place. The map tiles come from the product’s map library; Flux styles the route, the markers, the popup and the legend that sit on top of them.

Not thisNot as the only way to read a route; pair it with the Itinerary, which carries the same stops as text. Not for a single address; a link to a map service is enough. Not as decoration on a page that does not need geography.
## Examples

### Route
A ring-road tour. The first four stops are confirmed; the leg through Akureyri is still planned. Choose a marker to move the popup.

1
2
3
4
5

Jökulsárlón

Night 4 · Glacier lagoon

- Confirmed

- Planned

htmlCopy`

1
2
3
4
5

Jökulsárlón
Night 4 · Glacier lagoon

Confirmed
Planned

`
## Anatomy
PartDescriptionGroundThe map library’s tiles, or layer-02 in the specimen, inside a hairline border.RouteAn SVG line: solid chart-1 when confirmed, dashed chart-muted when planned.MarkerA numbered button on surface-brand with a layer-01 ring, positioned by --flux-x and --flux-y. The selected marker inverts to layer-01 with a brand border.PopupThe selected stop’s name and night, on surface-overlay with shadow-md, above its marker.LegendWhat the two line styles mean, in the bottom corner.
## API
NameKindDescription`flux-map`classThe container. data-flux-map selects markers and moves the popup. Give it role="group" and a name.`flux-map__routes | __route | __route--planned`classThe SVG of route lines over the ground. With a map library, read --flux-map-route and --flux-map-route-planned with getComputedStyle and pass them to its line layer.`flux-map__marker`classA button per stop with aria-pressed and aria-label naming the stop number and place. data-title and data-meta fill the popup.`--flux-x | --flux-y`attributeInline custom properties placing a marker or the popup as a percentage of the map. A map library computes them from coordinates.`flux-map__popup | __popup-title | __popup-meta`classThe details of the selected stop.`flux-map__legend`classThe key for the line styles.
## States
StateTreatmentMarkersurface-brand with a mono number in text-on-color.Selectedlayer-01 with a brand border and brand number, and the popup above it.Planned legDashed chart-muted line.
## Keyboard
KeysAction`Tab`Moves through the markers in route order.`Enter / Space`Selects the marker and moves the popup to it.`Escape`Closes the popup.
## Accessibility

- The map is supplementary. Put the same stops in an Itinerary or a list on the page; a screen reader cannot follow a line.
- Markers are buttons in route order, named with their number and place.
- Confirmed and planned differ in line style as well as colour, and the legend says which is which.
- Turn off the map library’s scroll-to-zoom inside a scrolling page, or a wheel gesture traps the reader in the map.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-map-height | -ground | -border
- --flux-map-route | -route-planned | -route-width | -route-dash
- --flux-map-marker-size | -marker-bg | -marker-text | -marker-ring
- --flux-map-marker-selected-bg | -marker-selected-text | -marker-selected-border
- --flux-map-popup-width | -popup-bg | -popup-shadow | -popup-padding
## Do and don’t
Do

- Use a muted, low-contrast tile style so the route and markers carry the colour.
- Number markers in the order the trip visits them.Don’t

- Do not use the map library’s default pins or palette; they bypass every theme.
- Do not animate the route drawing in; the line is information, not a transition.[PreviousCalendar view](/components/calendar/)[NextFlow diagram](/components/flow/)
