from lib.hero_state import HeroState
import random


class Hero:
    def __init__(self, name, level, tendency):
        self._name = name
        self._level = level
        self._tendency = tendency
        self._state = HeroState.ALIVE

    @property
    def name(self):
        return self._name

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        if level < 1:
            raise ValueError("Level must be larger than zero")
        self._level = level

    @property
    def tendency(self):
        return self._tendency

    @tendency.setter
    def tendency(self, tendency):
        if tendency.lower() not in {"good", "evil"}:
            raise ValueError("Tendency must be either good or bad")
        self._tendency = "good" if tendency == "good" else "evil"

    def attack(self, attacked_hero):
        if self._state is not HeroState.DEAD:
            print(f"{self._name} attacked {attacked_hero.name}!")
            attacked_hero.take_damage() \
                if self._level > attacked_hero.level \
                else self.take_damage()

    def take_damage(self):
        self._state = HeroState.INJURED \
            if self._state == HeroState.ALIVE \
            else HeroState.DEAD
        # give boost to change the odds
        self.level += random.randint(1, 8)
        print(f"{self._name} got hit")
        if self._state == HeroState.DEAD:
            print(f"{self._name} died")
            return

        print(f"{self._name} got a boost to level {self._level}")

    def is_dead(self):
        return self._state == HeroState.DEAD
