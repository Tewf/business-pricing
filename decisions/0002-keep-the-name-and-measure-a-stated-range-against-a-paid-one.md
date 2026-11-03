# 0002: Keep the name, and measure a stated range against a paid one

**Decision:** The repository keeps its name after the frame step. The baseline of its first review is B1: a stated range and curve checked against a paid measure on the same good.

**Status:** accepted, 2026-11-04. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/2e5b6f0c3e67d2dc8195a63cf882d46170e79a5a/shapes/decision-record.md).

## Context

- The frame step found the field's words: willingness to pay, stated preference, incentive-compatible elicitation, hypothetical bias ([frame](../evidence/willingness-to-pay/frame.md)).
- "Pricing" is wider than that field: it covers how a price is set, where the first job answers how willingness to pay is measured.
- The review found a stated answer overstates a paid one by 21% on average for consumer goods, and that an auction does not clearly beat other costly forms ([review](../evidence/willingness-to-pay/review.md)).
- The review is finished only when it names a baseline.

## Decision

- Keep the name. The mismatch is partial, and a rename moves the address for no gain.
- Name the baseline B1: a stated range and curve from survey rows, checked against a BDM bid or a pre-order with a deposit on the same good.
- Report the hypothetical bias as a ratio, and call the paid figure the one that counts.
- Name the evidence topic willingness-to-pay, the field's word.

## Consequences

- A reader can compare any pre-sale price test with B1 and with the studies that bear on each of its parts.
- The program `checks/local/wtp_range.py` computes the stated side and the bias; its tests run in CI.
- **Bad:** B1 has one paid arm, and an auction did not beat a referendum vote in the meta-analysis, so the paid arm may carry its own bias ([against](../evidence/willingness-to-pay/against.md)).
- **Bad:** every premium for self-design comes from students in classroom bids, so B1 asks for buyers.

## See also

[Decisions](README.md); [baseline](../evidence/willingness-to-pay/baseline.md); [record 0001](0001-a-repository-of-its-own.md).
