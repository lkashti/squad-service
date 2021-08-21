from src.entities.squad import Squad
from src.entities.hero import Hero


class Service:
    def __init__(self) -> None:
        self._squads = []

    @property
    def squads(self) -> None:
        return self._squads

    def create_squad(self, name: str, tendency: str) -> None:
        """
        Creates a squad and appends it to the squads list
        :param name: Squad name
        :param tendency: Either good/evil
        :return: None
        """
        self._squads.append(Squad(name, tendency)) \
            if not self.is_squad_exists(name) \
            else print(f"{name} already exists")

    def get_squad(self, squad_name: str) -> Squad:
        """
        Retrieves a squad by name
        :param squad_name: Squad name
        :return: Squad object
        """
        for squad in self._squads:
            if squad.name == squad_name:
                return squad

    def remove_squad(self, squad_name: str) -> None:
        """
        Removes a squad from the squad list
        :param squad_name: Squad name
        :return: None
        """
        self._squads = list(
            filter(lambda s: s.name != squad_name, self._squads)
        )

    def is_squad_exists(self, squad_name: str) -> bool:
        """
        Checks if a squad exists in the squad list
        :param squad_name: Squad name
        :return: boolean
        """
        for squad in self._squads:
            if squad.name == squad_name:
                return True
        return False

    def get_squad_power(self, squad_name: str) -> int:
        """
        Retrieves the sum of hero levels in a selected squad
        :param squad_name: Squad name
        :return: integer
        """
        for squad in self._squads:
            if squad.name == squad_name:
                return squad.power

    @staticmethod
    def create_hero(name: str, level: int, tendency: str) -> Hero:
        """
        Creates a Hero object
        :param name: Hero name
        :param level: Hero level(power)
        :param tendency: Either good/evil
        :return: Hero object
        """
        return Hero(name, level, tendency)

    def add_hero_to_squad(self, hero: Hero, squad_name: str) -> None:
        """
        Adds a hero to a selected squad
        :param hero: Hero object to be added
        :param squad_name: Squad name for the hero to be added to
        :return: None
        """
        for squad in self._squads:
            if squad.name == squad_name:
                squad.add(hero)

    def remove_hero_from_squad(self, hero_name: str, squad_name: str) -> None:
        """
        Removes a hero from a selected squad
        :param hero_name: Hero name
        :param squad_name: Squad name for the here to be removed from
        :return:
        """
        for squad in self._squads:
            if squad.name == squad_name:
                squad.heroes = list(
                    filter(lambda h: h.name != hero_name, squad.heroes)
                )

    def remove_hero_from_all_squads(self, hero_name) -> None:
        """
        Removes a hero from all squads
        :param hero_name: Hero name
        :return: None
        """
        for squad in self._squads:
            squad.heroes = list(
                filter(lambda h: h.name != hero_name, squad.heroes)
            )

    def battle(self, squad1_name, squad2_name) -> None:
        """
        Simulates a battle between squads
        :param squad1_name: Competitor one
        :param squad2_name: Competitor two
        :return: None
        """
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
            print(f"{winner.name} won!")
            squad1.is_in_action, squad2.is_in_action = False, False
        else:
            print("These squads are invalid for battle")

    @staticmethod
    def is_valid_battle(squad1: Squad, squad2: Squad) -> bool:
        """
        Validates that two given squads a eligible for a battle:
        Requires:
        Non-emptiness,
        Both are in rest,
        At least one squad is evil
        No shared heroes.
        :param squad1: Competitor one object
        :param squad2: Competitor two object
        :return: True only if both squads are eligible for a battle
        """
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
        """
        Checks if hero exists in two given squads
        :param squad1: first squad
        :param squad2: second squad
        :return: True if a hero exists in two given squads
        """
        for hero in squad1.heroes:
            if hero in squad2.heroes:
                return True
        return False
