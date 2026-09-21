# Flux — /foundations/elevation/

Source: https://flux.kaptio.com/foundations/elevation/

Foundations

# Elevation & layers
A surface placed on layer-01 uses layer-02. A surface inside that uses layer-03. Nobody chooses a grey, and nothing breaks when the theme changes.

## The problem it solves
Hand-picked greys work until the background moves.

The usual way to separate a card from its page is to pick a slightly different grey. It works — once, on one background, in one theme. Put the same card inside a panel and the contrast disappears. Switch to dark and the relationship inverts.

Carbon’s answer, adopted here, is to name the nesting level rather than the colour. A component asks for “one level up from where I am”, and the theme decides what that means. In light that is a step towards white; in dark it is a step towards a lighter neutral; in deep it is a step through the teal ramp.

## The layer set
TokenMeaningLightDarkDeep`--flux-layer-00`Page ground`canvas``neutral-950``primary-800``--flux-layer-01`First surface`white``neutral-900``primary-700``--flux-layer-02`A surface inside that`neutral-50``neutral-800``primary-600``--flux-layer-03`A surface inside that`neutral-100``neutral-700``primary-600``--flux-layer-hover-01…03`Hover fill per level`—``—``—`CarefulIn the deep theme `layer-03` aliases `layer-02`. The teal ramp does not have another usable step that keeps text above 7:1, and an unreadable third level is worse than a repeated one. Three levels of nesting on a teal ground is a sign the layout needs flattening rather than another token.
## Nesting, live
Switch the theme in the top bar. Nothing below has theme-specific code.

layer-01layer-02layer-03cssCopy`.panel        { background: var(--flux-layer-01); }
.panel .panel { background: var(--flux-layer-02); }
.panel .panel .panel { background: var(--flux-layer-03); }`
## Shadow
Flux is a flat system. Shadow means “this floats above the page”, and almost nothing does.

TokenUse`--flux-shadow-sm`Barely there. A raised surface that is still part of the page.`--flux-shadow-md`Hover on an interactive card. The ceiling for anything in flow.`--flux-shadow-lg`Popovers, dropdowns, tooltips.`--flux-shadow-xl`Modals and the command palette. Genuinely above the page.NeverA coloured shadow, a glow, or a shadow used as decoration on a static card. If a surface is not floating, it separates with a layer step and a hairline — not with depth it does not have.
## A naming collision worth knowing
Two unrelated things in Flux use the word “layer”.

TokenWhat it is`--flux-layer-01, -02, -03`Elevation. New in 2.0.`--flux-layer-core, --flux-layer-edge, …`Kaptio product accent colours, inherited from Flux 1.x. Graphic use only.`--flux-product-core, --flux-product-edge, …`The same product accents under their 2.0 names. Prefer these.The v1 product names still resolve and always will. New code should use the`product-*` forms so that "layer" means elevation and nothing else.

## Do and don’t
Do

- Step one layer per level of nesting, and let the theme decide the colour.
- Separate surfaces with a layer step and a hairline before reaching for shadow.
- Reserve shadow for things that genuinely float: overlays, popovers, modals.
- Use product-* for product accents in new code.Don’t

- Do not hand-pick a grey to separate two surfaces.
- Do not skip a layer level to get more contrast.
- Do not nest three levels deep on the deep theme.
- Do not use a coloured or glowing shadow.[PreviousLayout & spacing](/foundations/layout/)[NextMotion](/foundations/motion/)
