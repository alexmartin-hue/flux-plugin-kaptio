# Flux — /components/spinner/

Source: https://flux.kaptio.com/components/spinner/

Component

# Spinner
An arc that turns while something loads, with the status written beside it.

Plain-text source, for agents and clipboard use: [/components/source/spinner.txt](/components/source/spinner.txt)

## When to use it
Says that a request is in flight and the interface has not stalled. The arc runs from the brand teal into the Edge pink and fades out, lengthening and shortening as it turns, so it reads as Kaptio rather than as a browser default. The brand modifier draws it in teal alone where a second hue would compete. The status is always text: visible next to the spinner, or read by assistive technology when the spinner stands alone.

Not thisNot for anything that finishes in under half a second; show the result. Not for a known amount of progress, such as an upload or an import with a count; say how far it has got in words and numbers. Not for a card, list or table whose layout is known; use a Skeleton. Not as a decoration on a page that has finished loading.
## Examples

### Sizes
Small sits inline with text or inside a control, the default fills a card or a panel, and large holds a page that is waiting for its first data.

Loading
Loading
LoadinghtmlCopy`Loading
Loading
Loading`
### With a label
Name what is loading. "Loading bookings" tells someone what to wait for; "Loading" alone does not.

Loading bookings
htmlCopy`

Loading bookings
`
### Teal only
flux-spinner--brand drops the pink. Use it beside status colours, on a product accent fill, or anywhere a second hue would read as meaning.

Loading suppliers
htmlCopy`

Loading suppliers
`
## Anatomy
PartDescriptionLoadingThe flux-loading wrapper. Carries role="status", so its label is announced when it appears.SpinnerThe ring, aria-hidden. A conic arc from --flux-spinner-head (teal) through --flux-spinner-accent (Edge pink) to transparent, cut to a ring an eighth of its size.LabelVisible text naming what is loading, or a flux-visually-hidden span when space allows only the ring.
## API
NameKindDescription`flux-loading`classThe wrapper. Give it role="status" and put the label inside it.`flux-spinner`classThe ring. Always aria-hidden="true": the label carries the meaning.`flux-spinner--sm`class--flux-spinner-size-sm, for inline use and inside controls.`flux-spinner--lg`class--flux-spinner-size-lg, for a page or region waiting for its first data.`flux-spinner--brand`classTeal only: the accent takes the head colour. For views where a second hue would compete with status colours.`aria-busy="true"`attributeOn the region being loaded, removed when its content arrives.
## States
StateTreatmentLoadingThe arc turns once every --flux-spinner-duration and grows from a tenth to half the ring and back.Reduced motionThe base layer runs the animation once, so the ring rests as a still arc beside its label.
## Keyboard
KeysAction`—`Not interactive. Focus stays where it was while content loads.
## Accessibility

- Put role="status" on flux-loading and render it with its label, so the label is announced once without moving focus.
- Mark the region being loaded with aria-busy="true" and clear it when the content arrives.
- Keep aria-hidden on the ring. A spinner announced as an image adds nothing the label does not say.
- The arc is a graphic of the brand teal and the Edge pink. Meaning is in the label, so its contrast is not relied on.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-spinner-size | -size-sm | -size-lg
- --flux-spinner-head | -accent
- --flux-spinner-duration | -ease
- --flux-spinner-gap | -label
## Do and don’t
Do

- Wait about half a second before showing a spinner, so a fast response never flashes one.
- Keep the layout of the content that is coming, and put the spinner where it will appear.
- Replace the spinner with a message and a retry action if loading fails or runs long.Don’t

- Do not add a glow or a shadow to the ring.
- Do not show more than one spinner for one request. Load a region once, not each card inside it.
- Do not use a spinner on a button that saves. Disable the button and change its label to say what is happening.
- Do not recolour the arc with a status hue. Loading is not a warning.[PreviousApp shell](/components/app-shell/)[NextProgress and meter](/components/progress/)
