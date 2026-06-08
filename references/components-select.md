# Flux — /components/select

Source: https://flux.kaptio.com/components/select

[Flux](/)       [Components](/components) / Inputs & Forms

# Select
Dropdown menus for choosing from a list of options.

### Default
Service typeSelect an option...
### With preselected value
Service typeAccommodation
### Disabled
Service typeSelect an option...
### Error state
Service typeSelect an option...Please select a service type.

Source  SelectDemo.tsx
The exact code behind the live demo above. Fetch it raw at
[/components/source/select.txt](/components/source/select.txt).

import React, { useState, useRef, useEffect } from "react";

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

const labelClass = "block text-sm font-medium text-[var(--flux-black)] mb-1";

interface CustomSelectProps {
label: string;
options: string[];
placeholder?: string;
disabled?: boolean;
error?: string;
defaultValue?: string;
}

function CustomSelect({
label,
options,
placeholder = "Select an option...",
disabled = false,
error,
defaultValue,
}: CustomSelectProps) {
const [open, setOpen] = useState(false);
const [selected, setSelected] = useState(defaultValue || "");
const ref = useRef<HTMLDivElement>(null);

useEffect(() => {
function handleClick(e: MouseEvent) {
if (ref.current && !ref.current.contains(e.target as Node)) setOpen(false);
}
document.addEventListener("mousedown", handleClick);
return () => document.removeEventListener("mousedown", handleClick);
}, []);

const borderColor = error
? "border-[var(--flux-error)]"
: open
? "border-[var(--flux-primary-400)]"
: "border-[var(--flux-grey-200)]";

const ringClass = open
? error
? "ring-1 ring-[var(--flux-error)]"
: "ring-1 ring-[var(--flux-primary-300)]"
: "";

return (
<div className="max-w-sm" ref={ref}>
<label className={labelClass}>{label}</label>
<div className="relative">
<button
type="button"
disabled={disabled}
onClick={() => !disabled && setOpen(!open)}
className={`w-full flex items-center justify-between px-3 py-2 rounded border ${borderColor} ${ringClass} bg-[var(--flux-surface)] text-sm text-left outline-none transition-all ${
disabled ? "opacity-50 cursor-not-allowed bg-[var(--flux-grey-50)]" : "cursor-pointer hover:border-[var(--flux-grey-300)]"
}`}
>
<span className={selected ? "text-[var(--flux-black)]" : "text-[var(--flux-grey-300)]"}>
{selected || placeholder}
</span>
<svg
className={`w-4 h-4 text-[var(--flux-grey-500)] transition-transform ${open ? "rotate-180" : ""}`}
fill="none"
viewBox="0 0 24 24"
stroke="currentColor"
>
<path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
</svg>
</button>

{open && (
<ul className="absolute z-50 mt-1 w-full rounded border border-[var(--flux-grey-200)] bg-[var(--flux-surface)] shadow-[var(--flux-shadow-lg)] py-1 max-h-60 overflow-auto">
{options.map((opt) => (
<li key={opt}>
<button
type="button"
onClick={() => {
setSelected(opt);
setOpen(false);
}}
className={`w-full text-left px-3 py-2 text-sm transition-colors cursor-pointer ${
selected === opt
? "bg-[var(--flux-primary-50)] text-[var(--flux-primary-800)] font-medium"
: "text-[var(--flux-black)] hover:bg-[var(--flux-grey-50)]"
}`}
>
<span className="flex items-center justify-between">
{opt}
{selected === opt && (
<svg className="w-4 h-4 text-[var(--flux-primary-500)]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
<path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
</svg>
)}
</span>
</button>
</li>
))}
</ul>
)}
</div>
{error && <p className="mt-1 text-xs text-[var(--flux-error)]">{error}</p>}
</div>
);
}

const serviceTypes = ["Departure", "Accommodation", "Activity", "Transfer"];

export default function SelectDemo() {
return (
<div>
<Section title="Default">
<CustomSelect label="Service type" options={serviceTypes} />
</Section>

<Section title="With preselected value">
<CustomSelect label="Service type" options={serviceTypes} defaultValue="Accommodation" />
</Section>

<Section title="Disabled">
<CustomSelect label="Service type" options={serviceTypes} disabled />
</Section>

<Section title="Error state">
<CustomSelect
label="Service type"
options={serviceTypes}
error="Please select a service type."
/>
</Section>
</div>
);
}                  [← Radio](/components/radio) [Skeleton →](/components/skeleton)
