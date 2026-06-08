# Flux — /components/spinner

Source: https://flux.kaptio.com/components/spinner

[Flux](/)       [Components](/components) / Feedback

# Spinner
Loading indicators for async operations.

### Sizes
sm · 16pxmd · 24pxlg · 40px
### Colors
PrimaryGreySuccess       Source  SpinnerDemo.tsx
The exact code behind the live demo above. Fetch it raw at
[/components/source/spinner.txt](/components/source/spinner.txt).

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

function Spinner({
size,
trackColor = "var(--flux-grey-200)",
arcColor = "var(--flux-primary-400)",
}: {
size: number;
trackColor?: string;
arcColor?: string;
}) {
const strokeWidth = size < 24 ? 3 : 4;
const radius = (size - strokeWidth) / 2;
const circumference = 2 * Math.PI * radius;

return (
<svg
className="animate-spin"
width={size}
height={size}
viewBox={`0 0 ${size} ${size}`}
fill="none"
>
<circle
cx={size / 2}
cy={size / 2}
r={radius}
stroke={trackColor}
strokeWidth={strokeWidth}
/>
<circle
cx={size / 2}
cy={size / 2}
r={radius}
stroke={arcColor}
strokeWidth={strokeWidth}
strokeDasharray={circumference}
strokeDashoffset={circumference * 0.75}
strokeLinecap="round"
/>
</svg>
);
}

export default function SpinnerDemo() {
return (
<div>
<Section title="Sizes">
<div className="flex items-center gap-8">
<div className="flex flex-col items-center gap-2">
<Spinner size={16} />
<span className="text-xs text-[var(--flux-grey-300)]">sm · 16px</span>
</div>
<div className="flex flex-col items-center gap-2">
<Spinner size={24} />
<span className="text-xs text-[var(--flux-grey-300)]">md · 24px</span>
</div>
<div className="flex flex-col items-center gap-2">
<Spinner size={40} />
<span className="text-xs text-[var(--flux-grey-300)]">lg · 40px</span>
</div>
</div>
</Section>

<Section title="Colors">
<div className="flex items-center gap-8">
<div className="flex flex-col items-center gap-2">
<Spinner size={24} arcColor="var(--flux-primary-400)" />
<span className="text-xs text-[var(--flux-grey-300)]">Primary</span>
</div>
<div className="flex flex-col items-center gap-2">
<Spinner size={24} arcColor="var(--flux-grey-300)" />
<span className="text-xs text-[var(--flux-grey-300)]">Grey</span>
</div>
<div className="flex flex-col items-center gap-2">
<Spinner size={24} arcColor="var(--flux-success)" />
<span className="text-xs text-[var(--flux-grey-300)]">Success</span>
</div>
</div>
</Section>
</div>
);
}                  [← Skeleton](/components/skeleton) [Switch →](/components/switch)
