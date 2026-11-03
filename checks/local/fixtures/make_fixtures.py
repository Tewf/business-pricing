"""Writes the two synthetic survey files next to it. No real person answered them; the seed makes them repeatable.

Van Westendorp rows: 60 people whose four prices are drawn around a typical price of 30, in order, with 3 rows
that break the order on purpose. Gabor-Granger rows: 40 people, each asked at prices 20 to 50, whose willingness
to pay is drawn around 32; an answer is yes when the price is at or below it.
Run:  python3 checks/local/fixtures/make_fixtures.py
"""
import csv
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(20261104)

with open(HERE / "vw_rows.csv", "w", newline="") as handle:
    out = csv.writer(handle)
    out.writerow(["respondent", "too_cheap", "cheap", "expensive", "too_expensive"])
    for person in range(1, 58):
        centre = random.gauss(30, 6)
        steps = sorted(abs(random.gauss(0, 4)) + 1 for _ in range(3))
        base = max(2.0, centre - 15)
        prices = [base, base + steps[0] * 2, base + steps[0] * 2 + steps[1] * 2, base + steps[0] * 2 + steps[1] * 2 + steps[2] * 2]
        out.writerow([person] + [round(p, 1) for p in prices])
    for person in (58, 59, 60):  # answers out of order
        out.writerow([person, 25, 20, 40, 35])

with open(HERE / "gg_rows.csv", "w", newline="") as handle:
    out = csv.writer(handle)
    out.writerow(["respondent", "price", "buy"])
    for person in range(1, 41):
        limit = random.gauss(32, 7)
        for price in (20, 25, 30, 35, 40, 45, 50):
            out.writerow([person, price, "yes" if price <= limit else "no"])
