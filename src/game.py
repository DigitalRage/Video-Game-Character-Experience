# game.py

from character import Character

class Game:
    def __init__(self):
        self.characters = []

    def add_character(self, character: Character):
        self.characters.append(character)
        print(f"✅ Character {character.name} added!")

    def find_character(self, name: str):
        for c in self.characters:
            if c.name.lower() == name.lower():
                return c
        return None

    def show_all_characters(self):
        if not self.characters:
            print("No characters created yet.")
            return

        print("=====================================")
        print("👥 ALL CHARACTERS 👥")
        for c in self.characters:
            print(f"- {c.name} ({c.character_class}, Level {c.level}, HP {c.hp}/{c.max_hp})")
        print("=====================================")

    def battle(self, char1: Character, char2: Character):
        print("=====================================")
        print("⚔️ BATTLE BEGINS! ⚔️")
        print(f"{char1.name} vs {char2.name}")
        print("=====================================")

        attacker, defender = char1, char2

        while char1.alive and char2.alive:
            attacker.attack_target(defender)

            if not defender.alive:
                print(f"🏆 {attacker.name} wins!")
                break

            attacker, defender = defender, attacker
