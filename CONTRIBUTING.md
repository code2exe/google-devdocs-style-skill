# Contributing

## The one rule that matters

**Cite the source.** This repository paraphrases a specific published style guide, so a
change is either supported by that guide or it isn't. Include the source URL and the
entry anchor, for example
`https://developers.google.com/style/word-list#file-system`.

Opinions about good technical writing are welcome in issues but can't go into the skill
as though they were Google's guidance. That distinction is the whole value of the
project — see [ACCURACY.md](ACCURACY.md) for what happened when an earlier draft
blurred it.

If you want to add advice the source guide doesn't contain, it goes in a clearly
labeled section and gets listed in NOTICE under additions.

## Most useful contributions

1. **Verified word list entries from the later alphabet.** Coverage in
   `references/word-list.md` thins out past roughly the letter S. Adding verified
   entries with source anchors is the highest-value work available.
2. **Corrections.** If the skill contradicts the source, that's a bug. Include both
   what the skill says and what the source says.
3. **Filling a "not individually verified" area** in ACCURACY.md by reading the
   corresponding source page and correcting the skill against it. Move the row out of
   that section in the same PR.
4. **Worked examples.** Before/after pairs with each change mapped to a rule. Keep the
   example text original — don't paste in real docs you don't own.

## Not looking for

- Reproduced text from the source guide. Paraphrase. The license permits copying, but
  the skill's value is compression, and verbatim passages make it longer without making
  it better.
- Google-product-specific naming rules (Google Cloud, Android, Workspace) unless they
  illustrate a general principle. Most users of this skill aren't writing Google docs.
- Expanding SKILL.md past roughly 250 lines. It loads on every trigger. New material
  belongs in a reference file with a pointer from SKILL.md.
- Anything that makes the skill trigger on marketing copy or general prose.

## Checks

Run before opening a PR:

```bash
python3 scripts/validate.py
```

It verifies frontmatter, that every relative link in the skill resolves, and that
SKILL.md stays within its line budget. CI runs the same script.

## Style of the skill itself

The skill is documentation about documentation, so it should follow its own rules:
second person, active voice, present tense, sentence-case headings, conditions before
instructions. A PR that adds a rule while violating it will get a friendly nudge.

Explain *why* a rule exists where it isn't obvious. A model that understands the reason
applies the rule better in cases the rule didn't anticipate, and a human reviewer who
understands the reason argues with the author instead of ignoring the feedback.
