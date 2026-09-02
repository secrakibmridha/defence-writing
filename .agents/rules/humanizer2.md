---
trigger: manual
description: Comprehensive rule for rewriting AI-generated text to sound natural and human, combining Wikipedia guidelines and standard AI-isms.
---

# Humanizer: Comprehensive AI Cleanup

Rewrite AI-sounding text so it reads like a human writer, not a chatbot. Do not change what it says or make up details. 
This rule combines guidelines from Wikipedia's "Signs of AI writing" and standard AI-ism checks.

## Core Directives

1. **Find AI patterns.** Check the text against the patterns below.
2. **Keep every claim.** You may shorten dull parts, expand useful parts, and merge or split paragraphs. Keep the information even when you change the structure.
3. **Do not invent facts.** Do not add a fact, name, number, date, quote, or citation unless it comes from the source or the user. 
4. **Match the voice.** Use the right tone for the text, such as formal, casual, or technical. Add personality only when the text and the writer call for it.
5. **Analyze the Sample (if provided).** If the user provides a writing sample, match their habits (sentence length, word choice, paragraph openings). A writing sample takes priority over these style rules.

## The Patterns to Eliminate

### 1. Content & Logic
- **Significance Inflation:** Avoid "marking a pivotal moment," "stands/serves as," "is a testament to." Use direct facts.
- **Name-dropping:** Don't just list well-known sources (NYT, BBC) or follower counts to prove importance. Integrate them naturally or remove if not useful.
- **Superficial "-ing" Analyses:** Remove "symbolizing," "reflecting," "showcasing," "highlighting" unless backed by specific data.
- **Promotional/Sales Language:** Remove "nestled within," "breathtaking," "vibrant," "boasts a," "rich."
- **Vague Attributions:** Replace "Experts believe," "Observers have cited," or "Industry reports" with specific names or studies, or remove the unsupported claim.
- **Formulaic Challenges/Outlook:** Remove stock sections about challenges or future prospects that repeat vague claims instead of adding facts ("Despite its challenges... continues to thrive").
- **Answering Unraised Objections:** Remove "This isn't mainly about..." or "I'm not trying to..." unless the text actually needs to defend against a stated objection.
- **Fake Alternatives:** Remove "A tempting option would be..." when no reader would actually consider it.
- **Pretending to Reveal a Deeper Truth:** Remove "The real question is," "at its core," "what really matters." 

### 2. Language & Vocabulary
- **AI Vocabulary:** Eliminate: *Actually, additionally, align with, crucial, delve, emphasizing, enduring, enhance, fostering, garner, gate/gating, highlight, interplay, intricate, key, landscape, pivotal, quietly, showcase, tapestry, testament, underscore, valuable, vibrant.*
- **Copula Avoidance:** Replace "serves as," "features," "offers," or "boasts" with simple verbs like "is," "are," or "has."
- **Negative Parallelisms & Clipped Endings:** Avoid "It's not just X, it's Y" and "no guessing." State the point directly.
- **Rule of Three:** Break up forced triplets (e.g., "innovation, inspiration, and insights"). Use 2 or 4+ items if more natural.
- **Synonym Cycling & Repeated Openings:** Don't constantly rename the subject ("The protagonist", "The hero"). Avoid starting several sentences with the same subject.
- **False Ranges:** Avoid "from X to Y" (e.g., "from the Big Bang to dark matter") when they don't form a real range. List specific topics instead.
- **Passive Voice & Missing Subjects:** Use active voice when it makes the actor and action clearer.
- **Hyphenated Word Pairs:** Don't overuse "cross-functional," "data-driven," "high-quality." Drop hyphens after the noun ("the report is high quality").
- **Formulaic Sayings:** Avoid "X is the Y of Z," "the currency of," "the language of."

### 3. Style & Formatting
- **Em and En Dashes:** Remove em dashes (—) and en dashes (–) unless the writer's sample uses them. Replace with commas, colons, or parentheses.
- **Boldface Overuse:** Remove unnecessary bolding of keywords.
- **Inline-header Lists:** Convert "Topic: Description" lists into flowing prose.
- **Title Case Headings:** Use sentence case for headings.
- **Emojis:** Remove all emojis.
- **Curly Quotes:** Convert “smart quotes” to "straight quotes" ("...").
- **A Heading Repeated in the First Sentence:** Remove the sentence if it only repeats the heading.
- **Writing about the Previous Version:** Describe current behavior; don't mention previous approaches unless it's a changelog.
- **Forced Punchlines:** Avoid turning each sentence into a dramatic closing line or using a row of short fragments.

### 4. Communication & Tone
- **Chatbot Artifacts:** Remove "I hope this helps," "Let me know," "Of course!," "Here is a..."
- **Cutoff Disclaimers & Guesses:** Remove "While specific details are limited," "As of [date]," "It is believed that," "She likely grew up." Do not invent facts or guess.
- **Sycophantic Tone:** Remove "Great question!" or "You're absolutely right!"
- **Filler Phrases:** Replace "In order to" with "To"; "Due to the fact that" with "Because."
- **Excessive Hedging:** Remove "could potentially possibly," "it's also possible," "to be fair." Keep qualifiers only when needed.
- **Generic Conclusions:** Remove vague optimism ("The future looks bright"). End on the last useful fact.
- **Fake-candid Openings:** Remove "Honestly?," "Look," "Real talk," when used as staged pauses.
- **Announcing the Next Point:** Remove "Let's dive in," "let's explore," "here's what you need to know." Just state the point.

## Mandatory Workflow

1. **Analyze:** Identify which patterns are present in the text.
2. **First Rewrite:** Write a draft eliminating all identified patterns. Use a direct, concise, and active voice. Keep every claim, do not invent facts.
3. **Audit Pass:** Ask: "What still sounds AI-generated?" and "Did the rewrite add or remove any fact?" Treat any unsupported addition or lost claim as an error.
4. **Final Polish:** Apply the dash rule and ensure the tone matches the writer's voice (if a sample was provided) or the appropriate context (formal, casual, etc.).
