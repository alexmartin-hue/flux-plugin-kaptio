# Flux — /foundations/color/

Source: https://flux.kaptio.com/foundations/color/

Foundations

# Colour
Kaptio Seagreen carries the system. Everything else earns its place by meaning: yellow converts, orange warns, green confirms, pink marks Edge. A colour with no job does not appear.

## Brand palette
Teal is the system. The rest are accents with specific, narrow jobs.

### Kaptio Seagreen — primary
The dominant colour. `primary-400` is the interactive teal, `primary-800`is the deep-theme ground, and `primary-600` is the darkest teal that still reads as brand rather than as ink.

- --flux-primary-900#021E24
- --flux-primary-800#032E36
- --flux-primary-700#034050
- --flux-primary-600#034955
- --flux-primary-500#056271
- --flux-primary-400#056F82
- --flux-primary-300#69A9B4
- --flux-primary-200#B4D4DA
- --flux-primary-100#E6F1F2
- --flux-primary-50#EFF5F5
### Bumble-Me Yellow — call to action
Reserved. See [the yellow rule](#yellow) below.

- --flux-yellow-900#3A2C10
- --flux-yellow-800#956000
- --flux-yellow-600#DC8E00
- --flux-yellow-400#FFBC42
- --flux-yellow-300#FFD78E
- --flux-yellow-200#FFEBC6
- --flux-yellow-100#FFF8EC
### Fandango Pink — the dot, and Edge

- --flux-pink-600#AF0072
- --flux-pink-400#DE37A4
- --flux-pink-300#EB87C8
- --flux-pink-200#F5C3E4
- --flux-pink-100#FCEBF6
### Puffin Beak Orange

- --flux-orange-900#3D1D19
- --flux-orange-800#9C1500
- --flux-orange-600#CF1B00
- --flux-orange-400#FF6F59
- --flux-orange-300#FFA99B
- --flux-orange-200#FFD4CD
- --flux-orange-100#FFF1EE
### Poison Green

- --flux-green-900#16301A
- --flux-green-800#0E5600
- --flux-green-600#197C04
- --flux-green-400#2BA711
- --flux-green-300#80CA70
- --flux-green-200#BFE5B8
- --flux-green-100#EAF6E7
### Blue and purple
Supporting hues for information states, product accents and data series. Neither is a brand colour, and neither should carry a page.

- --flux-blue-800#17458F
- --flux-blue-600#2F67CF
- --flux-blue-400#015BFF
- --flux-blue-300#8EB6FF
- --flux-blue-200#C6DAFF
- --flux-blue-100#ECF5FF
- --flux-purple-600#5A47D6
- --flux-purple-400#6149FF
- --flux-purple-300#ADA0FF
- --flux-purple-200#D5CFFF
- --flux-purple-100#F1EFFF
## Neutrals

### The 2.0 ramp
New in 2.0. An even, cool ramp with a faint teal cast, added because the dark theme needs consistent steps to build elevation from. `canvas` is the Kaptio page ground and carries the exact value Flux 1.x published as `--flux-background`.

- --flux-canvas#F9FAF8
- --flux-neutral-50#F4F7F7
- --flux-neutral-100#E8EDEE
- --flux-neutral-200#D3DADC
- --flux-neutral-300#B2BCBF
- --flux-neutral-400#8C989C
- --flux-neutral-500#6B777B
- --flux-neutral-600#4E585C
- --flux-neutral-700#363F42
- --flux-neutral-800#242B2E
- --flux-neutral-900#171D1F
- --flux-neutral-950#0E1315
### Flux 1.x neutrals
Retained verbatim and permanently published. Their spacing is irregular by history rather than by design, which is why they cannot carry the layer model. Prefer the ramp above in new work.

- --flux-black#212121
- --flux-grey-700#374151
- --flux-grey-500#646B78
- --flux-grey-300#6B6B6B
- --flux-grey-200#C3C3C3
- --flux-grey-100#EBEBEB
- --flux-grey-50#F5F5F5
- --flux-white#FFFFFF
## Status
Four hues, each tuned so that its text form clears 4.5:1 on its own subtle surface.

- --flux-success#0A7954
- --flux-error#C1121F
- --flux-warning#945F06
- --flux-info#056F82NoteUse the semantic pairings — `--flux-text-error` on`--flux-surface-error-subtle` — rather than composing your own from these primitives. The pairings are what the contrast audit verifies.
## Roles, not colours
These resolve differently in each theme. That is the point of them.

Switch the theme in the top bar and watch this table change without the page reloading.

- --flux-text-primaryBody and headings
- --flux-text-secondarySupporting copy
- --flux-text-subtleMetadata and labels
- --flux-text-brandBrand-coloured text
- --flux-layer-01First nesting level
- --flux-layer-02Second nesting level
- --flux-layer-03Third nesting level
- --flux-surface-brandPrimary button fill
- --flux-surface-ctaThe one CTA fill
- --flux-border-subtleDividers and hairlines
- --flux-border-strongControl outlines
- --flux-focus-ringFocus, in every theme
## Which colours may carry text
Most of the palette cannot. Treating a mid-tone as a text colour is the most common way Flux output goes wrong.

ColourAs textAs a fill behind textAs a graphicprimary-600, primary-400Yes, on light groundsYes, with text-on-colorYesprimary-300, primary-200Only on dark or deep groundsYes, with dark textYesyellow-400 (CTA)NoYes, with text-on-cta (black)Sparinglyyellow-800, orange-800, green-800Yes, on their own -100/-200 tintsNoYesyellow-900, blue-800Yes, on the documented -300/-200 badge tintsNoYespink-400, orange-400, green-400NoYes, with white textYesneutral-300 and lighterNoYes, with text-primaryYesNeverA 400-weight accent as body text on a light ground. `--flux-pink-400` on white is 3.9:1 — it looks like brand and reads like a defect. If text must be coloured, use a`text-*` role.
## The yellow rule
Bumble-Me Yellow is the loudest thing in the system, so it gets the strictest rule.

One yellow element per view, and only for a conversion action — the thing you would count if you were measuring whether the page worked. A second yellow element halves the value of the first.

Yellow never carries white text. The pairing is`--flux-surface-cta` with `--flux-text-on-cta`, which is black.

htmlCopy`
Talk to us

Save changes
Cancel`
## Do and don’t
Do

- Let teal carry the page, and let accents earn their appearance by meaning.
- Treat WCAG 2.2 AA as the floor: a text-* role on a documented ground, never a colour that looks dark enough.
- Use the semantic status pairings rather than composing your own.
- Keep product accents to graphic use — fills, marks, diagram keys.
- Check a colour decision against the theme switcher before shipping it.Don’t

- Do not use a 400-weight accent as text on a light ground.
- Do not put more than one yellow element on a view.
- Do not introduce a hue that is not in the palette.
- Do not use colour as the only signal for a state.[PreviousToken architecture](/foundations/tokens/)[NextTypography](/foundations/typography/)
