# Flux — /get-started/upgrading/

Source: https://flux.kaptio.com/get-started/upgrading/

Get started

# Upgrading from 1.x
1.x keeps serving at the URL it always served from. 2.0 is a version prefix away, and moving to it is a decision you make per application rather than one that happens to you overnight.

## Two URLs
The version is in the path because the old path is a live dependency.

Kaptio applications import the hosted stylesheet at runtime, from a URL their own deploys do not control. Publishing 2.0 over the top of it would have changed every one of them at once, without a review, a test run or a way back. So it did not go over the top of it.

URLServesChanges again`/tokens/flux.css`Flux 1.x, exactly as it wasNever`/tokens/v2/flux.css`The current 2.x buildWithin 2.x, additivelyEnforcedThe 1.x files are checked against a recorded hash on every build. If a byte changes, the build fails rather than publishing it to a URL other repositories depend on.
## The upgrade
cssCopy`/* Before */
@import url("https://flux.kaptio.com/tokens/flux.css");

/* After */
@import url("https://flux.kaptio.com/tokens/v2/flux.css");`Or pin the package, which is the right choice for anything you ship. See [Install](/get-started/install/).

## Six differences to check
Everything else in the 1.x surface carries over under the same name and the same light-theme value. These six do not, so grep for them before you move.

Token1.x2.0What to do`--flux-grey-400``#212121`RemovedUse --flux-text-primary, or --flux-neutral-900 for graphic fills.`--flux-flow-achieved-duration``—`RemovedSet the duration on the animation directly, or propose a token.`--flux-flow-return-countdown``5000``8s`Breaks any JavaScript parsing it as a number. Read it as a time or hard-code the value.`--flux-flow-header-height``3rem``3.5rem`Check anything positioned against the header offset.`--flux-flow-header-bg``#F5F5F5`WhiteThe header now sits flat against the page. Add a hairline if it needs separating.`--flux-flow-entry-duration``300ms``480ms`Entry motion is slower. Nothing breaks; it will look different.CarefulFive of the six are `--flux-flow-*`, which only the booking flow uses. If your application does not reference that group, `--flux-grey-400` is the only name you need to look for.
## Three behaviour changes
Three things behave differently without any token changing name, and all three are fixes.

### 1. The focus ring is darker
Flux 1.x used `--flux-primary-300` for focus, which measures 2.4:1 on white and fails WCAG 1.4.11. 2.0 uses `--flux-primary-400` at 5.8:1. Focus rings will look slightly stronger. This is the intended outcome.

### 2. Bold weights are forced to 700
The base layer now sets `font-weight: 700` on`b`, `strong`, every heading and `th`. If your CSS requested Lexend 500 or 600, the browser was synthesising it; now it resolves to the real bold. Text that was faux-bold will look correct rather than smeared.

### 3. The root font size is fluid
`html` now uses `clamp(16px, 0.875rem + 0.4vw, 19px)`. Below roughly 1280px nothing changes. Above it, every `rem` in your layout grows proportionally — which is the point, but it will surprise you once if you have mixed`px` and `rem` in the same layout.

CarefulIf a layout looks wrong on a large display after upgrading, look for `px` values sitting next to `rem` values. They no longer scale together.
## The v1 alias table
What the old names now mean, and what to reach for in new code.

Flux 1.xStill worksPrefer in new code`--flux-background`Yes`--flux-surface-page``--flux-surface`Yes`--flux-layer-01``--flux-surface-alt`Yes`--flux-layer-02``--flux-heading`Yes`--flux-text-primary``--flux-layer-core`Yes`--flux-product-core``--flux-layer-edge`Yes`--flux-product-edge``--flux-layer-pex`Yes`--flux-product-pex``--flux-layer-agents`Yes`--flux-product-agents``--flux-grey-100, -200, …`Yes`--flux-neutral-100, -200, …`CarefulThe `--flux-layer-*` product names now sit beside`--flux-layer-01…03`, which are elevation levels and something else entirely. Moving to `--flux-product-*` removes the ambiguity, which is why it is worth doing even though nothing forces it.
## What to adopt, and when
Ordered by return on effort.

ChangeEffortWhyMove colour references from primitives to semantic rolesMediumThe prerequisite for every theme. Nothing else in 2.0 works without it.Replace hand-picked greys with layer-01…03LowNested surfaces stop needing a decision, and start working in every theme.Use the mono voice for metadata and labelsLowThe cheapest visible upgrade. Data stops looking like prose.Rename layer-core and friends to product-*LowRemoves the collision with the elevation tokens.Adopt the component layerVariesOnly where you are already rebuilding. Existing components that reference tier 2 are fine as they are.[PreviousThemes](/get-started/themes/)[NextToken architecture](/foundations/tokens/)
