# Flux — /foundations/accessibility/

Source: https://flux.kaptio.com/foundations/accessibility/

Foundations

# Accessibility
Flux guarantees the parts a token can guarantee, and checks them mechanically on every build. Documented intent is worth very little; a build that fails is worth a great deal.

## The contract
GuaranteeStandardEnforced bySystem contrast floorWCAG 2.2 AA — 4.5:1 text, 3:1 non-textBuild-time audit and agent ruleBody and primary text contrastWCAG AAA — 7:1Build-time auditSecondary and other text contrastWCAG AA — 4.5:1Build-time auditNon-text contrast (borders, icons, focus)WCAG 1.4.11 — 3:1Build-time auditVisible focus on every interactive elementWCAG 2.4.7Base layer in flux.cssReduced-motion supportWCAG 2.3.3Base layer in flux.cssText resize to 200%WCAG 1.4.4rem-based scale and fluid rootVerifiedThe current build checks 312 pairings across three themes. All pass. Run`npm run check` to reproduce it.
## Contrast, verified
Every text role is checked against every ground it can legitimately sit on, in every theme.

WCAG 2.2 AA is the floor for the whole system: 4.5:1 for text, 3:1 for icons, control borders and the focus ring. Body and primary text are held to AAA (7:1) as well. The audit walks the semantic layer directly: it resolves every`text-*` and `icon-*` token against every`layer-*` and `surface-*` token it is allowed to appear on, in light, dark and deep, and computes the ratio. A failure is a non-zero exit code, and the build stops before it produces anything.

This is why the dark and deep themes are not simply inverted. Several roles had to move several steps up their ramp to clear 7:1 on the third layer, and in the deep theme`text-subtle` and `text-placeholder` collapsed onto the same value because the teal ramp does not contain two distinct greys that both pass. The audit found those; nobody spotted them by eye.

bashCopy`npm run check:contrast

Contrast check passed — 312 pairings across 3 themes meet WCAG thresholds.`
## Focus
Teal, 2px, offset by 2px, in every theme, applied by the base layer.

cssCopy`/* From flux.css. Nothing has to opt in. */
:where(a, button, input, select, textarea, summary, [tabindex]):focus-visible {
outline: var(--flux-focus-ring-width) solid var(--flux-focus-ring);
outline-offset: var(--flux-focus-ring-offset);
}`Flux 1.x published `--flux-primary-300` as its focus colour. On white that is 2.4:1, below the 3:1 that WCAG 1.4.11 requires for a non-text indicator — a documented token that failed the standard it was meant to satisfy. 2.0 moves the light-theme focus ring to `--flux-primary-400`, which measures 5.8:1.

The colour is the same teal in all three themes. Focus is the one signal a keyboard user cannot afford to hunt for, so it does not adapt, and it is never a browser default or a Tailwind blue.

Never`outline: none` without an equivalent replacement. Removing focus makes an interface unusable by keyboard, and it is the single most common accessibility defect in generated UI code.
## What is exempt, and why
Two categories are deliberately outside the audit.

TokenExemptionBasis`--flux-text-disabled`No contrast minimumWCAG 1.4.3 exempts inactive controls. Disabled text is meant to read as unavailable.`--flux-border-default`Not held to 3:1Decorative separation only. Any border that conveys the boundary of a control uses --flux-border-strong, which is audited.This is why `--flux-field-border` binds to `border-strong` rather than`border-default`. A field's edge is what tells you where to click, so it is a non-text element carrying information, and it is held to 3:1.

## What tokens cannot do for you
Colour and focus are the easy half. The rest is structure, and it is on you.

- Semantic HTML. A `div` with a click handler is not a button however it is styled. Every component page states which element to use.
- Accessible names. An icon-only button, an avatar and a bare input all need one. Flux cannot infer it.
- Keyboard behaviour. Tabs need roving tabindex; modals need focus return. Both are documented on their component pages, and both are commonly skipped.
- State beyond colour. A red border is not an error message. Pair it with`aria-invalid` and text that says what to do.
- Heading order. Style with the token, structure with the element. A styled `h4` after an `h1` is a broken outline.
## Do and don’t
Do

- Treat WCAG 2.2 AA as the floor. Use semantic text roles rather than picking a colour that looks dark enough.
- Use native elements — button, dialog, select, table — before reaching for ARIA.
- Give every icon-only control an accessible name.
- Bind error text to its field with aria-describedby.
- Run npm run check before shipping a token change.Don’t

- Do not remove the focus outline.
- Do not use colour as the only signal for a state.
- Do not use a placeholder as a label.
- Do not choose a heading level for its size.
- Do not put a click handler on a div.[PreviousMotion](/foundations/motion/)[NextButton](/components/button/)
