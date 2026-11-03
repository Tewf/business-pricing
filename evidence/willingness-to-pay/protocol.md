# Protocol: how the pool was built

A first pass, run on 2026-11-04 by one reviewer, a language model working under the maintainer's direction. Terms are in [frame](frame.md).

**Shape:** [protocol](https://github.com/Tewf/reader-ergonomics-review/blob/c43f2770000a9af5c2aa3cbc6f997da7a7e13b34/shapes/protocol.md)

## 1. Why grey literature

Garousi's seven questions (Table 4), paraphrased and answered for this topic. One yes suggests including grey sources (Garousi 2019).

| Question | Answer |
|---|---|
| Is the subject too complex for the formal literature alone? | no |
| Is there a lack of volume or quality in the formal literature? | yes: no study of a waiting list as evidence of demand was found |
| Is the context important to the results? | yes: a price method is chosen in a survey tool, and a rule in a statute |
| Is the goal to corroborate science with practice? | yes: the stated methods are sold as tools |
| Is the goal to challenge practice with evidence, or the reverse? | yes: practice treats a stated range as a price |
| Would a synthesis of both communities help? | yes |
| Is there a large volume of practitioner sources showing interest? | yes: pre-order and waitlist guides are many |

## 2. Questions

- Q1 which measure predicts what people pay, and by how much does a stated answer miss?
- Q2 how large is the self-design premium, and when does it vanish?
- Q3 what does a waiting list say about demand?
- Q4 where do law and ethics stop two prices for two people?
- Q5 how does a first number act on the price accepted?

## 3. Existing reviews

- Found: three meta-analyses of the hypothetical bias (Schmidt 2020; Penn 2018; Murphy 2005).
- Found: a survey of WTP methods (Breidert 2006), a review of reference prices (Mazumdar 2005) and a review of anchoring (Furnham 2011).
- Not found, in these searches: a review of the self-design premium across studies (F14 to F17), and a review of the waiting list as evidence of demand (F18 to F20).

## 4. Formal search

Database: OpenAlex, title and abstract (a title filter for a named lead), no key and no identity. Counts are of 2026-11-04. Per string, the top 8 by citations were screened, fewer where fewer came back.

| Id | String as run | Count | New concept |
|---|---|---|---|
| F1 | "hypothetical bias" "willingness to pay" meta-analysis | 19 | yynyynnn |
| F2 | "Van Westendorp" "price sensitivity meter" | 50 | ynnnnnnn |
| F3 | "Gabor-Granger" OR "Gabor and Granger" pricing | 1963922 | failed: the OR inside quotes matched everything, nothing screened |
| F4 | title: Price as an Indicator of Quality: Report on an Enquiry | 2 | yn |
| F5 | "willingness to pay" "Becker-DeGroot-Marschak" OR "BDM" elicitation hypothetical real | 82 | nnynnnnn |
| F6 | "purchase intent" "actual purchase" stated intentions calibration | 0 | not run: zero results, the string was wrong, F7 and F8 replace it |
| F7 | "when do purchase intentions predict sales" | 1 | y |
| F8 | title: Adjusting stated intention measures to predict trial purchase of new products | 2 | yn |
| F9 | "how should consumers" "willingness to pay" measured empirical comparison state-of-the-art approaches | 2 | yn |
| F10 | "review of methods for measuring willingness-to-pay" | 1 | y |
| F11 | "Van Westendorp" validity OR critique OR "price sensitivity meter" bias | 5 | nnnnn |
| F12 | "are choice experiments incentive compatible" | 1 | y |
| F13 | "conjoint" "willingness to pay" "incentive-aligned" OR "incentive aligned" real purchase | 12 | nnnnnn |
| F14 | "I designed it myself" effect | 6 | ynnnnn |
| F15 | "toolkits for user innovation" "willingness to pay" watches | 1 | y |
| F16 | configurators "willingness to pay" self-designed customer co-design premium | 0 | not run: zero results, the string was wrong, F17 replaces it |
| F17 | title: The IKEA effect: When labor leads to love | 2 | yn |
| F18 | crowdfunding "pre-order" OR "preorder" demand validation entrepreneurs | 17 | nnnnnn |
| F19 | "waiting list" OR "waitlist" demand signal new product launch | 243 | nnnnny |
| F20 | "smoke test" OR "fake door" OR "landing page" demand validation startups experiment | 43 | nnnnnn |
| F21 | title: Learning through crowdfunding | 15 | ynn |
| F22 | title: A theory of crowdfunding | 150 | nyn |
| F23 | title: Online price discrimination and EU data privacy law | 2 | yn |
| F24 | title: Personalized pricing and consumer welfare | 6 | ynn |
| F25 | title: Measuring price discrimination and steering on e-commerce web sites | 1 | y |
| F26 | title: Fairness as a constraint on profit seeking entitlements in the market | 2 | yn |
| F27 | title: Coherent arbitrariness stable demand curves without stable preferences | 3 | ynn |
| F28 | title: One swallow doesn't make a summer new evidence on anchoring effects | 2 | yn |
| F29 | title: Reference price research: review and propositions | 1 | y |
| F30 | title: Anchoring: a review | 1212 | ynn |
| F31 | title: Price Sensitivity Meter Van Westendorp NSS | 0 | not run: zero results, Van Westendorp 1976 is not indexed |

The strings F3, F6, F16 and F31 returned nothing usable. A zero is a statement about the string.

## 5. Grey search

The web searches returned a synthesis, not a list; their rows say `not recorded`. A page read directly has its own row.

| Id | Producer or engine | String or what was read | Result | New concept |
|---|---|---|---|---|
| G1 | web search | "I designed it myself" effect, Franke Schreier Kaiser, full text | 20 links; found the author copy; read in full | not recorded |
| G2 | web search | the watch-market toolkit study of 2004, full text | 10 links; the two repository copies sat behind a bot challenge, not read | not recorded |
| G3 | web search | Murphy 2005 meta-analysis hypothetical bias, abstract | 20 links; found the working paper; read in full | not recorded |
| G4 | web search | Miller 2011 willingness to pay results | 20 links; abstract only; the full text was not found | not recorded |
| G5 | web search | Voelckner 2006 comparison of methods | 10 links; abstract opening only | not recorded |
| G6 | web search | Gabor Granger method, origin and use | 10 links; vendor pages; the origin as Gabor 1966 | not recorded |
| G7 | web search | Morwitz 2007 purchase intentions | 10 links; summaries only; found Armstrong 2000, read | not recorded |
| G8 | web search | the 2014 study of configurators as learning instruments | 10 links; found the author copy; read in part | not recorded |
| G9 | web search | the 2019 modernisation Directive, point (ea), personalised price | 20 links; found the text of Article 4 | not recorded |
| G10 | web search | the 2013 report on personalised pricing | 20 links; summaries only | not recorded |
| G11 | web search | waitlist conversion to paying customers, pre-sell to validate demand | 20 links; vendor blogs; three read | not recorded |
| G12 | page | Gabor-Granger method, a software vendor's guide | 1 page; read | y |
| G13 | page | Van Westendorp meter, the same vendor's guide | 1 page; read | y |
| G14 | page | package for the Van Westendorp meter, CRAN page and manual | 1 page; read | y |
| G15 | page | the 2019 modernisation Directive, Article 4, adopted text on a national legislation site | 1 page; read | y |
| G16 | page | the 2016 data protection Regulation, Article 22, on a third-party copy | 1 page; read | y |
| G17 | page | experiment library, the pre-order play | 1 page; read | y |
| G18 | page | a founders' guide, is a waitlist proof of demand | 1 page; read | n |
| G19 | page | a launch tool's waitlist playbook | 1 page; read | n |

## 6. Stopping rule

- Effort bounded: the top 8 results per string by citations, stated before the search.
- Saturation: a string stops after 5 consecutive results that add no concept (F2, F11, F13, F18, F20 stopped so).
- The pool stops at 40 sources, the first-pass ceiling.

## 7. Selection

- Include: a work that measures a stated against a real willingness to pay, a self-design premium, a demand signal before sale, or a rule on a personalised price. Include a method's origin and a tool that implements it.
- Exclude: studies of one country's food or one environmental good with no method point; blogs that restate a vendor.

## 8. Quality of grey sources

Garousi's 20 criteria (Table 7) in eight groups: authority 4, methodology 6, objectivity 4, date 1, position 1, novelty 2, impact 1, outlet 1. The threshold is 10 of 20. Scores are in [sources](sources.md).

## 9. Extraction and synthesis

- Read in full or in part: Franke 2010, Franke 2014, Murphy 2005, Armstrong 2000 and the legal texts and tool pages in G12 to G19.
- Read from the abstract: the others; a figure from one is marked secondary in [review](review.md).
- Franke 2010 was extracted as text; its decimal points were lost and restored from its tables and from the text, which says "over 40%" for 4.75 and 6.85 euros.
- The synthesis is narrative, by question, and traceable through [sources](sources.md).

## 10. Not searched, and limits

- Not searched: databases other than OpenAlex, SSRN working papers, the law of any one member state, case law, Google Scholar.
- Not recorded: the web searches (G1 to G11) returned a synthesis of the results, not a list of them, so no letter per result was kept.
- Not read: Van Westendorp 1976 is not online; List 2001, Voelckner 2006, Breidert 2006, Morwitz 2007, Kahneman 1986 and Furnham 2011 are located only.
- Not bypassed: two repository copies and the EUR-Lex text answered with a bot challenge; none was circumvented.
- One reviewer, no second rater, no inter-rater agreement. Search engines personalise and change.
