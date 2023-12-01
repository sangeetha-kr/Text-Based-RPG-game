import random
import time

class Player:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.max_health = health  # New attribute to track maximum health
        self.attack = attack
        self.defense = defense
        self.inventory = {"Health Potion": 3, "Attack Boost": 2}
        self.experience = 0

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= max(0, damage - self.defense)

    def attack_enemy(self):
        return random.randint(1, self.attack)

    def use_health_potion(self):
        if "Health Potion" in self.inventory and self.inventory["Health Potion"] > 0:
            self.health = min(self.max_health, self.health + 10)
            self.inventory["Health Potion"] -= 1
            print("You used a Health Potion and restored 10 health.")
        else:
            print("You don't have any Health Potions.")

    def use_attack_boost(self):
        if "Attack Boost" in self.inventory and self.inventory["Attack Boost"] > 0:
            self.attack += 3
            self.inventory["Attack Boost"] -= 1
            print("You used an Attack Boost and gained +3 attack for the next battle.")
        else:
            print("You don't have any Attack Boosts.")

class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= max(0, damage)

    def attack_player(self):
        return random.randint(1, self.attack)

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def battle(player, enemy):
    print_slow(f"A wild {enemy.name} appears!\n")

    while player.is_alive() and enemy.is_alive():
        print(f"{player.name}'s Health: {player.health} | {enemy.name}'s Health: {enemy.health}")
        print(f"{player.name}'s Inventory: {player.inventory}\n")

        print("1. Attack")
        print("2. Use Health Potion")
        print("3. Use Attack Boost")
        print("4. Run Away")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            player_damage = player.attack_enemy()
            enemy.take_damage(player_damage)
            print_slow(f"{player.name} attacks {enemy.name} for {player_damage} damage!")

            enemy_damage = enemy.attack_player()
            player.take_damage(enemy_damage)
            print_slow(f"{enemy.name} attacks {player.name} for {enemy_damage} damage!")

        elif choice == '2':
            player.use_health_potion()

        elif choice == '3':
            player.use_attack_boost()

        elif choice == '4':
            print_slow("You managed to escape from the battle.")
            break

        else:
            print_slow("Invalid choice. Please enter a number between 1 and 4.")

        if not enemy.is_alive():
            print_slow(f"You defeated {enemy.name}!")
            player.experience += 10
            print(f"You gained 10 experience points. Total Experience: {player.experience}")
            break

        if not player.is_alive():
            print_slow("You were defeated. Game over.")
            break

def main():
    print_slow("Welcome to the Enhanced Text-Based RPG Game!\n")

    player_name = input("Enter your character's name: ")
    player = Player(player_name, health=25, attack=10, defense=5)

    enemies = [Enemy("Goblin", health=15, attack=7),
               Enemy("Orc", health=20, attack=10),
               Enemy("Dragon", health=35, attack=15)]

    for enemy in enemies:
        input("Press Enter to continue...\n")
        battle(player, enemy)

        if not player.is_alive():
            break

    if player.is_alive():
        print_slow("Congratulations! You cleared the game.")

if __name__ == "__main__":
    main()
