"""Willingness to pay from survey rows: the Van Westendorp range and a Gabor-Granger demand curve.

A tool, not a check: it has no NAME and no check(), so the standard's runner imports it and skips it.
Run it:  python3 checks/local/wtp_range.py vw rows.csv   |   gg rows.csv   |   bias stated.csv real.csv

Van Westendorp (1976) asks four prices per person: too cheap, cheap, expensive, too expensive.
Its range is a stated, hypothetical object; evidence/willingness-to-pay/baseline.md says what it is compared with.
Definitions follow the pricesensitivitymeter package for R (Alletsee, CRAN): the four points are crossings of the
cumulative curves, taken at the lowest crossing, between the prices people gave, by linear interpolation.

Gabor-Granger (1966) shows each person a ladder of prices and asks whether they would buy at each one.
Its object is a demand curve, with the revenue-maximising price on it.

Time O(n log n) in the rows; space O(n). Standard library only.
"""
import csv
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

VW_COLUMNS = ("too_cheap", "cheap", "expensive", "too_expensive")
GG_COLUMNS = ("respondent", "price", "buy")


class SurveyError(ValueError):
    """A row or a file that cannot be read as a survey answer."""


@dataclass(frozen=True)
class Range:
    """The four Van Westendorp points; None when two curves never cross."""
    marginal_cheapness: float | None
    optimal: float | None
    indifference: float | None
    marginal_expensiveness: float | None
    respondents: int
    dropped: int


@dataclass(frozen=True)
class DemandPoint:
    price: float
    share: float
    revenue: float


def read_csv(path: str | Path, columns: tuple[str, ...]) -> list[dict[str, str]]:
    """The rows of a CSV file; every named column must be there."""
    with open(path, newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        missing = [name for name in columns if name not in (reader.fieldnames or [])]
        if missing:
            raise SurveyError(f"{path}: missing column(s) {', '.join(missing)}")
        return list(reader)


def _number(value: str, where: str) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError):
        raise SurveyError(f"{where}: '{value}' is not a number") from None
    if number != number or number < 0:
        raise SurveyError(f"{where}: '{value}' is not a price")
    return number


def _crossing(grid: list[float], first: list[float], second: list[float]) -> float | None:
    """The lowest price where `first` meets or falls below `second`, found between grid prices by interpolation."""
    for index, price in enumerate(grid):
        gap = first[index] - second[index]
        if gap == 0:
            return price
        if index and (first[index - 1] - second[index - 1]) * gap < 0:
            before = first[index - 1] - second[index - 1]
            return grid[index - 1] + (price - grid[index - 1]) * before / (before - gap)
    return None


def van_westendorp(rows: list[dict[str, str]], consistent_only: bool = True) -> Range:
    """The acceptable price range and the two inner points from rows holding the four prices.

    With consistent_only, a person whose answers break too_cheap < cheap < expensive < too_expensive is dropped.
    """
    people = []
    for number, row in enumerate(rows, start=2):
        answer = tuple(_number(row.get(name, ""), f"row {number} {name}") for name in VW_COLUMNS)
        people.append(answer)
    kept = [p for p in people if not consistent_only or p[0] < p[1] < p[2] < p[3]]
    if not kept:
        raise SurveyError("no respondent left to analyse")
    grid = sorted({price for person in kept for price in person})
    total = len(kept)

    def share(position: int, above: bool) -> list[float]:
        """Share of people whose answer is at or above the price (above) or at or below it."""
        if above:
            return [sum(p[position] >= price for p in kept) / total for price in grid]
        return [sum(p[position] <= price for p in kept) / total for price in grid]

    too_cheap, cheap = share(0, True), share(1, True)
    expensive, too_expensive = share(2, False), share(3, False)
    not_cheap = [1 - value for value in cheap]
    not_expensive = [1 - value for value in expensive]
    return Range(
        marginal_cheapness=_crossing(grid, too_cheap, not_cheap),
        optimal=_crossing(grid, too_cheap, too_expensive),
        indifference=_crossing(grid, cheap, expensive),
        marginal_expensiveness=_crossing(grid, too_expensive, not_expensive),
        respondents=total,
        dropped=len(people) - total,
    )


def _non_increasing(values: list[float]) -> list[float]:
    """The closest non-increasing sequence in least squares: pool adjacent violators."""
    blocks: list[list[float]] = []  # each block: [sum, count]
    for value in values:
        blocks.append([value, 1])
        while len(blocks) > 1 and blocks[-2][0] / blocks[-2][1] < blocks[-1][0] / blocks[-1][1]:
            last = blocks.pop()
            blocks[-1][0] += last[0]
            blocks[-1][1] += last[1]
    return [block[0] / block[1] for block in blocks for _ in range(int(block[1]))]


def gabor_granger(rows: list[dict[str, str]], monotone: bool = True) -> list[DemandPoint]:
    """The share who would buy at each price, with revenue per asker, in rising price order.

    With monotone, the curve is made non-increasing by pooling adjacent prices, since a demand curve cannot rise.
    """
    answers: dict[float, list[float]] = defaultdict(list)
    for number, row in enumerate(rows, start=2):
        price = _number(row.get("price", ""), f"row {number} price")
        buy = row.get("buy", "").strip().lower()
        if buy not in {"0", "1", "yes", "no", "true", "false"}:
            raise SurveyError(f"row {number} buy: '{row.get('buy')}' is not yes or no")
        answers[price].append(1.0 if buy in {"1", "yes", "true"} else 0.0)
    if not answers:
        raise SurveyError("no answer to analyse")
    prices = sorted(answers)
    shares = [sum(answers[p]) / len(answers[p]) for p in prices]
    if monotone:
        shares = _non_increasing(shares)
    return [DemandPoint(p, s, p * s) for p, s in zip(prices, shares)]


def best_price(curve: list[DemandPoint]) -> DemandPoint:
    """The point of the curve with the highest revenue; the lowest price on a tie."""
    return max(curve, key=lambda point: (point.revenue, -point.price))


def hypothetical_bias(stated: list[float], real: list[float]) -> float:
    """Mean stated willingness to pay over mean real willingness to pay, minus one.

    Real means paid, or bid under an incentive-compatible rule; 0.21 reads as the stated figure being 21% above it.
    This is the response-ratio idea of Schmidt 2020, on means.
    """
    if not stated or not real:
        raise SurveyError("both lists need at least one value")
    mean_real = sum(real) / len(real)
    if mean_real <= 0:
        raise SurveyError("the real mean must be positive")
    return (sum(stated) / len(stated)) / mean_real - 1


def _column(path: str, name: str) -> list[float]:
    return [_number(row[name], f"{path} {name}") for row in read_csv(path, (name,))]


def main(argv: list[str]) -> int:
    usage = "usage: wtp_range.py vw ROWS.csv | gg ROWS.csv | bias STATED.csv REAL.csv  (bias reads a column named wtp)"
    try:
        if len(argv) == 3 and argv[1] == "vw":
            result = van_westendorp(read_csv(argv[2], VW_COLUMNS))
            for name, value in vars(result).items():
                print(f"{name}: {value if value is None else round(value, 2)}")
        elif len(argv) == 3 and argv[1] == "gg":
            curve = gabor_granger(read_csv(argv[2], GG_COLUMNS))
            for point in curve:
                print(f"price {point.price:g}  share {point.share:.3f}  revenue {point.revenue:.2f}")
            print(f"best price: {best_price(curve).price:g}")
        elif len(argv) == 4 and argv[1] == "bias":
            print(f"hypothetical bias: {hypothetical_bias(_column(argv[2], 'wtp'), _column(argv[3], 'wtp')):.3f}")
        else:
            print(usage)
            return 2
    except (SurveyError, OSError) as error:
        print(f"error: {error}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
