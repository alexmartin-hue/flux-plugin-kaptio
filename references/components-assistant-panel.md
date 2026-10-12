# Flux — /components/assistant-panel/

Source: https://flux.kaptio.com/components/assistant-panel/

Component

# Assistant panel
A side panel for conversing with Runa: messages, cited sources, suggestions and a prompt.

Plain-text source, for agents and clipboard use: [/components/source/assistant-panel.txt](/components/source/assistant-panel.txt)

## When to use it
Gives an AI assistant a consistent, quiet place beside the work it is helping with. The conversation is a log, so new messages are announced. Replies cite the records they were drawn from as links, so every claim can be checked. Suggestions offer a first prompt, a disclaimer sits under the prompt field, and Enter sends while Shift and Enter adds a line. The panel says it is working while a reply is pending, and the page supplies the reply.

Not thisNot as the only way to do something the interface could do directly. Not for system notifications; use a Toast. Not with a chat bubble style, an avatar for the assistant, or a typing animation.
## Examples

### In a booking
Type a message or press a suggestion. On this page, a sample reply arrives after a moment.

## Runa

Booking KB-104931

You

Which rooms are still unconfirmed?

Runa

Six double rooms at Hotel Rangá for 14–16 September are still on request. The supplier was asked three days ago and has not replied.

- [KB-104931Supplier request](#)

- [CT-2026-118Hotel Rangá contract](#)

Draft a reminder to the hotel
Find alternative hotels

Ask Runa

Runa can be wrong. Check figures against the booking before you send them.

htmlCopy`

Runa
Booking KB-104931

You
Which rooms are still unconfirmed?

Runa
Six double rooms at Hotel Rangá for 14–16 September are still on request. The supplier was asked three days ago and has not replied.

KB-104931Supplier request
CT-2026-118Hotel Rangá contract

Draft a reminder to the hotel
Find alternative hotels

Ask Runa

Runa can be wrong. Check figures against the booking before you send them.

`
### Working
While a reply is pending, the log holds a status with a small Spinner and a sentence. The script adds it on send and removes it when the page responds.

You

Find alternative hotels near Hella for 14 September.

Runa is working on it

htmlCopy`

You
Find alternative hotels near Hella for 14 September.

Runa is working on it

`
## Anatomy
PartDescriptionHeaderThe product mark in the agents accent, the assistant’s name, the context it is working in, and a close button.Logrole="log" holding the messages, scrolling on its own.MessageThe assistant’s replies sit on the panel ground; the person’s messages sit right-aligned on layer-02, as a bubble with a small tail towards their side.SourcesLinks under a reply, each with a mono reference.SuggestionsSmall secondary buttons with a starting prompt. Hidden once the conversation starts, if the page chooses.ComposerA labelled textarea that grows with its text, a send button, and the disclaimer.
## API
NameKindDescription`flux-assistant`classThe panel, an aside labelled by its title.`data-flux-assistant`attributeThe assistant’s name. Wires sending, suggestions and the working status.`flux-assistant__header | __mark | __heading | __title | __subtitle | __close`classThe header and its parts. The mark is graphic only.`flux-assistant__log`classOn the role="log" element.`flux-assistant__message`classA reply. Start it with a visually hidden sender name.`flux-assistant__message--user`classThe person’s message.`flux-assistant__sources | __source | __source-ref`classThe cited sources under a reply.`flux-assistant__suggestions`classThe suggestion row. Hidden when empty.`data-flux-assistant-suggestion`attributeOn a suggestion button: sends its text as a message.`flux-assistant__composer | __field | __send | __disclaimer`classThe prompt form and its parts.`flux-assistant-message`elementEvent dispatched on send, with detail.message and detail.respond({ paragraphs, sources }). Sources are { label, ref, href }.
## States
StateTreatmentEmptyThe log is empty and the suggestions offer a first prompt.WorkingA status with a small Spinner and a sentence, until the reply arrives.RepliedThe reply, with its sources as links.
## Keyboard
KeysAction`Enter`In the prompt, sends the message.`Shift Enter`In the prompt, adds a new line.`Tab`Moves through sources, suggestions, the prompt and send.
## Accessibility

- The log is role="log", so new messages are announced politely as they arrive.
- Each message starts with a visually hidden sender, so the conversation reads as a dialogue.
- The prompt has a visible label; the disclaimer is bound to it with aria-describedby.
- The agents accent is a graphic mark only. All text uses text roles.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-assistant-width | -height | -bg | -border
- --flux-assistant-padding | -gap | -user-bg | -tail-size
- --flux-assistant-mark | -mark-size | -meta
- --flux-assistant-source-bg | -source-hover
## Do and don’t
Do

- Cite the records a reply was drawn from, with their references.
- Say what the assistant is working on, in the subtitle.
- Let the person check and edit anything the assistant drafts before it is sent.Don’t

- Do not stream text in with a typing effect or animate the reply.
- Do not give the assistant a face, a coloured bubble or a glow.
- Do not use the product accent for text.[PreviousFile upload](/components/file-upload/)[NextRich text editor](/components/rich-text-editor/)
