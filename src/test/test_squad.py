from unittest import TestCase
from src.entities.squad import Squad
from src.entities.hero import Hero


class TestSquad(TestCase):

    def test_default_squad(self):
        s = Squad("squad", "good")
        self.assertEqual(s.name, "squad")
        self.assertEqual(s.tendency, "good")
        self.assertEqual(s.power, 0)
        self.assertEqual(s.is_empty(), True)

    def test_tendency(self):
        with self.assertRaises(ValueError):
            Squad("squad", "goo")

    def test_is_hero_exists(self):
        s = Squad("squad", "good")
        hero = Hero("hero", 1, "good")
        s.add(hero)
        self.assertTrue(s.is_hero_exists(hero.name))

    def test_add(self):
        s = Squad("squad", "good")
        hero = Hero("hero", 1, "good")
        s.add(hero)
        self.assertEqual(s.get_hero_by_name(hero.name), hero)
        self.assertTrue(s.is_hero_exists(hero.name))

    def test_refuse_add(self):
        s = Squad("squad", "good")
        hero = Hero("hero", 1, "evil")
        s.add(hero)
        self.assertIsNone(s.get_hero_by_name(hero.name))
        self.assertFalse(s.is_hero_exists(hero.name))

    def test_is_in_action(self):
        s = Squad("squad", "good")
        s.is_in_action = True
        self.assertTrue(s.is_in_action)

    def test_is_not_in_action(self):
        s = Squad("squad", "good")
        self.assertFalse(s.is_in_action)
