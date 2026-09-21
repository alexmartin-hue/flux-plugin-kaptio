# Flux — /get-started/install/

Source: https://flux.kaptio.com/get-started/install/

Get started

# Install
Two ways in. A hosted stylesheet when you want tokens in the next minute, and a pinned package when you want a build that cannot change underneath you.

## Hosted, for prototypes
One line. Fonts, tokens, three themes and the base rules.

cssCopy`@import url("https://flux.kaptio.com/tokens/v2/flux.css");`Or from HTML, which avoids the request waterfall an @import creates:

htmlCopy``CarefulThe hosted file tracks the current 2.x release. That is right for a prototype, a slide deck or a one-off page, and wrong for anything you ship — use the package below.The `/v2/` in that path is deliberate. `/tokens/flux.css` without it is Flux 1.x, frozen, still imported at runtime by applications that cannot redeploy to follow a change. 2.0 is not a drop-in replacement for it — see [Upgrading](/get-started/upgrading/).

## Package, for applications
Pinned, versioned, published to the Kaptio GitLab registry.

bashCopy`# Once per machine, or in .npmrc at the repo root.
npm config set @kaptio:registry https://gitlab.com/api/v4/packages/npm/

npm install @kaptio/flux-tokens`cssCopy`/* In your root stylesheet, before anything of your own. */
@import "@kaptio/flux-tokens/flux.css";`ImportGives you`@kaptio/flux-tokens/flux.css`Fonts, all three tiers, base rules. The usual choice.`@kaptio/flux-tokens/flux-tokens.css`Tokens only. Use when you self-host fonts.`@kaptio/flux-tokens/flux.json`Every token as data, for tooling.`@kaptio/flux-tokens/flux-tailwind.css`The Tailwind v4 preset.
## With Tailwind
The preset clears Tailwind's defaults rather than sitting beside them.

cssCopy`@import "tailwindcss";
@import "@kaptio/flux-tokens/flux.css";
@import "@kaptio/flux-tokens/flux-tailwind.css";`Order matters. The preset resets Tailwind's colour, spacing, radius and font namespaces to empty and then repopulates them from Flux tokens. After it loads,`bg-primary-400` is Kaptio Seagreen and `bg-blue-500` does not exist.

That is deliberate. Leaving Tailwind's palette in place means every generated component is one autocomplete away from off-brand, and no amount of documentation closes that gap.

NeverArbitrary-value syntax — `bg-[#056F82]`, `p-[14px]`,`text-[15px]`. It bypasses the token layer entirely, and it is invisible to every theme.
## The component layer
Optional. Working CSS for the twelve documented components, built from tier-3 tokens.

cssCopy`@import "@kaptio/flux-tokens/flux.css";
@import "@kaptio/flux-tokens/flux-components.css";`htmlCopy``Import it and `.flux-button`, `.flux-card` and the rest work immediately, in all three themes. Or read it as the reference implementation and reproduce the same token bindings in React, Lightning Web Components or whatever the project uses — the bindings are the contract, not the class names.

Include `flux-components.js` when using Select or Date picker. It provides listbox and calendar keyboard handling, visible-value updates and ordinary form submission through hidden inputs. The other components remain CSS-only.

## What each artifact contains
FileSizeContents`flux.css`25.7 kBFont imports, 345 tokens across three tiers and three themes, base rules.`flux-tokens.css`23.9 kBThe same tokens, without font imports or base rules.`flux.json`69.1 kBEvery token as structured data, grouped by tier and theme.`flux-tailwind.css`16.9 kBTailwind v4 theme block. Clears defaults, remaps names.`flux-components.css`25.7 kBThe twelve components, as framework-agnostic CSS.`flux-components.js`15.0 kBBehaviour for Select and Date picker.
## Verify the install
Three checks that catch the usual failures.

- Body text should be Lexend Light, not the system sans. If it is not, the font request failed or a later stylesheet is overriding `font-family`.
- Tab to any link. The focus ring should be teal, 2px, offset. A blue ring means a reset is loading after Flux; a missing ring means something set `outline: none`.
- Set `data-flux-theme="dark"` on ``. If the page inverts cleanly, you are on the semantic tier. If parts stay light, those parts are referencing primitives or raw values.htmlCopy``[PreviousOverview](/)[NextThemes](/get-started/themes/)
