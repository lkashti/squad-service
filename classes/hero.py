from lib.hero_state import HeroState


class Hero:
    def __init__(self, name, level, tendency):
        self.name = name
        self.level = level
        self.tendency = tendency
        self.state = HeroState.ALIVE
        self.member_of = []

    @property
    def tendency(self):
        return self._tendency

    @tendency.setter
    def tendency(self, tendency):
        if tendency.lower() not in {"good", "evil"}:
            raise ValueError("Tendency must be either good or bad")
        self._tendency = "good" if tendency == "good" else "evil"

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        if level < 1:
            raise ValueError("Level must be larger than zero")
        self._level = level

    def attack(self, attacked_hero):
        if self.state is not HeroState.DEAD:
            print(f"Attacking {attacked_hero.name}!")
            self.take_damage() \
                if self.level > attacked_hero.level \
                else attacked_hero.take_damage()

    def take_damage(self):
        self.state = HeroState.INJURED \
            if self.state == HeroState.ALIVE \
            else HeroState.DEAD
