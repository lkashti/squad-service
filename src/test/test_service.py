from unittest import TestCase
from src.service import Service


class TestService(TestCase):

    def test_create_squad(self):
        serv = Service()
        serv.create_squad("squad", "good")
        self.assertTrue(serv.is_squad_exists("squad"))

    def test_get_squad(self):
        serv = Service()
        serv.create_squad("squad", "good")
        squad = serv.get_squad("squad")
        self.assertIsNotNone(squad)

    def test_remove_squad(self):
        serv = Service()
        serv.create_squad("squad", "good")
        serv.remove_squad("squad")
        self.assertFalse(serv.is_squad_exists("squad"))

    def test_is_squad_exists(self):
        serv = Service()
        serv.create_squad("squad", "good")
        self.assertTrue(serv.is_squad_exists("squad"))

    def test_get_squad_power(self):
        serv = Service()
        serv.create_squad("squad", "good")
        hero = serv.create_hero("hero", 1, "good")
        serv.add_hero_to_squad(hero, "squad")
        self.assertEqual(serv.get_squad_power("squad"), 1)

    def test_create_hero(self):
        hero = Service.create_hero("hero", 1, "good")
        self.assertIsNotNone(hero)
        self.assertEqual(hero.name, "hero")
        self.assertEqual(hero.level, 1)
        self.assertEqual(hero.tendency, "good")

    def test_add_hero_to_squad(self):
        serv = Service()
        serv.create_squad("squad", "good")
        serv.add_hero_to_squad(serv.create_hero("hero", 1, "good"), "squad")
        exists = serv.get_squad("squad").is_hero_exists("hero")
        self.assertTrue(exists)

    def test_remove_hero_from_squad(self):
        serv = Service()
        serv.create_squad("squad", "good")
        serv.add_hero_to_squad(serv.create_hero("hero", 1, "good"), "squad")
        serv.remove_hero_from_squad("hero", "squad")
        exists = serv.get_squad("squad").is_hero_exists("hero")
        self.assertFalse(exists)

    def test_remove_hero_from_all_squads(self):
        serv = Service()
        serv.create_squad("squad1", "good")
        serv.create_squad("squad2", "good")
        hero = serv.create_hero("hero", 1, "good")
        serv.add_hero_to_squad(hero, "squad1")
        serv.add_hero_to_squad(hero, "squad2")
        serv.remove_hero_from_all_squads("hero")
        exists_in_squad_1 = serv.get_squad("squad1").is_hero_exists("hero")
        exists_in_squad_2 = serv.get_squad("squad2").is_hero_exists("hero")
        self.assertFalse(exists_in_squad_1)
        self.assertFalse(exists_in_squad_2)
        self.assertEqual(exists_in_squad_1, exists_in_squad_2)

    def test_is_valid_battle(self):
        serv = Service()

        serv.create_squad("heroes", "good")
        hero = serv.create_hero("hero", 1, "good")
        serv.add_hero_to_squad(hero, "heroes")

        serv.create_squad("villains", "evil")
        villain = serv.create_hero("villain", 1, "evil")
        serv.add_hero_to_squad(villain, "villains")

        self.assertTrue(
            serv.is_valid_battle(
                serv.get_squad("heroes"),
                serv.get_squad("villains")
            )
        )

    def test_is_sharing_heroes(self):
        serv = Service()
        serv.create_squad("squad1", "good")
        serv.create_squad("squad2", "good")
        hero = serv.create_hero("hero", 1, "good")
        serv.add_hero_to_squad(hero, "squad1")
        serv.add_hero_to_squad(hero, "squad2")
        self.assertTrue(
            serv.is_sharing_heroes(
                serv.get_squad("squad1"),
                serv.get_squad("squad2")
            )
        )
