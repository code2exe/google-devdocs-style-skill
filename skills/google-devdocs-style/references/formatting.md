# Formatting and organization

## Contents

- [Text formatting](#text-formatting)
- [Headings and titles](#headings-and-titles)
- [Lists](#lists)
- [Tables](#tables)
- [Notices](#notices)
- [Links and cross-references](#links-and-cross-references)
- [Code in text](#code-in-text)
- [Code samples](#code-samples)
- [Command-line syntax](#command-line-syntax)
- [Placeholders](#placeholders)
- [UI elements](#ui-elements)
- [Numbers, dates, and units](#numbers-dates-and-units)
- [Images and figures](#images-and-figures)
- [Markdown vs. HTML](#markdown-vs-html)

## Text formatting

**Bold** (`**` in Markdown, `<b>` in HTML) is only for UI elements, run-in headings,
and the label at the start of a notice. Prefer `**` over `__` — it's easier to see in
a text editor.

*Italics* (`_` in Markdown, `<i>` or `<em>` in HTML) is for:

- Terms being introduced or defined
- Words used as words ("the term *idempotent*")
- Emphasis, when the sentence can't carry it alone — which is rare
- Titles of full-length works (books, films, series), unless the title is link text
- Mathematical variables (*x* + *y* = 3) but not operators
- Version variables (version 1.4.*x*)

Prefer `_` over `*` for italics so bold and italics stay visually distinct in source.
Use `<em>` in HTML when the emphasis is semantic; Markdown can't express that.

Underline is for link text only.

`Code font` (backticks, or `<code>`) covers inline code, user input, filenames, paths,
class and method and variable names, HTTP status codes, console output, and
placeholders.

Never override font family, size, or color inline. Use semantic markup and let the
site's stylesheet decide.

Titles of shorter works — articles, blog posts, episodes — go in quotation marks unless
they're link text.

Use American English punctuation conventions for quotation marks. Put quotation marks
and terminal punctuation outside of link text.

Don't use `&` for *and*, including in headings and nav. The exception is naming a UI
element or menu that literally contains `&`.

## Headings and titles

- Sentence case, always. Capitalize the first word and proper nouns only.
- Task-oriented headings use a gerund or imperative: "Configuring the proxy" or
  "Configure the proxy." Be consistent within a doc set.
- Don't skip heading levels.
- Keep headings unique within a page so anchors stay stable and link text stays clear.
- Don't put code font, links, or trailing punctuation in headings unless the code
  reference is genuinely necessary.
- Don't stack two headings with no text between them.
- Mark an optional section by adding *(Optional)* in the heading text.
- Once a heading is published, its anchor is a contract. Changing it breaks inbound
  links — if you must change it, leave a redirect or keep the old anchor.

## Lists

Three kinds, each with a job:

- **Numbered** — sequences and ranked items.
- **Bulleted** — everything else where order doesn't matter.
- **Description (definition) lists** — pairs of related data: term and its meaning,
  parameter and its description.

Rules:

- Introduce a list with a complete sentence ending in a colon. Not a fragment the items
  complete.
- Keep items parallel: all noun phrases, or all imperative clauses — not a mix.
- Capitalize the first word of each item.
- End each item with a period if any item is a complete sentence. If all items are short
  fragments, omit terminal punctuation — consistently within the list.
- Aim for two to nine items. One item isn't a list. More than nine suggests grouping or
  a table.
- Use a run-in bold lead-in when items have a name plus explanation: **Term** — the
  explanation.
- Avoid nesting more than two levels deep.
- Don't put an entire paragraph of prose inside a bullet when it belongs in body text.

## Tables

- Use tables for data with two or more dimensions, not for layout.
- Give every table a real header row, and a caption or introduction when the content
  isn't self-evident.
- Sentence case in headers. Keep cell content parallel.
- Left-align text; right-align numbers on the decimal.
- Don't leave cells empty — use an em dash or "Not applicable" so screen readers convey
  intent.
- If a table has only one column, it's a list.

## Notices

Order: label in bold, then the content. Keep them rare — a page of warnings trains
readers to skip all of them.

Which notice types exist is platform-specific, so match whatever your doc system and
doc set already use rather than inventing labels. Types in common use:

- **Note:** neutral, useful-to-know information.
- **Important:** information the reader needs to avoid a bad outcome.
- **Caution:** risk of data loss, cost, or a hard-to-undo change.
- **Warning:** risk of harm or security compromise.

Don't put a notice between a heading and its first paragraph, and don't put procedure
steps inside a notice.

## Links and cross-references

- Link text describes the destination. Use the page or section title where practical.
- Never "click here," "this link," "read more," or a bare URL as link text.
- Punctuation and quotation marks go outside the link.
- Introduce links with standardized phrasing: "For more information, see X." "To learn
  how to Y, see Z."
- When linking off-site, name the source so the reader knows they're leaving.
- Don't let a link's text depend on surrounding sentence context, since screen reader
  users may navigate by link list alone.

## Code in text

- Put code elements in code font, and add a qualifying noun: "the `example.yaml` file,"
  "the `Fetch` method," "the `retries` field."
- Don't pluralize or possessive-ize a code element: "the values of `item`," not
  "`item`'s values" or "`item`s."
- Don't start a sentence with a lowercase code element if you can avoid it — recast the
  sentence.
- Code font isn't emphasis. Don't use it for product names or ordinary nouns.

## Code samples

- Introduce every sample with a sentence saying what it does, ending in a colon.
- Samples must be complete enough to run, or explicitly marked as a fragment.
- No real credentials, keys, tokens, account IDs, or internal hostnames.
- Use the reserved example domains (`example.com`, `example.org`, `example.net`) and
  RFC 5737 documentation IP ranges (`192.0.2.0/24`, `198.51.100.0/24`,
  `203.0.113.0/24`).
- Wrap long lines rather than forcing horizontal scroll.
- Label the language on the fence so syntax highlighting works.
- Explain what the reader should notice in the sample; don't leave interpretation to
  them.

## Command-line syntax

- Show one command per code block when the reader must inspect output between commands.
- Don't include the shell prompt (`$`, `>`) in copyable commands — it breaks
  copy-paste.
- Show output in a separate block, introduced with "The output is similar to the
  following:" — and say what the reader should look for.
- Truncate long output with an ellipsis rather than pasting hundreds of lines.
- In syntax specifications: put optional elements in square brackets, group alternatives
  in braces separated by pipes, and mark repeatable elements with an ellipsis.

## Placeholders

- Uppercase, code font: `PROJECT_ID`, `REGION`, `CLUSTER_NAME`.
- Use underscores between words, and no spaces.
- Explain every placeholder immediately after the command, in the order it appears:
  "Replace `PROJECT_ID` with your Google Cloud project ID."
- Use the same placeholder name for the same value across the whole document.
- Don't use angle brackets around placeholders — readers type them literally.

## UI elements

- Element labels in bold, matching the label's own capitalization exactly.
- Use the interaction verb the element actually takes: *click* a button or link,
  *select* a checkbox or menu item, *enter* text, *go to* a page.
- Chain menu selections with angle brackets: **Settings > Privacy > Cookies**.
- Refer to elements by label, not by position, shape, or color.
- Name the icon and include it if the doc system supports it; otherwise use the icon's
  accessible label.
- Don't say "the Save button button" — one noun is enough: "click **Save**."

## Numbers, dates, and units

- Spell out zero through nine in prose; use numerals for 10 and up. Always use numerals
  for measurements, versions, percentages, and anything in a table or UI.
- Don't start a sentence with a numeral — recast it.
- Use commas as thousands separators in prose (1,000), and be aware they're not
  universal.
- Dates: *January 4, 2026* or ISO 8601 *2026-01-04*. Never *1/4/26*.
- Times: include the time zone, and prefer UTC for anything technical.
- Don't use seasons as time markers. Use months, quarters, or dates.
- Put a space between a number and its unit (100 MB), except for percent and degrees
  (50%, 20°C).
- Use standard unit abbreviations, and spell out the unit on first use if it's obscure.

## Images and figures

- Every meaningful image needs alt text that conveys the information, not a
  description of the picture. Decorative images get empty alt text.
- Never put information only in an image — images aren't translated, indexed, or read
  aloud.
- Provide high-resolution or vector images where practical.
- Number and caption figures when the doc refers back to them, and refer to them as
  "the preceding figure" / "the following figure," not "above" / "below."
- Screenshots go stale fast. Use them only when a UI element is genuinely hard to find,
  and crop tightly.

## Markdown vs. HTML

Prefer Markdown for prose docs — it's readable in source and diffs cleanly. Reach for
HTML only when you need something Markdown can't express: semantic emphasis, complex
tables, definition lists, or accessibility attributes. When you do use HTML, use
semantic elements (`<em>`, `<strong>`, `<code>`, `<th>`) rather than presentational ones.

---

*Provenance: guidance on this page is drawn from the Google developer documentation
style guide (CC BY 4.0) and reorganized for use as a skill. Where the source is
silent, this file says so. Canonical source: https://developers.google.com/style*
