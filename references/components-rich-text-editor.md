# Flux — /components/rich-text-editor/

Source: https://flux.kaptio.com/components/rich-text-editor/

Component

# Rich text editor
A field with a formatting toolbar for short structured text, and the prose styles it produces.

Plain-text source, for agents and clipboard use: [/components/source/rich-text-editor.txt](/components/source/rich-text-editor.txt)

## When to use it
For text that needs a little structure: itinerary notes, supplier instructions, a description shown to travellers. The toolbar covers bold, italic, a heading, a quote and two kinds of list, as one tab stop with arrow-key movement, and each button shows whether its format applies at the cursor. The content is styled by flux-prose, the same class that renders the saved text elsewhere, so what is written is what is shown.

Not thisNot for plain text; use a Textarea. Not for long documents with tables, images and comments; that needs a dedicated editor engine. Not for code.
## Examples

### Editor
Select text and use the toolbar, or move through it with the arrow keys. The pressed state follows the cursor.

Itinerary notes

## Day 2: Golden Circle
Pick-up from the hotel at 08:30. Bring a waterproof layer for Gullfoss.

- Þingvellir National Park
- Geysir geothermal area
- Gullfoss waterfall

htmlCopy`
Itinerary notes

Day 2: Golden CirclePick-up from the hotel at 08:30. Bring a waterproof layer for Gullfoss.Þingvellir National ParkGeysir geothermal areaGullfoss waterfall

`
### Prose
flux-prose renders the saved text anywhere it is read: a booking summary, a traveller document. Headings, lists, quotes, links and code take Flux sizes and roles.

## Day 2: Golden Circle

Pick-up from the hotel at 08:30. Bring a waterproof layer for Gullfoss; the spray carries well beyond the viewing platform.

- Þingvellir National Park

- Geysir geothermal area

- Gullfoss waterfall

Lunch is included at Friðheimar. Tell the guide about allergies at pick-up.
Booking reference `KB-104931`. Full terms are in the [booking conditions](#).

htmlCopy`
Day 2: Golden Circle
Pick-up from the hotel at 08:30. Bring a waterproof layer for Gullfoss; the spray carries well beyond the viewing platform.

Þingvellir National Park
Geysir geothermal area
Gullfoss waterfall

Lunch is included at Friðheimar. Tell the guide about allergies at pick-up.
Booking reference KB-104931. Full terms are in the booking conditions.
`
## Anatomy
PartDescriptionLabelA field label for the content.Toolbarrole="toolbar" in groups divided by hairlines, on layer-02.ToolA square icon button with an accessible name and aria-pressed.ContentA contenteditable region with role="textbox", aria-multiline and flux-prose.
## API
NameKindDescription`flux-editor`classThe field surface holding the toolbar and the content.`data-flux-editor`attributeWires the toolbar, its roving focus and its pressed states.`flux-editor__toolbar | __group`classThe toolbar, with role="toolbar" and a label, and its groups.`flux-editor__tool`classA toolbar button. Give it an aria-label and aria-pressed.`data-command`attributeOn a tool: bold, italic, heading, quote, bullets or numbers.`flux-editor__content`classThe contenteditable region. Add flux-prose, role="textbox", aria-multiline="true" and aria-labelledby.`data-placeholder`attributeOn the content: shown while it is empty. It does not replace the label.`flux-prose`classStyles rich text anywhere it is read, held to the reading measure.
## States
StateTreatmentDefaultThe field border around the toolbar and the content.HoverThe field hover border.FocusThe border turns border-focus while focus is inside, and the content draws an inset focus ring.Tool pressedsurface-selected fill and icon-brand, with aria-pressed="true".
## Keyboard
KeysAction`Tab`Moves to the toolbar, which is one stop, then to the content.`← → Home End`In the toolbar, moves between tools.`Enter, Space`On a tool, applies or removes its format.`⌘B, ⌘I or Ctrl B, Ctrl I`In the content, bold and italic.
## Accessibility

- The toolbar has a label and roving tabindex, so it is one tab stop.
- Each tool reports aria-pressed, so the state is not conveyed by fill alone.
- The content has role="textbox" and aria-multiline, and is labelled by the visible label.
- Formatting uses the browser’s editing commands so the component works without an engine; a product with its own editor engine binds the same toolbar markup to it.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-editor-bg | -border | -border-hover
- --flux-editor-toolbar-bg | -toolbar-padding
- --flux-editor-tool-size | -tool-icon | -tool-hover | -tool-pressed-bg | -tool-pressed-icon
- --flux-editor-content-padding | -min-height
- --flux-prose-text | -gap | -heading-2 | -heading-3 | -quote-border | -quote-text | -link
## Do and don’t
Do

- Offer only the formats the text needs.
- Render saved text with flux-prose so it matches the editor.
- Sanitise the HTML on the server before it is stored or shown.Don’t

- Do not offer colour, font or size controls. Flux sets those.
- Do not use the editor where a Textarea would do.[PreviousAssistant panel](/components/assistant-panel/)[NextBadge](/components/badge/)
