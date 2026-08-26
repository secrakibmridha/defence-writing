---
trigger: always_on
description: "Enforces Q1-journal-quality academic writing standards for an undergraduate Civil Engineering thesis."
---

# Academic Writing Guide — Undergraduate Thesis

> **Thesis**: *Comparative Analysis of Local Laboratory and Imported Low-Cost Bitumen for Bangladesh Road Construction (Focusing on Aggregate Shape)*
> **Degree**: B.Sc. in Civil Engineering, Sylhet Engineering College (SUST)
> **Authors**: Md. Rakibul Hasan Mridha & Md Sagor Hossain Saddas

---

## 1. Overarching Principles

1. **Write for a Q1-journal audience.** Every paragraph must read as if it were destined for a Scopus-indexed, Q1-quartile journal (e.g., *Construction and Building Materials*, *International Journal of Pavement Engineering*).
2. **Evidence over opinion.** Never state a claim without a supporting citation or experimental result. Unsupported assertions are strictly forbidden.
3. **Precision over decoration.** Prefer concrete, quantitative language. Avoid vague qualifiers like "very", "really", "a lot", "significantly" (unless reporting a statistical test with p-value).
4. **Reproduce, don't plagiarise.** Paraphrase sources in your own voice. Never copy-paste sentences from papers, even partially. Always cite.

---

## 2. Tone and Voice

| ✅ DO | ❌ DON'T |
|---|---|
| Use **third person, passive or impersonal active** voice: *"The Marshall stability test was conducted…"*, *"This study investigates…"* | Use first person ("I found…") or informal second person ("You can see…") |
| Maintain a **formal, objective, dispassionate** tone throughout | Use colloquial language, contractions ("don't", "can't"), or exclamations |
| Use **hedged language** for interpretive claims: *"suggests", "indicates", "appears to"* | Make absolute claims without statistical backing: "This proves…", "It is certain that…" |
| Be **concise and direct**; one idea per sentence where possible | Write run-on sentences or pack multiple ideas into one clause |
| Use **discipline-specific terminology** accurately (e.g., "rutting", "Marshall stability", "penetration grade", "optimum binder content") | Use layman synonyms when precise technical terms exist |

---

## 3. Section-Specific Writing Standards

### 3.1 Abstract (150–300 words)
- **Structure**: Background → Gap → Objective → Method → Key Results (with numbers) → Conclusion/Implication.
- Must be **self-contained** — no citations, no abbreviations without definition, no references to figures/tables.
- Include **quantitative highlights**: e.g., "Marshall stability improved by 18.7% with 20% cubical aggregate replacement."

### 3.2 Introduction
- **Paragraph 1–2**: Broad context (road infrastructure in Bangladesh, bitumen's role).
- **Paragraph 3–4**: Narrow to the specific problem (quality variation, import bans, aggregate shape effects). Every factual statement must carry a `\cite{}`.
- **Final paragraph**: Clear statement of objectives and scope. End with a brief roadmap sentence: *"Section 2 reviews the existing literature; Section 3 details the experimental methodology…"*

### 3.3 Literature Review
- Organise **thematically**, NOT as a list of paper summaries. Suggested themes:
  1. Bitumen grading and properties in tropical climates
  2. Performance comparison of local vs. imported bitumen
  3. Aggregate shape and its influence on mix design
  4. Marshall mix design and performance evaluation
  5. Cost-effectiveness studies in pavement engineering
- For each theme: **synthesise** findings across multiple sources, identify **agreements**, **contradictions**, and **gaps**.
- End with a **critical gap statement** that directly motivates your study.
- **Citation density**: Aim for ≥2 citations per paragraph. A paragraph with zero citations in the Literature Review is a red flag.

### 3.4 Methodology
- Write in **past tense, passive voice**: *"Specimens were compacted at 75 blows per face…"*
- Specify **all standards** used (ASTM, AASHTO, BDS) with full designation on first mention: e.g., *"ASTM D5 — Standard Test Method for Penetration of Bituminous Materials"*.
- Include **exact quantities, proportions, temperatures, and durations**.
- Reference equipment models and calibration status where relevant.
- Describe aggregate gradation with reference to MoRTH/Superpave specifications.

### 3.5 Results and Discussion
- Present results **objectively first**, then **interpret**.
- Every figure and table must be **referenced in the text before it appears**: *"Figure 3.1 illustrates the variation in Marshall stability…"*
- Compare your findings **explicitly with prior literature**: *"The observed penetration value of 65 dmm aligns with findings by Islam and Tarefder (2019), who reported…"*
- Use **percentage changes**, **error margins**, and **statistical measures** (standard deviation, coefficient of variation) where applicable.
- Discuss **anomalies and limitations** honestly — this demonstrates rigour.

### 3.6 Conclusion
- **No new data or citations** in the conclusion.
- Restate key findings concisely (bullet points are acceptable for an undergraduate thesis).
- Provide **practical recommendations** (e.g., for RHD specifications).
- Suggest **future research directions** in the final paragraph.

---

## 4. Citation and Referencing Rules

1. **Citation style**: Use `\cite{}` commands with BibTeX keys from `biblography.bib`. The bibliography style is `plain` (numeric).
2. **Every factual claim** in Introduction, Literature Review, and Discussion that is not your original finding **must** have a citation.
3. **Avoid orphan citations**: Don't just drop `\cite{X}` — integrate it: *"Teja and Krishna \cite{teja2020effect} demonstrated that flaky aggregates reduce rutting resistance by up to 23%."*
4. **Prefer primary sources** (journal articles, conference proceedings) over textbooks or websites.
5. **Recency**: Prioritise references from the last 10 years (2016–2026). Older references are acceptable for foundational concepts.

   - Every entry must have `author`, `title`, `year`, and `journal`/`booktitle`.
   - Use `doi` fields whenever available — they are the most durable identifiers.
   - Use consistent key naming: `{firstauthorlastname}{year}{keyword}` (e.g., `islam2019performance`).

---

## 5. Figures and Tables

1. **Every figure/table must be referenced in the text** before it appears.
2. **Captions must be self-explanatory**: A reader should understand the figure without reading the body text.
3. **Tables**: Use `booktabs` package conventions (`\toprule`, `\midrule`, `\bottomrule`). No vertical rules. Include units in column headers.
4. **Figures**: Minimum 300 DPI for raster images. Use vector formats (PDF/EPS) for charts and plots when possible.
5. **Numbering**: Figures and tables are numbered by section (e.g., Figure 3.1, Table 4.2) — this is already configured in the preamble.
6. **Placement**: Use `[H]` (from `float` package) sparingly; prefer `[htbp]` and let LaTeX optimise placement.

---

## 6. LaTeX Conventions

1. **Non-breaking spaces** before `\cite{}`: use `~\cite{}` to prevent line breaks.
2. **Units**: Use consistent formatting — either `\,` or the `siunitx` package: *"60\,°C"*, *"2.5\,kN"*.
3. **Abbreviations**: Define on first use with full form: *"Roads and Highways Department (RHD)"*. Use abbreviation thereafter.
4. **Cross-references**: Use `\label{}` and `\ref{}` (or `\autoref{}`) instead of hard-coding numbers.
5. **Equations**: Number only equations that are referenced in the text.
6. **Consistent decimal points**: Use periods (not commas) for decimal separators.

---

## 7. Common Pitfalls to Avoid

| Pitfall | Fix |
|---|---|
| "Many researchers have studied…" (no citation) | Cite at least 2–3 specific studies |
| "The results were good" | Quantify: "Marshall stability exceeded 8 kN, surpassing the minimum 5.5 kN threshold specified by RHD" |
| Starting a sentence with a citation number: "[5] showed that…" | Use author names: "Islam and Tarefder [5] showed that…" |
| Switching tenses within a section | Methodology → past tense; Results → past tense; Discussion → present tense for established facts, past for your work |
| Listing studies one-by-one: "A (2019) found X. B (2020) found Y. C (2021) found Z." | Synthesise: "Several studies have reported improvements in stability with cubical aggregates (A, 2019; B, 2020), though C (2021) observed no significant difference at lower replacement ratios." |
| Copy-pasting the abstract from another project | Write a **new abstract** matching the actual thesis content (bitumen + aggregate, not NLP) |
| Using "etc." in formal writing | List all items explicitly or use "among others" |
| "It was found that…" (dangling "it") | Name the subject: "The penetration test revealed that…" |

---

## 8. Quality Checklist Before Submission

- [ ] Every paragraph in Introduction and Literature Review has ≥1 citation
- [ ] All figures/tables are referenced in the text before they appear
- [ ] No first-person pronouns outside of Acknowledgement
- [ ] Abstract contains quantitative key findings
- [ ] Abstract matches the actual thesis content (not a placeholder)
- [ ] All abbreviations defined on first use
- [ ] Units are consistent and correctly formatted throughout
- [ ] Bibliography has ≥25 entries from reputable sources
- [ ] No `\cite{}` commands produce "?" in the compiled PDF
- [ ] Grammar and spell-check completed (use Grammarly or similar)
- [ ] All test standards (ASTM, AASHTO, BDS) cited with full designation
- [ ] Conclusion contains no new data or citations
- [ ] Page margins, font size, and spacing match department requirements

---

## 9. Sentence Starters and Transition Phrases (Reference Bank)

### Introducing a Topic
- "A growing body of literature has examined…"
- "The performance of flexible pavements is fundamentally governed by…"
- "In the context of Bangladesh's expanding road network,…"

### Citing Evidence
- "According to [Author] \cite{key}, …"
- "Prior investigations have demonstrated that… \cite{key1, key2}."
- "Empirical evidence suggests that… \cite{key}."

### Contrasting
- "However, these findings contrast with those of [Author] \cite{key}, who reported…"
- "Conversely, …"
- "Notwithstanding these results, …"

### Presenting Results
- "The experimental data indicate that…"
- "As illustrated in Figure X.X, …"
- "A notable increase of X% was observed in…"

### Identifying Gaps
- "Despite extensive research on [topic], limited attention has been devoted to…"
- "A critical gap remains in understanding…"
- "No prior study has systematically compared…"

---

## 10. Discipline-Specific Terminology Guide

Use the following terms precisely:

| Term | Meaning | Context |
|---|---|---|
| Penetration grade | Classification of bitumen by penetration depth (e.g., 60/70, 80/100) | Bitumen characterisation |
| Marshall stability | Maximum load sustained by a specimen at 60°C (kN) | Mix design evaluation |
| Flow value | Deformation at maximum load (mm) | Mix design evaluation |
| Optimum Binder Content (OBC) | Binder percentage yielding optimal mix properties | Mix design |
| Indirect Tensile Strength (ITS) | Tensile stress at failure under diametral loading | Moisture damage assessment |
| Flakiness Index / Elongation Index | Shape parameters of coarse aggregates | Aggregate characterisation |
| Cubical aggregate | Aggregates with roughly equal dimensions in all axes | Aggregate shape study |
| Rutting | Permanent deformation in wheel paths | Pavement distress |
| Stripping | Loss of bond between bitumen and aggregate in presence of water | Moisture susceptibility |
| VMA / VFB / Air Voids | Volumetric properties of compacted bituminous mix | Marshall mix design |

---

*This guide is automatically applied to all `.tex`, `.bib`, and `.md` files in the workspace. Follow it rigorously for every piece of writing.*