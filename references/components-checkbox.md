# Flux — /components/checkbox

Source: https://flux.kaptio.com/components/checkbox

[Flux](/)       [Components](/components) / Inputs & Forms

# Checkbox
Toggle individual options on or off.

### Default
AccommodationActivitiesTransfers
### Disabled
Unchecked disabledChecked disabled       Source  CheckboxDemo.tsx
The exact code behind the live demo above. Fetch it raw at
[/components/source/checkbox.txt](/components/source/checkbox.txt).

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

const checkmarkSvg = (
<svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M2.5 6L5 8.5L9.5 3.5" stroke="white" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" />
</svg>
);

function Checkbox({
label,
checked,
onChange,
disabled = false,
}: {
label: string;
checked: boolean;
onChange: (checked: boolean) => void;
disabled?: boolean;
}) {
return (
<label
className={`flex items-center gap-2.5 select-none ${disabled ? "opacity-50 cursor-not-allowed" : "cursor-pointer"}`}
>
<button
type="button"
role="checkbox"
aria-checked={checked}
disabled={disabled}
onClick={() => onChange(!checked)}
className={`
flex items-center justify-center w-[18px] h-[18px] rounded shrink-0
transition-colors duration-150
${
checked
? "bg-[var(--flux-primary-400)] border border-[var(--flux-primary-400)]"
: "bg-[var(--flux-surface)] border border-[var(--flux-grey-200)]"
}
${disabled ? "pointer-events-none" : ""}
`}
>
{checked && checkmarkSvg}
</button>
<span className="text-sm text-[var(--flux-black)]">{label}</span>
</label>
);
}

export default function CheckboxDemo() {
const [values, setValues] = useState<Record<string, boolean>>({
accommodation: false,
activities: false,
transfers: false,
});

const toggle = (key: string) =>
setValues((prev) => ({ ...prev, [key]: !prev[key] }));

return (
<div>
<Section title="Default">
<div className="flex flex-col gap-3">
<Checkbox label="Accommodation" checked={values.accommodation} onChange={() => toggle("accommodation")} />
<Checkbox label="Activities" checked={values.activities} onChange={() => toggle("activities")} />
<Checkbox label="Transfers" checked={values.transfers} onChange={() => toggle("transfers")} />
</div>
</Section>

<Section title="Disabled">
<div className="flex flex-col gap-3">
<Checkbox label="Unchecked disabled" checked={false} onChange={() => {}} disabled />
<Checkbox label="Checked disabled" checked={true} onChange={() => {}} disabled />
</div>
</Section>
</div>
);
}                  [← Card](/components/card) [Code Block →](/components/code-block)
