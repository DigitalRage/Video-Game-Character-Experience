# character.py

class Character:
    def __init__(self, name: str, character_class: str):
        self.name = name
        self.character_class = character_class
        self.level = 1

        # Class-based stats
        if character_class.lower() == "warrior":
            self.max_hp = 120
            self.attack = 10
            self.defense = 8
        elif character_class.lower() == "mage":
            self.max_hp = 75
            self.attack = 25
            self.defense = 2
        elif character_class.lower() == "archer":
            self.max_hp = 100
            self.attack = 18
            self.defense = 5
        else:
            self.max_hp = 100
            self.attack = 10
            self.defense = 5

        self.hp = self.max_hp
        self.alive = True

    def display_info(self):
        print("=====================================")
        print(f"Name:   {self.name}")
        print(f"Class:  {self.character_class}")
        print(f"Level:  {self.level}")
        print(f"Health: {self.hp}/{self.max_hp}")
        print(f"Attack: {self.attack}")
        print(f"Defense:{self.defense}")
        print("Status: " + ("Alive" if self.alive else "Knocked Out"))
        print("=====================================")

    def level_up(self):
        self.level += 1
        self.max_hp += 10
        self.attack += 3
        self.defense += 2
        self.hp = self.max_hp
        print(f"{self.name} leveled up to Level {self.level}!")

    def take_damage(self, amount: int):
        damage = amount - self.defense
        if damage < 0:
            damage = 0

        self.hp -= damage

        if self.hp <= 0:
            self.hp = 0
            self.alive = False
            print(f"{self.name} has been knocked out!")
        else:
            print(f"{self.name} takes {damage} damage. HP: {self.hp}/{self.max_hp}")

        return self.hp

    def attack_target(self, target):
        if not self.alive:
            print(f"{self.name} cannot attack because they are knocked out.")
            return

        print(f"{self.name} attacks {target.name} for {self.attack} attack power!")
        target.take_damage(self.attack)
