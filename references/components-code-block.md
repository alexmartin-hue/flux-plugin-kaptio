# Flux — /components/code-block

Source: https://flux.kaptio.com/components/code-block

[Flux](/)       [Components](/components) / Data Display

# Code Block
Monospace display for code snippets and tokens.

### Inline Code
Use the `--flux-primary-400` token for primary actions. Configure surfaces with `--flux-surface` and backgrounds with `--flux-background`.

### Block
CSSCopy`:root {
--flux-primary-400: #0A6E5F;
--flux-primary-800: #032E36;
--flux-surface: #FFFFFF;
--flux-background: #F8F8F8;
}`       Source  CodeBlockDemo.tsx
The exact code behind the live demo above. Fetch it raw at
[/components/source/code-block.txt](/components/source/code-block.txt).

import React, { useState, useCallback } from "react";

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

const snippet = `:root {
--flux-primary-400: #0A6E5F;
--flux-primary-800: #032E36;
--flux-surface: #FFFFFF;
--flux-background: #F8F8F8;
}`;

export default function CodeBlockDemo() {
const [copied, setCopied] = useState(false);

const handleCopy = useCallback(() => {
navigator.clipboard.writeText(snippet).then(() => {
setCopied(true);
setTimeout(() => setCopied(false), 1500);
});
}, []);

return (
<div>
<Section title="Inline Code">
<p className="text-sm text-[var(--flux-black)] leading-relaxed">
Use the{" "}
<code
className="text-sm px-1.5 py-0.5 rounded"
style={{
fontFamily: "var(--flux-font-mono)",
backgroundColor: "var(--flux-primary-100)",
color: "var(--flux-primary-400)",
}}
>
--flux-primary-400
</code>{" "}
token for primary actions. Configure surfaces with{" "}
<code
className="text-sm px-1.5 py-0.5 rounded"
style={{
fontFamily: "var(--flux-font-mono)",
backgroundColor: "var(--flux-primary-100)",
color: "var(--flux-primary-400)",
}}
>
--flux-surface
</code>{" "}
and backgrounds with{" "}
<code
className="text-sm px-1.5 py-0.5 rounded"
style={{
fontFamily: "var(--flux-font-mono)",
backgroundColor: "var(--flux-primary-100)",
color: "var(--flux-primary-400)",
}}
>
--flux-background
</code>
.
</p>
</Section>

<Section title="Block">
<div className="relative rounded overflow-hidden" style={{ backgroundColor: "#032E36" }}>
<div className="flex items-center justify-between px-4 py-2 border-b border-white/10">
<span className="text-xs font-bold" style={{ color: "#8BB9BF", fontFamily: "var(--flux-font-mono)" }}>
CSS
</span>
<button
onClick={handleCopy}
className="text-xs px-2.5 py-1 rounded font-bold transition-colors"
style={{
color: copied ? "#2BA711" : "#E6F1F2",
backgroundColor: copied ? "rgba(43,167,17,0.15)" : "rgba(255,255,255,0.1)",
}}
>
{copied ? "Copied!" : "Copy"}
</button>
</div>
<pre className="p-4 overflow-x-auto">
<code
className="text-sm leading-relaxed"
style={{ fontFamily: "var(--flux-font-mono)", color: "#E6F1F2" }}
>
{snippet}
</code>
</pre>
</div>
</Section>
</div>
);
}                  [← Checkbox](/components/checkbox) [Hero →](/components/hero)
