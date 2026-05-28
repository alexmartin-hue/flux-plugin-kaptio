# Flux Cursor skill

Teaches Cursor agents to apply the [Flux design system](https://flux.kaptio.com) when building or reviewing Kaptio UI.

This repository is a **Cursor Agent Skill** hosted on GitHub. Clone it and link it into each developer's `~/.cursor/skills/` directory so Cursor can discover it automatically.

## What is included

| Path | Purpose |
|------|---------|
| `SKILL.md` | Main skill — workflow, MUI mapping, compliance checklist |
| `references/quick-reference.md` | Curated tokens, colors, typography, products |
| `references/*.md` | Page snapshots scraped from https://flux.kaptio.com |
| `scripts/scrape_flux.py` | Regenerate references after Flux site updates |
| `scripts/install.ps1` / `scripts/install.sh` | Symlink this repo into `~/.cursor/skills/flux` |

Coverage includes foundations (colors, typography, spacing, shadows, tokens, iconography), all documented components, products (Core, Quest, Voyage, Circle, Edge, Agents), patterns (including Salesforce ↔ Edge transitions), brand, assets, changelog, and don'ts.

## Quick install

### 1. Clone from GitHub

```bash
git clone https://github.com/alexmartin-hue/flux-plugin-kaptio.git
cd flux-plugin-kaptio
```

### 2. Link into Cursor skills

**Windows (PowerShell):**

```powershell
.\scripts\install.ps1
```

**macOS / Linux:**

```bash
chmod +x scripts/install.sh
./scripts/install.sh
```

This creates a junction/symlink at `~/.cursor/skills/flux` pointing at this repository. Cursor loads skills from that directory automatically.

### Project-level install (optional)

For a team working in one repository, add this repo as a submodule so the skill travels with the project:

```bash
git submodule add https://github.com/alexmartin-hue/flux-plugin-kaptio.git .cursor/skills/flux
```

Cursor also discovers skills under `.cursor/skills/` in the workspace.

### Manual install

If you prefer not to use the install scripts:

**Windows:**

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.cursor\skills"
cmd /c mklink /J "$env:USERPROFILE\.cursor\skills\flux" "C:\path\to\flux-plugin-kaptio"
```

**macOS / Linux:**

```bash
mkdir -p ~/.cursor/skills
ln -s /path/to/flux-plugin-kaptio ~/.cursor/skills/flux
```

## How to use in Cursor

In chat, say things like:

- "Use the flux skill to style this MUI form"
- "Does this UI match Flux?"
- "Build a card using Flux tokens"

The agent should read `SKILL.md` → `references/quick-reference.md` → specific `references/*.md` files as needed.

## Refresh after Flux updates

Locally:

```bash
python scripts/scrape_flux.py
```

Then skim `references/changelog.md` and update `references/quick-reference.md` if tokens or components changed materially.

In GitHub Actions, run the **Flux references** workflow manually (Actions → Flux references → Run workflow) to scrape and commit updated `references/` automatically. It also runs on a weekly schedule (Mondays 06:00 UTC).

## GitHub Actions

| Job | When | Purpose |
|-----|------|---------|
| `validate-scrape` | Pull requests and pushes to `main` | Ensures committed references match flux.kaptio.com |
| `update-references` | Manual dispatch or weekly schedule | Re-scrapes and commits reference updates |

## Team rollout checklist

1. Share the GitHub repo URL with the team: https://github.com/alexmartin-hue/flux-plugin-kaptio
2. Each developer clones the repo and runs `scripts/install.ps1` or `scripts/install.sh`.
3. Optionally enable GitHub Actions on the repo (on by default for public repos).
4. When Flux releases change tokens or components, review `references/changelog.md` and update `references/quick-reference.md`.

## Limitations

- Component reference files are **text extracted** from the docs site. Interactive examples and visuals remain on https://flux.kaptio.com.
- For exhaustive token lists in code, prefer `flux.json` in the kaptio-flux repo on GitLab (`kaptio1/platform-and-services/edge/kaptio-flux`, path `src/tokens/flux.json`), not only the scraped markdown.

## Repository layout

```
flux-plugin-kaptio/
├── SKILL.md                 # Cursor skill entry point
├── references/
│   ├── quick-reference.md   # Hand-curated summary (not overwritten by scraper)
│   ├── index.md             # Generated page index
│   └── *.md                 # Scraped Flux pages
├── scripts/
│   ├── scrape_flux.py
│   ├── install.ps1
│   └── install.sh
├── .github/workflows/
│   └── references.yml
└── README.md
```

## Related links

- Flux design system: https://flux.kaptio.com
- Token exports: https://flux.kaptio.com/assets
- Canonical token source (GitLab): `kaptio1/platform-and-services/edge/kaptio-flux`
