from unittest import TestCase
from src.entities.hero import Hero


class TestHero(TestCase):

    def test_tendency(self):
        h = Hero("hero", 1, "good")
        self.assertEqual(h.tendency, "good")

    def test_incorrect_tendency(self):
        with self.assertRaises(ValueError):
            Hero("hero", 1, "goo")

    def test_level(self):
        h = Hero("hero", 1, "good")
        self.assertEqual(h.level, 1)

    def test_incorrect_level(self):
        with self.assertRaises(ValueError):
            Hero("hero", 0, "good")
