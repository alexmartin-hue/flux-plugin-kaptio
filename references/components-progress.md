# Flux — /components/progress

Source: https://flux.kaptio.com/components/progress

[Flux](/)       [Components](/components) / Feedback

# Progress
Determinate progress bars showing completion.

### Default
Progress60%
### Sizes
smmdlg
### Animated
Progress0%Advance to 25%       Source  ProgressDemo.tsx
The exact code behind the live demo above. Fetch it raw at
[/components/source/progress.txt](/components/source/progress.txt).

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

function ProgressBar({
value,
height = "h-2",
showLabel = false,
}: {
value: number;
height?: string;
showLabel?: boolean;
}) {
return (
<div className="w-full">
{showLabel && (
<div className="flex justify-between mb-1.5">
<span className="text-xs font-bold text-[var(--flux-black)]">Progress</span>
<span className="text-xs font-bold text-[var(--flux-black)]">{value}%</span>
</div>
)}
<div className={`w-full ${height} rounded-full bg-[var(--flux-grey-100)]`}>
<div
className={`${height} rounded-full bg-[var(--flux-primary-400)] transition-all duration-500`}
style={{ width: `${value}%` }}
/>
</div>
</div>
);
}

export default function ProgressDemo() {
const steps = [0, 25, 50, 75, 100];
const [stepIndex, setStepIndex] = useState(0);

const cycle = () => {
setStepIndex((prev) => (prev + 1) % steps.length);
};

return (
<div>
<Section title="Default">
<ProgressBar value={60} showLabel />
</Section>

<Section title="Sizes">
<div className="space-y-4">
<div>
<span className="text-xs text-[var(--flux-grey-300)] mb-1 block">sm</span>
<ProgressBar value={45} height="h-1" />
</div>
<div>
<span className="text-xs text-[var(--flux-grey-300)] mb-1 block">md</span>
<ProgressBar value={45} height="h-2" />
</div>
<div>
<span className="text-xs text-[var(--flux-grey-300)] mb-1 block">lg</span>
<ProgressBar value={45} height="h-3" />
</div>
</div>
</Section>

<Section title="Animated">
<div className="space-y-4">
<ProgressBar value={steps[stepIndex]} showLabel />
<button
onClick={cycle}
className="px-4 py-2 text-sm font-bold rounded bg-[var(--flux-primary-400)] text-white hover:opacity-90 transition-opacity"
>
Advance to {steps[(stepIndex + 1) % steps.length]}%
</button>
</div>
</Section>
</div>
);
}                  [← Note](/components/note) [Radio →](/components/radio)
