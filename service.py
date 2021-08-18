from classes.squad import Squad
import random


def battle(squad1, squad2):
    assignments = []
    squad1.switch_state()
    squad2.switch_state()
    if not is_valid_battle(squad1, squad2):
        print("Good squads do not fight one another")
        return
    random.shuffle(squad1.members)
    random.shuffle(squad2.members)
    # make random assignments for a different result each battle
    assignments = list(
        (zip(squad1.members, squad2.members))
    )
    random.shuffle(assignments)
    while True:



def is_valid_battle(squad1, squad2):
    return False if squad1.tendency == squad2.tendency == "good" else True
