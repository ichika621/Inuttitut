# -*- coding: utf-8 -*-
"""
Step 3c — Build data/phrases.json: an EVERYDAY-FUNCTION vocabulary scaffold,
complementary to data/nouns.json, for the new "strengthen everyday Inuttut use
toward CEFR A2" goal (see docs/a2-gap-analysis.md).

This is a SCAFFOLD, not finished teaching content:
  - It only ever surfaces entries and forms that already exist in
    data/dictionary.json. It never invents, translates, combines, or
    constructs new Inuttut — Inuttut is polysynthetic, so stitching English
    word order onto dictionary citation forms would produce wrong Inuttut.
    Building real sentences/dialogue needs a fluent speaker, not a script.
  - Every record is flagged "needs_speaker_review": true. Verb entries carry
    an extra note: the dictionary gives a CITATION form, not necessarily the
    inflected form a learner would actually say in a sentence.
  - It is additive only — does not touch tag_dictionary.py, build_nouns.py,
    or build_story.py, and is not wired into index.html/js/app.js yet.

Filter (deliberately broader than nouns.json's noun-only filter):
  INCLUDE  pos == "v." (everyday actions), OR
           theme == "greetings" (already a curated high-frequency set), OR
           pos-less entries whose gloss matches a FUNCTION keyword (time,
           place, feelings, requests) even though they aren't concrete nouns.
  EXCLUDE  anything already kept in data/nouns.json (phrases.json is meant to
           complement it, not duplicate it).

Usage:  python scripts/build_phrases.py
"""
import io, json, re
from collections import Counter

DICT_IN = "data/dictionary.json"
NOUNS_IN = "data/nouns.json"
OUT = "data/phrases.json"

# Function taxonomy — a second, CEFR-A2-oriented axis alongside the existing
# `theme` tags. See docs/a2-gap-analysis.md for the rationale behind each
# category. Matched against the gloss HEAD only (the short lead phrase before
# any comma/semicolon/colon/parenthetical), not the whole definition — the
# dictionary's longer descriptive glosses ("About to go off (the hammer in a
# gun: puttunga)") are specialised entries, not common everyday-use words, so
# a plain substring search over the full gloss pulls in far too much noise
# (e.g. "from" inside "a loan word from English", "can" inside "can hold a
# lot of things").
#
# Two match tiers per category:
#   exact   closed-class function words ("no", "please", "here") — matched
#           only when they ARE the whole head, so "No appetite" doesn't get
#           swept in as the core word "No".
#   prefix  open-class content verbs ("come", "carry", "ask") — matched when
#           they're the FIRST word of the head, so "Ask for" / "Come here"
#           still count (still the core everyday verb) but a random gloss
#           that merely contains the word elsewhere does not.
FUNCTION_WORDS = [
    ("greetings_social",
        {"hello", "welcome", "thanks", "thank you", "goodbye", "good-bye",
         "sorry", "yes", "no", "good morning", "good night", "please"},
        {"meet", "visit"}),
    ("personal_info",
        {"name", "age", "home", "called"},
        {"live", "born", "work"}),
    ("needs_requests",
        {"want", "need", "help", "wait"},
        {"give", "take", "ask", "borrow", "buy", "sell", "lend", "share", "let"}),
    ("feelings_health",
        {"happy", "sad", "tired", "sleepy", "sick", "hungry", "thirsty",
         "afraid", "scared", "angry", "mad", "glad", "hurt", "pain", "ill", "well"},
        {"love", "feel", "cry", "laugh"}),
    ("time_weather",
        {"today", "tomorrow", "yesterday", "now", "later", "morning",
         "evening", "night", "winter", "summer", "spring", "fall", "autumn",
         "soon", "always", "never", "cold", "warm", "weather"},
        {"snow", "wind", "rain", "storm"}),
    ("place_direction",
        {"here", "there", "inside", "outside", "up", "down", "near", "far",
         "north", "south", "east", "west"},
        {"come", "go", "arrive", "leave", "return", "enter"}),
    ("food_meals",
        {"meal", "breakfast", "dinner", "supper"},
        {"eat", "drink", "cook", "boil", "fry", "bake"}),
    ("daily_routine",
        {"rest"},
        {"wake", "sleep", "wash", "dress", "sit", "stand", "walk", "run",
         "clean", "play"}),
    ("land_activities",
        set(),
        {"hunt", "fish", "fishing", "paddle", "travel", "camp", "sled",
         "boat", "carry", "pull", "push", "throw", "catch"}),
]
MAX_HEAD_WORDS = 6  # only short, high-frequency-style glosses qualify

def gloss_head(gloss):
    """The short lead phrase: parens stripped, cut at first , ; or :"""
    g = re.sub(r"\([^)]*\)", "", gloss)
    g = re.split(r"[,;:]", g)[0]
    return g.strip().rstrip(".").strip()

def classify_function(head, pos):
    low = head.lower()
    words = low.split()
    if not words or len(words) > MAX_HEAD_WORDS:
        return None
    for func, exact, prefix in FUNCTION_WORDS:
        if low in exact or words[0] in prefix:
            return func
    if pos == "v." and len(words) <= 2:
        return "actions_general"
    return None

def load(path):
    return json.load(io.open(path, encoding="utf-8"))

def main():
    dictionary = load(DICT_IN)
    noun_ids = {n["id"] for n in load(NOUNS_IN)}

    phrases = []
    for rec in dictionary:
        if rec["id"] in noun_ids:
            continue
        pos = rec.get("pos")
        head = gloss_head(rec["english"])
        # NB: dictionary.json's existing `theme=="greetings"` tag is matched
        # against the WHOLE gloss (tag_dictionary.py), so it also catches
        # unrelated entries like "No appetite" or "No wonder that he" just for
        # containing the word "no". Don't trust it here — classify purely off
        # the head, which is intentionally stricter.
        func = classify_function(head, pos)
        if not func:
            continue

        r = dict(rec)
        r["function"] = func
        r["cefr_relevance"] = "A1" if rec.get("difficulty", 3) <= 2 else "A2"
        r["needs_speaker_review"] = True
        if pos == "v.":
            r["review_note"] = (
                "Dictionary gives a citation form only; Inuttut verbs inflect "
                "heavily. Confirm with a speaker before using this form in a "
                "sentence-level exercise."
            )
        phrases.append(r)

    phrases.sort(key=lambda r: (r["function"], r["english"]))
    io.open(OUT, "w", encoding="utf-8").write(
        json.dumps(phrases, ensure_ascii=False, indent=1))

    fc = Counter(p["function"] for p in phrases)
    cc = Counter(p["cefr_relevance"] for p in phrases)
    print("dictionary entries:", len(dictionary), "| already in nouns.json:", len(noun_ids))
    print("phrases.json entries:", len(phrases))
    print("by function:", dict(fc.most_common()))
    print("by cefr_relevance:", dict(cc))
    print("verbs among them (review_note attached):",
          sum(1 for p in phrases if p.get("pos") == "v."))

if __name__ == "__main__":
    main()
