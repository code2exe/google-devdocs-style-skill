# google-devdocs-style

An [Agent Skill](https://code.claude.com/docs/en/skills) that teaches Claude to write,
edit, and review developer documentation in the style of the
[Google developer documentation style guide](https://developers.google.com/style).

> **Unofficial.** This project is not affiliated with, endorsed by, or connected to
> Google LLC. It is an independent adaptation of a publicly available, CC BY 4.0
> licensed style guide. See [NOTICE](NOTICE).

## What it does

Ask Claude for a README, a runbook, an API reference, or a migration guide and you
generally get competent prose with LLM-default habits baked in: title-case headings,
"simply run the following command," passive constructions, `currently` sprinkled
through, "click here" links, and steps that tell you *what* before *where*.

This skill replaces those defaults with a specific, defensible house style, and gives
Claude a review mode that grades findings by severity instead of dumping a flat list
of nitpicks.

It covers voice and tone, second person, active voice, present tense, sentence-case
headings, procedures and numbered steps, lists and tables, code font versus bold
versus italics, placeholders, command-line syntax, UI interaction verbs, modal verbs,
inclusive and non-ableist word choice, timeless wording, and writing for a global
audience.

## What it deliberately doesn't do

- **Marketing copy, social posts, narrative essays.** Different goals. The skill says
  so in its own description so it stays out of the way.
- **Override your project's conventions.** The source guide puts project-specific
  style *above itself* in its reference hierarchy, and so does this skill. If your doc
  set already says "the Console" or "replica set," the skill defers and tells you it
  noticed rather than silently re-terming your docs.
- **Claim completeness.** The source guide is around fifty pages and updated
  frequently. [ACCURACY.md](ACCURACY.md) states exactly which parts have been verified
  against the source and which haven't.

## Install

### Claude Code

Personal (available in every project):

```bash
git clone https://github.com/YOUR_USERNAME/google-devdocs-style-skill.git
mkdir -p ~/.claude/skills
cp -r google-devdocs-style-skill/skills/google-devdocs-style ~/.claude/skills/
```

Project scope (versioned with your repo, so your whole team gets it on clone):

```bash
mkdir -p .claude/skills
cp -r /path/to/google-devdocs-style-skill/skills/google-devdocs-style .claude/skills/
```

Start a new session, then run `/skills` to confirm it loaded. Project scope is the
better default if you're not yet sure you want the skill firing everywhere.

Uninstall by deleting the folder. Disable temporarily by renaming it with a leading
underscore.

### claude.ai and Claude Desktop

Package the skill folder as a `.zip`, rename it to `.skill`, and upload it through the
skills interface. Or clone the repo and drag `skills/google-devdocs-style` in, if your
client supports folder upload.

### Other agents

The `SKILL.md` format is portable. Copy `skills/google-devdocs-style` into your
agent's skills directory — `.cursor/skills/` for Cursor, and the equivalent elsewhere.
Nothing in the skill depends on Claude-specific tooling.

## Structure

```
skills/google-devdocs-style/
├── SKILL.md                       # entry point: core rules, mode selection, pointers
├── references/
│   ├── procedures.md              # steps, sub-steps, commands, output, multi-path tasks
│   ├── formatting.md              # headings, lists, tables, notices, links, code, units
│   ├── language.md                # grammar, punctuation, tense, voice, timelessness
│   ├── word-list.md               # verified preferred terms and inclusive replacements
│   └── review-checklist.md        # eight-pass edit workflow with severity grading
└── examples/
    ├── procedure-rewrite.md       # before/after with every change mapped to a rule
    └── review-report.md           # what a well-shaped review looks like
```

The split is deliberate. Only `SKILL.md` (~200 lines) loads when the skill triggers;
the reference files load on demand. That keeps the context cost low for a skill that
fires often — which matters, because a documentation skill should fire on most
documentation work, not just when someone says "style guide."

## Usage

It triggers on its own for documentation work. To invoke it explicitly:

```
Review docs/deployment.md against the style guide.
Write a quickstart for the auth service.
Rewrite these steps in Google developer docs style.
```

For review work, ask for the severity-graded report — that's where the skill earns
its keep over generic "make this better" editing.

## Contributing

Corrections with a source URL are the most valuable contribution, especially verified
word list entries from the later alphabet. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[CC BY 4.0](LICENSE), matching the source guide. Attribution and the full list of
changes made to the original are in [NOTICE](NOTICE).
