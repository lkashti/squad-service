from src.entities.hero import Hero


class Squad:
    def __init__(self, name: str, tendency: str) -> None:
        self.name = name
        self.tendency = tendency
        self.__heroes = []
        self.is_in_action = False

    @property
    def power(self) -> int:
        return sum(hero.level for hero in self.heroes)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name) -> str:
        self.__name = name

    @property
    def tendency(self) -> str:
        return self.__tendency

    @tendency.setter
    def tendency(self, tendency: str) -> None:
        if tendency.lower() not in {"good", "evil"}:
            raise ValueError("Tendency must be either good or bad")
        self.__tendency = "good" if tendency == "good" else "evil"

    @property
    def heroes(self) -> list:
        return self.__heroes

    @property
    def is_in_action(self) -> bool:
        return self.__is_in_action

    @is_in_action.setter
    def is_in_action(self, state: bool) -> None:
        self.__is_in_action = state

    def is_empty(self) -> int:
        return len(self.__heroes) == 0

    def is_hero_exists(self, hero):
        for h in self.__heroes:
            if h.name == hero.name:
                return True
        return False

    def add(self, hero: Hero) -> None:
        if not self.is_hero_exists(hero) and hero.tendency == self.tendency:
            self.__heroes.append(hero)
