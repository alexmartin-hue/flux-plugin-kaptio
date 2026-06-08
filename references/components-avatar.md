# Flux — /components/avatar

Source: https://flux.kaptio.com/components/avatar

[Flux](/)       [Components](/components) / Data Display

# Avatar
User or entity representation with image or initials.

### Sizes
SMMDLG
### With image

### With Status
JDAK
### Group
ABCDEFGH       Source  AvatarDemo.tsx
The exact code behind the live demo above. Fetch it raw at
[/components/source/avatar.txt](/components/source/avatar.txt).

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

function Avatar({
initials,
image,
size = "md",
showStatus = false,
}: {
initials: string;
image?: string;
size?: "sm" | "md" | "lg";
showStatus?: boolean;
}) {
const dims = { sm: "w-8 h-8", md: "w-10 h-10", lg: "w-14 h-14" };
const textSize = { sm: "text-xs", md: "text-sm", lg: "text-lg" };

return (
<div className="relative inline-flex">
{image ? (
<img
src={image}
alt={initials}
className={`${dims[size]} rounded-full object-cover`}
/>
) : (
<div
className={`${dims[size]} ${textSize[size]} rounded-full bg-[var(--flux-primary-100)] text-[var(--flux-primary-400)] font-bold flex items-center justify-center`}
>
{initials}
</div>
)}
{showStatus && (
<span className="absolute bottom-0 right-0 block w-2.5 h-2.5 rounded-full bg-[var(--flux-success)] ring-2 ring-white" />
)}
</div>
);
}

export default function AvatarDemo() {
return (
<div>
<Section title="Sizes">
<div className="flex items-center gap-4">
<Avatar initials="SM" size="sm" />
<Avatar initials="MD" size="md" />
<Avatar initials="LG" size="lg" />
</div>
</Section>

<Section title="With image">
<div className="flex items-center gap-4">
<Avatar initials="KS" image="/images/avatar-example.png" size="sm" />
<Avatar initials="KS" image="/images/avatar-example.png" size="md" />
<Avatar initials="KS" image="/images/avatar-example.png" size="lg" />
<Avatar initials="KS" image="/images/avatar-example.png" size="lg" showStatus />
</div>
</Section>

<Section title="With Status">
<div className="flex items-center gap-4">
<Avatar initials="JD" size="md" showStatus />
<Avatar initials="AK" size="md" showStatus />
</div>
</Section>

<Section title="Group">
<div className="flex items-center">
{["AB", "CD", "EF", "GH"].map((initials, i) => (
<div key={initials} className={i > 0 ? "-ml-2" : ""}>
<div className="w-10 h-10 rounded-full bg-[var(--flux-primary-100)] text-[var(--flux-primary-400)] font-bold text-sm flex items-center justify-center ring-2 ring-[var(--flux-surface)]">
{initials}
</div>
</div>
))}
</div>
</Section>
</div>
);
}                  [← Accordion](/components/accordion) [Badge →](/components/badge)
