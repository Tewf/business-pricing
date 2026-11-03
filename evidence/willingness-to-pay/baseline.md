# Baseline

Step 5 of the review: the baseline the work is compared against. Evidence is in [review](review.md).

**Shape:** [baseline](https://github.com/Tewf/reader-ergonomics-review/blob/c43f2770000a9af5c2aa3cbc6f997da7a7e13b34/shapes/baseline.md)

## B1: a stated range checked against a paid measure on the same good

1. Ask a sample the four Van Westendorp prices and a Gabor-Granger ladder for one good, and compute the range and the curve with `checks/local/wtp_range.py`.
2. On the same good, ask a second sample for a paid answer: a BDM bid with a real draw, or a pre-order with a small deposit.
3. Compare the two: the ratio of the stated mean to the paid mean, minus one (the hypothetical bias), and whether the best price of the curve is the best price of the paid demand.
4. Report the range as stated and the paid figure as the one that counts.

This is the design of Miller 2011, cut to two arms, and the practice of Kloss 2016 for the meter.

## Compared with what the review found

| Item | In B1 | Fit |
|---|---|---|
| A paid benchmark (Miller 2011) | a BDM bid or a deposit | matches |
| The bias reported as a ratio (Schmidt 2020) | stated mean over paid mean, minus one | matches |
| Reference size to expect (Schmidt 2020; Murphy 2005) | 21% for consumer goods, a median ratio of 1.35 | matches |
| Stated methods kept as a range or a rank, not a price (Kloss 2016; Miller 2011) | the range is reported beside the paid figure | matches |
| A self-design arm (Franke 2010) | the same good off the shelf and self-designed, both in BDM | in part |
| A waiting list read as intention (Jamieson 1989) | a sign-up with the price shown, not a count | in part |
| Disclosure of a personalised price (EU 2019 Directive) | one price per good, so no disclosure is due | matches |

## What B1 lacks

- A study of a waiting list as a predictor, which none of the sources gives (position, Not found).
- Buyers in place of students: every premium comes from classroom bids (against).
- A second paid measure, since an auction did not beat a referendum vote (Penn 2018); one paid arm may carry its own bias.
- The law of the places of sale, which is the design document's to find.

## How it is measured

- The hypothetical bias as a ratio, by `hypothetical_bias` in the program: stated mean over paid mean, minus one.
- Whether the best price of the stated curve falls within the paid demand's top revenue price, the decision metric of Miller 2011.
- The premium as the paid mean of the self-designed good over the paid mean of the same good off the shelf, minus one, with the number of bidders.
- A repeat: the program runs on any rows, and its tests pass on a fixture without a real respondent.

## The review is finished

The baseline is named: B1. The next work is a design document that fixes the good, the paid measure and the stakes.
