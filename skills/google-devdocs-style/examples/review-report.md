# Example: a review report

What a good review looks like when someone hands you a doc and asks you to check it.
The shape matters: severity first, fix included, and the author left room to disagree.

## The report

> I read the migration guide against the style guide. Three things worth changing
> before it ships, plus a handful of mechanical fixes.
>
> ### Blocking
>
> **The step 4 command doesn't match the placeholder explanation.** The command uses
> `--project-id` but the text below explains `PROJECT_NAME`. A reader following this
> literally gets an error. Which is correct?
>
> **Real credentials in the step 7 output block.** The sample output includes what
> looks like a live bearer token (`ya29.a0Af…`). Replace it with a truncated
> placeholder even if the token is already rotated.
>
> ### Should fix
>
> **Prerequisites arrive at step 6.** The guide requires the `roles/editor` role, but
> the reader doesn't find that out until they've already provisioned a cluster.
> Moving the requirement above step 1 saves them a rollback. Suggested opening:
> "Before you start, make sure you have the Editor role on the project."
>
> **Steps 2, 5, and 9 bury the location.** Each starts with the action and ends with
> where to do it — "Click **Deploy** in the Cloud console." Reversing them ("In the
> Cloud console, click **Deploy**") means the reader isn't halfway through an action
> before learning they're in the wrong window.
>
> **Three links read "click here" or "this page."** Screen reader users often
> navigate by pulling up a list of links with no surrounding sentence, so these
> become three identical entries. Suggested: "see [Configure a service account]".
>
> ### Style
>
> - Headings are title case throughout; the guide uses sentence case. Nine headings.
> - "whitelist the runner IP" (step 5) → "add the runner's IP address to the
>   allowlist." The verb form doesn't get a one-word substitute.
> - "master branch" (steps 8 and 11) → `main` branch.
> - Six instances of *currently* and two of *for now* — all deletable without
>   changing the meaning, and they'll date the doc.
> - "will be created," "is returned," "can be configured" — six passive
>   constructions. Four hide who acts, which matters in a permissions doc.
> - *utilize* (×3) → *use*. *in order to* (×4) → *to*.
> - "file system" is written as "filesystem" in five places.
>
> ### Optional
>
> - You use both "VM" and "instance" for the same thing. Either is fine, but picking
>   one would help translators, who may otherwise read them as distinct concepts.
> - Step 12 offers both a console path and a CLI path. The guide suggests documenting
>   one — the shortest keyboard-accessible route — and splitting alternatives into
>   tabs. Your call; if most of your readers script this, the CLI path alone may be
>   the better single answer.
>
> ### One note on the hierarchy
>
> Your doc set consistently writes "the Console" with a capital C, which the guide
> would lowercase. I left it alone — project-specific style outranks the guide, and
> consistency inside your doc set is worth more than matching Google. Flagging it
> only so the choice is deliberate.

## Why it's shaped this way

- **Severity first.** An author with 20 minutes fixes the token leak, not the title
  case. Burying a credential leak in an alphabetical list of nitpicks is a
  disservice.
- **Counts, not instances.** "Nine headings" beats nine separate bullets. Mechanical
  fixes get aggregated; judgment calls get argued individually.
- **The fix is included.** "Passive voice in step 3" makes the author do the work
  twice. Give the replacement sentence.
- **Reasons, not citations.** "Screen reader users navigate by link list" persuades;
  "violates the cross-references guidance" doesn't.
- **Blocking items can be questions.** The mismatched placeholder isn't a style
  violation to correct unilaterally — only the author knows which is right.
- **Optional items stay optional.** Framing them as preferences the author can
  decline keeps the rest of the report credible.
- **Naming the hierarchy conflict** shows you noticed rather than missed it, and
  concedes the point to the doc set.

---

*Provenance: rules cited above come from the Google developer documentation style
guide (CC BY 4.0). The example doc and report are original, written for this skill.
Canonical source: https://developers.google.com/style*
