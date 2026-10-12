# Flux — /components/walkthrough/

Source: https://flux.kaptio.com/components/walkthrough/

Component

# Walkthrough and storyboard
Numbered steps beside the interface they describe, and a strip of screens that tells a flow frame by frame.

Plain-text source, for agents and clipboard use: [/components/source/walkthrough.txt](/components/source/walkthrough.txt)

## When to use it
Explains how a task is done. The walkthrough pairs each step’s text with a frame holding the real components involved, and stacks the two when its container is narrow. The storyboard is the overview: one small screen per moment, numbered, with a caption, for a flow people should understand before they read the detail.

Not thisNot for a task people are doing right now; use the Stepper, which validates as it goes. Not for events in time; use the Timeline. Not for marketing feature lists; this is for explaining a sequence where order is the meaning.
## Examples

### Walkthrough
Three steps to confirm an on-request booking. Each frame holds the components the step talks about.

### Check what is still on request

Open the booking. Anything a supplier has not yet confirmed is marked On request, and the booking cannot be confirmed until it is resolved.

Hotel Borg, 2 roomsConfirmed
Glacier walk, 12 placesOn request

The services list on the booking.

### Chase the supplier

The note tells you who to contact and by when. Record their answer on the service, and the badge changes to match.

Reply due by 9 October

Iceland Guides holds the places until then.

### Confirm the booking

When every service is confirmed, Confirm booking becomes available. The agent receives the confirmation straight away.

Confirm booking

htmlCopy`

Check what is still on request
Open the booking. Anything a supplier has not yet confirmed is marked On request, and the booking cannot be confirmed until it is resolved.

Hotel Borg, 2 roomsConfirmed
Glacier walk, 12 placesOn request

The services list on the booking.

Chase the supplier
The note tells you who to contact and by when. Record their answer on the service, and the badge changes to match.

Reply due by 9 October
Iceland Guides holds the places until then.

Confirm the booking
When every service is confirmed, Confirm booking becomes available. The agent receives the confirmation straight away.

Confirm booking

`
### Storyboard
The same flow as four frames, for an overview before the detail.

KB-104931

1 service on request

The agent opens the booking.

Glacier walk

On request

They find the service still waiting.

Glacier walk

Confirmed

The supplier’s answer is recorded.

Ready to confirm

Confirm booking

The booking is confirmed to the agent.

htmlCopy`

KB-104931
1 service on request

The agent opens the booking.

Glacier walk
On request

They find the service still waiting.

Glacier walk
Confirmed

The supplier’s answer is recorded.

Ready to confirm
Confirm booking

The booking is confirmed to the agent.

`
## Anatomy
PartDescriptionWalkthroughAn ordered list. Its container query stacks text over media below 44rem.Step markerA CSS counter in a surface-brand square, so the number comes from the list order.Step textA heading and a paragraph at the reading measure.MediaA figure with a layer-02 frame holding real Flux components or a screenshot, and an optional caption.StoryboardAn ordered grid of frames, each a bordered 4:3 screen and a caption numbered in brand mono.
## API
NameKindDescription`flux-walkthrough`classOn the ol of steps. It is the container for the narrow layout.`flux-walkthrough__step`classAn li holding the text and the media. Its number comes from the list order.`flux-walkthrough__text | __title`classThe step heading and its paragraphs.`flux-walkthrough__media | __frame`classThe figure and the layer-02 frame that holds components or an image.`flux-storyboard`classOn the ol of frames. Frames fill the row at 16rem minimum.`flux-storyboard__frame | __screen | __caption`classA frame, its 4:3 screen and its numbered caption.`flux-storyboard__screen-title | __screen-meta`classText inside a schematic screen.
## States
StateTreatmentWideWalkthrough text and media side by side, two to three.NarrowBelow a 44rem container, media stacks under the text.
## Keyboard
KeysAction`Tab`Reaches links in the text. Components in a frame are illustrations; give their controls tabindex="-1" or use a screenshot.
## Accessibility

- Both are ordered lists, so the step count and position are announced.
- Each step has a real heading, so the walkthrough can be navigated by headings.
- A screenshot in a frame needs alt text saying what it shows, not what it is.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-walkthrough-gap | -marker-size | -marker-bg | -marker-text
- --flux-walkthrough-media-bg | -media-padding
- --flux-storyboard-frame-width | -gap | -number
- --flux-storyboard-screen-bg | -screen-border | -screen-padding
## Do and don’t
Do

- Show the real components in the frame, so the walkthrough stays true when they change.
- Keep one idea per step.Don’t

- Do not number content where order is not the meaning; this is for sequences.
- Do not let a storyboard replace the walkthrough for people doing the task; it is the overview.[PreviousStepper and wizard](/components/stepper/)[NextList and detail](/components/split-view/)
