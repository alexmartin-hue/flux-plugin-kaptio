# Flux — /components/file-upload/

Source: https://flux.kaptio.com/components/file-upload/

Component

# File upload
A dropzone over a native file input, and a list of the chosen files with their progress and errors.

Plain-text source, for agents and clipboard use: [/components/source/file-upload.txt](/components/source/file-upload.txt)

## When to use it
For attaching documents to a record: passport scans, supplier contracts, invoices. The native file input covers the dropzone, so a click anywhere opens the picker and a dropped file lands in the input without scripting. Each file joins a list with its size and state. The script checks the accepted types and the size limit, then hands valid files to the page through a flux-upload event; the page uploads them and reports progress, success or failure back to the item.

Not thisNot for importing data that needs mapping and validation row by row; that is a dedicated import flow. Not for a single avatar or logo, where a button that opens the picker is enough.
## Examples

### Default
Choose or drop files. A file over 10 MB, or of another type, is listed with an error. On this page, every third upload fails so the Retry action can be seen.

Passport scans

PDF, JPG or PNG, up to 10 MB each. One file per traveller.

Choose files or drop them here

htmlCopy`

Passport scans

PDF, JPG or PNG, up to 10 MB each. One file per traveller.

Choose files or drop them here

`
### File states
Uploaded, uploading with an inline progress bar, and failed with a reason and a retry.

passport-anna-jonsdottir.pdf
1.2 MB · Uploaded

passport-marianne-hollis.jpg
3.4 MB · Uploading

45%

passport-scan-full-resolution.png
14.8 MB · Larger than 10 MB.

passport-olafur-gunnarsson.pdf
0.9 MB · The connection dropped.

Retry

htmlCopy`

passport-anna-jonsdottir.pdf
1.2 MB · Uploaded

passport-marianne-hollis.jpg
3.4 MB · Uploading

45%

passport-scan-full-resolution.png
14.8 MB · Larger than 10 MB.

passport-olafur-gunnarsson.pdf
0.9 MB · The connection dropped.

Retry

`
## Anatomy
PartDescriptionLabelA field label for the input, with an info bubble that states the accepted types and size.DropzoneA dashed outline with an icon and a prompt. It turns teal on hover and fills while a file is dragged over it.InputThe native file input, invisible, covering the dropzone.File listA bordered list of items, hidden while empty, announced politely as it changes.ItemA file icon, the name, a mono size and the state, an inline progress bar while uploading, and a remove button.
## API
NameKindDescription`flux-upload`classWraps the dropzone and the list.`data-flux-upload`attributeWires dragging, checking, listing and the upload events.`data-max-mb`attributeOn flux-upload: the largest file accepted, in megabytes. State it in the info bubble too.`flux-upload__dropzone | __icon | __prompt | __action`classThe dropzone and its contents.`flux-upload__input`classOn the input type="file". Use accept and multiple as usual. It is cleared after each pick, so the same file can be chosen again.`flux-upload__list | __item`classThe file list and each file. data-state is ready, uploading, done or error.`flux-upload__remove`classThe remove button. Label it "Remove" and the file name.`flux-upload`elementEvent dispatched per valid file, with detail.file, detail.progress(percent), detail.complete() and detail.fail(message).`flux-upload-remove`elementEvent dispatched when a file is removed, with detail.file.
## States
StateTreatmentIdleA dashed border-strong outline on layer-01.HoverThe outline turns border-brand.Drag overA solid border-brand outline and a surface-brand-subtle fill.FocusThe Flux focus ring around the dropzone.UploadingAn inline small progress bar below the file name.DoneThe file icon turns text-success and the state reads Uploaded.ErrorThe icon and the state text turn text-error, with the reason in words. A failed upload offers Retry.DisabledA disabled input dims the dropzone and stops it accepting files.
## Keyboard
KeysAction`Tab`Focuses the input, then each item’s actions.`Enter, Space`Opens the file picker.
## Accessibility

- The input is the real control, labelled by the field label, with the constraints in the info bubble it references.
- The file list is a polite live region, so added files, failures and completions are announced.
- Every state is in words as well as colour.
- Removing a file moves focus to the next file’s remove button, or back to the input.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-upload-padding | -gap | -bg | -bg-active
- --flux-upload-border | -border-active
- --flux-upload-icon | -icon-size | -text
- --flux-upload-item-padding-y | -item-padding-x | -item-gap | -item-divider
- --flux-upload-meta | -success
## Do and don’t
Do

- State the accepted types and size limit in the info bubble before anyone picks a file.
- Say why a file failed: too large, wrong type, or what the server said.
- Let people remove a file at any point, including while it uploads.Don’t

- Do not put the size limit below the dropzone as help text.
- Do not silently drop a file that fails a check.
- Do not block the rest of the form while files upload.[PreviousList and detail](/components/split-view/)[NextAssistant panel](/components/assistant-panel/)
