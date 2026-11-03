# Pricing

[![Checks against reader-ergonomics](https://github.com/Tewf/business-pricing/actions/workflows/checks.yml/badge.svg)](https://github.com/Tewf/business-pricing/actions/workflows/checks.yml)
[![Site](https://github.com/Tewf/business-pricing/actions/workflows/pages.yml/badge.svg)](https://tewf.github.io/business-pricing/)

How a price is set and tested: **willingness to pay** and how it is measured, personalised pricing with its law and its ethics, and anchors and reference prices. A program estimates willingness to pay from survey data.

This page in French: [README.fr.md](README.fr.md).

> **Status (2026-11-04):** the first review is written, as a first pass of 39 sources, and ends on a named baseline,
> B1. A program computes the Van Westendorp range and a Gabor-Granger curve from survey rows. The name is kept
> after the frame step ([record 0002](decisions/0002-keep-the-name-and-measure-a-stated-range-against-a-paid-one.md)).
> It is not an official standard, not a peer-reviewed study and not a new result.
>
> **How it is made:** with Claude, an AI assistant by Anthropic, under the maintainer's direction, the way
> reader-ergonomics was made. Corrections are welcome as issues.

## Where it sits

![business-model links business-pricing for the price; business-pricing links business-customer for demand data and business-behavioral for anchors; all obey the standard, and the review is written in the shapes of reader-ergonomics-review.](where-it-sits.svg)

<details>
<summary>Graphviz source</summary>

```dot
// Where business-pricing sits. Colours: business family purple, AI-augmented family green, reader-ergonomics family blue; this repository has the thick border.
digraph where_it_sits {
  graph [rankdir=TB, nodesep=0.45, ranksep=0.5, bgcolor="white", pad=0.2, fontname="Inter"];
  node  [shape=box, style="rounded,filled", fontname="Inter", fontsize=13, margin="0.2,0.1", penwidth=1.5, fontcolor="#1F2328"];
  edge  [fontname="Inter", fontsize=11, color="#3D434B", fontcolor="#55575F", penwidth=1.3, arrowsize=0.8];
  ME [label=<<b>business-pricing</b><br/><font point-size="11" color="#55575F">how a price is set and tested</font>>, fillcolor="#F1EAF7", color="#7A4FA3", penwidth=2.6];
  business_customer [label=<<b>business-customer</b><br/><font point-size="11" color="#55575F">customer discovery and demand</font>>, fillcolor="#F1EAF7", color="#7A4FA3"];
  business_behavioral [label=<<b>business-behavioral</b><br/><font point-size="11" color="#55575F">what behavioural economics measured</font>>, fillcolor="#F1EAF7", color="#7A4FA3"];
  business_model [label=<<b>business-model</b><br/><font point-size="11" color="#55575F">how a model is written and tested</font>>, fillcolor="#F1EAF7", color="#7A4FA3"];
  AP [label=<<b>ai-augmented-project</b><br/><font point-size="11" color="#55575F">AI-augmented family: the method</font>>, fillcolor="#E6F2EA", color="#2E7D4F"];
  RV [label=<<b>reader-ergonomics-review</b><br/><font point-size="11" color="#55575F">reader-ergonomics family: the review as a genre</font>>, fillcolor="#E8EEF8", color="#2F5DA8"];
  RE [label=<<b>reader-ergonomics</b><br/><font point-size="11" color="#55575F">the standard</font>>, fillcolor="#E8EEF8", color="#2F5DA8"];
  ME -> business_customer [label=" links, for demand data"];
  ME -> business_behavioral [label=" links, for anchors"];
  business_model -> ME [label=" links, for the price"];
  ME -> AP [label=" follows its method"];
  ME -> RV [label=" writes its review in its shapes"];
  AP -> RE [label=" obeys"];
  RV -> RE [label=" obeys"];
  ME -> RE [label=" obeys"];
}
```

</details>

- **It links [business-customer](https://github.com/Tewf/business-customer)** for the demand data a price is read from, and **[business-behavioral](https://github.com/Tewf/business-behavioral)** for the replication status of anchoring and framing.
- **[business-model](https://github.com/Tewf/business-model) links it** for the price; this repository does not depend on the model.
- **Its method is [ai-augmented-project](https://github.com/Tewf/ai-augmented-project)'s**: scope, review, baseline and plan, and the registers of decisions and of provisional values. It does not depend on that repository's other parts.
- **It writes its review in the shapes of [reader-ergonomics-review](https://github.com/Tewf/reader-ergonomics-review)**, the review as a genre; the shapes are that repository's.
- **It obeys [reader-ergonomics](https://github.com/Tewf/reader-ergonomics/blob/2e5b6f0c3e67d2dc8195a63cf882d46170e79a5a/standard.md)** (v1.21.0) and runs its checks in CI.
- **It links down only.** The family's map is [business](https://github.com/Tewf/business). A venture appears here as an example, never as the subject.

## Scope

| | What | Why |
|---|---|---|
| in | ways to measure willingness to pay: Van Westendorp, Gabor-Granger and conjoint analysis | each gives a different object, a range, a curve or a trade-off, and a price chosen from one must say which |
| in | the incentive-compatible measure: an auction or a real pre-order set against a stated answer | what people say and what they pay differ, and only a costly act counts as evidence of payment |
| in | the premium for a self-designed good against the same good off the shelf, and its measure before any sale | the effect is documented (a sense of accomplishment, the joy of the process), so it is measured, not assumed |
| in | how a waiting list is read as evidence of demand | a sign-up costs nothing, so it overstates demand, and the review says by how much |
| in | price discrimination and personalised pricing, with their law and their ethics | a price that depends on the person raises questions of consumer and data protection that a seller must answer first |
| in | anchors and reference prices as they act on a price | the number a buyer sees first moves the number they accept, and a price list is an anchor whether it is meant to be or not |
| in | a program that estimates willingness to pay from survey data | a method nobody can run on data is not yet an answer |
| later | price tests on live sales | they need sales, which a skeleton has not |
| out | the estimation of demand from choices, and the design of a customer study | [business-customer](https://github.com/Tewf/business-customer) |
| out | whether an effect replicates, and the line between a nudge and a dark pattern | [business-behavioral](https://github.com/Tewf/business-behavioral) |

## The first job: a literature review

Done as a first pass on 2026-11-04, in the five steps of a thesis review: [evidence/willingness-to-pay](evidence/willingness-to-pay/README.md). It holds 39 sources, 30 formal and 9 grey, and most figures are read from abstracts and marked.

## What the review found

- **The field's name is willingness-to-pay measurement.** Its gap between a stated and a paid answer is the hypothetical bias. "Pricing" is wider, so the name matches in part and is kept.
- **A stated answer overstates a paid one.** The mean overshoot is 21% for consumer goods over 77 studies (Schmidt 2020, secondary), and the median ratio is 1.35 over 83 observations (Murphy 2005). Indirect methods such as conjoint overstate more than direct questions. An auction did not reduce the bias much against a referendum vote (Penn 2018, secondary).
- **The self-design premium is measured at +37% to +92% by students, and vanishes when the task is not finished.**
  - In BDM bids by business students, the same T-shirt design was worth 44% more when designed than off the shelf, and a ski design 62% more (Franke 2010, read in full).
  - It was +92% for a design that fitted taste and +37% for one that did not. More design freedom raised the bid for a watch face from 19.21 to 30.34 euros, and a person who bid on another design paid no premium.
  - Watches showed about +100% by contingent valuation and Vickrey auctions (Franke 2004, secondary). The effect needs a finished task (Norton 2012, secondary).
  - Conditions: students, goods under about 100 euros, bids in a classroom. No premium measured on buyers in a real sale was found.
- **No study of a waiting list as evidence of demand was found.** The nearest evidence is stated purchase intention, which beat an extrapolation of past sales for existing products (Armstrong 2000). A sign-up that costs nothing is a stated intention at no price.
- **Two prices for two people need disclosure in the EU.** A personalised price must be disclosed where applicable (EU 2019 Directive, Article 4). A solely automated decision with significant effect needs a contract, a law or explicit consent (EU 2016 GDPR, Article 22). The law of one member state was not read.

## The baseline

**B1** is a stated range checked against a paid measure on the same good ([baseline](evidence/willingness-to-pay/baseline.md)).

- a sample answers the four Van Westendorp prices and a Gabor-Granger ladder, read by `checks/local/wtp_range.py`;
- a second sample bids in BDM with a real draw, or pre-orders with a small deposit;
- the hypothetical bias is reported as a ratio, and the paid figure is the one that counts.

It lacks buyers in place of students, a second paid arm, and a study of the waiting list.

## Questions the review must answer

- **Measure.** Which measure of willingness to pay predicts what people really pay, and by how much does a stated answer miss?
- **Premium.** How large is the premium for a self-designed good against the same good off the shelf, and when does it vanish?
- **Waiting list.** What does a waiting list say about demand, and what must be recorded for it to say more?
- **Limits.** Where do law and ethics stop a seller from showing two people two prices?

## Check it

```sh
git clone https://github.com/Tewf/reader-ergonomics
python3 reader-ergonomics/checks/run.py path/to/this/repository
```

CI runs the same checks on every push, and a run fails on any error
([checks.yml](https://github.com/Tewf/business-pricing/blob/master/.github/workflows/checks.yml)). Every push to
master also renders the site, [tewf.github.io/business-pricing](https://tewf.github.io/business-pricing/)
([pages.yml](https://github.com/Tewf/business-pricing/blob/master/.github/workflows/pages.yml)).

## Contents

| Part | Summary |
|---|---|
| [evidence](evidence/) | the first review, on willingness to pay: five steps, 39 sources, a named baseline |
| [decisions](decisions/) | one record per choice that shapes this repository, each opening with the decision in one sentence |
| [checks/local](checks/local/wtp_range.py) | a program for the Van Westendorp range and a Gabor-Granger curve, with tests |

## Licence

Code under the [Apache License 2.0](LICENSE); prose under [CC BY 4.0](LICENSES/CC-BY-4.0.txt). Reuse it as you wish,
with credit to this repository; [CITATION.cff](CITATION.cff) gives a citation if you need one.
