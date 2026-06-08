# Flux — /components/input

Source: https://flux.kaptio.com/components/input

[Flux](/)       [Components](/components) / Inputs & Forms

# Input
Text fields for single-line data entry, including multi-select.

### Default
Full name
### With placeholder
Email address
### Error state
UsernameUsername must be at least 3 characters.

### Disabled
Company
## Multi Select

### Default
Select multiple items from a dropdown. Checkboxes toggle individual items. Action labels appear on hover to show context-aware actions.

Analytics, Sales2 items selected — Hover over items to see action labels. Different actions appear based on selection state.

### Keyboard Navigation
Full keyboard support for accessibility and power users.

Select features...↑ ↓Navigate between rows← →Switch checkbox / action focusEnter / SpaceToggle or execute actionEscClose dropdown
### Controlled State
Manage selections programmatically with external controls.

AnalyticsClear AllCore FeaturesCreative TeamsSelected: Analytics

Source  2 files
The exact code behind the live demo above. Fetch it raw at
[/components/source/input.txt](/components/source/input.txt).

InputDemo.tsx

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

const labelClass = "block text-sm font-medium text-[var(--flux-black)] mb-1";
const inputBase =
"w-full px-3 py-2 rounded border border-[var(--flux-grey-200)] bg-[var(--flux-surface)] text-sm text-[var(--flux-black)] focus:border-[var(--flux-primary-400)] focus:ring-1 focus:ring-[var(--flux-primary-300)] outline-none transition-colors";

export default function InputDemo() {
return (
<div>
<Section title="Default">
<div className="max-w-sm">
<label className={labelClass}>Full name</label>
<input type="text" className={inputBase} defaultValue="Jane Doe" />
</div>
</Section>

<Section title="With placeholder">
<div className="max-w-sm">
<label className={labelClass}>Email address</label>
<input
type="email"
className={inputBase}
placeholder="you@example.com"
/>
</div>
</Section>

<Section title="Error state">
<div className="max-w-sm">
<label className={labelClass}>Username</label>
<input
type="text"
className={`${inputBase} !border-[var(--flux-error)] focus:!ring-[var(--flux-error)]`}
defaultValue="ab"
/>
<p className="mt-1 text-xs text-[var(--flux-error)]">
Username must be at least 3 characters.
</p>
</div>
</Section>

<Section title="Disabled">
<div className="max-w-sm">
<label className={labelClass}>Company</label>
<input
type="text"
disabled
className={`${inputBase} opacity-50 cursor-not-allowed bg-[var(--flux-grey-50)]`}
defaultValue="Kaptio"
/>
</div>
</Section>
</div>
);
}                MultiSelectDemo.tsx

import { useState, useRef, useEffect, useCallback } from 'react';

function Section({ title, children }: { title: string; children: React.ReactNode }) {
return (
<div className="mb-10">
<h3 className="text-sm font-bold text-[var(--flux-heading)] mb-3">{title}</h3>
{children}
</div>
);
}

interface MultiSelectOption {
id: string;
label: string;
}

interface MultiSelectProps {
options: MultiSelectOption[];
selected: string[];
onChange: (selected: string[]) => void;
placeholder?: string;
}

function CheckIcon({ className }: { className?: string }) {
return (
<svg width="14" height="14" viewBox="0 0 14 14" fill="none" className={className}>
<path d="M11.5 4L5.5 10L2.5 7" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" />
</svg>
);
}

function ChevronDown({ className }: { className?: string }) {
return (
<svg width="14" height="14" viewBox="0 0 14 14" fill="none" className={className}>
<path d="M3.5 5.5L7 9L10.5 5.5" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" />
</svg>
);
}

function MultiSelect({ options, selected, onChange, placeholder = 'Select items...' }: MultiSelectProps) {
const [open, setOpen] = useState(false);
const [focusIdx, setFocusIdx] = useState(0);
const [focusCol, setFocusCol] = useState<'checkbox' | 'button'>('checkbox');
const containerRef = useRef<HTMLDivElement>(null);
const listRef = useRef<HTMLDivElement>(null);

const isSelected = (id: string) => selected.includes(id);

const toggle = useCallback((id: string) => {
onChange(
isSelected(id)
? selected.filter(s => s !== id)
: [...selected, id]
);
}, [selected, onChange]);

const selectOnly = useCallback((id: string) => {
onChange([id]);
}, [onChange]);

const getButtonAction = useCallback((id: string): { label: string; action: () => void } => {
if (selected.length === 0) {
return { label: 'Select Only', action: () => selectOnly(id) };
}
if (selected.length === 1 && isSelected(id)) {
return { label: 'Select All', action: () => onChange(options.map(o => o.id)) };
}
if (isSelected(id)) {
return { label: 'Select Only', action: () => selectOnly(id) };
}
return { label: 'Select Only', action: () => selectOnly(id) };
}, [selected, options, onChange, selectOnly]);

useEffect(() => {
if (!open) return;
function onKeyDown(e: KeyboardEvent) {
switch (e.key) {
case 'ArrowDown':
e.preventDefault();
setFocusIdx(i => Math.min(i + 1, options.length - 1));
break;
case 'ArrowUp':
e.preventDefault();
setFocusIdx(i => Math.max(i - 1, 0));
break;
case 'ArrowLeft':
e.preventDefault();
setFocusCol('checkbox');
break;
case 'ArrowRight':
e.preventDefault();
setFocusCol('button');
break;
case 'Enter':
case ' ':
e.preventDefault();
if (focusCol === 'checkbox') {
toggle(options[focusIdx].id);
} else {
getButtonAction(options[focusIdx].id).action();
}
break;
case 'Escape':
setOpen(false);
break;
}
}
document.addEventListener('keydown', onKeyDown);
return () => document.removeEventListener('keydown', onKeyDown);
}, [open, focusIdx, focusCol, options, toggle, getButtonAction]);

useEffect(() => {
if (!open) return;
function onClick(e: MouseEvent) {
if (containerRef.current && !containerRef.current.contains(e.target as Node)) {
setOpen(false);
}
}
document.addEventListener('mousedown', onClick);
return () => document.removeEventListener('mousedown', onClick);
}, [open]);

useEffect(() => {
if (open && listRef.current) {
const focused = listRef.current.querySelector(`[data-idx="${focusIdx}"]`);
focused?.scrollIntoView({ block: 'nearest' });
}
}, [focusIdx, open]);

const selectedLabels = options.filter(o => selected.includes(o.id)).map(o => o.label);

return (
<div ref={containerRef} className="relative w-72">
<button
type="button"
onClick={() => { setOpen(v => !v); setFocusIdx(0); setFocusCol('checkbox'); }}
className="w-full flex items-center justify-between px-3 py-2 rounded border border-[var(--flux-grey-200)] bg-[var(--flux-surface)] text-sm text-[var(--flux-heading)] hover:border-[var(--flux-grey-300)] transition-colors"
>
<span className={selectedLabels.length === 0 ? 'text-[var(--flux-grey-300)]' : ''}>
{selectedLabels.length === 0
? placeholder
: selectedLabels.length <= 2
? selectedLabels.join(', ')
: `${selectedLabels.length} items selected`
}
</span>
<ChevronDown className={`text-[var(--flux-grey-300)] transition-transform duration-200 ${open ? 'rotate-180' : ''}`} />
</button>

{open && (
<div
ref={listRef}
className="absolute top-full left-0 right-0 mt-1 z-50 rounded border border-[var(--flux-grey-200)] bg-[var(--flux-surface)] shadow-lg overflow-hidden max-h-64 overflow-y-auto"
>
{options.map((option, i) => {
const checked = isSelected(option.id);
const focused = i === focusIdx;
const action = getButtonAction(option.id);

return (
<div
key={option.id}
data-idx={i}
className={`flex items-center gap-0 transition-colors ${focused ? 'bg-[var(--flux-primary-50)]' : 'hover:bg-[var(--flux-grey-50)]'}`}
onMouseEnter={() => setFocusIdx(i)}
>
<button
type="button"
onClick={() => { toggle(option.id); setFocusCol('checkbox'); }}
className={`flex items-center gap-2.5 flex-1 px-3 py-2 text-left transition-colors ${
focused && focusCol === 'checkbox'
? 'outline-none'
: ''
}`}
>
<span className={`
w-4 h-4 rounded flex items-center justify-center flex-shrink-0 border transition-colors
${checked
? 'bg-[var(--flux-primary-600)] border-[var(--flux-primary-600)] text-white'
: 'border-[var(--flux-grey-200)] bg-[var(--flux-surface)]'
}
${focused && focusCol === 'checkbox' ? 'ring-2 ring-[var(--flux-primary-300)] ring-offset-1' : ''}
`}>
{checked && <CheckIcon />}
</span>
<span className="text-sm text-[var(--flux-heading)]">{option.label}</span>
</button>

<button
type="button"
onClick={() => { action.action(); setFocusCol('button'); }}
className={`
px-3 py-2 text-[11px] font-bold text-[var(--flux-primary-400)] whitespace-nowrap
opacity-0 transition-opacity
${focused ? 'opacity-100' : 'group-hover:opacity-100'}
${focused && focusCol === 'button' ? 'opacity-100 underline' : ''}
`}
>
{action.label}
</button>
</div>
);
})}
</div>
)}
</div>
);
}

const actionOptions: MultiSelectOption[] = [
{ id: 'analytics', label: 'Analytics' },
{ id: 'marketing', label: 'Marketing' },
{ id: 'sales', label: 'Sales' },
{ id: 'support', label: 'Support' },
{ id: 'engineering', label: 'Engineering' },
{ id: 'design', label: 'Design' },
];

const featureOptions: MultiSelectOption[] = [
{ id: 'dashboard', label: 'Dashboard' },
{ id: 'reports', label: 'Reports' },
{ id: 'notifications', label: 'Notifications' },
{ id: 'api-access', label: 'API Access' },
{ id: 'sso', label: 'Single Sign-On' },
{ id: 'audit-log', label: 'Audit Log' },
{ id: 'webhooks', label: 'Webhooks' },
{ id: 'custom-roles', label: 'Custom Roles' },
];

export default function MultiSelectDemo() {
const [selected1, setSelected1] = useState<string[]>(['analytics', 'sales']);
const [selected2, setSelected2] = useState<string[]>([]);
const [selected3, setSelected3] = useState<string[]>(['analytics']);

return (
<div>
<Section title="Default">
<p className="text-sm text-[var(--flux-black)] mb-4">
Select multiple items from a dropdown. Checkboxes toggle individual items. Action labels appear on hover to show context-aware actions.
</p>
<MultiSelect
options={actionOptions}
selected={selected1}
onChange={setSelected1}
placeholder="Select departments..."
/>
{selected1.length > 0 && (
<p className="mt-3 text-xs text-[var(--flux-black)]">
<span className="font-bold text-[var(--flux-heading)]">{selected1.length} item{selected1.length !== 1 ? 's' : ''} selected</span>
{' '}— Hover over items to see action labels. Different actions appear based on selection state.
</p>
)}
</Section>

<Section title="Keyboard Navigation">
<p className="text-sm text-[var(--flux-black)] mb-4">
Full keyboard support for accessibility and power users.
</p>
<div className="mb-4">
<MultiSelect
options={featureOptions}
selected={selected2}
onChange={setSelected2}
placeholder="Select features..."
/>
</div>
<div className="grid grid-cols-2 gap-2">
{[
{ keys: '↑ ↓', desc: 'Navigate between rows' },
{ keys: '← →', desc: 'Switch checkbox / action focus' },
{ keys: 'Enter / Space', desc: 'Toggle or execute action' },
{ keys: 'Esc', desc: 'Close dropdown' },
].map(item => (
<div key={item.keys} className="flex items-start gap-2 text-xs text-[var(--flux-black)]">
<kbd className="font-mono text-[10px] px-1.5 py-0.5 rounded border border-[var(--flux-grey-100)] bg-[var(--flux-grey-50)] text-[var(--flux-heading)] whitespace-nowrap flex-shrink-0">
{item.keys}
</kbd>
<span>{item.desc}</span>
</div>
))}
</div>
</Section>

<Section title="Controlled State">
<p className="text-sm text-[var(--flux-black)] mb-4">
Manage selections programmatically with external controls.
</p>
<div className="flex items-start gap-4">
<MultiSelect
options={actionOptions}
selected={selected3}
onChange={setSelected3}
placeholder="Select departments..."
/>
<div className="flex flex-wrap gap-1.5 pt-1">
<button
onClick={() => setSelected3([])}
className="text-[11px] font-bold px-2.5 py-1 rounded border border-[var(--flux-grey-100)] text-[var(--flux-black)] hover:text-[var(--flux-heading)] hover:border-[var(--flux-grey-200)] transition-colors"
>
Clear All
</button>
<button
onClick={() => setSelected3(actionOptions.filter(o => ['analytics', 'sales', 'support'].includes(o.id)).map(o => o.id))}
className="text-[11px] font-bold px-2.5 py-1 rounded border border-[var(--flux-grey-100)] text-[var(--flux-black)] hover:text-[var(--flux-heading)] hover:border-[var(--flux-grey-200)] transition-colors"
>
Core Features
</button>
<button
onClick={() => setSelected3(actionOptions.filter(o => ['engineering', 'design', 'marketing'].includes(o.id)).map(o => o.id))}
className="text-[11px] font-bold px-2.5 py-1 rounded border border-[var(--flux-grey-100)] text-[var(--flux-black)] hover:text-[var(--flux-heading)] hover:border-[var(--flux-grey-200)] transition-colors"
>
Creative Teams
</button>
</div>
</div>
{selected3.length > 0 && (
<p className="mt-3 text-xs text-[var(--flux-black)]">
Selected: <span className="font-bold text-[var(--flux-heading)]">{actionOptions.filter(o => selected3.includes(o.id)).map(o => o.label).join(', ')}</span>
</p>
)}
</Section>
</div>
);
}                  [← Date Picker](/components/date-picker) [Journey →](/components/journey)
