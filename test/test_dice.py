import unittest
from game.dice import Dice

class TestDice(unittest.TestCase):

    def setUp(self):
        self.dice = Dice()

    def test_roll_range(self):
        for _ in range(50):
            val = self.dice.roll()
            self.assertIn(val, range(1, 7))

    def test_return_type(self):
        val = self.dice.roll()
        self.assertIsInstance(val, int)

    def test_cheat_roll(self):
        val = self.dice.roll(cheat_number=6)
        self.assertEqual(val, 6)

    def test_cheat_does_not_affect_next(self):
        self.dice.roll(cheat_number=6)
        val = self.dice.roll()
        self.assertIn(val, range(1, 7))

    def test_extreme_rolls(self):
        vals = [self.dice.roll() for _ in range(100)]
        self.assertTrue(any(v == 1 for v in vals))
        self.assertTrue(any(v == 6 for v in vals))

    def test_multiple_rolls(self):
        rolls = [self.dice.roll() for _ in range(20)]
        self.assertTrue(all(1 <= r <= 6 for r in rolls))

    def test_no_state_needed(self):
        self.assertEqual(self.dice.roll(cheat_number=3), 3)
        self.assertIn(self.dice.roll(), range(1, 7))

    def test_repeat_rolls_differ(self):
        vals = [self.dice.roll() for _ in range(10)]
        self.assertTrue(any(v != vals[0] for v in vals))

    def test_roll_randomness(self):
        vals = [self.dice.roll() for _ in range(50)]
        self.assertTrue(any(vals.count(v) < 10 for v in set(vals)))

    def test_stability(self):
        self.assertIn(self.dice.roll(), range(1, 7))
