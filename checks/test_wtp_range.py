"""Tests of checks/local/wtp_range.py: hand-worked cases, then the synthetic fixtures.

Run: python3 -m unittest discover -s checks
"""
import contextlib
import importlib.util
import io
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("wtp_range", HERE / "local" / "wtp_range.py")
wtp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wtp)
FIXTURES = HERE / "local" / "fixtures"


def vw(*people):
    return [dict(zip(wtp.VW_COLUMNS, map(str, person))) for person in people]


def gg(*answers):
    return [{"respondent": str(i), "price": str(price), "buy": buy} for i, (price, buy) in enumerate(answers)]


class VanWestendorp(unittest.TestCase):
    # Three people whose four prices step by 10: worked by hand, the curves cross at 30, 35, 35 and 40.
    STEPS = vw((10, 20, 30, 40), (20, 30, 40, 50), (30, 40, 50, 60))

    def test_hand_worked_points(self):
        result = wtp.van_westendorp(self.STEPS)
        self.assertAlmostEqual(result.marginal_cheapness, 30)
        self.assertAlmostEqual(result.optimal, 35)
        self.assertAlmostEqual(result.indifference, 35)
        self.assertAlmostEqual(result.marginal_expensiveness, 40)
        self.assertEqual((result.respondents, result.dropped), (3, 0))

    def test_order_of_the_range(self):
        result = wtp.van_westendorp(self.STEPS)
        self.assertLess(result.marginal_cheapness, result.marginal_expensiveness)

    def test_a_shift_of_every_price_shifts_every_point(self):
        shifted = vw(*[tuple(price + 100 for price in person) for person in [(10, 20, 30, 40), (20, 30, 40, 50), (30, 40, 50, 60)]])
        before, after = wtp.van_westendorp(self.STEPS), wtp.van_westendorp(shifted)
        self.assertAlmostEqual(after.optimal - before.optimal, 100)
        self.assertAlmostEqual(after.marginal_expensiveness - before.marginal_expensiveness, 100)

    def test_inconsistent_person_is_dropped_or_kept_on_request(self):
        rows = self.STEPS + vw((25, 20, 40, 35))
        self.assertEqual(wtp.van_westendorp(rows).dropped, 1)
        kept = wtp.van_westendorp(rows, consistent_only=False)
        self.assertEqual((kept.respondents, kept.dropped), (4, 0))

    def test_bad_input_is_named(self):
        with self.assertRaises(wtp.SurveyError):
            wtp.van_westendorp(vw((10, 20, "abc", 40)))
        with self.assertRaises(wtp.SurveyError):
            wtp.van_westendorp(vw((10, 20, -3, 40)))
        with self.assertRaises(wtp.SurveyError):
            wtp.van_westendorp(vw((40, 30, 20, 10)))  # every row inconsistent, none left

    def test_fixture(self):
        result = wtp.van_westendorp(wtp.read_csv(FIXTURES / "vw_rows.csv", wtp.VW_COLUMNS))
        self.assertEqual((result.respondents, result.dropped), (57, 3))
        self.assertLess(result.marginal_cheapness, result.marginal_expensiveness)
        for value in (result.marginal_cheapness, result.optimal, result.indifference, result.marginal_expensiveness):
            self.assertIsNotNone(value)
            self.assertTrue(10 < value < 50)  # the fixture is drawn around 30
        self.assertAlmostEqual(result.marginal_cheapness, 17.7, places=1)  # pinned: a change here is a change of method
        self.assertAlmostEqual(result.marginal_expensiveness, 33.2, places=1)


class GaborGranger(unittest.TestCase):
    def test_share_and_best_price(self):
        rows = gg(*[(10, "yes")] * 4, *[(20, "yes")] * 3, (20, "no"), (30, "yes"), *[(30, "no")] * 3)
        curve = wtp.gabor_granger(rows)
        self.assertEqual([p.price for p in curve], [10, 20, 30])
        self.assertEqual([p.share for p in curve], [1.0, 0.75, 0.25])
        self.assertEqual([p.revenue for p in curve], [10.0, 15.0, 7.5])
        self.assertEqual(wtp.best_price(curve).price, 20)

    def test_a_rising_stretch_is_pooled(self):
        rows = gg((10, "yes"), (10, "no"), (20, "yes"), (20, "yes"), (30, "no"), (30, "no"))
        raw = wtp.gabor_granger(rows, monotone=False)
        self.assertEqual([p.share for p in raw], [0.5, 1.0, 0.0])
        pooled = wtp.gabor_granger(rows)
        self.assertEqual([p.share for p in pooled], [0.75, 0.75, 0.0])

    def test_a_tie_takes_the_lower_price(self):
        curve = wtp.gabor_granger(gg((10, "yes"), (20, "yes"), (20, "no"), (20, "no"), (20, "yes"), (10, "yes")))
        self.assertEqual([p.revenue for p in curve], [10.0, 10.0])
        self.assertEqual(wtp.best_price(curve).price, 10)

    def test_bad_answers_are_named(self):
        with self.assertRaises(wtp.SurveyError):
            wtp.gabor_granger(gg((10, "maybe")))
        with self.assertRaises(wtp.SurveyError):
            wtp.gabor_granger([])

    def test_fixture(self):
        curve = wtp.gabor_granger(wtp.read_csv(FIXTURES / "gg_rows.csv", wtp.GG_COLUMNS))
        self.assertEqual(len(curve), 7)
        shares = [p.share for p in curve]
        self.assertEqual(shares, sorted(shares, reverse=True))
        self.assertEqual(wtp.best_price(curve).price, 25)  # pinned


class Bias(unittest.TestCase):
    def test_stated_above_real(self):
        self.assertAlmostEqual(wtp.hypothetical_bias([12, 12], [10, 10]), 0.2)
        self.assertAlmostEqual(wtp.hypothetical_bias([10], [10]), 0.0)

    def test_empty_or_zero_is_refused(self):
        with self.assertRaises(wtp.SurveyError):
            wtp.hypothetical_bias([], [1])
        with self.assertRaises(wtp.SurveyError):
            wtp.hypothetical_bias([1], [0])


class Files(unittest.TestCase):
    def test_missing_column_is_named(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "rows.csv"
            path.write_text("price,buy\n10,yes\n")
            with self.assertRaises(wtp.SurveyError) as caught:
                wtp.read_csv(path, wtp.GG_COLUMNS)
            self.assertIn("respondent", str(caught.exception))

    def test_command_line(self):
        with contextlib.redirect_stdout(io.StringIO()):
            self._command_line()

    def _command_line(self):
        self.assertEqual(wtp.main(["wtp_range.py", "vw", str(FIXTURES / "vw_rows.csv")]), 0)
        self.assertEqual(wtp.main(["wtp_range.py", "gg", str(FIXTURES / "gg_rows.csv")]), 0)
        self.assertEqual(wtp.main(["wtp_range.py", "vw", str(FIXTURES / "nope.csv")]), 1)
        self.assertEqual(wtp.main(["wtp_range.py"]), 2)


if __name__ == "__main__":
    unittest.main()
