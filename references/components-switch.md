# Flux — /components/switch

Source: https://flux.kaptio.com/components/switch

[Flux](/)       [Components](/components) / Inputs & Forms

# Switch
Binary toggle for on/off states.

### Default
Off
### Sizes
SmallMedium (default)Large
### Disabled
Disabled       Source  SwitchDemo.tsx
The exact code behind the live demo above. Fetch it raw at
[/components/source/switch.txt](/components/source/switch.txt).

import { useState } from "react";

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

function Switch({
checked,
onChange,
disabled = false,
size = "md",
}: {
checked: boolean;
onChange: (checked: boolean) => void;
disabled?: boolean;
size?: "sm" | "md" | "lg";
}) {
const dims = {
sm: { track: "w-9 h-5", thumb: "w-4 h-4", translate: "translate-x-4" },
md: { track: "w-11 h-6", thumb: "w-5 h-5", translate: "translate-x-5" },
lg: { track: "w-[52px] h-7", thumb: "w-6 h-6", translate: "translate-x-6" },
}[size];

return (
<button
type="button"
role="switch"
aria-checked={checked}
disabled={disabled}
onClick={() => onChange(!checked)}
className={`
relative inline-flex items-center rounded-full shrink-0
transition-colors duration-200 ease-in-out
${dims.track}
${checked ? "bg-[var(--flux-primary-400)]" : "bg-[var(--flux-grey-200)]"}
${disabled ? "opacity-50 cursor-not-allowed" : "cursor-pointer"}
`}
>
<span
className={`
inline-block rounded-full bg-white shadow-md
transition-transform duration-200 ease-in-out
${dims.thumb}
${checked ? dims.translate : "translate-x-0.5"}
`}
/>
</button>
);
}

export default function SwitchDemo() {
const [defaultOn, setDefaultOn] = useState(false);
const [smOn, setSmOn] = useState(false);
const [lgOn, setLgOn] = useState(true);

return (
<div>
<Section title="Default">
<div className="flex items-center gap-3">
<Switch checked={defaultOn} onChange={setDefaultOn} />
<span className="text-sm text-[var(--flux-black)]">{defaultOn ? "On" : "Off"}</span>
</div>
</Section>

<Section title="Sizes">
<div className="flex flex-col gap-4">
<div className="flex items-center gap-3">
<Switch checked={smOn} onChange={setSmOn} size="sm" />
<span className="text-xs text-[var(--flux-black)]">Small</span>
</div>
<div className="flex items-center gap-3">
<Switch checked={defaultOn} onChange={setDefaultOn} />
<span className="text-xs text-[var(--flux-black)]">Medium (default)</span>
</div>
<div className="flex items-center gap-3">
<Switch checked={lgOn} onChange={setLgOn} size="lg" />
<span className="text-xs text-[var(--flux-black)]">Large</span>
</div>
</div>
</Section>

<Section title="Disabled">
<div className="flex items-center gap-3">
<Switch checked={false} onChange={() => {}} disabled />
<span className="text-sm text-[var(--flux-black)]">Disabled</span>
</div>
</Section>
</div>
);
}                  [← Spinner](/components/spinner) [Table →](/components/table)
