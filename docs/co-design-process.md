# Co-design process

The stated goal for this app is content **"co-designed with Inuit speakers and
educators."** That hasn't happened yet — everything shipped so far (vocabulary
selection, the folktale retellings, the new function taxonomy in
`data/phrases.json`) is a single developer's best-effort draft, built to be
concrete enough to react to, not to be final. This doc is the plan for closing
that gap. It is a process document, not a claim that review has occurred.

## Principle

**Nothing about us without us.** Concretely, that means:

- Community members review and can reject or change content — including
  content already shipped — not just rubber-stamp it.
- Attribution and consent are ongoing, not a one-time checkbox. Someone who
  contributes or reviews content can ask for changes or removal later.
- The dictionary source (Labrador Virtual Museum) and any speaker/educator
  contributor are credited by name where they consent to be.
- Sensitive material is flagged *before* asking for review, not discovered
  during it — see `docs/folktale-research.md`'s existing attribution-strength
  table and sensitivity flags (the Act 3 shamanic material and Act 1/2
  mistreatment themes are already marked as needing the highest scrutiny).

## Who

The project's existing docs already identify the natural first contacts,
because the folktale content already needed this review before any public
release:

- **Nunatsiavut Government** — the relevant governing body for Nunatsiavut
  content and language matters.
- **Torngâsok Cultural Centre / Illusuak Cultural Centre** — cultural review
  for the folktale retellings, art, and audio.
- **Labrador Virtual Museum** (the dictionary's publisher) — the vocabulary
  source; a natural first point of contact since they're already credited and
  may have views on how their dictionary is used pedagogically.
- **Educators** working in Nunatsiavut/Inuttut-medium or Inuttut-as-subject
  programs — for the A2 pedagogical side specifically (is the function
  taxonomy in `docs/a2-gap-analysis.md` the right shape? what do youth
  actually need day to day?).

This list is a starting point, not a confirmed partnership — none of these
contacts have been made yet as far as this repo's history shows.

## Outreach package (prepare before reaching out)

Don't ask an open-ended "what should we teach" — bring something concrete to
react to, so people can spend their time correcting rather than generating
from scratch:

1. A short walkthrough (video or live demo) of the current build.
2. The current vocabulary list (`data/nouns.json` + the new
   `data/phrases.json` scaffold), clearly labelled as auto-generated and
   unreviewed.
3. `docs/a2-gap-analysis.md` — what's missing and why, so the conversation
   can start at "is this the right set of gaps" rather than from zero.
4. The specific, scoped questions:
   - Is the vocabulary/function selection appropriate and correctly used?
   - Which folktale material (per `docs/folktale-research.md`'s sensitivity
     flags) should be softened further, reframed, or dropped entirely?
   - Should the game mechanic itself (folktale RPG) change, or does it fit?
   - Who should be credited, and how (name, community, organisation, or
     anonymised)?

## Review cycle

1. Reviewer feedback is captured verbatim (don't paraphrase corrections away).
2. Changes land as normal commits/data edits, each referencing what feedback
   prompted them — so there's a traceable history of "why does this say
   this," the same way `docs/folktale-research.md` already documents
   attribution strength per tale.
3. Data records that have been through review should carry that explicitly —
   e.g. a `reviewed: true` / `reviewed_by` / `review_date` convention added to
   the relevant JSON records (not yet implemented; a Phase 2 task once an
   actual review has happened, so the schema matches what real review
   feedback looks like rather than a guess).
4. Nothing marked `needs_speaker_review: true` (the entire current
   `data/phrases.json` scaffold) should be presented to end users as
   validated teaching content until it's been through this cycle.

## What's realistic right now

This is a solo/small-scale project, not a funded institutional one. Realistic
near-term steps:

- Keep every unreviewed assumption clearly labelled in-app and in docs (this
  is already the project's existing practice for art/audio — extend it to
  vocabulary/function content too).
- Reach out to the Labrador Virtual Museum first — lowest-friction, and
  they're already the credited data source.
- Treat any single response so far as **input from one perspective**, not
  community consensus — Nunatsiavut isn't a monolith, and one educator's or
  speaker's feedback doesn't stand in for the Nunatsiavut Government's or
  Torngâsok/Illusuak's formal review.
- Don't publish beyond a private/testing audience until at least one round of
  real review has happened on both the folktale content (already flagged as
  needed) and the new function-taxonomy vocabulary.
