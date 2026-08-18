# Procedures

A procedure is a numbered sequence of steps that accomplishes one task. Lists that
aren't sequences belong in [formatting.md](formatting.md) instead.

## Contents

- [Introducing a procedure](#introducing-a-procedure)
- [Single-step procedures](#single-step-procedures)
- [Sub-steps](#sub-steps)
- [Ordering components within a step](#ordering-components-within-a-step)
- [Multi-action steps](#multi-action-steps)
- [Multiple paths to the same outcome](#multiple-paths-to-the-same-outcome)
- [Optional and repeated steps](#optional-and-repeated-steps)
- [Location, goal, and result](#location-goal-and-result)
- [Full guidance table](#full-guidance-table)

## Introducing a procedure

Give the reader context the heading doesn't already give. If the heading says it all,
skip the intro rather than restating it.

End the intro with a colon when the steps come immediately after. Use a period when
something else intervenes, like a note.

The intro must be a complete sentence or an imperative statement — never a fragment
that the numbered steps finish.

Recommended:
- To customize the buttons, follow these steps:
- Customize the buttons:
- To customize the buttons, do the following:

Not recommended:
- To customize the buttons:

## Single-step procedures

One step is a bullet, not a numbered list containing a single item, and not a
"follow this step:" preamble.

Recommended:

- To flush the entire log, click **Clear logcat**.

## Sub-steps

Sub-steps take lowercase letters. Sub-sub-steps take lowercase roman numerals. A step
that has sub-steps behaves like an introductory sentence — end it with a colon or
period as appropriate.

```
1. To add a VM instance, do the following:
   a. Click Create instance.
   b. For Name, enter a name for the VM instance, and then do the following:
      i.  For Region, specify where you want to deploy the instance.
      ii. For Machine type, select an option.
   c. Click Create.
2. To connect to the VM instance by using SSH, click SSH.
```

## Ordering components within a step

When a step has several parts, order them like this:

1. Describe the action.
2. Show the command, if there is one.
3. Explain any placeholders in the command.
4. Explain the command further, if needed.
5. Show the output, if the reader needs to check it.
6. In a separate paragraph, explain the result of the action.

Example shape:

> Plan the Terraform deployment:
>
> ```
> terraform plan -out=NAME
> ```
>
> Replace `NAME` with the name of your Terraform plan.
>
> The output is similar to the following:
>
> ```
> Plan: 26 to add, 0 to change, 0 to destroy.
> ```
>
> The output shows what resources Terraform adds, changes, or destroys.

## Multi-action steps

One action per step, with one exception: sequential menu selections can be combined
using angle brackets.

- Click **Next > Finish**.
- Click **File > New > Document**.

If a step feels long, split it. If the reader must press **Enter** to complete the
step, include that in the same step — don't make pressing Enter its own step.

Don't document keyboard shortcuts as the instruction. "Copy the command, and then
paste it" rather than "Press Ctrl+C, then Ctrl+V."

## Multiple paths to the same outcome

Prefer documenting exactly one procedure that every reader can follow. Choose:

1. The path that works with a keyboard alone.
2. The shortest path.
3. The path using the language or tool most of the audience already knows.

If you genuinely must document several paths (console vs. CLI vs. API, for example),
separate them into different pages, headings, or tabs — never interleave them.

## Optional and repeated steps

Optional steps start with `Optional:`.

Recommended: `1. Optional: Enter an arbitrary string.`
Not recommended: `1. (Optional) Enter an arbitrary string.`

Don't repeat a procedure that appears elsewhere. Link to it: "Create a user as you did
in the previous step."

## Location, goal, and result

**Location before action.** Tell the reader where they are before what to do.

- Recommended: In Google Docs, click **File > New > Document**.
- Not recommended: Click **File > New > Document** in Google Docs.

If a task spans several headings, restate the location in the first step of each
procedure, even if it hasn't changed.

**Goal before action.**

- Recommended: To start a new document, click **File > New > Document**.
- Not recommended: Click **File > New > Document** to start a new document.

If the "To ..." framing might read as optional, use the colon form instead: "Sort the
data by date: click **Data > Sort**."

**Result after action, same paragraph.** Include a result only when the reader needs it
to proceed, and don't double-describe UI that the next step already names.

- Recommended: Click **Run**. The query results appear after the query runs.
- Recommended: `1. Click Enter.` / `2. In the New file dialog that appears, click Next.`
- Not recommended: `1. Click Enter. The New file dialog appears.` / `2. In the New file
  dialog, click Next.`

Justifications work the same way — action first, reason second: "Store the private key
in a secure location. You need it later."

## Full guidance table

| Guidance | Recommended | Not recommended |
| --- | --- | --- |
| Start each step with an imperative verb | Clone the repository that contains the sample data. | You need the project ID later. Retrieve the project ID. |
| Use complete sentences | — | — |
| Use parallel structure and consistent verb forms | Download the key to your machine. Click **More**, and then click **Download**. | Download the key by clicking **More** and then clicking **Download** file. |
| Mark optional steps with `Optional:` | Optional: Enter an arbitrary string. | (Optional) Enter an arbitrary string. |
| Set the context (tool, environment) | In Cloud Shell, connect to the development cluster. | Connect to the development cluster. |
| State location before action | In the Google Cloud console, go to the **Monitoring** page. | Go to the **Monitoring** page in the Google Cloud console. |
| State purpose before action | To start a new document, click **File > New**. | Click **File > New** to start a new document. |
| Avoid directional language | In the preceding diagram... / In the following diagram... | In the above diagram... / In the diagram below... |
| Don't say *please* in ordinary instructions | To open a document, click **File > Open**. | To open a document, please click **File > Open**. |
| Don't say "run the following command" | In Cloud Shell, deploy the load generator: | Run the following command to deploy the load generator: |
| Include Enter as part of the step | Click the search box, type `custom function`, and then press **Enter**. | Click the search box and type `custom function`. Press **Enter**. |
| Skip keyboard shortcuts | Copy the command, and then paste it. | Press Ctrl+C, and then press Ctrl+V. |
| Give only the best way when several exist | — | — |
| Front-load prerequisites | The following hardware and software are required: | (Requirements revealed at step 7.) |
| Minimize step count and interruptions | — | — |
| One reader decision per list item | — | — |

If a UI element is genuinely hard to find, add a screenshot rather than describing its
screen position.

---

*Provenance: guidance on this page is drawn from the Google developer documentation
style guide (CC BY 4.0) and reorganized for use as a skill. Where the source is
silent, this file says so. Canonical source: https://developers.google.com/style*
