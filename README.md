# Flux Cursor skill

Teaches Cursor agents to apply the [Flux design system](https://flux.kaptio.com) when building or reviewing Kaptio UI.

This repository is a **Cursor Agent Skill**. Clone it from GitLab and link it into each developer's `~/.cursor/skills/` directory so Cursor can discover it automatically.

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

### 1. Clone from GitLab

```bash
git clone git@gitlab.com:kaptio1/<group>/flux-plugin-kaptio.git
cd flux-plugin-kaptio
```

Replace the path with your team's GitLab project URL once the repo is hosted.

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
git submodule add git@gitlab.com:kaptio1/<group>/flux-plugin-kaptio.git .cursor/skills/flux
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

In GitLab CI, trigger the **update-references** job (manual or scheduled) to scrape and commit updated `references/` automatically.

## GitLab CI

| Job | When | Purpose |
|-----|------|---------|
| `validate-scrape` | Merge requests and default branch | Ensures committed references match flux.kaptio.com |
| `update-references` | Manual, web, or schedule | Re-scrapes and commits reference updates |

To enable scheduled refreshes, add a pipeline schedule in GitLab (e.g. weekly). The update job requires permission for `CI_JOB_TOKEN` to push to the default branch.

## Team rollout checklist

1. Push this repository to GitLab under a shared group (e.g. `kaptio1/platform-and-services/flux-plugin-kaptio`).
2. Share the clone URL with the team.
3. Each developer runs `scripts/install.ps1` or `scripts/install.sh` after cloning.
4. Optionally add a weekly GitLab schedule to run `update-references`.
5. When Flux releases change tokens or components, review `references/changelog.md` and update `references/quick-reference.md`.

## Limitations

- Component reference files are **text extracted** from the docs site. Interactive examples and visuals remain on https://flux.kaptio.com.
- For exhaustive token lists in code, prefer `flux.json` in the [kaptio-flux](https://gitlab.com/kaptio1/platform-and-services/edge/kaptio-flux) repo (`src/tokens/flux.json`), not only the scraped markdown.

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
├── .gitlab-ci.yml
└── README.md
```

## Related links

- Flux design system: https://flux.kaptio.com
- Token exports: https://flux.kaptio.com/assets
- Canonical token source: `kaptio1/platform-and-services/edge/kaptio-flux`
