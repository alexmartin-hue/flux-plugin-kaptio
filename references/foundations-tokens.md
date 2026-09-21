# Flux — /foundations/tokens/

Source: https://flux.kaptio.com/foundations/tokens/

Foundations

# Token architecture
Three tiers, one direction of reference. Components point at roles, roles point at values, and nothing points back up. That single rule is what makes three themes possible without a component knowing any of them exist.

## The three tiers
TierHoldsExampleTheme-awarePrimitiveRaw values with no meaning attached`--flux-primary-400: #056F82`NoSemanticRoles, resolved per theme`--flux-text-link: var(--flux-primary-400)`YesComponentDimensions and bindings for one part`--flux-button-height-md: 2.25rem`InheritsA primitive is a fact about a colour or a size. `--flux-primary-400` is a particular teal; it is not a link, or a border, or a brand. Naming it after its use would be a lie the moment it appears somewhere else.

A semantic token is a decision about a role. `--flux-text-link` means "what a link looks like here", and its value is whatever the active theme says. This is the only tier that changes between themes, which is exactly why it is the tier your code should reference.

A component token is a decision about one part of one component —`--flux-field-height`, `--flux-card-padding`. Component tokens that carry colour point at semantic tokens, never at primitives, so they theme for free.

## Which tier to reference
Semantic, in almost every case.

cssCopy`/* Correct. A role. Resolves per theme, survives a palette change. */
.summary-panel {
background: var(--flux-layer-01);
color: var(--flux-text-primary);
border: var(--flux-hairline) solid var(--flux-border-subtle);
}

/* Wrong. A primitive in a place that needs a role. Locks in one theme. */
.summary-panel {
background: var(--flux-white);
color: var(--flux-black);
border: 1px solid var(--flux-grey-100);
}

/* Wrong. A raw value. Invisible to every theme and every future change. */
.summary-panel {
background: #ffffff;
color: #212121;
border: 1px solid #ebebeb;
}`NotePrimitives are legitimate in exactly two places: inside the definition of a semantic token, and in graphic contexts with no interface role — a chart series, an illustration fill, a product accent mark.
## Naming
Semantic names follow Carbon’s functional convention under Flux’s existing`--flux-` prefix: a category, then a role, then an optional state. Flat kebab-case, no nesting, no abbreviations.

CategoryAnswersExamplestext-*What colour is this text?`text-primary, text-subtle, text-on-color`layer-*What is the fill of this nesting level?`layer-01, layer-hover-02`surface-*What is the fill of this named surface?`surface-page, surface-brand, surface-backdrop`border-*What colour is this edge?`border-subtle, border-interactive`icon-*What colour is this icon?`icon-primary, icon-brand`focus-*How is focus drawn?`focus-ring, focus-ring-width`Careful`--flux-layer-01` is an elevation level. `--flux-layer-core` and its siblings are product accent colours inherited from Flux 1.x. They are unrelated. In new code use the 2.0 names — `--flux-product-core`, `--flux-product-edge` — and keep the word "layer" for elevation.
## The compatibility contract
Flux 2.0 is strictly additive. No name was removed, and no value changed.

Every token Flux 1.x published exists in 2.0 with a byte-identical value in the light theme. `--flux-background`, `--flux-surface`,`--flux-heading` and the rest are permanent aliases, not deprecations with a timer on them.

What changed is that they became theme-aware — but only for consumers who opt into a theme v1 never had. A page that never sets `data-flux-theme` renders exactly as it did before.

## How tokens are generated
One TypeScript source, four published artifacts. Nothing is hand-edited.

ArtifactFor`flux.css`The full bundle: fonts, all three tiers, base rules.`flux-tokens.css`Tokens only, for projects that load their own fonts.`flux.json`Machine-readable, for tooling and design tools.`flux-tailwind.css`A Tailwind v4 preset that displaces the default palette.The generator validates before it emits. If a theme is missing a key another theme declares, or a semantic token references a primitive that does not exist, the build fails. Drift between the three themes is not something anyone has to notice by eye.

bashCopy`npm run tokens        # regenerate all four artifacts
npm run check         # regenerate, then audit every contrast pairing`
## Do and don’t
Do

- Reference semantic tokens in product code, and let the theme resolve them.
- Add a new semantic token when you find yourself reaching for a primitive twice.
- Bind component colour tokens to semantic tokens, never to primitives.
- Regenerate the artifacts rather than editing the generated CSS.Don’t

- Do not use a raw hex, rem or millisecond value where a token exists.
- Do not reference a primitive for an interface role.
- Do not add a token to one theme without adding it to all three.
- Do not rename or remove a Flux 1.x token. The contract is permanent.[PreviousUpgrading from 1.x](/get-started/upgrading/)[NextColour](/foundations/color/)
