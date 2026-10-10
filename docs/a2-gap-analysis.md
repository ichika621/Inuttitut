# CEFR A2 gap analysis

Purpose: figure out, concretely, what stands between the current build (an
absolute-beginner, nouns-only folktale game) and the new goal — helping
Nunatsiavut youth who already know some Inuttut **strengthen everyday use**,
toward roughly **CEFR A2**. This is Phase 0/1 groundwork; it doesn't decide
final lesson content (that needs speaker/educator input — see
[`co-design-process.md`](co-design-process.md)), it maps the shape of what's
missing so that input has something concrete to react to.

## What "A2" actually asks for

CEFR A2 ("Waystage") is not "more vocabulary." Its can-do statements are about
**handling routine, everyday exchanges** on familiar topics:

- Understand and use frequently-used everyday expressions and very basic
  phrases (personal/family info, shopping, local geography, employment).
- Communicate in simple, routine tasks requiring a direct exchange of
  information on familiar, routine matters.
- Describe, in simple terms, aspects of your background, immediate
  environment, and matters of immediate need.

None of that is satisfiable by isolated noun flashcards, however many of
them. It requires **verbs, question forms, requests, feelings, and short
functional exchanges** — i.e. language *used for something*, not language
*labelled*.

## Current content inventory

| What | Status |
|---|---|
| Taught vocabulary | 27 nouns total across 4 acts (see README Step 3) |
| Part of speech surfaced to the learner | Nouns only — verbs exist in the dictionary (436 `v.` entries) but are never taught, tapped, or tested |
| Exercise types | Pick-the-picture, noun multiple-choice, matching, noun-ordering (battles) |
| Functional coverage | None explicit — greetings/requests/feelings are theme tags on nouns.json's sibling `dictionary.json`, but the *game* never surfaces them as things to learn |
| Review mechanism | A queue that re-shows a missed word ~2 answers later (not a real spaced-repetition schedule) |

So the honest gap isn't "wrong vocabulary," it's **wrong grammatical/functional
shape of content entirely** — the app currently can't teach "I'm tired," "can
you help me," or "where are you going," because it only ever teaches single
nouns in isolation.

## Function taxonomy (the new axis)

`scripts/build_phrases.py` (Step 3c) tags everyday-function vocabulary along a
category axis chosen to line up with A2 topic areas, separate from the
existing `theme` axis (which is about subject matter — animals, weather —
not communicative function):

| Function category | A2 relevance | Scaffold count (`data/phrases.json`) |
|---|---|---|
| `actions_general` | core everyday verbs (do, make, catch, agree…) | 305 |
| `place_direction` | come/go/here/there/arrive/leave — describing movement & location | 48 |
| `needs_requests` | want/need/help/ask/borrow — asking for things | 28 |
| `daily_routine` | wake/sleep/wash/dress/clean/play | 25 |
| `feelings_health` | happy/sad/tired/sick/afraid — describing state | 25 |
| `land_activities` | hunt/fish/paddle/travel/carry — land-based everyday life | 24 |
| `time_weather` | today/tomorrow/cold/warm/snow/wind | 13 |
| `food_meals` | eat/drink/cook/meal | 10 |
| `greetings_social` | yes/no/sorry/thank you/meet | 10 |
| `personal_info` | name/home/born/work | 3 |

**Read the thin rows correctly.** `personal_info` has 3 entries not because
that topic doesn't matter for A2 (it's arguably the *most* important — "what's
your name," "where do you live" are the canonical A2 opener) but because the
dictionary is a **word list**, not a phrasebook: single-word dictionary
entries can give you the noun `Home` or the verb `Live`, but "My name is
Elisapee" or "Where do you live?" is a *constructed sentence* — that requires
a fluent speaker to write correctly (Inuttut is polysynthetic; you can't
assemble it by pasting English word order onto dictionary citation forms).
`greetings_social` is similarly thin because most real greeting *exchanges*
("how are you" → response) are conversational units, not single dictionary
words.

**Read this as: the scaffold covers single-word vocabulary reasonably well;
it does not and cannot cover phrase/sentence-level content.** That's the
biggest single item for Phase 3 co-design — not more scripting, but speaker-
authored dialogue lines for the functions above.

## Priority recommendation for Phase 2/3

Roughly in order of A2 payoff per unit of effort:

1. **`greetings_social` + `personal_info`** — smallest vocabulary footprint,
   highest conversational payoff (every A2 exam and every real interaction
   opens here). Needs speaker-authored short exchanges, not just words.
2. **`needs_requests` + `feelings_health`** — lets a learner actually ask for
   help or say how they are, which is the core "use it more in daily life"
   ask behind this whole redesign.
3. **`daily_routine` + `food_meals`** — good fit for the existing
   visual-novel format (a character's day), reuses the "conversation with
   inline word-tap" mechanic already built.
4. **`place_direction` + `time_weather`** — natural fit with the existing
   land/season theming already in the folktale acts; lower urgency since the
   current noun set already touches weather/nature vocabulary.
5. **`land_activities`** — culturally rich and already thematically present
   in Acts 2–3, but more specialised; good material for the "culture card"
   side rather than core drilling.

## What this doc does *not* do

It does not decide final copy, does not invent any Inuttut phrases, and does
not commit to a mechanic (that's Phase 2). It exists so that when speakers and
educators are approached (see `co-design-process.md`), there's a concrete
"here's what we think is missing and why" instead of an open-ended "what
should we teach."
