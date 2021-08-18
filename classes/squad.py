from lib.squad_state import SquadState
from classes.hero import Hero


class Squad:
    def __init__(self, name, tendency, members=None):
        self.name = name
        self.tendency = tendency
        self.members = members if members else []
        self.state = SquadState.RESTING

    @property
    def tendency(self):
        return self._tendency

    @tendency.setter
    def tendency(self, tendency):
        if tendency.lower() not in {"good", "evil"}:
            raise ValueError("Tendency must be either good or bad")
        self._tendency = "good" if tendency == "good" else "evil"

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_state):
        self._state = new_state

    def switch_state(self):
        self.state = SquadState.IN_ACTION \
            if not SquadState.IN_ACTION \
            else SquadState.RESTING

    def add(self, hero):
        if type(hero) is not Hero:
            raise TypeError("Only a hero can be added to a squad")
        self.members.append(hero) \
            if hero.tendency == self.tendency \
            else print("Unable to add a hero with different tendency")
        hero.member_of.append(self.name)
