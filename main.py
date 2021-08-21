from src.service import Service


def menu() -> None:
    print("\n[1] Create a squad")
    print("[2] Add new hero to squad")
    print("[3] Start a battle between two squads")
    print("[4] Remove a hero")
    print("[5] Remove a hero from a squad")
    print("[6] Remove a squad")
    print("[7] Display current squads")
    print("\n[0] EXIT")


def display_squads(serv: Service) -> None:
    print("NAME\tTENDENCY\tPOWER\tHEROES")
    for s in serv.squads:
        print(s.name, end="\t")
        print(s.tendency, end="\t\t")
        print(s.power, end="\t\t")
        print(list(h.name for h in serv.get_squad(s.name).heroes))


def main():
    serv = Service()

    menu()
    option = int(input("\nChoose an option: "))

    while option != 0:
        if option == 1:
            name = input("squad name: ")
            tendency = input("tendency (good/evil): ")
            serv.create_squad(name, tendency)
            print(f"{name} squad created!")
        elif option == 2:
            name = input("hero name: ")
            level = int(input("hero level: "))
            tendency = input("hero tendency (good/evil): ")
            target_squad_name = input(
                f"Enter squad name the for {name} to join: "
            )
            new_hero = serv.create_hero(name, level, tendency)
            serv.add_hero_to_squad(new_hero, target_squad_name)
            print(f"{name} was added to {target_squad_name}!")
        elif option == 3:
            squad1_name = input("Squad 1 name: ")
            squad2_name = input("Squad 2 name: ")
            serv.battle(squad1_name, squad2_name)
        elif option == 4:
            name = input("hero name to be removed: ")
            serv.remove_hero_from_all_squads(name)
            print(f"{name} removed from all squads")
        elif option == 5:
            hero_name = input("hero name to be removed: ")
            squad_name = input("squad name to remove the hero from: ")
            serv.remove_hero_from_squad(hero_name, squad_name)
            print(f"{name} was removed from {target_squad_name}!")
        elif option == 6:
            squad_name = input("squad name to be removed: ")
            serv.remove_squad(squad_name)
            print(f"{squad_name} was removed")
        elif option == 7:
            display_squads(serv)
        else:
            print("Invalid option, try again")
        menu()
        option = int(input("\nChoose an option: "))


if __name__ == "__main__":
    main()
