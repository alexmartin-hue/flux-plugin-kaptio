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

bashCopy`# .npmrc at the repo root. The registry is private, so every install authenticates.
@kaptio:registry=https://gitlab.com/api/v4/projects/80171946/packages/npm/
//gitlab.com/api/v4/projects/80171946/packages/npm/:_authToken=${CI_JOB_TOKEN}`bashCopy`npm install @kaptio/flux-tokens@2.2.1`A pipeline in another project can read the package with `CI_JOB_TOKEN` once that project is on the job token allowlist of `kaptio1/kaptio-tooling/kaptio-flux`. Ask a maintainer to add it. Locally, set `CI_JOB_TOKEN` to a personal access token with the `read_api` scope; npm fails on the unset variable otherwise.

cssCopy`/* In your root stylesheet, before anything of your own. */
@import "@kaptio/flux-tokens/flux.css";`ImportGives you`@kaptio/flux-tokens/flux.css`Fonts, all three tiers, base rules. The usual choice.`@kaptio/flux-tokens/flux-tokens.css`Tokens only. Use when you self-host fonts.`@kaptio/flux-tokens/flux.json`Every token as data, for tooling.`@kaptio/flux-tokens/flux-tailwind.css`The Tailwind v4 preset.
## With Tailwind
The preset clears Tailwind's defaults rather than sitting beside them.

cssCopy`@import "tailwindcss";
@import "@kaptio/flux-tokens/flux.css";
@import "@kaptio/flux-tokens/flux-tailwind.css";`Order matters. The preset resets Tailwind's colour, spacing, radius and font namespaces to empty and then repopulates them from Flux tokens. After it loads,`bg-primary-400` is Kaptio Seagreen and `bg-blue-500` does not exist.

That is deliberate. Leaving Tailwind's palette in place means every generated component is one autocomplete away from off-brand, and no amount of documentation closes that gap.

Every stock colour family resolves to the nearest Flux ramp step, and steps 700 and darker stay readable as text, at 4.5:1 or better on white. The weight utilities resolve to the loaded weights: `font-medium` is Lexend Light and`font-semibold` Lexend Bold. Load `flux-prototype.css` before the preset and the same utilities follow the prototype weights instead.

NeverArbitrary-value syntax — `bg-[#056F82]`, `p-[14px]`,`text-[15px]`. It bypasses the token layer entirely, and it is invisible to every theme.
## The component layer
Optional. Working CSS for the 48 documented components, built from tier-3 tokens.

cssCopy`@import "@kaptio/flux-tokens/flux.css";
@import "@kaptio/flux-tokens/flux-components.css";`htmlCopy``Import it and `.flux-button`, `.flux-card` and the rest work immediately, in all three themes. Or read it as the reference implementation and reproduce the same token bindings in React, Lightning Web Components or whatever the project uses — the bindings are the contract, not the class names.

Include `flux-components.js` on any page with an interactive component. It provides keyboard handling, visible-value updates and form values for Select, Date picker, Slider and Search; chart inspection and Heatmap navigation; the data table, Menu, Tooltip, App shell, Reorder and Editable cell; and opens Modal and Drawer from invoker commands in browsers that lack them. Markup added after the page loads is wired too; see[In React and other frameworks](#frameworks). Each component’s API lists the attributes that require it. Static components such as Button, Card, Badge and a plain Table need no script.

## In React and other frameworks
The script follows the document, so markup a framework mounts later works without wiring.

htmlCopy`

`jsCopy`// main.tsx, once, before the app renders.
import '@kaptio/flux-tokens/flux-components.js';``flux-components.js` enhances every component when it enters the document — on load, on a lazily loaded route, or when a framework mounts or re-renders it — and when the parts it needs arrive later, such as a Select’s options. It releases the listeners a component attaches to the page when the component leaves, and restores them if it is inserted again. Enhancing is idempotent, so React’s StrictMode double mount is safe. For an explicit lifecycle, such as a test that renders into a detached container, call `Flux.enhance(root)` and`Flux.dispose(root)`.

Three components move or rewrite markup the framework owns. When the framework renders that state, cancel the component’s event with `preventDefault()` and render the change from `event.detail`:

EventOnWhen cancelled`flux-sort`Data tableRows and aria-sort are left to the framework. The sort is still announced.`flux-select-change`SelectThe value text, aria-selected and the hidden input are left to the framework.`flux-reorder · flux-board-move`Reorder, BoardThe item goes back where it started, and the framework renders the move.jsxCopy`const ref = useRef(null);
useEffect(() => {
const table = ref.current;
const onSort = (event) => {
event.preventDefault();
setSort({ column: event.detail.column, direction: event.detail.direction });
};
table.addEventListener('flux-sort', onSort);
return () => table.removeEventListener('flux-sort', onSort);
}, []);

return …;`NoteKey a component on its data, not on its position, so a re-render moves the enhanced element rather than handing its listeners to a different record.
## What each artifact contains
FileSizeContents`flux.css`53.1 kBFont imports, 817 tokens across three tiers and three themes, base rules.`flux-tokens.css`51.4 kBThe same tokens, without font imports or base rules.`flux.json`144.7 kBEvery token as structured data, grouped by tier and theme.`flux-tailwind.css`21.9 kBTailwind v4 theme block. Clears defaults, remaps names.`flux-components.css`156.7 kBThe 48 components, as framework-agnostic CSS.`flux-components.js`103.2 kBBehaviour for the interactive components: keyboard handling, form values and invoker commands.
## Verify the install
Three checks that catch the usual failures.

- Body text should be Lexend Light, not the system sans. If it is not, the font request failed or a later stylesheet is overriding `font-family`.
- Tab to any link. The focus ring should be teal, 2px, offset. A blue ring means a reset is loading after Flux; a missing ring means something set `outline: none`.
- Set `data-flux-theme="dark"` on ``. If the page inverts cleanly, you are on the semantic tier. If parts stay light, those parts are referencing primitives or raw values.htmlCopy``[PreviousOverview](/)[NextThemes](/get-started/themes/)
