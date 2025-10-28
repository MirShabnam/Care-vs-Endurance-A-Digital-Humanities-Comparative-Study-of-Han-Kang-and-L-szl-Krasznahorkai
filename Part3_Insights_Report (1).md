
# Part 3 — Insights & Interpretation (from compiled datasets)
*Generated: 2025-10-28 12:27*

This report draws **comparative insights** from the structured data prepared in Parts 1–2.
It focuses on: corpus scope & accessibility, form/genre footprint, temporal footprint, translation ecology,
and a proxy measure for **shared thematic terrain** using our curated theme lexicons.

---

## 1) Corpus Scope & Accessibility
- **Total titles listed**
  - Han Kang: 13
  - László Krasznahorkai: 13
- **English availability (ratio)**
  - Han Kang: 0.46
  - Krasznahorkai: 0.92

**Insight:** Both authors have significant English availability, enabling robust cross-lingual DH analysis.
Krasznahorkai’s backlist shows strong translation coverage via New Directions; Han’s recent titles have accelerated English releases.

---

## 2) Form & Genre Footprint
See per-author bar charts:
- `plot_genre_Han_Kang.png`
- `plot_genre_László_Krasznahorkai.png`

**Insight:**
- Han Kang’s footprint mixes **novels** with **lyric/fragmentary prose**, complementing a philosophy of restraint and care.
- Krasznahorkai concentrates on **novels/novellas** with long-form narrative pressure, matching an endurance/apocalypse register.

---

## 3) Temporal Footprint (Original Publication Timeline)
Chart: `plot_timeline_footprint.png`

**Insight:** The temporal curves suggest distinct waves—
Han’s intensifies post-2007 (The Vegetarian → Human Acts → The White Book → Greek Lessons → We Do Not Part),
while Krasznahorkai shows peaks around **1985–1999**, then a renewed cluster **2008–2021**.

---

## 4) Translation Ecology (Gateways to Global Reception)
- **Top Translators**
  - Han Kang → prominently **Deborah Smith** (and **Emily Yae Won** emerging for Greek Lessons), see `plot_translators_Han_Kang.png`.
  - Krasznahorkai → **George Szirtes** and **Ottilie Mulzet** dominate, see `plot_translators_László_Krasznahorkai.png`.

- **Translation Lag (Original → English)**
  - Boxplot: `plot_translation_lag.png`

**Insight:** Han’s recent works reach English faster (lower median lag) — indicating **rapid international resonance** of her ethics-of-care poetics.
Krasznahorkai’s earlier titles experienced longer lags historically, but recent works (2016–2024) show **tightened turnaround**.

---

## 5) Thematic Convergence (Proxy via Lexicon Overlap)
- **Jaccard overlap** of curated keywords (Han vs Krasznahorkai): **0.02**
- **Overlapping tokens:** breath

**Insight:** As curated, overlap is intentionally small (distinct lexicon poles). This reflects our hypothesis:
**Han = care/silence/body/repair** vs **Krasznahorkai = apocalypse/disorder/endurance**.
Common ground will surface not at the surface-keyword level but **via latent topics** (e.g., *art, witness, fragility, history*).

---

## 6) Synthesis — Literary/Philosophical Insights (Data-anchored)

1. **Twin ethics: Care vs Endurance.**  
   Genre footprints and translation ecosystems align with our philosophical reading:
   Han’s mixed forms and fragmentary prose sustain **non-violating witness**, while Krasznahorkai’s long-form novels enact **immersive endurance**.

2. **Institutional pathways matter.**  
   Translator networks form **interpreting gateways**: Smith & Yae Won (Han), Szirtes & Mulzet (Krasznahorkai).
   These networks shape Anglophone reception — a factor to model in citation/coverage studies.

3. **Acceleration of global attention.**  
   Translation lag analysis shows recent **compression of time-to-English**, especially for Han. This mirrors a world hungry for
   literature that offers **care and repair** vocabularies alongside crisis narratives.

4. **Temporal waves reflect political weather.**  
   Krasznahorkai’s early cluster (late socialism → post-1989 transitions) vs Han’s 2007–present surge (Korean historical memory → global ethics-of-care)
   support a **history-to-form** linkage: social ruptures leave signatures on publication timelines and genres.

5. **Surface divergence, latent convergence.**  
   Lexicon overlap is small by design, yet both authors orbit **fragility, harm, and the role of art**.
   The “common core” is expected to emerge in **topic models** and **concordance evidence**, not raw keyword unions.

6. **Media-theoretical corollary.**  
   In attention economies of crisis: **Han** models *care as signal compression* (clarity, restraint), while **Krasznahorkai** models *endurance as signal expansion* (pressure, duration).
   Both are **pedagogies of attention** for the present/future.

---

## 7) Recommended Next Analytic Steps
- Run MALLET/LDA on **fair-use excerpt corpus** (k=10–12) to quantify the “maximum talked about” themes.
- Stylometry on sentence lengths and punctuation density (Han < Krasznahorkai expected).
- Emotion/affect pass using lexicons (sadness/anticipation/trust) normalized per 1,000 tokens.
- Modal verbs and deictics for **present vs future** stance mapping.
- Geospatial NER to contrast *intimate interiors* (Han) vs *porous borders* (Krasznahorkai).

---

### Artifacts
- Data tables: `part3_scope_accessibility.csv`, `part3_genre_counts.csv`, `part3_timeline_counts.csv`, `part3_translator_counts.csv`, `part3_translation_lag_stats.csv`
- Figures: `plot_timeline_footprint.png`, `plot_genre_Han_Kang.png`, `plot_genre_László_Krasznahorkai.png`, `plot_translators_Han_Kang.png`, `plot_translators_László_Krasznahorkai.png`, `plot_translation_lag.png`

