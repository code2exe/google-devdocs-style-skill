# Language, grammar, and punctuation

## Contents

- [Person](#person)
- [Voice and tense](#voice-and-tense)
- [Sentence structure](#sentence-structure)
- [Paragraphs](#paragraphs)
- [Capitalization](#capitalization)
- [Abbreviations](#abbreviations)
- [Pronouns](#pronouns)
- [Contractions, possessives, plurals](#contractions-possessives-plurals)
- [Articles and prepositions](#articles-and-prepositions)
- [Punctuation](#punctuation)
- [Verbs in reference documentation](#verbs-in-reference-documentation)
- [Anthropomorphism](#anthropomorphism)
- [Timeless documentation](#timeless-documentation)
- [Excessive claims](#excessive-claims)
- [Third-party content](#third-party-content)

## Person

Second person. *You* means the reader.

Use *we* only for the organization publishing the doc, and only when the organization's
recommendation or decision is the point ("We recommend enabling audit logs"). Don't use
*we* for actions the reader takes — "we then create a cluster" hides who is acting.

Don't call the reader *the user* unless you mean a different person: the end user of the
software the reader is building. That distinction matters constantly in developer docs,
so keep it sharp.

Avoid *let's*.

## Voice and tense

**Active voice.** The subject performs the action. Passive voice hides the actor, which
in instructions is a defect, not a stylistic preference.

- Recommended: The scheduler retries the job.
- Not recommended: The job is retried.

Passive is acceptable when the actor is genuinely unknown or irrelevant, or when the
object is the real subject of the sentence.

**Present tense.** Documentation describes what the system does, not what it will do.

- Recommended: The request returns a `409` if the resource exists.
- Not recommended: The request will return a `409` if the resource exists.

Use future tense only for something that genuinely happens later in real time.

**Avoid the subjunctive and complex conditionals** where a simple form works. "If the
value is null, the call fails" beats "Should the value be null, the call would fail."

## Sentence structure

- Condition first, then instruction. "If the check fails, restart the service."
- Subject-verb-object. Keep the subject and verb near the start.
- One idea per sentence. If a sentence has three clauses, it's probably two sentences.
- Avoid strings of nouns as modifiers — never more than two. "A hybrid cloud-native
  DevSecOps pipeline" is unreadable; "a cloud-native DevSecOps pipeline in a hybrid
  environment" isn't.
- Put *only* immediately before the word it modifies. "Request only one token," not
  "Only request one token." If it's still ambiguous, rewrite.
- Avoid phrasal verbs when a single verb works: *use*, not *make use of*. Some phrasal
  verbs are the standard term and should stay: *set up*, *log in*, *sign in*, *back up*.
- Prefer positive constructions. Tell readers what they can do before what they can't.

## Paragraphs

- Three to five sentences is a good target. One-sentence paragraphs are fine when the
  point stands alone.
- Lead with the topic sentence. Readers scan; give them the point first.
- One topic per paragraph. If a paragraph needs "also" twice, split it.

## Capitalization

- Sentence case for headings, titles, table headers, list items, figure captions, and
  nav labels.
- Capitalize product and feature names exactly as the product does. Don't capitalize
  generic descriptions of features.
- Don't capitalize a word for emphasis or importance.
- Never use all caps for emphasis. All caps is for placeholders and constants only.
- Match the exact capitalization of code elements and UI labels, even when it looks odd
  mid-sentence.

## Abbreviations

- Spell out the term on first use, with the abbreviation in parentheses: virtual private
  cloud (VPC). Then use the abbreviation.
- Don't spell out abbreviations more familiar than their expansions (API, HTTP, URL,
  SQL, JSON).
- Don't create your own abbreviations for convenience.
- Don't use an abbreviation in a heading or title that you haven't defined yet on the
  page, unless it's universally known.
- Use *for example* and *that is* rather than *e.g.* and *i.e.* — the Latin forms are
  frequently mixed up. When *for example* introduces an example, follow it with a
  comma, and separate the example from the rest of the sentence with a dash, commas,
  or parentheses.
- Avoid *etc.*, *and so forth*, and *and so on* wherever possible. Rewrite to name
  the items or use *such as* to signal the list is partial. If you genuinely need one
  of them, use *etc.* — and always include its period, even before a comma.
- Don't add an apostrophe to pluralize an abbreviation: APIs, not API's.

## Pronouns

- Singular *they* is correct and preferred over *he or she* or *(s)he*.
- Keep relative pronouns — *that*, *which*, *who* — even when speech drops them.
  "The rules that you defined," not "the rules you defined."
- Never leave an antecedent ambiguous. If a sentence has two candidate nouns, use the
  noun instead of *it* or *this*.
- Don't start a sentence with bare *This* or *That* referring back to a whole previous
  sentence. Add the noun: "This behavior means..."

## Contractions, possessives, plurals

- Common contractions are encouraged: *don't*, *you're*, *it's*, *can't*. They make the
  tone conversational.
- Avoid uncommon or ambiguous contractions: *there'd*, *it'll*, *mustn't*, and anything
  that reads as a typo.
- Don't form a plural with `'s`.
- Don't make product, company, feature, or trademarked names plural or possessive.
- Don't use possessive forms with code elements. "The value of `token`," not
  "`token`'s value."

## Articles and prepositions

- Don't drop *the*, *a*, or *an* to save space. Missing articles are one of the most
  common sources of translation ambiguity.
- Choose *a* or *an* by the sound of the following word, including for abbreviations: an
  API, a URL, an SQL query (if you say "ess-cue-el"), a SQL query (if you say "sequel")
  — pick one and be consistent within the doc set.
- Don't stack prepositions. Rewrite instead.
- Ending a sentence with a preposition is fine when the alternative is contorted.

## Punctuation

- **Serial comma**, always: red, white, and blue.
- **Colons** introduce lists, procedures, and code blocks. Don't put a colon after a
  fragment that the following items complete. Capitalize after a colon only if what
  follows is a complete sentence.
- **Semicolons** are usually a sign the sentence should be two sentences. Use sparingly.
- **Em dashes** set off a break in thought — like this — with no surrounding spaces.
  Don't overuse them.
- **En dashes** are for ranges: pages 10–15. In prose, prefer *from 10 to 15*.
- **Hyphens** join compound modifiers before a noun (a well-known pattern), but not after
  (the pattern is well known). Don't hyphenate an *-ly* adverb.
- **Parentheses** for genuinely incidental information. If it matters, it isn't
  parenthetical.
- **Slashes** are ambiguous. Write *and*, *or*, or *and or* explicitly. Exceptions:
  established forms and paths.
- **Ellipses** only for truncated output or omitted text. Not for a trailing thought.
- **Periods** end every complete sentence, including in list items and table cells
  containing sentences. No period after a heading.
- **Quotation marks**: periods and commas inside; colons and semicolons outside; question
  marks depend on whether the question is part of the quote. Use straight quotes in code
  and curly quotes in prose if the toolchain supports it.
- No exclamation points except inside code where the language requires one.
- One space after a period, not two.

## Verbs in reference documentation

Reference entries describe behavior in a consistent, clipped, third-person form.

- Methods and functions: start with a third-person verb — "Returns the number of
  active sessions." Not "Return..." and not "This method returns..."
- Booleans: "Whether the resource is enabled," not "True if enabled."
- Parameters and fields: noun phrase — "The maximum number of retries." State the
  default and whether it's required.
- Classes and types: noun phrase — "A connection to a single database."
- Use the same verb for the same behavior across every entry. Reference docs are read by
  comparison, so inconsistency reads as a difference in behavior.
- Say what happens on error, and name the exception or status code.

## Anthropomorphism

Software doesn't have intent, perception, or feelings. Replace mental verbs with
mechanical ones:

| Avoid | Use |
| --- | --- |
| The API wants a token | The API requires a token |
| The parser sees the field | The parser reads the field |
| The service knows the schema | The service has the schema |
| The job thinks it finished | The job reports that it finished |
| The system is happy | The health check passes |

Also avoid *smart*, *intelligent*, and *understands* as descriptions of ordinary logic.

## Timeless documentation

Docs outlive the moment they're written. Remove anything that dates them:

- *currently*, *now*, *at the time of writing*, *recently*, *new*, *newest*, *soon*,
  *upcoming*, *in the near future*
- References to "the old console" or "the new UI"
- Relative dates ("last month") — use absolute ones
- Claims about competitors' current capabilities

Add to that list: *presently*, *at present*, *as of this writing*, *latest*, *old*,
*older*, *eventually*, *future*, and *does not yet*. Two get an exception — *now* is
fine when genuinely contrasting versions ("in versions earlier than 1.10 you could
use only the default, but now you can assign a custom value"), and *latest* is fine
with a reference point ("the June 2021 release includes the latest tools").

Version ranges are a common source of dated or spatial language. Use **later** and
**earlier**, never *higher*, *lower*, *newer*, *older*, or *2.2+*, and always anchor
to a version number or release date. Note that the highest version number isn't
necessarily the latest: 2.0.1 can ship after 3.0. Android documentation inverts this
and uses *higher* and *lower* — a reminder that project style outranks the guide.

Don't pre-announce unreleased features, dates, or deprecations that haven't been
publicly committed. If something is genuinely in preview, use the project's official
lifecycle label rather than inventing one.

## Excessive claims

Say what the system does under what conditions. Avoid absolutes and marketing
intensifiers: *seamless*, *effortless*, *simply*, *just*, *easy*, *any*, *all*, *never*,
*always*, *fully secure*, *bulletproof*, *zero-downtime*, *infinitely scalable*,
*guaranteed*. Where a guarantee genuinely exists, name it and cite the limit — "the API
retries up to three times," not "the API always succeeds."

Don't tell the reader something is easy. If it goes wrong for them, you've told them
they're the problem.

## Third-party content

- Don't restate third-party documentation; link to its canonical page so it stays
  correct.
- Don't include third-party code or content without checking its license.
- Attribute quoted material and keep quotations short.
- Follow trademark conventions: use the correct name and form, don't make trademarks
  possessive or plural, and don't use them as verbs.

---

*Provenance: guidance on this page is drawn from the Google developer documentation
style guide (CC BY 4.0) and reorganized for use as a skill. Where the source is
silent, this file says so. Canonical source: https://developers.google.com/style*
