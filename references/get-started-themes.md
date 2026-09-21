# Flux — /get-started/themes/

Source: https://flux.kaptio.com/get-started/themes/

Get started

# Themes
One attribute changes every colour in the system. No component knows which theme is active, because no component references a colour — only a role.

## Switching
htmlCopy``Light is the default and needs no attribute. Setting it explicitly is still useful when you are scoping a light region inside a dark page.

jsCopy`// Persisted, and applied before first paint so there is no flash.
const dark = matchMedia('(prefers-color-scheme: dark)').matches;
const stored = localStorage.getItem('flux-theme');
const theme = stored ?? (dark ? 'dark' : 'light');

document.documentElement.setAttribute('data-flux-theme', theme);`NotePut that script inline in ``, before the first paint. A theme applied after the stylesheet loads produces a visible flash of the wrong theme, which is worse than not offering the choice.
## The three themes
ThemeGroundFor`light`canvas — the Kaptio off-whiteThe default. Carries the Flux 1.x values, so an existing page renders as it did.`dark`neutral-950Dense product UI. Neutral rather than teal, so brand accents and status colours still read as signals.`deep`primary-800 — Kaptio tealSlides, marketing and brand surfaces. This is the ground Kaptio decks already use; 2.0 gives it a name and a full token set.CarefulDeep is a brand ground, not a dark mode. Its tonal range is narrow, which is why`layer-03` aliases `layer-02` and`text-placeholder` aliases `text-subtle`. For information-dense interfaces, use dark.
## All three at once
The same markup, three grounds, no theme-specific code.

Light

### September departures

Twenty-four published, three awaiting supplier.

Publish
On request

Dark

### September departures

Twenty-four published, three awaiting supplier.

Publish
On request

Deep

### September departures

Twenty-four published, three awaiting supplier.

Publish
On request

htmlCopy`
September departures
Twenty-four published, three awaiting supplier.

Publish
On request

`
## Scoping a theme to a region
The attribute works on any element, not only the root.

htmlCopy`

…

Kaptio Edge

`A scoped region must set its own background from `--flux-surface-page` or a`layer-*` token. Setting the attribute changes what the tokens resolve to; it does not paint anything by itself.

## Following the system preference
cssCopy`/* Flux does not do this for you, deliberately: a product should decide
whether its users want the OS preference honoured. */
@media (prefers-color-scheme: dark) {
:root:not([data-flux-theme]) {
color-scheme: dark;
}
}`Most Kaptio product surfaces are light by default because they sit beside Salesforce, which is light. Honour the system preference where the surface stands alone — an internal tool, a dashboard someone keeps open all day — and let it be an explicit choice elsewhere.

## Do and don’t
Do

- Apply the theme attribute before first paint.
- Persist the reader’s choice.
- Give a scoped theme region its own background token.
- Test a new component in all three themes before shipping it.Don’t

- Do not write theme-specific CSS in a component. If you need to, a token is missing.
- Do not use deep for dense product UI.
- Do not nest three layer levels on the deep theme.
- Do not assume light. Anything that references a primitive will not follow the theme.[PreviousInstall](/get-started/install/)[NextUpgrading from 1.x](/get-started/upgrading/)
