# Curriculum roadmap — path to A2

Personal working document: concretely, what would this app teach, in what
order, to actually get someone from "knows some Inuttut" to "roughly A2"?
This is a design sketch grounded in the data that actually exists in this
repo (`data/nouns.json`, `data/phrases.json`) — not a finished syllabus, and
not something to publish to learners as-is. Treat every stage below as a
hypothesis to be corrected in the co-design process
([`co-design-process.md`](co-design-process.md)), not a committed plan.

## How to read this

Three honesty constraints shape everything below:

1. **Word counts are real**, pulled directly from the current data files
   (queried 2026-08-13). Nothing here is a round-number guess.
2. **Grammar content is deliberately thin and heavily caveated.** This repo
   has a *dictionary* (word list), not a grammar reference. Inuit languages
   are polysynthetic — a single word can carry what an English sentence
   needs a dozen words for — and Labrador Inuttut's specific inflectional
   patterns aren't documented anywhere in this project. Anywhere this doc
   says something grammar-shaped, it's a **placeholder flagged for a real
   grammar source or speaker**, not a rule to implement.
3. **"Buildable now" vs "needs speaker content"** is marked per stage. A lot
   of this roadmap cannot be built from the dictionary alone — CEFR A2 is
   fundamentally about *using* language in exchanges, and exchanges have to
   be authored by someone who actually speaks Inuttut.

## CEFR sub-stages used here

CEFR's A1/A2 are broad; for a word-by-word roadmap it helps to split each
into two:

| Stage | Roughly | Can-do shape |
|---|---|---|
| **A1.1** | absolute basics | recognise/produce isolated words & fixed formulas (hi, thanks, yes/no) |
| **A1.2** | elementary | name people/things/self, short fixed exchanges |
| **A2.1** | pre-intermediate | simple sentences about daily life, ask/answer routine questions |
| **A2.2** | intermediate waystage | connect a few sentences, handle short everyday transactions |

This app's current shipped content (27 nouns, no sentence production) sits
below A1.1 — it's vocabulary recognition, not "use." Everything below is
about closing that specific gap.

## The roadmap

| # | Stage | CEFR | Source | Available pool | Status |
|---|---|---|---|---|---|
| 0 | *(shipped)* Folktale noun core | pre-A1 | `nouns.json` (curated 27) | 2983 nouns total | ✅ built |
| 1 | Greetings & social formulas | A1.1 | `phrases.json` `greetings_social` | 10 | ✅ words scaffolded / ❌ exchanges need authoring |
| 2 | Naming people & self | A1.1–A1.2 | `nouns.json` `family` (51) + `phrases.json` `personal_info` (3) | 54 | ⚠️ thin — needs authored phrases |
| 3 | Daily routine & needs | A1.2–A2.1 | `phrases.json` `daily_routine` (25) + `needs_requests` (28) | 53 | ✅ words / ❌ sentences |
| 4 | Feelings & simple health | A2.1 | `phrases.json` `feelings_health` (25) | 25 | ✅ words / ❌ sentences |
| 5 | Food & meals | A1.2–A2.1 | `nouns.json` `food` (42) + `phrases.json` `food_meals` (10) | 52 | ✅ words / ❌ sentences |
| 6 | Time & weather | A2.1 | `nouns.json` `weather` (73) + `phrases.json` `time_weather` (13) | 86 | ✅ words / ❌ sentences |
| 7 | Place, direction & land life | A2.1–A2.2 | `phrases.json` `place_direction` (48) + `land_activities` (24) + `nouns.json` `hunting_tools` (80) | 152 | ✅ words / ❌ sentences |
| 8 | Body & everyday description | A2.2 | `nouns.json` `body` (123) + `phrases.json` `actions_general` (305, needs curation) | large | ⚠️ `actions_general` is a dumping-ground tag, needs manual sub-sorting first |
| 9 | Integration — folktale acts as immersion | A2.2 | existing Acts 1–4, re-authored to *use* stages 1–8's vocabulary in context instead of teaching isolated nouns | — | ❌ requires rewriting story beats |

Stage numbers are a **teaching order**, not act numbers — the existing Acts
1–4 don't need to be renumbered, but their *content* (which words get taught
in which scene) would be re-derived from this table rather than the current
"27 hand-picked simplest nouns" logic.

## Per-stage detail

### Stage 1 — Greetings & social formulas (A1.1)
- **Words (10):** yes, no, sorry, thank you, meet (×2 forms) — see
  `data/phrases.json` where `function == "greetings_social"`.
- **Can-do target:** recognise and produce a greeting exchange; say yes/no;
  thank someone; apologise.
- **Gap:** the actual *exchange* ("how are you" → response) isn't in the
  dictionary as single words — this needs 3–5 short authored dialogue
  snippets, not more vocabulary.
- **Mechanic fit:** drop-in replacement for the game's existing VN opening
  lines — lowest-effort integration of anything in this roadmap.

### Stage 2 — Naming people & self (A1.1–A1.2)
- **Words:** `family` theme nouns (51: mother, father, brother, sister,
  friend, grandchild…) + `personal_info` (3: born, home, work).
- **Can-do target:** introduce yourself, name family members, say where you
  live.
- **Gap — the thinnest stage in the whole roadmap.** "My name is ___," "I'm
  from ___," "This is my ___" are constructed sentences; the dictionary gives
  isolated words only. This is the single highest-value thing to bring to a
  speaker for authoring, since it's the canonical opener for basically any
  real conversation.

### Stage 3 — Daily routine & needs (A1.2–A2.1)
- **Words (53):** `daily_routine` (wake, sleep, wash, dress, sit, stand,
  walk, run, clean, play, rest — 25) + `needs_requests` (want, need, help,
  ask, give, take, borrow, buy… — 28).
- **Can-do target:** describe a simple daily routine; ask for something or
  for help.
- **Mechanic fit:** good match for a "day in the life" VN scene format,
  reusing the existing beat/expression system.

### Stage 4 — Feelings & simple health (A2.1)
- **Words (25):** happy, sad, tired, sick, hungry, thirsty, afraid, angry,
  hurt, pain, glad, love, feel, cry, laugh…
- **Can-do target:** say how you feel; recognise feeling-words in context.
- **Note:** pairs naturally with Stage 3 — "I'm tired" after "I woke up."

### Stage 5 — Food & meals (A1.2–A2.1)
- **Words (52):** `nouns.json` `food` theme (42: berry, egg, meat, blubber…)
  + `phrases.json` `food_meals` (eat, drink, cook, meal, breakfast…).
- **Can-do target:** talk about eating/drinking; name common foods.

### Stage 6 — Time & weather (A2.1)
- **Words (86):** `weather` nouns (73: snow, wind, storm, cold, fog…) +
  `time_weather` phrases (today, tomorrow, morning, winter, cold, warm…).
- **Can-do target:** say what the weather's like; talk about today/tomorrow,
  the season.
- **Note:** the existing folktale acts already lean heavily on weather/season
  imagery (long night, spring), so this stage has the most natural narrative
  overlap with content already built.

### Stage 7 — Place, direction & land life (A2.1–A2.2)
- **Words (152):** `place_direction` (here, there, come, go, arrive,
  leave… 48) + `land_activities` (hunt, fish, paddle, carry, travel… 24) +
  `hunting_tools` nouns (spear, boat, sled, net… 80).
- **Can-do target:** say where something/someone is; describe simple
  land-based activities.
- **Note:** culturally the richest stage — good candidate for tying into
  Culture Cards, not just drilling.

### Stage 8 — Body & everyday description (A2.2)
- **Words:** `body` nouns (123) are clean and ready. `actions_general` (305)
  is **not** — it's this taxonomy's catch-all bucket for any short verb gloss
  that didn't match a more specific category (see
  `docs/a2-gap-analysis.md`), so it mixes genuinely common verbs ("carry,"
  "ask") with obscure/specialised ones ("agree upon amongst themselves").
  **Before using it for teaching, it needs a manual pass** to split
  high-frequency verbs from specialised ones — not more scripting, human
  judgment on what's actually "everyday."

### Stage 9 — Integration (A2.2)
- Re-thread Acts 1–4's existing folktale scenes so their dialogue *uses*
  stage 1–8 vocabulary in context (a character says "I'm tired" in Stage-4
  vocabulary, not just narrates around it in English) instead of the current
  pattern of teaching an isolated noun per line.
- This is a rewrite of `data/story.json`'s beats, not new data collection —
  but every rewritten line needs the same speaker-review flag as everything
  else here.

## Grammar — what this roadmap does *not* claim

Vocabulary lists don't add up to A2 by themselves; A2 needs learners to
combine words into short sentences. This repo currently has **no
grammatical basis** for teaching that — no verb paradigm tables, no case/
possessive system documented, nothing dialect-verified. Two honest options,
not decided here:

1. **Speaker-authored model sentences** (recommended) — instead of teaching
   abstract rules, each stage above ships as a handful of real,
   speaker-confirmed example sentences using that stage's vocabulary, and
   the learner absorbs pattern by exposure (how the existing VN mechanic
   already works for single words — extend the same idea to short sentences).
   This sidesteps needing a formal grammar description at all.
2. **A real grammar reference** — if one becomes available (e.g. through the
   Labrador Virtual Museum, Nunatsiavut Government, or an educator contact),
   revisit this section with actual paradigms.

**Do not let anyone — including a future version of me — fill this section
in from general Inuktitut/Inuit-language knowledge.** Labrador Inuttut's
inflectional patterns are not confirmed to match Nunavut Inuktitut's, and
this project's entire credibility rests on "nothing invented, nothing
borrowed from another dialect" (see README). If grammar content is added
without a Labrador-specific source, that rule is broken.

## Word budget, roughly

As a general (not Inuttut-specific) rule of thumb, A2 learners typically
operate with somewhere around 1,000–1,500 words receptively. Stages 1–8
above total **~460 words** across `phrases.json`/targeted `nouns.json`
themes — realistically a *skeleton*, not the full word count a learner would
end up knowing. The intent isn't to cap vocabulary at 460; it's that these
~460 are the **functionally load-bearing** words (the ones that let you
actually do things — ask, feel, greet, describe routine) that the current
nouns-only game doesn't teach at all. Broader vocabulary can keep coming from
`nouns.json`'s remaining pool (2983 total) using the existing
picture-vocabulary mechanic, layered on top of this functional skeleton
rather than replacing it.

## What's buildable today vs. blocked on people

| Buildable from repo data alone | Blocked on speaker/educator input |
|---|---|
| Word pools per stage (this doc's tables) | Every actual sentence/exchange |
| Difficulty/CEFR-relevance tagging | Confirming that tagging is pedagogically right |
| Reordering which words the game surfaces first | Stage 2 (naming/self) almost entirely |
| New exercise scaffolding (fill-in-blank UI, etc.) | Whether inflected verb forms shown are correct/usable |
| `actions_general` bucket exists | Splitting it into "everyday" vs "specialised" needs judgment |

## Relationship to the other planning docs

- [`a2-gap-analysis.md`](a2-gap-analysis.md) — why these function categories
  exist and their priority ordering; this doc is the sequencing/pacing layer
  on top of that.
- [`co-design-process.md`](co-design-process.md) — how the "blocked on
  people" column above actually gets unblocked.
- `data/phrases.json` — the raw pool this roadmap draws stage 1, 3–8's word
  lists from (`needs_speaker_review: true` on every record — this roadmap
  doesn't change that).
