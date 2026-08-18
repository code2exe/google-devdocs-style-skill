# google-devdocs-style

An [Agent Skill](https://code.claude.com/docs/en/skills) that teaches a coding agent to
write, edit, and review developer documentation in the style of the
[Google developer documentation style guide](https://developers.google.com/style).

> **Unofficial.** This project is not affiliated with, endorsed by, or connected to
> Google LLC. It is an independent adaptation of a publicly available, CC BY 4.0
> licensed style guide. See [NOTICE](NOTICE).

## What it does

Ask an agent for a README, a runbook, an API reference, or a migration guide and you
generally get competent prose with LLM-default habits baked in: title-case headings,
"simply run the following command," passive constructions, `currently` sprinkled
through, "click here" links, and steps that tell you *what* before *where*.

This skill replaces those defaults with a specific, defensible house style, and adds a
review mode that grades findings by severity instead of dumping a flat list
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

Nothing in this skill is Claude-specific: it's plain Markdown with `name` and
`description` frontmatter, no scripts, and no tool dependencies. Any agent that reads
the `SKILL.md` format can use it.

### Any agent (recommended)

The open [skills CLI](https://skills.sh) installs into whichever agents you target and
knows the right directory for each:

```bash
# Project scope (default) — travels with the repo
npx skills@latest add code2exe/google-devdocs-style-skill

# Pick specific agents
npx skills@latest add code2exe/google-devdocs-style-skill -a claude-code -a cursor

# Global — available across all your projects
npx skills@latest add code2exe/google-devdocs-style-skill -g
```

Housekeeping: `npx skills list`, `npx skills check`, `npx skills update`,
`npx skills remove google-devdocs-style`.

Pin `@latest` — older CLI versions don't create the Claude Code link, so the skill
installs but never appears. Flag names have shifted between releases; if `-a` is
rejected, run `npx skills add --help`.

### Manual install

Clone, then copy `skills/google-devdocs-style` into your agent's skills directory:

| Agent | Directory |
| --- | --- |
| Claude Code | `~/.claude/skills/` (personal) or `.claude/skills/` (project) |
| Codex CLI | `~/.codex/skills/`; also reads `.agents/skills/` directly |
| Cursor | `.cursor/skills/` |
| Gemini CLI, Copilot, OpenCode, Windsurf | supported by the CLI — let it place the files |
| Antigravity | copy into its own customizations folder; it doesn't read the shared agents folder |

```bash
git clone https://github.com/code2exe/google-devdocs-style-skill.git
mkdir -p ~/.claude/skills
cp -r google-devdocs-style-skill/skills/google-devdocs-style ~/.claude/skills/
```

Start a new session afterward. In Claude Code, `/skills` confirms it loaded. Uninstall
by deleting the folder; disable temporarily by renaming it with a leading underscore.

Project scope is the better default if you're not yet sure you want the skill firing
everywhere — it's versioned and reviewable alongside the code it describes.

### claude.ai and Claude Desktop

Zip the `skills/google-devdocs-style` folder, rename it to `.skill`, and upload it
through the skills interface.

### A portability caveat worth knowing

This skill is built around progressive disclosure: `SKILL.md` is a ~210-line summary
that points to reference files the agent loads **only when it needs them**. That keeps
the context cost low for a skill designed to trigger on most documentation work.

Claude Code and Codex both load bundled files on demand, so they get the full ~1,400
lines of guidance as needed. Some hosts read only `SKILL.md` and ignore the rest of the
folder. On those, the skill still works but runs shallow — you get the core rules and
lose the word list, the review checklist, and the examples, with no error explaining
why.

If your agent behaves that way, ask it directly: *"Read
references/word-list.md and tell me the preferred form of 'front end'."* If it can't,
it isn't loading the references, and you'll want to paste the relevant file in
manually for detailed work.

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
