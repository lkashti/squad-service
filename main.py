from service import battle
from classes.squad import Squad
from classes.hero import Hero


def main():
    avengers = Squad("The Avengers", "good")
    avengers.add(Hero("Iron Man", 5, "good"))
    avengers.add(Hero("Thor", 7, "good"))
    avengers.add(Hero("Ant-Man", 3, "good"))

    frightful_four = Squad("The Frightful Four", "evil")
    frightful_four.add(Hero("Hydro-Man", 8, "evil"))
    frightful_four.add(Hero("Klaw", 4, "evil"))

    battle(avengers, frightful_four)


if __name__ == "__main__":
    main()
