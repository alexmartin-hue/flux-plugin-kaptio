# Flux — /foundations/motion/

Source: https://flux.kaptio.com/foundations/motion/

Foundations

# Motion
Motion in Flux confirms that something happened. It is fast, it is short, and it does not perform. If an animation draws attention to itself rather than to the change it describes, it is the wrong animation.

## Two tracks
After Carbon: productive motion for feedback the user is waiting on, expressive motion for transitions that carry meaning.

TrackForFeelProductiveHover, focus, toggles, field states, anything the user triggered and is waiting on.Quick out, quick settle. The user should barely register it.ExpressiveModals, drawers, page transitions, anything that changes what the screen is about.A little more travel and a little more time, because the change is worth noticing.Nearly all product motion is productive. Expressive motion is for the handful of moments where the interface reorganises itself.

## Easing
TokenCurveUse`--flux-ease-productive``cubic-bezier(0.2, 0, 0.38, 0.9)`The default. Interface feedback.`--flux-ease-expressive``cubic-bezier(0.4, 0.14, 0.3, 1)`Overlays and meaningful transitions.`--flux-ease-entrance``cubic-bezier(0, 0, 0.38, 0.9)`Something arriving. Decelerates in.`--flux-ease-exit``cubic-bezier(0.2, 0, 1, 0.9)`Something leaving. Accelerates out.`--flux-ease``cubic-bezier(0.4, 0, 0.2, 1)`Flux 1.x general-purpose curve. Retained.NoteEntrance and exit are asymmetric on purpose. Things that arrive should settle; things that leave should get out of the way.
## Duration
TokenValueUse`--flux-duration-fast`150msHover, focus, small state changes. The default.`--flux-duration-normal`200msDropdowns, tooltips, expanding rows.`--flux-duration-slow`300msModals, drawers, panels.`--flux-duration-deliberate`480msMarketing and slide transitions only.CarefulAnything over 300ms in product UI feels like latency rather than polish. The reader is waiting on the result, not watching the transition.
## What may animate
Transform and opacity are cheap. Everything else costs a layout pass.

cssCopy`/* Correct. Composited, no layout work, honest about what changed. */
.panel {
transition:
background-color var(--flux-duration-fast) var(--flux-ease-productive),
border-color var(--flux-duration-fast) var(--flux-ease-productive),
opacity var(--flux-duration-fast) var(--flux-ease-productive);
}

/* Wrong. transition: all animates properties you did not think about,
including ones that force layout on every frame. */
.panel {
transition: all 0.3s ease;
}`PropertyVerdictopacity, transformYes. Composited.background-color, border-color, colorYes, at duration-fast.box-shadowSparingly. Only where a surface genuinely lifts.width, height, top, left, margin, paddingNo. Animate transform instead.transition: allNever.NeverA scale transform on button hover. A card that lifts and grows. A gradient that shifts on hover. Flux buttons change colour and nothing else, and that restraint is what makes a dense interface feel calm.
## Reduced motion
Handled by the base layer, for everyone, without anyone remembering to.

cssCopy`/* From flux.css. Applies to every consumer automatically. */
@media (prefers-reduced-motion: reduce) {
@layer flux.base {
*, *::before, *::after {
animation-duration: 1ms !important;
animation-iteration-count: 1 !important;
transition-duration: 1ms !important;
scroll-behavior: auto !important;
}
}
}`This is deliberately mechanical. Asking every engineer and every agent to remember a media query produces a system where most things honour the preference and a few do not, which is indistinguishable from not honouring it.

If a specific animation carries meaning that cannot survive being removed, handle it in your own reduced-motion query rather than opting out of this one.

## Do and don’t
Do

- Default to duration-fast with ease-productive.
- Name the properties you are transitioning.
- Use entrance and exit curves for things that arrive and leave.
- Let the base layer handle reduced motion.Don’t

- Do not use transition: all.
- Do not animate layout properties.
- Do not scale or lift on hover.
- Do not exceed 300ms in product UI.[PreviousElevation & layers](/foundations/elevation/)[NextAccessibility](/foundations/accessibility/)
