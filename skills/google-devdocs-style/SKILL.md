---
name: google-devdocs-style
description: Write, edit, or review developer documentation in Google developer documentation style. Use this skill whenever the user asks for technical documentation to be written, rewritten, tightened, made consistent, "made to read like Google docs," or checked against a style guide — and also proactively whenever the deliverable is itself developer documentation (README, runbook, API reference, quickstart, how-to guide, migration guide, release notes, onboarding doc, SOP, architecture doc) even if the user never mentions style. Covers voice and tone, second person, active voice, present tense, sentence case headings, procedures and numbered steps, lists and tables, code font vs. bold vs. italics, placeholders, command-line syntax, UI interaction verbs, modal verbs, inclusive and non-ableist word choices, timeless wording, writing for a global audience, and a verified word list. Don't use it for marketing copy, social posts, or narrative essays.
---

# Google developer documentation style

Editorial style for developer-facing documentation, distilled from Google's public
developer documentation style guide (CC BY 4.0, https://developers.google.com/style).

Use this for docs whose readers are software developers and technical practitioners.
Don't apply it to marketing copy, LinkedIn posts, or narrative essays — those have
different goals.

## Reference hierarchy

Resolve style questions in this order, and say which level you used when it matters:

1. **The project's own style.** Existing terminology, product names, and documented
   exceptions in the repo or doc set win. If a doc set already says "replica set" or
   "workspace," match it — don't silently re-term things.
2. **This skill.** The general guidance below.
3. **Third-party references.** Spelling: Merriam-Webster. Non-technical style: Chicago
   Manual of Style. Technical style: Microsoft Writing Style Guide (filter out
   Microsoft-product-specific advice).

These are guidelines, not laws. Depart from them when doing so makes the content
clearer for its actual readers — then be consistent within the document.

## The ten rules that matter most

If nothing else survives, keep these:

1. **Second person.** Address the reader as *you*. Reserve *we* for the authoring
   organization's decisions, and avoid it in instructions.
2. **Active voice.** Make it clear who performs the action. "The service returns a
   token," not "A token is returned."
3. **Present tense.** "The command creates a cluster," not "will create."
4. **Sentence case** for every heading, title, table header, and nav label.
5. **Conditions before instructions.** "If the build fails, check the logs" — not the
   reverse. State *where* before *what*: "In Cloud Shell, run the migration."
6. **Imperative steps.** Every numbered step starts with a verb the reader acts on.
7. **Code font for code, bold for UI, italics for terms.** Nothing else. See
   [Formatting](references/formatting.md).
8. **Descriptive link text.** Link the thing being described, never "click here" or a
   bare URL.
9. **Timeless and non-pre-announcing.** No "currently," "new," "recently," or
   "coming soon." Docs get read years later.
10. **Write for a global audience.** Short sentences, simple words, no idioms, no
    seasons, no humor that depends on culture.

## Choosing a mode

**Writing new docs.** Pick the right shape first, then apply style:

| Reader intent | Shape |
| --- | --- |
| "Get me running fast" | Quickstart: prerequisites, then a single happy path, no options |
| "Do this specific task" | How-to guide: numbered procedure, one goal |
| "What are the parameters" | Reference: tables and consistent verb phrases, no narrative |
| "Why is it built this way" | Conceptual/architecture doc: prose, diagrams, no steps |
| "It's broken at 3 a.m." | Runbook: symptom → diagnosis → action, each step verifiable |

State the audience and prerequisites near the top. Tell readers what they need
*before* they start — hardware, permissions, credentials, quota — not halfway through
step 7.

**Reviewing or editing existing docs.** Work through
[references/review-checklist.md](references/review-checklist.md), then report findings
grouped by severity, each with the specific fix. Show before/after for anything
non-obvious. Don't rewrite silently — if you make heavy changes, summarize what
changed and why so the author can push back.

## Voice and tone

Conversational and friendly, but not frivolous. Think knowledgeable colleague
explaining something at a whiteboard: warm, direct, no filler.

- Contractions are fine and usually better ("don't," "you'll").
- Skip *simply*, *just*, *easy*, *quick*, *obviously*, and *of course*. They either
  pad the sentence or make a struggling reader feel stupid.
- Don't use *please* when explaining how to use a product, even a hard task, and
  never write *please note*. Do use it when you're asking for something that
  inconveniences the reader: "If the issue persists, please contact support."
- Don't anthropomorphize software. Systems don't "want," "think," "see," or "know."
  They receive, return, evaluate, reject.
- No excessive claims — avoid *seamless*, *effortless*, *bulletproof*, *fully
  secure*, *any*, *all*, *never fails*. Say what the thing does and under what
  conditions.
- Explain jargon on first use, or link to a definition. Prefer the plain word:
  *use* not *utilize*, *start* not *commence*, *so* not *consequently*.

## Procedures

The single highest-leverage area, and where most docs fail. Full detail in
[references/procedures.md](references/procedures.md). The essentials:

- Introduce a procedure with a complete sentence ending in a colon, not a fragment the
  steps complete. "To customize the buttons, follow these steps:" — not "To customize
  the buttons:".
- One action per step. Combine only sequential menu picks: **File > New > Document**.
- Single-step procedure → a bullet, not a numbered list of one.
- Sub-steps use lowercase letters; sub-sub-steps use lowercase roman numerals.
- Goal before action: "To start a new document, click **File > New**."
- Location before action: "In the Google Cloud console, go to the **Monitoring** page."
- Optional steps begin `Optional:` — not `(Optional)`.
- Put results in the same step as the action, and only when the reader needs them to
  navigate. Don't announce a dialog in one step and then re-describe it in the next.
- No directional language (*above*, *below*, *the box on the right*) — it breaks for
  screen readers, RTL layouts, and reflowed mobile pages. Use *preceding* and
  *following*.
- Avoid "run the following command." Say what the command accomplishes, then show it.
- Don't offer two ways to do the same thing. Pick the shortest keyboard-accessible one.

## Formatting quick reference

Full rules in [references/formatting.md](references/formatting.md).

| Element | Treatment |
| --- | --- |
| UI elements, run-in headings, notice labels | **Bold** (`**`, not `__`) |
| Terms being defined, words as words, math and version variables | *Italics* (`_`, not `*`) |
| Code, filenames, class and method names, HTTP codes, console output, placeholders | `Code font` |
| Code samples and command blocks | Fenced code blocks |
| Underline | Links only — never for emphasis |
| Titles of full-length works | Italics |
| Titles of articles, episodes | Quotation marks |

Never use `&` as a conjunction, including in headings. Use *and*.

## Global audience and inclusion

Much of a doc's readership won't be reading in a first language, and some of it will be
machine-translated. That makes clarity a mechanical requirement, not a nicety.

- Short sentences. Standard subject-verb-object order. Subject and verb early.
- Keep helper words that conversational English drops: *that*, *then*, *of*, *which*.
  "Assumes that you have..." and "Start the profiler, and then run the app."
- Use a term for exactly one concept, and use the same term every time, with the same
  capitalization.
- Qualify code references: "the `example.yaml` file," not bare "`example.yaml`."
- Spell out abbreviations on first use.
- Replace ambiguous pronouns with the noun.
- No idioms (*ballpark figure*, *back burner*), no sports metaphors, no holidays, no
  seasons as time markers, no culture-dependent humor.
- Unambiguous dates: *January 4, 2026* or *2026-01-04*, never *1/4/26*.
- Diverse example names; reserved example domains (`example.com`) and RFC 5737
  documentation IP ranges.
- Inclusive terminology and no ableist metaphors — see
  [references/word-list.md](references/word-list.md).

## Accessibility

- Alt text on every meaningful image; decorative images get empty alt text.
- Images carry no information that isn't also in the text. Images don't get translated,
  indexed, or read aloud.
- Heading levels descend in order without skipping.
- Tables get real header rows. Don't use tables for layout.
- Don't rely on color alone to convey meaning.
- Don't document keyboard shortcuts as the only path; prefer paths any reader can follow.

## Reference files

Read the relevant file when the task goes deeper than the summaries above:

- [references/procedures.md](references/procedures.md) — steps, sub-steps, commands,
  output, multi-path tasks, the full recommended/not-recommended table
- [references/formatting.md](references/formatting.md) — headings, lists, tables,
  notices, links, numbers, dates, units, placeholders, command-line syntax, code samples
- [references/language.md](references/language.md) — grammar, punctuation,
  capitalization, abbreviations, pronouns, sentence structure, reference-doc verbs
- [references/word-list.md](references/word-list.md) — preferred terms, terms to
  avoid, and inclusive replacements
- [references/review-checklist.md](references/review-checklist.md) — ordered pass for
  editing existing docs, with severity levels

Worked before-and-after transformations live in `examples/`. Read one when you want
to calibrate how heavy an edit should be.

## Accuracy and scope

Two habits keep this skill honest:

**Look words up rather than inferring them.** The source word list has hundreds of
entries, is updated frequently, and its rulings are often counterintuitive —
`frontend` is closed but `file system` is open; `namespace` is closed but `name
server` is open. The word list here is a verified subset. For any term it doesn't
cover, check https://developers.google.com/style/word-list, and fall back to
Merriam-Webster's first listed spelling if the guide is silent.

**Distinguish the guide's two warning strengths.** *Avoid* means prefer something
else when possible — the term is usable if it's genuinely clearest, ideally defined
on first use. *Don't use* means prefer never. Reporting an *avoid* as though it were
a *don't use* makes a review feel arbitrary, which is how authors learn to ignore
style feedback.

When you're unsure whether a rule exists, say so rather than asserting it. An
invented rule delivered confidently costs more than an admitted gap.

## Output

Markdown by default. Produce a file when the doc is a deliverable the user will commit
or publish; answer inline when they're asking a style question or want a short passage
fixed. Match the surrounding doc set's conventions when editing into an existing repo.

---

Guidance adapted from the Google developer documentation style guide, used under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Not affiliated with or
endorsed by Google.
