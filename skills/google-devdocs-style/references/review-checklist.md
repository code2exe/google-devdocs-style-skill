# Review checklist

Use this when editing or reviewing a doc someone else wrote. Work the passes in order —
structural problems change what the sentence-level fixes should be, so fixing prose
first wastes effort.

## Pass 1 — Structure and fitness for purpose

- Does the doc have one clear purpose, and does its type match that purpose (quickstart,
  how-to, reference, concept, runbook)? Mixed types are the most common structural
  defect: a conceptual overview with steps buried in it serves neither reader.
- Is the audience and its assumed knowledge stated near the top?
- Are prerequisites — permissions, quota, credentials, tools, cost — all listed *before*
  the first step?
- Do headings descend without skipping levels, and does the heading outline alone tell a
  reader what the doc covers?
- Is anything documented twice? Consolidate and link.
- Is there content that belongs in a different doc?
- Does the doc end where the reader's task ends, with next steps or verification?

## Pass 2 — Procedures

- Every step starts with an imperative verb.
- One action per step, except chained menu selections.
- Location stated before action; goal stated before action.
- Optional steps marked `Optional:`.
- Placeholders explained immediately after each command.
- Output shown where the reader needs to verify, with a note on what to look for.
- No directional language, no keyboard shortcuts as the only path, no "run the following
  command."
- Only one way to accomplish the task, unless alternatives are separated into tabs or
  headings.
- Can a reader complete this using a keyboard alone?

## Pass 3 — Voice, tense, person

- Second person throughout; *we* only for the publisher's recommendations.
- Active voice; every instruction has a clear actor.
- Present tense.
- Conditions before instructions.
- No anthropomorphism.
- No *simply*, *just*, *easy*, *quick*, *obviously*. No *please* in ordinary
  instructions, and no *please note*.
- Modal verbs correct: *can* for ability and permission, *might* for possibility,
  *must* for requirements. No *should* used to mean *must*.
- Version ranges use *later* and *earlier*, not *higher*, *lower*, or *2.2+* — and
  give a version number as the reference point.
- No excessive claims or absolutes.

## Pass 4 — Formatting

- Sentence case in all headings, titles, table headers, captions.
- Bold only for UI elements, run-in headings, notice labels.
- Italics only for defined terms, words as words, full-length work titles, math and
  version variables.
- Code font for all code elements, with a qualifying noun.
- Placeholders uppercase in code font.
- Lists parallel in structure, punctuation, and capitalization; introduced by a complete
  sentence with a colon.
- Numbered lists only for sequences and rankings.
- Tables have header rows and no empty cells.
- Notices are sparse, correctly labeled, and outside procedures.

## Pass 5 — Links and references

- All link text describes its destination; no "click here," no bare URLs.
- Punctuation outside link text.
- Cross-references use standardized introductions.
- Off-site links identify the source.
- Third-party material is linked rather than restated, and is properly attributed.
- No broken or heading-dependent anchors.

## Pass 6 — Global audience and translation

- Sentences short; one idea each.
- Simple words in place of Latinate or inflated ones.
- Helper words present: *that*, *then*, *of*, *which*.
- One term per concept, used consistently with consistent capitalization.
- Abbreviations spelled out on first use.
- No ambiguous pronouns.
- No idioms, sports metaphors, holidays, seasons, or culture-dependent humor.
- Unambiguous dates and time zones.
- Diverse example names; reserved example domains and documentation IP ranges.

## Pass 7 — Accessibility and inclusion

- Alt text on all meaningful images; empty alt on decorative ones.
- No information conveyed by image alone.
- No information conveyed by color alone.
- Inclusive terminology throughout — check against
  [word-list.md](word-list.md).
- No ableist metaphors.
- Singular *they*.

## Pass 8 — Durability and safety

- No *currently*, *new*, *recently*, *soon*, or relative dates.
- No pre-announcement of unreleased features or dates.
- No real credentials, keys, tokens, internal hostnames, customer names, or account IDs
  in samples or output.
- Deprecation and lifecycle language matches the project's official labels.
- Version numbers and API versions specific rather than implied.

## Reporting findings

Group by severity, and give the fix rather than just the diagnosis:

- **Blocking** — factually wrong, unsafe, leaks credentials, procedure doesn't work, or
  a reader can't complete the task.
- **Should fix** — structural or procedural problems that measurably slow the reader:
  missing prerequisites, buried conditions, non-parallel steps, undescriptive links.
- **Style** — voice, tense, formatting, terminology, word choice.
- **Optional** — preferences where the guide allows either form.

For anything beyond a mechanical fix, show before and after. If you rewrite heavily,
summarize what changed and why so the author can disagree. And name which level of the
reference hierarchy a call came from — if the doc set's own convention conflicts with
this guide, the doc set wins, and the author should hear that you noticed.

---

*Provenance: guidance on this page is drawn from the Google developer documentation
style guide (CC BY 4.0) and reorganized for use as a skill. Where the source is
silent, this file says so. Canonical source: https://developers.google.com/style*
