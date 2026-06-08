# Flux — /components/tooltip

Source: https://flux.kaptio.com/components/tooltip

[Flux](/)       [Components](/components) / Layout & Overlay

# Tooltip
Contextual hints that appear on hover.

### Positions
TopRightBottomLeft       Source  TooltipDemo.tsx
The exact code behind the live demo above. Fetch it raw at
[/components/source/tooltip.txt](/components/source/tooltip.txt).

import React, { useState } from "react";

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

type Position = "top" | "right" | "bottom" | "left";

const positionClasses: Record<Position, string> = {
top: "bottom-full left-1/2 -translate-x-1/2 mb-2",
right: "left-full top-1/2 -translate-y-1/2 ml-2",
bottom: "top-full left-1/2 -translate-x-1/2 mt-2",
left: "right-full top-1/2 -translate-y-1/2 mr-2",
};

const arrowClasses: Record<Position, string> = {
top: "top-full left-1/2 -translate-x-1/2 border-t-[var(--flux-primary-800)] border-x-transparent border-b-transparent",
right: "right-full top-1/2 -translate-y-1/2 border-r-[var(--flux-primary-800)] border-y-transparent border-l-transparent",
bottom: "bottom-full left-1/2 -translate-x-1/2 border-b-[var(--flux-primary-800)] border-x-transparent border-t-transparent",
left: "left-full top-1/2 -translate-y-1/2 border-l-[var(--flux-primary-800)] border-y-transparent border-r-transparent",
};

function TooltipButton({
label,
position,
tooltipText,
}: {
label: string;
position: Position;
tooltipText: string;
}) {
const [visible, setVisible] = useState(false);

return (
<div className="relative inline-flex">
<button
onMouseEnter={() => setVisible(true)}
onMouseLeave={() => setVisible(false)}
className="px-4 py-2 text-sm font-bold rounded border border-[var(--flux-grey-200)] text-[var(--flux-black)] hover:bg-[var(--flux-grey-100)] transition-colors"
>
{label}
</button>
{visible && (
<div
className={`absolute ${positionClasses[position]} bg-[var(--flux-primary-800)] text-white text-xs px-2.5 py-1.5 rounded shadow-lg whitespace-nowrap z-10`}
>
{tooltipText}
<span
className={`absolute ${arrowClasses[position]} border-4 w-0 h-0`}
/>
</div>
)}
</div>
);
}

export default function TooltipDemo() {
return (
<div>
<Section title="Positions">
<div className="flex items-center justify-center gap-6 py-8">
<TooltipButton label="Top" position="top" tooltipText="Tooltip on top" />
<TooltipButton label="Right" position="right" tooltipText="Tooltip on right" />
<TooltipButton label="Bottom" position="bottom" tooltipText="Tooltip on bottom" />
<TooltipButton label="Left" position="left" tooltipText="Tooltip on left" />
</div>
</Section>
</div>
);
}                  [← Textarea](/components/textarea) [Outcome Header →](/components/outcome-header)
