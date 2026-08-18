# Word list

## Scope and provenance

This file records entries **verified against the source word list** at
https://developers.google.com/style/word-list.

Two things to know before relying on it:

1. **It is a subset.** The canonical list has hundreds of entries and is updated
   frequently. Coverage here is strongest for terms in the earlier part of the
   alphabet plus cross-cutting items drawn from other pages of the guide. For any
   term not listed here, look it up at the source rather than inferring — the
   guide's rulings are often more specific and less intuitive than they look
   (for example, `frontend` is closed but `file system` is open).
2. **When the term isn't in the guide at all**, the guide's own fallback applies:
   use Merriam-Webster, and where an entry lists several spellings, take the first.
   That's how *canceled* beats *cancelled*.

## How the guide grades its warnings

The source distinguishes two strengths, and the difference matters when you're
deciding whether to flag something in a review:

- **Avoid / use with caution** — prefer something else *when possible*. The term
  may be ambiguous or obscure. You can still use it if it's the clearest option;
  define it on first use.
- **Don't use** — prefer never using it. Either it's badly ambiguous or it carries
  an offensive or non-inclusive association. If the term appears in code you're
  documenting, reference it only as the code item, in code font, and switch to the
  preferred term in prose thereafter.

Some entries apply only to Android, Google Cloud, or Google Workspace
documentation. Android in particular **inverts** some general rules — see
[version ranges](#version-ranges).

## Contents

- [Non-inclusive terms](#non-inclusive-terms)
- [Ableist and figurative language](#ableist-and-figurative-language)
- [Gendered language](#gendered-language)
- [Modal verbs](#modal-verbs)
- [Version ranges](#version-ranges)
- [Words that date a document](#words-that-date-a-document)
- [Plain language and precision](#plain-language-and-precision)
- [Commonly confused pairs](#commonly-confused-pairs)
- [UI interaction verbs](#ui-interaction-verbs)
- [Spelling and compound forms](#spelling-and-compound-forms)
- [Irregular plurals](#irregular-plurals)
- [Abbreviations and naming](#abbreviations-and-naming)

## Non-inclusive terms

| Don't use | Use instead |
| --- | --- |
| blacklist (noun) | denylist, excludelist, blocklist |
| whitelist (noun) | allowlist, trustlist, safelist |
| graylist / greylist | provisional list |
| blacklist / whitelist / denylist / allowlist as **verbs** | rewrite the action: "To deny requests from an IP address, add it to `dos.yaml`" |
| master | primary, main, original, parent, initiator, driver, controller, manager, mixer, aggregator, publisher, leader, active. Use with caution; **never** alongside *slave* |
| slave | worker, replica, secondary, responder, subscriber, follower, standby |
| grandfathered, grandfather clause | legacy, exempt, made an exception |
| blackhat, blackhole, blast radius | name the actual violation; *dropped without notification*; *affected area* |
| black-box (testing) | opaque-box testing; for monitoring, *synthetic monitoring* |
| gray-box (testing) | describe what it does; if a term is needed, *translucent-box testing* |
| grayed-out | unavailable |
| first class, first-class citizen | higher-order, anonymous, nested, or describe the actual capability |
| demilitarized zone (DMZ) | perimeter network |
| break-glass | emergency access, manual fallback, preplanned procedure |
| brown bag | learning session, lunch and learn, informal training |
| build cop, build sheriff | build monitor |
| dojo | training, workshop |
| ghetto | clumsy, workaround, inelegant |
| final solution | solution, definitive, optimal, best, last |
| mom test, grandmother test, girlfriend test | beginner user test, novice user test |
| monkey (of people), monkey test | name the function: *automated, random tests* |
| ninja, guru, sherpa | expert, specialist, teacher, guide |
| gypsy | Romani, Roma, Traveller, as appropriate |
| reservation ("off the") | — |
| RTFM | "For more information, see …" |
| pets versus cattle | persistent versus dynamic; manually configured versus automated |
| STONITH / STOMITH | describe the feature |
| Black Friday, Cyber Monday, "the holidays" | peak scale event; specific quarters or months |
| sexy | fast, powerful, elegant |
| native (of people) | — |
| native (of software) | built-in, platform-specific |
| primitive (disparagingly) | use with caution |
| preferred pronouns | pronouns |

**Note on the master/slave pair:** the source calls *master* "use with caution" but
*slave* "don't use," and prohibits the pair in any context. Common paired
replacements: primary/secondary, primary/replica, original/replica,
controller/worker, initiator/responder, publisher/subscriber, leader/follower,
active/standby.

## Ableist and figurative language

| Don't use | Use instead |
| --- | --- |
| crazy, insane, bonkers, mad, lunatic, loony | complicated, complex, baffling, strange, unexpected — and only for inanimate things |
| sane | valid, sensible |
| sanity check | quick check, confidence check, preliminary check, coherence check |
| cripple | precise language: "it slowed the server down" |
| lame, gimp, gimpy | precise, non-figurative description of the deficiency |
| retarded | slowed |
| dumb down | simplify, remove technical jargon |
| blind to, blind eye to | ignore, unaware of, disregard, avoid, reject |
| blind writes | a write operation without a read operation |
| blind change | change without first confirming the value |
| abnormal, deficient, deformed (of a **person**) | — (all three are OK for system conditions) |
| chubby, fat | unused, overextended; high-capacity, full-featured |
| hang, hung | stop responding, not responding |
| kill | stop, exit, cancel, end (exception: Linux signals) |
| abort | stop, exit, cancel, end (exception: the Linux signal) |
| nuke | remove; or *attack*, as in denial-of-service attack |
| housekeeping | maintenance, cleanup |
| slice and dice | segment data for analysis; break information into smaller parts |
| single pane of glass | single interface, unified interface |
| shift left | shift earlier, move to an earlier phase (OK for binary operations) |
| spin up | create, start (OK for a hard disk) |
| hands off / hands on | automated; customizable |
| out of the box, outside the box (figurative) | — (OK literally) |
| jank, janky | only for a graphics glitch from data loss or refresh rate |
| health check, healthy | use only if it's the literal UI term; prefer *responsive* |
| postmortem | retrospective (exception: *blameless postmortem* in DR and DevOps) |

For people, the source recommends specific rather than euphemistic terms: *person
who is blind*, *screen reader user*, *person with a motor disability*, *wheelchair
user*, *person with limited mobility*.

## Gendered language

| Avoid | Use instead |
| --- | --- |
| he, she, him, her, his, hers (generic) | singular *they*, *their* |
| he/she, (s)he, gender-neutral *he* | singular *they* |
| guys, you guys | everyone, folks |
| man hours, manhours | person hours |
| manpower | staff, workforce |
| manmade | artificial, manufactured, synthetic |
| manned | staffed, crewed |
| man-in-the-middle (MITM) | on-path attacker, person-in-the-middle (PITM) |
| female adapter | socket |
| male adapter | plug |

## Modal verbs

This set is easy to get wrong and the guide is specific:

| Verb | Use |
| --- | --- |
| **can** | ability, permission, an optional action, a possible outcome |
| **might** | possibility or an uncertain outcome |
| **must** | a required action or state (*you need* also works) |
| **may** | reserve for official policy or legal considerations. For possibility use *can* or *might*; for permission use *can* |
| **could** | avoid; use *can* |
| **should** | generally avoid — it's ambiguous by definition |
| **shall** | avoid except on legal advice |
| **would** | see the guide's recommendations wording |

For recommendations and requirements, the guide has a dedicated page on
prescriptive documentation word choice rather than relying on *should*.

## Version ranges

The general rule uses temporal words, not spatial ones:

- **later**, not *higher*, *newer*, or *2.2+* — "Use version 2.2 or later."
- **earlier**, not *lower*, *older*, or *below* — "versions earlier than 1.17.0."
- Always give a version number or release date as a reference point.
- The highest version number isn't necessarily the latest: 2.0.1 can ship after 3.0.

**Android documentation inverts this**: use *higher* and *lower* for version
ranges, not *later* and *earlier*. This is the clearest example of why
project-specific style outranks the general guide.

For document position, use *earlier* / *preceding* and *later* / *following* —
never *above*, *below*, *higher*, or *lower*.

## Words that date a document

All of these are flagged for timeless documentation, and several can also
prematurely disclose product strategy:

*currently*, *now*, *presently*, *at present*, *as of this writing*, *new*,
*newer*, *latest*, *old*, *older*, *soon*, *eventually*, *future*, *in the
future*, *does not yet*.

- "Windows isn't supported" — not "isn't currently supported."
- "The Google Cloud console doesn't support this IAM role" — not "does not yet support."
- *now* is acceptable when genuinely contrasting past and present across versions.
- *latest* is acceptable with a reference point: "The June 2021 release includes…"

## Plain language and precision

| Avoid | Use instead |
| --- | --- |
| utilize, leverage | use (or *build on*, *take advantage of*) |
| in order to | to (keep it only where it aids clarity or readability) |
| prior to, subsequent to | before, after |
| e.g. | for example, such as |
| i.e. | that is |
| etc., and so forth, and so on | rewrite: "problems such as instability or high latency." If you truly need one, use *etc.* with its period |
| and/or | rewrite (allowed only where space is tight, as in a table) |
| aka | also known as, or parentheses, or *or* |
| authN, authZ | authentication, authorization |
| repo | repository |
| regex | regular expression |
| k8s | Kubernetes |
| CLI (generic) | name the specific interface, e.g. *Google Cloud CLI* |
| comprise | consist of, contain, include |
| config (in prose) | configuration, configuring |
| execute | run, when the meaning is the same |
| access (verb) | see, edit, find, use, view |
| agnostic | platform-independent |
| allows you to, enables you to | lets you |
| desire, desired | want, need |
| impact (verb) | affect |
| performant | a precise term: *accurate*, *fast* |
| learnings | knowledge, things you learned |
| cons, pros | disadvantages, advantages |
| easy, easily, simple, simply, quick, quickly | delete — the meaning usually survives without them |
| just | usually delete. *just* is acceptable where it conveys that one option is simpler than another — preferred over *simply* in that case |
| anti-pattern | name the practice: "Avoid these five SQL errors" |
| off-the-shelf, COTS | ready-made, prebuilt, standard, default |
| scale (alone) | add magnitude and direction: *scales up*, *at a larger scale* |
| roll out | gradual, in stages, phases, progressive |
| possible / impossible (for ability) | you can / you can't |
| hit | click, press, type |
| exploit (meaning "use") | use — reserve *exploit* for the security sense |
| for instance | for example, like, such as (avoids collision with *instance*) |
| nonce | define on first use; in end-user docs, "a number used only once" |
| foo, bar, baz | a meaningful placeholder name |
| dummy variable (for a placeholder) | placeholder |
| NoOps | fully managed |
| per (outside rates) | *for each*, *according to*, *in response to*. Use *per* for rates: *requests per day* |

**please** — the guide is narrower than "never." Don't use it in the normal course
of explaining how to use a product, even for a difficult task, and never write
*please note*. It *is* appropriate when you're asking for something that
inconveniences the reader or benefits you: "If the issue persists, please contact
your account representative."

## Commonly confused pairs

| Pair | Guidance |
| --- | --- |
| since / because | *because* for causation. *since* is ambiguous — it can mean elapsed time |
| as / because | same; *as* can refer to passage of time |
| once / after | *after* for sequence |
| while / although | see the guide; *while* is ambiguous |
| between / among | *between* for two or more distinct things; *among* for members of a group or non-distinct things |
| each / all | *each* is individual, not collective. "a list of all the items," not "a list of each item" |
| deprecate / remove | *deprecated* means recommended against, not gone. Don't use it to mean removed, deleted, shut down, or turned down |
| authenticate / authorize | users *authenticate* their identity; client apps send *authorized* requests on an authenticated user's behalf. Use *against* as the preposition with *authenticate* |
| confidential / sensitive | *confidential* data is protected against unauthorized access; *sensitive* data is data whose release might be harmful |
| media type / MIME type / content type | prefer *media type*. *content type* is OK when referring to the `Content-Type` header. Don't use *MIME type* for media type |
| runtime / run time | *runtime* is the environment software runs in; *run time* is the moment during execution, as contrasted with compile time |
| data flow / dataflow | two words if *flow of data* substitutes; one word for stream processing and reactive programming |
| plain text / plaintext | *plain text* generally; *plaintext* in cryptography |
| dialog / dialogue | *dialog* for the UI element; *dialogue* only for people talking |
| directory / folder | *directory* in a command-line context, *folder* in a GUI context; match the tool if it picks one. Default to *directory* |
| fill in / fill out | *fill in* individual fields; *fill out* an entire form |
| limits / quota | be specific: *usage limit*, *service limit*. In Google Cloud contexts the standard term is *quota* |
| key pair / key-value pair | different things — a pair of keys vs. a variable-value pairing |
| review / read | *review* means read critically and comment; use *read* for reading something for the first time |
| element / tag | a tag marks the start or end of an element; don't call an element a tag |
| display | transitive only. "The area appears" or "is displayed" — not "the area displays" |
| persist | not a transitive verb. "To make the token persistent," not "to persist the token" |
| enter / type | *enter* for entering text generally; if pressing Enter matters, say so explicitly |
| about / on | "For more information **about** indexes," not "on indexes" |

## UI interaction verbs

| Action | Verb |
| --- | --- |
| Button, link, list item, radio button (mouse) | **click** — never *click on*. Hyphenate *right-click*, *double-click* |
| Android and touch targets | **tap** |
| Physical or capacitive button, key combination | **press** |
| Marking a checkbox, choosing from options, selecting text | **select** — not *check* |
| Clearing a checkbox | **clear** — not *uncheck* or *deselect* |
| Moving the pointer onto an element | **point to**; use **hold the pointer over** when the UI must react or duration matters. Never *hover* |
| Dragging | **drag** — not *click and drag* or *drag and drop*. *drag-and-drop* is OK as an adjective |
| Expanding a section | **expand** or *click to expand*; the element is an **expander arrow** |

Don't use *hamburger menu* or *kebab menu* — use the icon's `aria-label`, such as
**Menu** or **More**. Don't use *pop-up* or *popup*: a window asking for or
presenting information is a **dialog**; a menu rising from the interface is a
**menu**. Don't use *left-nav* or *right-nav*; use **navigation menu** for apps
and **content navigation menu** for docs. Don't use *disclosure triangle*.

Avoid *Copy and paste* — say what to enter, not how: "In the **Query** field, enter
the output from the previous step."

For keyboard commands, write `Control+S`, not *Ctl-S* or *Cmd-S*, and mention both
when your audience spans macOS and Windows or Linux: `Control+S` (`Command+S` on
macOS).

Avoid *Create a new …* — use *Create a …* unless you must distinguish from another
recently created item.

## Spelling and compound forms

Closed (one word):

`autohealing`, `autopopulate`, `autoscaling`, `autotagging`, `backend`,
`checkbox`, `codebase`, `codelab`, `colocate`, `datastore`, `data type`→ see open,
`ecommerce`, `email`, `endpoint`, `filename`, `frontend`, `hardcode`, `healthcare`,
`hostname`, `hotspot`, `inline`, `intercluster`, `lifecycle`, `livestream`,
`metafeed`, `metageneration`, `microservices`, `namespace`, `nonce`, `plugin`
(noun), `prebuilt`, `precapture`, `preemptible`, `prerecorded`, `presubmit`,
`runbook`, `screenshot`, `startup` (noun), `setup` (noun), `single most`.

Open (two words):

`ad hoc`, `bare metal`, `data center`, `data cleaning`, `data source`, `data type`,
`file system`, `home screen` (Android), `key ring`, `lock screen` (Android),
`name server`, `plain text`, `status bar`.

Hyphenated:

`big-endian`, `little-endian`, `blue-green`, `dead-letter queue`,
`distributed denial-of-service (DDoS)`, `double-tap`, `drop-down`, `error-prone`,
`key-value pair`, `multi-cluster`, `multi-region`, `multi-service`,
`multi-tenancy`, `non-key`, `on-premises`, `parent-child`, `pre-existing`,
`pre-shared key`, `read-only`, `sign-in` (noun), `single sign-on`.

Notable corrections to common habits:

| Correct | Not |
| --- | --- |
| frontend, backend | front end, front-end, back end, back-end |
| file system | filesystem |
| data center | datacenter |
| datastore | data store |
| data source | datasource |
| name server | nameserver |
| namespace | name space |
| filename | file name |
| healthcare | health care, health-care |
| fintech | FinTech, fin-tech — and write out *financial technology (fintech)* on first mention |
| ad tech | adtech, ad-tech — write out *advertising technology (ad tech)* first |
| on-premises | on prem, on premise, on-premise |
| pre-existing | preexisting |
| read-only | read only |
| runbook | run book |
| documentation set | doc set, docset |
| ecommerce | e-commerce |
| email | e-mail, Email |
| internet, base64, egress, ingress | Internet, Base64 (unless part of a formal name) |
| curl | cURL |
| HTTPS | HTTPs |
| IPsec | IPSec |
| NoSQL | No-SQL, No SQL |
| OAuth 2.0 | OAuth 2, OAuth2, Oauth |
| SHA-1 | SHA1 |
| N/A | NA — spell out *not available* or *not applicable* first |
| Markdown | markdown |
| ID | Id, id (except in string literals and enums) |
| AM, PM | a.m., p.m. — all caps, no periods, space before |
| A/B testing | A-B testing |
| Control+S | Ctl-S |
| RFC 2318 | RFC2318 |
| appendixes | appendices |

Verb/noun/adjective splits: `fail over` (v) / `failover` (n, adj) · `log in` (v) /
`login` (n, adj) — but *sign in* is generally better · `set up` (v) / `setup` (n) ·
`start up` (v) / `startup` (n) · `sign in` (v) / `sign-in` (n) — and *sign in to*,
never *sign into* · `plug in` (v) / `plug-in` (adj) / `plugin` (n) ·
`high availability` (n) / `high-availability` (adj) · `load balancing` (n) /
`load-balancing` (adj) · `clickthrough` (n) / `click through` (v).

*drop-down* is usually removable entirely — prefer *list* or *menu*, add
*drop-down* only to prevent ambiguity, and never use it as a standalone noun.

## Irregular plurals

Use *appendixes*, *indexes*, and *matrixes* rather than the Latin forms, unless
there's a domain reason (mathematical or financial) for *indices* or *matrices*.
*emoji* is both singular and plural. *data* is singular and a mass noun: "the data
is," "less data," not "the data are" or "fewer data."

## Abbreviations and naming

- Write out on first mention: *infrastructure as a service (IaaS)*, *platform as a
  service (PaaS)*, *software as a service (SaaS)*, *financial technology
  (fintech)*, *Domain Name System Security Extensions (DNSSEC)*,
  *Internationalized Domain Name (IDN)*, *Internet Key Exchange (IKE)*.
- No expansion needed: *AI*, *CPU*, *DevOps*, *IPsec*, *OS*, *REST* (don't expand
  *Representational State Transfer* — the expansion means nothing to newcomers).
- *AI* is fine unexpanded for most audiences. Write *generative AI* in sentence
  case, spelled out — not *gen AI* or *Gen AI*.
- Article choice follows pronunciation: *a SQL* ("sequel"), *an SAP* (letters),
  *a FHIR* ("fire").
- Don't use *Google* or *Googling* as a verb — *search with Google*.
- *don't use as a verb*: `ssh`, RDP, email, interface, screenshot, canary,
  redline, Google. Write "connect by using SSH," "connect using RDP," "send email,"
  "take a screenshot."
- Products: use the full official name first. *Google Cloud*, not *GCP*, *Cloud
  Platform*, or *Cloud*. *Google Cloud console* (lowercase *console*), and *the
  console* after first mention if no other console is in play. Don't use *dashboard*
  or *portal* to mean a console.
- Refer to your own text as *this document* — not *this page*, *this article*, or
  *this doc*. *this tutorial*, *this quickstart*, and *this codelab* are fine for
  those types.

---

*Provenance: guidance on this page is drawn from the Google developer documentation
style guide (CC BY 4.0) and reorganized for use as a skill. Where the source is
silent, this file says so. Canonical source: https://developers.google.com/style*
