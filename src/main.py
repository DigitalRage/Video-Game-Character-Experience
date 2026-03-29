# main.py

from game import Game
from character import Character

def choose_class():
    while True:
        print("Choose character class:")
        print("[1] Warrior (High Health & Defense)")
        print("[2] Mage (High Attack, Low Health)")
        print("[3] Archer (Balanced Stats)")
        choice = input("Enter class choice (1-3): ").strip()

        if choice == "1":
            return "Warrior"
        elif choice == "2":
            return "Mage"
        elif choice == "3":
            return "Archer"
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def main():
    game = Game()

    while True:
        print("=====================================")
        print("⚔️ CHARACTER CREATOR ⚔️")
        print("=====================================")
        print("🎮 MAIN MENU:")
        print("[1] Create New Character")
        print("[2] View Character")
        print("[3] Level Up Character")
        print("[4] Battle Characters")
        print("[5] View All Characters")
        print("[6] Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            print("=====================================")
            print("✨ CREATE CHARACTER ✨")
            print("=====================================")

            name = input("Enter character name: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue

            character_class = choose_class()
            new_char = Character(name, character_class)
            game.add_character(new_char)
            new_char.display_info()
            input("Press Enter to continue...")

        elif choice == "2":
            name = input("Enter character name to view: ").strip()
            char = game.find_character(name)
            if char:
                char.display_info()
            else:
                print("Character not found.")
            input("Press Enter to continue...")

        elif choice == "3":
            name = input("Enter character name to level up: ").strip()
            char = game.find_character(name)
            if char:
                char.level_up()
                char.display_info()
            else:
                print("Character not found.")
            input("Press Enter to continue...")

        elif choice == "4":
            if len(game.characters) < 2:
                print("You need at least two characters to battle.")
                input("Press Enter to continue...")
                continue

            game.show_all_characters()
            fighter1_name = input("Enter first fighter: ").strip()
            fighter2_name = input("Enter second fighter: ").strip()

            char1 = game.find_character(fighter1_name)
            char2 = game.find_character(fighter2_name)

            if char1 and char2 and char1 is not char2:
                game.battle(char1, char2)
            else:
                print("Invalid fighters.")
            input("Press Enter to continue...")

        elif choice == "5":
            game.show_all_characters()
            input("Press Enter to continue...")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid menu choice.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
