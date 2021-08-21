from src.entities.squad import Squad
from src.entities.hero import Hero


class Service:
    def __init__(self) -> None:
        self._squads = []

    @property
    def squads(self) -> None:
        return self._squads

    def create_squad(self, name: str, tendency: str) -> None:
        self._squads.append(Squad(name, tendency)) \
            if not self.is_squad_exists(name) \
            else print(f"{name} already exists")

    def get_squad(self, squad_name: str) -> Squad:
        for squad in self._squads:
            if squad.name == squad_name:
                return squad

    def remove_squad(self, squad_name: str) -> None:
        self._squads = list(
            filter(lambda s: s.name != squad_name, self._squads)
        )

    def is_squad_exists(self, squad_name: str) -> bool:
        for squad in self._squads:
            if squad.name == squad_name:
                print("exists")
                return True
        return False

    def get_squad_power(self, squad_name: str) -> int:
        for squad in self._squads:
            if squad.name == squad_name:
                return squad.power

    @staticmethod
    def create_hero(name: str, level: int, tendency: str) -> Hero:
        return Hero(name, level, tendency)

    def add_hero_to_squad(self, hero: Hero, squad_name: str) -> None:
        for squad in self._squads:
            if squad.name == squad_name:
                squad.add(hero)

    def remove_hero_from_squad(self, hero_name: str, squad_name: str) -> None:
        for squad in self._squads:
            if squad.name == squad_name:
                squad.heroes = list(
                    filter(lambda h: h.name != hero_name, squad.heroes)
                )

    def remove_hero_from_all_squads(self, hero_name) -> None:
        for squad in self._squads:
            squad.heroes = list(
                filter(lambda h: h.name != hero_name, squad.heroes)
            )

    def battle(self, squad1_name, squad2_name) -> None:
        squad1 = self.get_squad(squad1_name)
        squad2 = self.get_squad(squad2_name)
        if Service.is_valid_battle(squad1, squad2):
            squad1.is_in_action, squad2.is_in_action = True, True
            squad1_power = self.get_squad_power(squad1.name)
            squad2_power = self.get_squad_power(squad2.name)
            if squad1_power == squad2_power:
                print("It's a Tie!")
            elif squad1_power > squad2_power:
                winner = squad1
            else:
                winner = squad2
            print(f"{winner.name} win!")
            squad1.is_in_action, squad2.is_in_action = False, False
        else:
            print("These squads are invalid for battle")

    @staticmethod
    def is_valid_battle(squad1: Squad, squad2: Squad) -> bool:
        if squad1.is_empty() or squad2.is_empty():
            return False
        if squad1.is_in_action or squad2.is_in_action:
            return False
        if squad1.tendency == squad2.tendency == "good":
            return False
        if Service.is_sharing_heroes(squad1, squad2):
            return False
        return True

    @staticmethod
    def is_sharing_heroes(squad1, squad2) -> bool:
        for hero in squad1.heroes:
            if hero in squad2.heroes:
                return True
        return False
