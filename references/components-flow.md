# Flux — /components/flow/

Source: https://flux.kaptio.com/components/flow/

Component

# Flow diagram
Steps and the connections between them on a pannable canvas, for automations and process maps.

Plain-text source, for agents and clipboard use: [/components/source/flow.txt](/components/source/flow.txt)

## When to use it
Shows how steps connect: a trigger, the conditions it passes through and the actions at the end. Nodes are buttons laid out on a grid of flow units, edges are curves with arrowheads in one SVG, and branch labels sit on their edges. Selecting a node highlights the edges that touch it. The canvas scrolls inside its frame, and a minimap shows where the viewport sits.

Not thisNot for a strictly linear sequence; use the Stepper or the Timeline. Not for an organisation chart or a hierarchy; use a tree or nested list. Not for editing a diagram freely; that needs a canvas library, which this component styles but does not replace.
## Examples

### Automation
Final documents go out 30 days before departure. Select a node to see its connections; scroll the canvas and watch the minimap.

Yes
No

- TriggerBooking confirmed. Then: Departs within 30 days

- ConditionDeparts within 30 days. Yes: Send final documents. No: Until 30 days before departure

- ActionSend final documents. Then: Assign tour guide

- WaitUntil 30 days before departure. Then: Send final documents

- ActionAssign tour guide

htmlCopy`

Yes
No

TriggerBooking confirmed. Then: Departs within 30 days
ConditionDeparts within 30 days. Yes: Send final documents. No: Until 30 days before departure
ActionSend final documents. Then: Assign tour guide
WaitUntil 30 days before departure. Then: Send final documents
ActionAssign tour guide

`
## Anatomy
PartDescriptionFrameA bordered layer-01 container with a scrolling viewport.CanvasSized in flow units with --flux-cols and --flux-rows, under a dot grid.NodeA button positioned by --flux-x, --flux-y, --flux-w and --flux-h, with a mono type label and a title. Selected nodes take surface-selected and a brand border.EdgeAn SVG path in border-strong with an arrowhead, in the same units as the nodes. Edges touching the selected node turn brand.Edge labelA mono label at the midpoint of a branch, on the canvas colour so the line breaks behind it.MinimapThe nodes in miniature and a frame for the visible area, in the bottom corner. Clicking it scrolls the canvas.
## API
NameKindDescription`flux-flow`classThe frame. data-flux-flow handles selection, the edge highlight and the minimap.`flux-flow__viewport`classThe scroll container. Give it role="region", a name and tabindex="0".`flux-flow__canvas`classSized by inline --flux-cols and --flux-rows in flow units.`flux-flow__edges | __edge | __arrow`classThe SVG, with viewBox="0 0 cols rows", its paths and arrowhead markers. data-from and data-to name the nodes an edge joins.`flux-flow__label`classAn edge label, positioned with unitless --flux-x and --flux-y.`flux-flow__nodes | __node | __node-type | __node-title`classThe ordered list of node buttons, each with data-node, aria-pressed and inline unitless --flux-x, --flux-y, --flux-w and --flux-h.`flux-flow__minimap | __minimap-node | __minimap-viewport`classThe overview, drawn in the same units.`flux-flow-select`attributeEvent dispatched on the frame when the selection changes. detail.node is the button, or null.
## States
StateTreatmentDefaultlayer-01 node with a border-strong hairline.Selectedsurface-selected, brand border, and brand edges in and out.ScrolledThe minimap frame follows the visible area.
## Keyboard
KeysAction`Tab`Moves through the nodes in list order, which is the order of the process.`Enter / Space`Selects the node, or clears the selection if it was selected.`Arrow keys`Scroll the canvas when the viewport has focus.
## Accessibility

- Edges are invisible to a screen reader, so each node carries hidden text naming what comes next: “Yes: Send final documents. No: Until 30 days before departure.” Write node titles so they read on their own after a branch label.
- List nodes in the order the process runs, not the order they were drawn.
- The minimap is hidden from assistive technology; the viewport scrolls with the keyboard.
- Selected state is a border and a ground change, and aria-pressed says it too.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-flow-unit | -height | -bg | -border | -grid
- --flux-flow-node-bg | -node-border | -node-padding | -node-type
- --flux-flow-node-selected-bg | -node-selected-border
- --flux-flow-edge | -edge-active | -edge-width | -label-bg
- --flux-flow-minimap-width | -minimap-bg | -minimap-node | -minimap-viewport
## Do and don’t
Do

- Lay the flow out left to right, branching up and down.
- Label every branch out of a condition.Don’t

- Do not colour nodes by type; the type label says it. Colour is for the selection.
- Do not cross edges when moving a node would avoid it.[PreviousMap](/components/map/)[NextApp shell](/components/app-shell/)
