# Flux — /components/button

Source: https://flux.kaptio.com/components/button

[Flux](/)       [Components](/components) / Inputs & Forms

# Button
Primary actions, secondary actions, and destructive operations.

### Variants
PrimarySecondaryOutlineGhostDanger
### Sizes
SmallMediumLarge
### States
DisabledLoading       Source  ButtonDemo.tsx
The exact code behind the live demo above. Fetch it raw at
[/components/source/button.txt](/components/source/button.txt).

import React from "react";

function Section({ title, children }: { title: string; children: React.ReactNode }) {
return (
<div className="mb-8">
<h3 className="text-sm font-bold text-[var(--flux-heading)] mb-3">{title}</h3>
<div className="p-6 rounded border border-[var(--flux-grey-100)] bg-[var(--flux-surface)]">
{children}
</div>
</div>
);
}

function Spinner() {
return (
<svg
className="animate-spin h-4 w-4"
viewBox="0 0 24 24"
fill="none"
xmlns="http://www.w3.org/2000/svg"
>
<circle
className="opacity-25"
cx="12"
cy="12"
r="10"
stroke="currentColor"
strokeWidth="4"
/>
<path
className="opacity-75"
fill="currentColor"
d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z"
/>
</svg>
);
}

const base =
"font-bold transition-all duration-150 focus:outline-none focus:ring-2 focus:ring-[var(--flux-primary-300)]";

const r = "rounded-[4px]";

export default function ButtonDemo() {
return (
<div>
<Section title="Variants">
<div className="flex flex-wrap gap-3">
<button
className={`${base} ${r} bg-[var(--flux-primary-600)] hover:bg-[var(--flux-primary-500)] active:bg-[var(--flux-primary-700)] text-white text-sm px-4 py-2`}
>
Primary
</button>
<button
className={`${base} ${r} bg-[var(--flux-grey-100)] hover:bg-[var(--flux-grey-200)] active:bg-[var(--flux-grey-100)] text-[var(--flux-black)] text-sm px-4 py-2`}
>
Secondary
</button>
<button
className={`${base} ${r} border border-[var(--flux-primary-600)] text-[var(--flux-primary-600)] bg-transparent hover:bg-[var(--flux-primary-50)] active:bg-[var(--flux-primary-100)] text-sm px-4 py-2`}
>
Outline
</button>
<button
className={`${base} ${r} bg-transparent text-[var(--flux-primary-600)] hover:bg-[var(--flux-primary-50)] active:bg-[var(--flux-primary-100)] text-sm px-4 py-2`}
>
Ghost
</button>
<button
className={`${base} ${r} bg-[var(--flux-error)] hover:opacity-90 active:opacity-100 text-white text-sm px-4 py-2`}
>
Danger
</button>
</div>
</Section>

<Section title="Sizes">
<div className="flex flex-wrap items-center gap-3">
<button
className={`${base} ${r} bg-[var(--flux-primary-600)] hover:bg-[var(--flux-primary-500)] active:bg-[var(--flux-primary-700)] text-white text-xs px-3 py-1.5`}
>
Small
</button>
<button
className={`${base} ${r} bg-[var(--flux-primary-600)] hover:bg-[var(--flux-primary-500)] active:bg-[var(--flux-primary-700)] text-white text-sm px-4 py-2`}
>
Medium
</button>
<button
className={`${base} ${r} bg-[var(--flux-primary-600)] hover:bg-[var(--flux-primary-500)] active:bg-[var(--flux-primary-700)] text-white text-base px-6 py-2.5`}
>
Large
</button>
</div>
</Section>

<Section title="States">
<div className="flex flex-wrap items-center gap-3">
<button
disabled
className={`${base} ${r} bg-[var(--flux-primary-600)] text-white text-sm px-4 py-2 opacity-50 cursor-not-allowed`}
>
Disabled
</button>
<button
className={`${base} ${r} bg-[var(--flux-primary-600)] hover:bg-[var(--flux-primary-500)] text-white text-sm px-4 py-2 inline-flex items-center gap-2`}
>
<Spinner />
Loading
</button>
</div>
</Section>
</div>
);
}                  [← Badge](/components/badge) [Card →](/components/card)
