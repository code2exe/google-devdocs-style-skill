# Accuracy and verification status

This skill paraphrases a large, frequently-updated style guide. Being straight about
what has been checked matters more than looking complete — a confidently stated
invented rule is worse than an admitted gap, because it makes every other rule in the
skill less trustworthy.

## Verified against the source

These pages of the source guide were read directly, and guidance drawn from them is
verified:

| Source page | Used in |
| --- | --- |
| [About this guide](https://developers.google.com/style) | Reference hierarchy, "break the rules" |
| [Highlights](https://developers.google.com/style/highlights) | The core rules |
| [Text-formatting summary](https://developers.google.com/style/text-formatting) | `references/formatting.md` |
| [Procedures](https://developers.google.com/style/procedures) | `references/procedures.md` |
| [Write for a global audience](https://developers.google.com/style/translation) | Global audience sections |
| [Word list](https://developers.google.com/style/word-list) | `references/word-list.md` |

## Partially verified

**The word list.** The source list runs to hundreds of entries. Coverage in
`references/word-list.md` is strongest for terms in the earlier part of the alphabet;
terms later in the alphabet are thinner. The file says so, and instructs looking terms
up at the source rather than inferring. If you contribute, adding verified entries
from the later alphabet is the single most useful thing you can do — see
[CONTRIBUTING.md](CONTRIBUTING.md).

## Not individually verified

Guidance in these areas is consistent with the source guide's stated principles but
was assembled from general technical-writing convention rather than read off the
specific source page. It is likely correct and possibly less specific than the source:

- Headings and titles beyond sentence case
- Lists, tables, and notices (notice *type names* are explicitly flagged as
  platform-specific in the skill, because they vary)
- Cross-references and link text beyond "descriptive, not 'click here'"
- Code samples, command-line syntax, and placeholder formatting details
- Numbers, dates, times, and units of measurement
- Images, figures, and alt text
- Accessibility specifics
- Punctuation beyond the serial comma and dash conventions
- Reference-documentation verb forms
- Abbreviations, pronouns, possessives, plurals, articles, prepositions

If you rely on any of these for a decision that matters, check the corresponding page
in the [source guide](https://developers.google.com/style) — the left navigation maps
almost one-to-one onto the list above.

## Known corrections already made

Recording these because they show the failure mode this file exists to prevent. An
earlier draft asserted, from recall rather than the source:

| Claimed | Actually |
| --- | --- |
| `front end` / `back end` open as nouns | `frontend` and `backend`, always closed |
| `filesystem` closed | `file system`, open |
| Spell out *CLI* on first use | Don't use *CLI* generically; name the specific interface |
| Prefer *repository* over *repo* in prose | Don't use *repo* at all |
| Never use *please* | Don't use it in ordinary instructions, but do when asking something that inconveniences the reader |
| Never use *etc.* | Avoid it, but if you need one of *etc.* / *and so on* / *and so forth*, use *etc.* |
| *dropdown* or *drop-down*, either | `drop-down`, usually omitted entirely, never a standalone noun |
| *comprise* usable with care | Don't use; use *consist of*, *contain*, or *include* |

An earlier draft also invented entries the source does not contain — *chaos monkey*,
*red team*, *dark pattern*, *tribal knowledge*, *Rube Goldberg* — which have been
removed. Some may be reasonable advice; they are not this style guide's advice, and
presenting them as such was the error.

## How to report an inaccuracy

Open an issue with the source URL and the anchor for the specific entry. Source
citations beat opinion — see [CONTRIBUTING.md](CONTRIBUTING.md).
