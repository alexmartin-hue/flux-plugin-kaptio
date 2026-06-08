# Flux — /components/date-picker

Source: https://flux.kaptio.com/components/date-picker

[Flux](/)       [Components](/components) / Inputs & Forms

# Date Picker
Five interactive date selection styles: inline calendar, popover input, range picker, compact chip, and full calendar with prominent navigation.

### 1. Single Date Picker
Input field that opens a calendar popover on click. Select a date to close automatically. Dismiss with Escape or by clicking outside.

Departure dateDD / MM / YYYY
### 2. Date Range Picker
First click sets the start date, second click sets the end date and closes. Range is highlighted as you hover. Shows as "May 27 – Jun 3".

Date rangeSelect dates       Source  DatePickerDemo.tsx
The exact code behind the live demo above. Fetch it raw at
[/components/source/date-picker.txt](/components/source/date-picker.txt).

import React, { useState, useRef, useEffect } from "react";

// ---------------------------------------------------------------------------
// Calendar utilities (no external date library)
// ---------------------------------------------------------------------------

const MONTH_NAMES = [
"January", "February", "March", "April", "May", "June",
"July", "August", "September", "October", "November", "December",
];
const SHORT_MONTH_NAMES = [
"Jan", "Feb", "Mar", "Apr", "May", "Jun",
"Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
];
const DAY_NAMES = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"];

function getDaysInMonth(year: number, month: number): number {
return new Date(year, month + 1, 0).getDate();
}

function getMonthStartOffset(year: number, month: number): number {
const day = new Date(year, month, 1).getDay();
return day === 0 ? 6 : day - 1;
}

function isSameDay(a: Date | null, b: Date | null): boolean {
if (!a || !b) return false;
return (
a.getFullYear() === b.getFullYear() &&
a.getMonth() === b.getMonth() &&
a.getDate() === b.getDate()
);
}

function isToday(date: Date): boolean {
return isSameDay(date, new Date());
}

function isBetween(date: Date, start: Date | null, end: Date | null): boolean {
if (!start || !end) return false;
const t = date.getTime();
const s = new Date(start.getFullYear(), start.getMonth(), start.getDate()).getTime();
const e = new Date(end.getFullYear(), end.getMonth(), end.getDate()).getTime();
return t > s && t < e;
}

function formatInputValue(date: Date | null): string {
if (!date) return "";
const y = date.getFullYear();
const m = String(date.getMonth() + 1).padStart(2, "0");
const d = String(date.getDate()).padStart(2, "0");
return `${d} / ${m} / ${y}`;
}

function formatRangeDisplay(start: Date | null, end: Date | null): string {
if (!start) return "";
const s = `${SHORT_MONTH_NAMES[start.getMonth()]} ${start.getDate()}`;
if (!end) return `${s} –`;
const e = `${SHORT_MONTH_NAMES[end.getMonth()]} ${end.getDate()}`;
return `${s} – ${e}`;
}

// ---------------------------------------------------------------------------
// Inject popover keyframes once
// ---------------------------------------------------------------------------

function usePopoverKeyframes() {
useEffect(() => {
const id = "flux-datepicker-keyframes";
if (document.getElementById(id)) return;
const s = document.createElement("style");
s.id = id;
s.textContent = `
@keyframes flux-pop-in {
from { opacity: 0; transform: translateY(-6px) scale(0.98); }
to   { opacity: 1; transform: translateY(0) scale(1); }
}
`;
document.head.appendChild(s);
}, []);
}

// ---------------------------------------------------------------------------
// Shared style helpers
// ---------------------------------------------------------------------------

const labelStyle: React.CSSProperties = {
display: "block",
fontSize: "0.875rem",
fontWeight: 500,
color: "var(--flux-black)",
marginBottom: "4px",
};

function triggerStyle(open: boolean, minWidth = 200): React.CSSProperties {
return {
display: "flex",
alignItems: "center",
gap: "8px",
padding: "8px 12px",
minWidth,
background: "var(--flux-surface)",
border: open
? "1px solid var(--flux-primary-400)"
: "1px solid var(--flux-grey-200)",
borderRadius: "var(--flux-radius-sm)",
cursor: "pointer",
fontSize: "0.875rem",
fontFamily: "inherit",
transition: "border-color 150ms, box-shadow 150ms",
boxShadow: open ? "0 0 0 1px var(--flux-primary-300)" : "none",
outline: "none",
};
}

const popoverStyle: React.CSSProperties = {
position: "absolute",
top: "calc(100% + 6px)",
left: 0,
background: "var(--flux-surface)",
border: "1px solid var(--flux-grey-100)",
borderRadius: "var(--flux-radius-lg)",
boxShadow: "var(--flux-shadow-lg)",
padding: "16px",
zIndex: 50,
minWidth: "268px",
animation: "flux-pop-in 160ms cubic-bezier(0.16, 1, 0.3, 1) forwards",
};

const clearLinkStyle: React.CSSProperties = {
fontSize: "0.75rem",
fontWeight: 500,
color: "var(--flux-grey-400, #9ca3af)",
background: "none",
border: "none",
cursor: "pointer",
padding: "0",
fontFamily: "inherit",
textDecoration: "underline",
textUnderlineOffset: "2px",
};

// ---------------------------------------------------------------------------
// CalendarIcon
// ---------------------------------------------------------------------------

function CalendarIcon() {
return (
<svg
width="16"
height="16"
viewBox="0 0 16 16"
fill="none"
style={{ flexShrink: 0 }}
>
<rect
x="1.5"
y="2.5"
width="13"
height="12"
rx="2"
stroke="currentColor"
strokeWidth="1.25"
/>
<path
d="M5 1V4M11 1V4M1.5 6.5H14.5"
stroke="currentColor"
strokeWidth="1.25"
strokeLinecap="round"
/>
</svg>
);
}

// ---------------------------------------------------------------------------
// Shared CalendarGrid
// ---------------------------------------------------------------------------

interface CalendarGridProps {
year: number;
month: number;
selected?: Date | null;
rangeStart?: Date | null;
rangeEnd?: Date | null;
hovered?: Date | null;
onSelect: (date: Date) => void;
onHover?: (date: Date | null) => void;
}

function CalendarGrid({
year,
month,
selected,
rangeStart,
rangeEnd,
hovered,
onSelect,
onHover,
}: CalendarGridProps) {
const daysInMonth = getDaysInMonth(year, month);
const offset = getMonthStartOffset(year, month);
const cells: (number | null)[] = [
...Array(offset).fill(null),
...Array.from({ length: daysInMonth }, (_, i) => i + 1),
];
while (cells.length % 7 !== 0) cells.push(null);

const cellSize = 34;

return (
<div style={{ userSelect: "none" }}>
<div
style={{
display: "grid",
gridTemplateColumns: `repeat(7, ${cellSize}px)`,
marginBottom: "3px",
}}
>
{DAY_NAMES.map((d) => (
<div
key={d}
style={{
width: cellSize,
height: 26,
display: "flex",
alignItems: "center",
justifyContent: "center",
fontSize: "0.6875rem",
fontWeight: 700,
color: "var(--flux-grey-300)",
letterSpacing: "0.03em",
}}
>
{d}
</div>
))}
</div>
<div
style={{
display: "grid",
gridTemplateColumns: `repeat(7, ${cellSize}px)`,
gap: "2px",
}}
>
{cells.map((day, idx) => {
if (!day) {
return <div key={idx} style={{ width: cellSize, height: cellSize }} />;
}

const thisDate = new Date(year, month, day);
const isSelected = isSameDay(thisDate, selected ?? null);
const isRangeStart = isSameDay(thisDate, rangeStart ?? null);
const isRangeEnd = isSameDay(thisDate, rangeEnd ?? null);
const effectiveEnd = rangeEnd ?? (rangeStart && hovered ? hovered : null);
const isInRange = isBetween(thisDate, rangeStart ?? null, effectiveEnd);
const today = isToday(thisDate);
const marked = isSelected || isRangeStart || isRangeEnd;

let bg = "transparent";
if (marked) bg = "var(--flux-primary-400)";
else if (isInRange) bg = "var(--flux-primary-100)";

let textColor = "var(--flux-black)";
if (marked) textColor = "var(--flux-white)";
else if (today) textColor = "var(--flux-primary-400)";

let borderRadius: string;
if (marked || (!isInRange)) {
borderRadius = "var(--flux-radius-full)";
} else {
if (isRangeStart) borderRadius = "var(--flux-radius-full) 0 0 var(--flux-radius-full)";
else if (isRangeEnd) borderRadius = "0 var(--flux-radius-full) var(--flux-radius-full) 0";
else borderRadius = "0";
}

return (
<button
key={idx}
type="button"
onClick={() => onSelect(thisDate)}
onMouseEnter={() => onHover?.(thisDate)}
onMouseLeave={() => onHover?.(null)}
style={{
width: cellSize,
height: cellSize,
display: "flex",
alignItems: "center",
justifyContent: "center",
fontSize: "0.8125rem",
fontWeight: marked ? 700 : today ? 600 : 400,
borderRadius,
background: bg,
color: textColor,
border: today && !marked
? "1.5px solid var(--flux-primary-200)"
: "1.5px solid transparent",
cursor: "pointer",
transition: "background 100ms var(--flux-ease), color 100ms var(--flux-ease)",
outline: "none",
fontFamily: "inherit",
}}
onFocus={(e) => {
e.currentTarget.style.boxShadow = "0 0 0 2px var(--flux-primary-300)";
}}
onBlur={(e) => {
e.currentTarget.style.boxShadow = "none";
}}
>
{day}
</button>
);
})}
</div>
</div>
);
}

// ---------------------------------------------------------------------------
// MonthNav
// ---------------------------------------------------------------------------

interface MonthNavProps {
year: number;
month: number;
onChange: (year: number, month: number) => void;
}

function MonthNav({ year, month, onChange }: MonthNavProps) {
const prev = () => {
if (month === 0) onChange(year - 1, 11);
else onChange(year, month - 1);
};
const next = () => {
if (month === 11) onChange(year + 1, 0);
else onChange(year, month + 1);
};

const navBtnStyle: React.CSSProperties = {
width: 26,
height: 26,
display: "flex",
alignItems: "center",
justifyContent: "center",
borderRadius: "var(--flux-radius-sm)",
border: "none",
background: "none",
cursor: "pointer",
color: "var(--flux-grey-400, #9ca3af)",
transition: "background 120ms, color 120ms",
fontFamily: "inherit",
};

return (
<div
style={{
display: "flex",
alignItems: "center",
justifyContent: "space-between",
marginBottom: "12px",
}}
>
<button
type="button"
onClick={prev}
aria-label="Previous month"
style={navBtnStyle}
onMouseEnter={(e) => {
e.currentTarget.style.background = "var(--flux-grey-50)";
e.currentTarget.style.color = "var(--flux-heading)";
}}
onMouseLeave={(e) => {
e.currentTarget.style.background = "none";
e.currentTarget.style.color = "var(--flux-grey-400, #9ca3af)";
}}
>
<svg width="13" height="13" viewBox="0 0 13 13" fill="none">
<path
d="M8.5 10.5L4.5 6.5L8.5 2.5"
stroke="currentColor"
strokeWidth="1.5"
strokeLinecap="round"
strokeLinejoin="round"
/>
</svg>
</button>
<span
style={{
fontSize: "0.875rem",
fontWeight: 700,
color: "var(--flux-heading)",
fontFamily: "inherit",
letterSpacing: "-0.01em",
}}
>
{MONTH_NAMES[month]} {year}
</span>
<button
type="button"
onClick={next}
aria-label="Next month"
style={navBtnStyle}
onMouseEnter={(e) => {
e.currentTarget.style.background = "var(--flux-grey-50)";
e.currentTarget.style.color = "var(--flux-heading)";
}}
onMouseLeave={(e) => {
e.currentTarget.style.background = "none";
e.currentTarget.style.color = "var(--flux-grey-400, #9ca3af)";
}}
>
<svg width="13" height="13" viewBox="0 0 13 13" fill="none">
<path
d="M4.5 2.5L8.5 6.5L4.5 10.5"
stroke="currentColor"
strokeWidth="1.5"
strokeLinecap="round"
strokeLinejoin="round"
/>
</svg>
</button>
</div>
);
}

// ---------------------------------------------------------------------------
// Section wrapper
// ---------------------------------------------------------------------------

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

// ---------------------------------------------------------------------------
// 1. Single Date Picker (Popover)
// ---------------------------------------------------------------------------

function SingleDatePicker() {
usePopoverKeyframes();
const today = new Date();
const [open, setOpen] = useState(false);
const [year, setYear] = useState(today.getFullYear());
const [month, setMonth] = useState(today.getMonth());
const [selected, setSelected] = useState<Date | null>(null);
const ref = useRef<HTMLDivElement>(null);

useEffect(() => {
function handler(e: MouseEvent) {
if (ref.current && !ref.current.contains(e.target as Node)) setOpen(false);
}
document.addEventListener("mousedown", handler);
return () => document.removeEventListener("mousedown", handler);
}, []);

useEffect(() => {
function handler(e: KeyboardEvent) {
if (e.key === "Escape") setOpen(false);
}
document.addEventListener("keydown", handler);
return () => document.removeEventListener("keydown", handler);
}, []);

const handleToggle = () => {
if (!open && selected) {
setYear(selected.getFullYear());
setMonth(selected.getMonth());
}
setOpen((v) => !v);
};

const handleSelect = (date: Date) => {
setSelected(date);
setOpen(false);
};

const chevronStyle: React.CSSProperties = {
color: "var(--flux-grey-300)",
flexShrink: 0,
transition: "transform 150ms",
transform: open ? "rotate(180deg)" : "rotate(0deg)",
};

return (
<div style={{ display: "flex", gap: "2.5rem", alignItems: "flex-end", flexWrap: "wrap" }}>
<div>
<label style={labelStyle}>Departure date</label>
<div ref={ref} style={{ position: "relative", display: "inline-block" }}>
<button
type="button"
onClick={handleToggle}
aria-haspopup="dialog"
aria-expanded={open}
style={triggerStyle(open)}
onMouseEnter={(e) => {
if (!open) e.currentTarget.style.borderColor = "var(--flux-grey-400, #9ca3af)";
}}
onMouseLeave={(e) => {
if (!open) e.currentTarget.style.borderColor = "var(--flux-grey-200)";
}}
>
<span
style={{
color: open ? "var(--flux-primary-400)" : "var(--flux-grey-300)",
display: "flex",
}}
>
<CalendarIcon />
</span>
<span
style={{
flex: 1,
textAlign: "left",
color: selected ? "var(--flux-black)" : "var(--flux-grey-300)",
}}
>
{selected ? formatInputValue(selected) : "DD / MM / YYYY"}
</span>
<svg width="12" height="12" viewBox="0 0 12 12" fill="none" style={chevronStyle}>
<path
d="M2 4L6 8L10 4"
stroke="currentColor"
strokeWidth="1.5"
strokeLinecap="round"
strokeLinejoin="round"
/>
</svg>
</button>

{open && (
<div role="dialog" aria-label="Choose date" style={popoverStyle}>
<MonthNav
year={year}
month={month}
onChange={(y, m) => {
setYear(y);
setMonth(m);
}}
/>
<CalendarGrid
year={year}
month={month}
selected={selected}
onSelect={handleSelect}
/>
{selected && (
<div
style={{
marginTop: "10px",
paddingTop: "10px",
borderTop: "1px solid var(--flux-grey-100)",
display: "flex",
justifyContent: "flex-end",
}}
>
<button
type="button"
onClick={() => {
setSelected(null);
setOpen(false);
}}
style={clearLinkStyle}
>
Clear
</button>
</div>
)}
</div>
)}
</div>
</div>

</div>
);
}

// ---------------------------------------------------------------------------
// 2. Date Range Picker (Popover, single calendar)
// ---------------------------------------------------------------------------

function DateRangePicker() {
usePopoverKeyframes();
const today = new Date();
const [open, setOpen] = useState(false);
const [year, setYear] = useState(today.getFullYear());
const [month, setMonth] = useState(today.getMonth());
const [rangeStart, setRangeStart] = useState<Date | null>(null);
const [rangeEnd, setRangeEnd] = useState<Date | null>(null);
const [hovered, setHovered] = useState<Date | null>(null);
const ref = useRef<HTMLDivElement>(null);

useEffect(() => {
function handler(e: MouseEvent) {
if (ref.current && !ref.current.contains(e.target as Node)) {
setOpen(false);
setHovered(null);
}
}
document.addEventListener("mousedown", handler);
return () => document.removeEventListener("mousedown", handler);
}, []);

useEffect(() => {
function handler(e: KeyboardEvent) {
if (e.key === "Escape") {
setOpen(false);
setHovered(null);
}
}
document.addEventListener("keydown", handler);
return () => document.removeEventListener("keydown", handler);
}, []);

const handleToggle = () => {
setOpen((v) => !v);
setHovered(null);
};

const handleSelect = (date: Date) => {
if (!rangeStart || rangeEnd) {
setRangeStart(date);
setRangeEnd(null);
setHovered(null);
} else {
const t = date.getTime();
const s = rangeStart.getTime();
if (t < s) {
setRangeEnd(rangeStart);
setRangeStart(date);
} else {
setRangeEnd(date);
}
setHovered(null);
setOpen(false);
}
};

const handleClear = () => {
setRangeStart(null);
setRangeEnd(null);
setHovered(null);
};

const selectingEnd = rangeStart !== null && rangeEnd === null;
const hasSelection = rangeStart !== null;
const displayValue = formatRangeDisplay(rangeStart, rangeEnd);

const chevronStyle: React.CSSProperties = {
color: "var(--flux-grey-300)",
flexShrink: 0,
transition: "transform 150ms",
transform: open ? "rotate(180deg)" : "rotate(0deg)",
};

return (
<div style={{ display: "flex", gap: "2.5rem", alignItems: "flex-end", flexWrap: "wrap" }}>
<div>
<label style={labelStyle}>Date range</label>
<div ref={ref} style={{ position: "relative", display: "inline-block" }}>
<button
type="button"
onClick={handleToggle}
aria-haspopup="dialog"
aria-expanded={open}
style={triggerStyle(open, 240)}
onMouseEnter={(e) => {
if (!open) e.currentTarget.style.borderColor = "var(--flux-grey-400, #9ca3af)";
}}
onMouseLeave={(e) => {
if (!open) e.currentTarget.style.borderColor = "var(--flux-grey-200)";
}}
>
<span
style={{
color: open ? "var(--flux-primary-400)" : "var(--flux-grey-300)",
display: "flex",
}}
>
<CalendarIcon />
</span>
<span
style={{
flex: 1,
textAlign: "left",
color: hasSelection ? "var(--flux-black)" : "var(--flux-grey-300)",
fontWeight: hasSelection ? 500 : 400,
}}
>
{displayValue || "Select dates"}
</span>
<svg width="12" height="12" viewBox="0 0 12 12" fill="none" style={chevronStyle}>
<path
d="M2 4L6 8L10 4"
stroke="currentColor"
strokeWidth="1.5"
strokeLinecap="round"
strokeLinejoin="round"
/>
</svg>
</button>

{open && (
<div role="dialog" aria-label="Choose date range" style={popoverStyle}>
<div
style={{
fontSize: "0.75rem",
fontWeight: 600,
color: "var(--flux-primary-400)",
marginBottom: "10px",
letterSpacing: "-0.01em",
visibility: selectingEnd ? "visible" : "hidden",
}}
>
Now select end date
</div>
<MonthNav
year={year}
month={month}
onChange={(y, m) => {
setYear(y);
setMonth(m);
}}
/>
<CalendarGrid
year={year}
month={month}
rangeStart={rangeStart}
rangeEnd={rangeEnd}
hovered={selectingEnd ? hovered : null}
onSelect={handleSelect}
onHover={selectingEnd ? setHovered : undefined}
/>
{hasSelection && (
<div
style={{
marginTop: "10px",
paddingTop: "10px",
borderTop: "1px solid var(--flux-grey-100)",
display: "flex",
justifyContent: "space-between",
alignItems: "center",
}}
>
{rangeStart && rangeEnd && (
<span
style={{
fontSize: "0.75rem",
color: "var(--flux-grey-400, #9ca3af)",
}}
>
{Math.round(
(rangeEnd.getTime() - rangeStart.getTime()) / 86_400_000
)}{" "}
nights
</span>
)}
<button
type="button"
onClick={handleClear}
style={{ ...clearLinkStyle, marginLeft: "auto" }}
>
Clear
</button>
</div>
)}
</div>
)}
</div>
</div>

</div>
);
}

// ---------------------------------------------------------------------------
// Main demo export
// ---------------------------------------------------------------------------

export default function DatePickerDemo() {
return (
<div>
<Section title="1. Single Date Picker">
<p
style={{
fontSize: "0.875rem",
color: "var(--flux-grey-500)",
marginBottom: "20px",
}}
>
Input field that opens a calendar popover on click. Select a date to close
automatically. Dismiss with Escape or by clicking outside.
</p>
<SingleDatePicker />
</Section>

<Section title="2. Date Range Picker">
<p
style={{
fontSize: "0.875rem",
color: "var(--flux-grey-500)",
marginBottom: "20px",
}}
>
First click sets the start date, second click sets the end date and closes.
Range is highlighted as you hover. Shows as "May 27 – Jun 3".
</p>
<DateRangePicker />
</Section>
</div>
);
}                  [← Hero](/components/hero) [Input →](/components/input)
