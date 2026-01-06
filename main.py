import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        # random damage between 80% and 120% of attack_power
        min_damage = int(self.attack_power * 0.8)
        max_damage = int(self.attack_power * 1.2)
        damage = random.randint(min_damage, max_damage)
        
        
        # check if opponent is blocking
        if getattr(opponent, "block_next_attack", False):
            print(f"{opponent.name} blocks the attack! No damage taken.")
            opponent.block_next_attack = False
            return
        
        opponent.health -= damage
        if opponent.health < 0:
            opponent.health = 0
            
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
            
    def heal(self):
        heal_amount = int(self.max_health * 0.25)  # heal 25% of max health
        old_health = self.health
        self.health = min(self.health + heal_amount, self.max_health)
        actual_healed = self.health - old_health
        print(
            f"{self.name} heals for {actual_healed} health! "
            f"Current health: {self.health}/{self.max_health}"
        )

    def display_stats(self):
        print(
            f"{self.name}'s Stats - "
            f"Health: {self.health}/{self.max_health}, "
            f"Attack Power: {self.attack_power}"
        )

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def special_ability_menu(self, opponent):
        print("\nSpecial Abilities (Warrior):")
        print("1. Power Strike (big hit)")
        print("2. Battle Cry (+attack this battle)")
        choice = input("Choose ability: ")

        if choice == "1":
            self.power_strike(opponent)
        elif choice == "2":
            self.battle_cry()
        else:
            print("Invalid choice. You waste your turn!")

    def power_strike(self, opponent):
        min_damage = int(self.attack_power * 1.2)
        max_damage = int(self.attack_power * 1.8)
        damage = random.randint(min_damage, max_damage)

        if getattr(opponent, "block_next_attack", False):
            print(f"{opponent.name} blocks the Power Strike! No damage.")
            opponent.block_next_attack = False
            return

        opponent.health -= damage
        if opponent.health < 0:
            opponent.health = 0

        print(f"{self.name} uses Power Strike on {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def battle_cry(self):
        bonus = 5
        self.attack_power += bonus
        print(
            f"{self.name} uses Battle Cry! "
            f"Attack power increased by {bonus}. Now: {self.attack_power}."
        )

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def special_ability_menu(self, opponent):
        print("\nSpecial Abilities (Mage):")
        print("1. Fireball (strong spell)")
        print("2. Arcane Shield (block next attack)")
        choice = input("Choose ability: ")

        if choice == "1":
            self.fireball(opponent)
        elif choice == "2":
            self.arcane_shield()
        else:
            print("Invalid choice. You waste your turn!")

    def fireball(self, opponent):
        min_damage = int(self.attack_power * 1.3)
        max_damage = int(self.attack_power * 1.9)
        damage = random.randint(min_damage, max_damage)

        if getattr(opponent, "block_next_attack", False):
            print(f"{opponent.name} blocks the Fireball! No damage.")
            opponent.block_next_attack = False
            return

        opponent.health -= damage
        if opponent.health < 0:
            opponent.health = 0

        print(f"{self.name} casts Fireball on {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def arcane_shield(self):
        self.block_next_attack = True
        print(f"{self.name} raises Arcane Shield! The next attack will be blocked.")

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        regen_amount = 5
        self.health = min(self.health + regen_amount, self.max_health)
        print(
            f"{self.name} regenerates {regen_amount} health! "
            f"Current health: {self.health}/{self.max_health}"
        )

# Created Archer class

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=30)

    def special_ability_menu(self, opponent):
        print("\nSpecial Abilities (Archer):")
        print("1. Quick Shot (two attacks)")
        print("2. Evade (dodge next attack)")
        choice = input("Choose ability: ")

        if choice == "1":
            self.quick_shot(opponent)
        elif choice == "2":
            self.evade()
        else:
            print("Invalid choice. You waste your turn!")

    def quick_shot(self, opponent):
        print(f"{self.name} uses Quick Shot!")
        for i in range(2):
            min_damage = int(self.attack_power * 0.6)
            max_damage = int(self.attack_power * 1.0)
            damage = random.randint(min_damage, max_damage)

            if getattr(opponent, "block_next_attack", False):
                print(f"{opponent.name} blocks one of the arrows! No damage.")
                opponent.block_next_attack = False
                continue

            opponent.health -= damage
            if opponent.health < 0:
                opponent.health = 0

            print(f"Arrow {i + 1} hits {opponent.name} for {damage} damage!")
            if opponent.health <= 0:
                print(f"{opponent.name} has been defeated!")
                break

    def evade(self):
        self.block_next_attack = True
        print(f"{self.name} prepares to Evade! The next attack will be dodged.")

# Created Paladin class 

class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=160, attack_power=20)

    def special_ability_menu(self, opponent):
        print("\nSpecial Abilities (Paladin):")
        print("1. Holy Strike (bonus holy damage)")
        print("2. Divine Shield (block next attack)")
        choice = input("Choose ability: ")

        if choice == "1":
            self.holy_strike(opponent)
        elif choice == "2":
            self.divine_shield()
        else:
            print("Invalid choice. You waste your turn!")

    def holy_strike(self, opponent):
        min_damage = int(self.attack_power * 1.4)
        max_damage = int(self.attack_power * 2.0)
        damage = random.randint(min_damage, max_damage)

        if getattr(opponent, "block_next_attack", False):
            print(f"{opponent.name} resists the Holy Strike! No damage.")
            opponent.block_next_attack = False
            return

        opponent.health -= damage
        if opponent.health < 0:
            opponent.health = 0

        print(f"{self.name} smites {opponent.name} with Holy Strike for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def divine_shield(self):
        self.block_next_attack = True
        print(f"{self.name} raises Divine Shield! The next attack will be blocked.")
        
        
        
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == "1":
        return Warrior(name)
    elif class_choice == "2":
        return Mage(name)
    elif class_choice == "3":
        return Archer(name)
    elif class_choice == "4":
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)


def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == "1":
            player.attack(wizard)
        elif choice == "2":
            if hasattr(player, "special_ability_menu"):
                player.special_ability_menu(wizard)
            else:
                print("This character has no special abilities!")
        elif choice == "3":
            player.heal()
        elif choice == "4":
            player.display_stats()
            wizard.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health <= 0:
            print(f"{wizard.name} has been defeated by {player.name}!")
            break

        print("\n--- Wizard's Turn ---")
        wizard.regenerate()
        wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0 and player.health > 0:
        print("Victory! You have defeated the Evil Wizard!")
    elif player.health <= 0 and wizard.health > 0:
        print("Defeat... The Evil Wizard has won.")


def main():
    print("Welcome to 'Defeat the Evil Wizard'!")
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)


if __name__ == "__main__":
    main()
        
        
    