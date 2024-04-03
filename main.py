from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def attack(self):
        return "удар мечом"


class Bow(Weapon):
    def attack(self):
        return "выстрел из лука"


class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def changeWeapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon:
            return f"{self.name} наносит {self.weapon.attack()}."
        else:
            return f"{self.name} атакует кулаками."


class Monster:
    def __init__(self, name):
        self.name = name


def main():
    fighter = Fighter("Боец")
    sword = Sword()
    bow = Bow()

    monsters = [Monster("Монстр 1"), Monster("Монстр 2")]

    for monster in monsters:
        print(f"Боец выбирает меч.")
        fighter.changeWeapon(sword)
        print(fighter.attack())
        print(f"{monster.name} побежден!")

        print(f"Боец выбирает лук.")
        fighter.changeWeapon(bow)
        print(fighter.attack())
        print(f"{monster.name} не побежден!")


if __name__ == "__main__":
    main()
