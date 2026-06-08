# Flux — /components/radio

Source: https://flux.kaptio.com/components/radio

[Flux](/)       [Components](/components) / Inputs & Forms

# Radio
Select one option from a mutually exclusive group.

### Vertical
EconomyBusinessFirst Class
### Horizontal
EconomyBusinessFirst Class
### Disabled
Disabled option       Source  RadioDemo.tsx
The exact code behind the live demo above. Fetch it raw at
[/components/source/radio.txt](/components/source/radio.txt).

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

function RadioOption({
label,
selected,
onSelect,
disabled = false,
}: {
label: string;
selected: boolean;
onSelect: () => void;
disabled?: boolean;
}) {
return (
<label
className={`flex items-center gap-2.5 select-none ${disabled ? "opacity-50 cursor-not-allowed" : "cursor-pointer"}`}
>
<button
type="button"
role="radio"
aria-checked={selected}
disabled={disabled}
onClick={onSelect}
className={`
flex items-center justify-center w-[18px] h-[18px] rounded-full shrink-0
transition-colors duration-150
${
selected
? "border-2 border-[var(--flux-primary-400)]"
: "border border-[var(--flux-grey-200)] bg-[var(--flux-surface)]"
}
${disabled ? "pointer-events-none" : ""}
`}
>
{selected && <span className="block w-2 h-2 rounded-full bg-[var(--flux-primary-400)]" />}
</button>
<span className="text-sm text-[var(--flux-black)]">{label}</span>
</label>
);
}

const options = ["Economy", "Business", "First Class"] as const;

export default function RadioDemo() {
const [vertical, setVertical] = useState<string>("Economy");
const [horizontal, setHorizontal] = useState<string>("Economy");

return (
<div>
<Section title="Vertical">
<div className="flex flex-col gap-3">
{options.map((opt) => (
<RadioOption key={opt} label={opt} selected={vertical === opt} onSelect={() => setVertical(opt)} />
))}
</div>
</Section>

<Section title="Horizontal">
<div className="flex items-center gap-6">
{options.map((opt) => (
<RadioOption key={opt} label={opt} selected={horizontal === opt} onSelect={() => setHorizontal(opt)} />
))}
</div>
</Section>

<Section title="Disabled">
<RadioOption label="Disabled option" selected={false} onSelect={() => {}} disabled />
</Section>
</div>
);
}                  [← Progress](/components/progress) [Select →](/components/select)
