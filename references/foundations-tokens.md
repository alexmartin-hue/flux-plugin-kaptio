# Flux — /foundations/tokens

Source: https://flux.kaptio.com/foundations/tokens

[Flux](/)
Foundations

# Token Reference

Every Flux token in one place. The canonical source is `flux.json` —
CSS and TypeScript files are generated from it automatically.

## How It Works
1  Edit flux.json

The single source of truth. Add, change, or remove tokens here.

2  Run generate-tokens

`npm run generate-tokens` reads the JSON and produces `flux.css` and `tokens.ts`.

3  Commit all three files

Push to GitLab. CI rebuilds. Figma Tokens Studio syncs from the JSON.

## Export Formats
flux.json

Figma Tokens Studio format. The canonical source.

{
"flux": {
"primary": {
"400": {
"value": "#056F82",
"type": "color",
"description": "Links, icons, interactive"
}
}
}
}                flux.css

CSS custom properties. Drop into any web project.

:root {
--flux-primary-400: #056F82;
--flux-yellow-400: #FFBC42;
/* ... */
}                tokens.ts

TypeScript export. Used by the Flux site components.

import { primaryColors } from './tokens';
// primaryColors.colors[0].hex => '#056F82'
## Figma Integration

- 1. Install [Tokens Studio](https://tokens.studio) plugin in Figma
- 2. Connect to GitLab: `kaptio1/platform-and-services/edge/kaptio-flux`
- 3. Set token file path: `src/tokens/flux.json`
- 4. Pull tokens — all colors, fonts, spacing appear in Figma
- 5. Edit tokens in Figma, push back to GitLab — CI regenerates everything
