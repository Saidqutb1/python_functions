import random


class Creature:
    def __init__(self, name, health=100, attack=10, defense=5):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
    
    def take_damage(self, damage):
        actual_damage = max(damage - self.defense, 0)
        self.health -= actual_damage
        return actual_damage
    
    def is_alive(self):
        return self.health > 0


# Определение дополнительных мифических существ
class Orc(Creature):
    def __init__(self, name):
        super().__init__(name, health=120, attack=15, defense=5)


class Elf(Creature):
    def __init__(self, name):
        super().__init__(name, health=100, attack=20, defense=3)


class HighElf(Creature):
    def __init__(self, name):
        super().__init__(name, health=110, attack=18, defense=4)


class Dwarf(Creature):
    def __init__(self, name):
        super().__init__(name, health=130, attack=12, defense=6)


class Troll(Creature):
    def __init__(self, name):
        super().__init__(name, health=150, attack=10, defense=8)


class Goblin(Creature):
    def __init__(self, name):
        super().__init__(name, health=80, attack=10, defense=2)


class Mage(Creature):
    def __init__(self, name):
        super().__init__(name, health=90, attack=25, defense=1)


class Priest(Creature):
    def __init__(self, name):
        super().__init__(name, health=85, attack=5, defense=3)
        self.heal_power = 10
    
    def heal(self, ally):
        if ally.is_alive():
            ally.health += self.heal_power
            return self.heal_power
        return 0


class DarkMage(Creature):
    def __init__(self, name):
        super().__init__(name, health=100, attack=20, defense=2)


class Dragon(Creature):
    def __init__(self, name):
        super().__init__(name, health=200, attack=30, defense=10)


class Wyvern(Creature):
    def __init__(self, name):
        super().__init__(name, health=180, attack=25, defense=8)


# Функция создания команды
def create_team(creature_type, count):
    team = []
    for i in range(count):
        team.append(creature_type(f"{creature_type.__name__} {i+1}"))
    return team


# Функция для управления битвами команд
def team_battle(team1, team2):
    turn = 0
    while any(creature.is_alive() for creature in team1) and any(creature.is_alive() for creature in team2):
        attacker_team = team1 if turn % 2 == 0 else team2
        defender_team = team2 if turn % 2 == 0 else team1

        attacker = random.choice([creature for creature in attacker_team if creature.is_alive()])
        defender = random.choice([creature for creature in defender_team if creature.is_alive()])

        if isinstance(attacker, Priest):
            heal_amount = attacker.heal(attacker_team[random.randint(0, len(attacker_team) - 1)])
            print(f"{attacker.name} лечит на {heal_amount}.")
        else:
            damage = attacker.attack + random.randint(-5, 5)
            actual_damage = defender.take_damage(damage)
            print(f"{attacker.name} атакует {defender.name} на {damage} урона ({actual_damage} фактического урона).")
            print(f"Здоровье {defender.name} теперь {defender.health}.\n")

        turn += 1

    winner_team = team1 if any(creature.is_alive() for creature in team1) else team2
    print("Победившая команда:")
    for creature in winner_team:
        if creature.is_alive():
            print(f"{creature.name} (здоровье: {creature.health})")


if __name__ == "__main__":
    # Пример создания команды
    team1 = create_team(HighElf, 5)
    team2 = create_team(Mage, 5)
    print("Битва начинается между Командой 1 и Командой 2!\n")
    team_battle(team1, team2)
