from src.entities.hero_state import HeroState


class Hero:
    def __init__(self, name: str, level: int, tendency: str) -> None:
        self.name = name
        self.level = level
        self.tendency = tendency
        self.state = HeroState.ALIVE

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name) -> str:
        self.__name = name

    @property
    def level(self) -> int:
        return self.__level

    @level.setter
    def level(self, level: int) -> None:
        if level < 1:
            raise ValueError("Level must be larger than zero")
        self.__level = level

    @property
    def tendency(self) -> str:
        return self.__tendency

    @tendency.setter
    def tendency(self, tendency: str) -> None:
        if tendency.lower() not in {"good", "evil"}:
            raise ValueError("Tendency must be either good or bad")
        self.__tendency = "good" if tendency == "good" else "evil"

    def is_alive(self) -> bool:
        return self.__state == HeroState.ALIVE

    def is_injured(self) -> bool:
        return self.__state == HeroState.INJURED

    def is_dead(self) -> bool:
        return self.__state == HeroState.DEAD
