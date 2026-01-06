**Defeat the Evil Wizard**

This project is a simple, text-based RPG battle game written in Python. I built it to practice Object-Oriented Programming (OOP) concepts like classes, inheritance, and methods while creating a small, interactive game.
​
**Project Overview**

In Defeat the Evil Wizard, the player creates a hero and battles a powerful Evil Wizard in a turn-based combat system. The player chooses a character class, then uses normal attacks, special abilities, and healing to survive while the wizard regenerates health and fights back. The game ends with a clear victory or defeat message based on who goes down first.

This project comes from a module assignment focused on:

- Practicing Python OOP principles

- Building an interactive menu-driven program

- Designing basic game logic such as damage, healing, and enemy behavior

**Features**

Four playable character classes:

- Warrior – High health, solid melee damage, offensive buffs

- Mage – Lower health, higher magic damage, defensive shield

- Archer – Balanced stats, double-shot and evasion abilities

- Paladin – Tanky character with holy damage and strong shielding
  ​

**Two unique special abilities for each class**

- Randomized attack damage within a range for less predictable combat

- Healing mechanic that restores a portion of health without exceeding the character’s maximum

- Evil Wizard enemy that regenerates health every turn and then attacks the player

- Turn-based battle loop with a simple text menu:

- Attack

- Use special ability

- Heal

- View player and wizard stats

- Clear victory and defeat messages at the end of the battle

**How It Works**

From a technical standpoint, this project is centered around a base Character class and several subclasses:

- **Character** defines shared attributes and behavior:

- name, health, attack_power, max_health

- Methods like attack(), heal(), and display_stats()

- A block_next_attack flag used by defensive abilities

**Warrior, Mage, Archer, and Paladin all inherit from Character and customize:**

- Starting health and attack power

- Their own special_ability_menu() implementation

- Two special abilities each (for example, Power Strike, Fireball, Quick Shot, Divine Shield)

- EvilWizard also inherits from Character and adds a regenerate() method so the wizard heals a fixed amount each turn before attacking.

**Gameplay is managed by two main functions:**

- create_character() prompts the player to choose a class and enter a name, then returns the appropriate character object.

- battle(player, wizard) runs the turn-based loop, handles the menu, applies attacks and healing, triggers the wizard’s regeneration and counterattacks, and decides when the game is over.

**How to Run the Game**

Make sure you have Python 3 installed on your system.

Clone or download this repository to your machine.

Open the project folder in VS Code or your preferred editor.

Run the main script from a terminal:

python main.py

**Follow the prompts in the terminal:**

- Choose your character class

- Enter your character’s name

- Use the numbered menu each turn to attack, use abilities, heal, or view stats

- The game runs entirely in the terminal and requires no additional dependencies beyond the Python standard library (random).

**What I Learned**

Through this project, I practiced:

- Designing and implementing class hierarchies in Python

- Using inheritance to share behavior and customize subclasses

- Managing game state and player choices in a loop

- Implementing randomized damage and a basic AI enemy with regeneration

- Writing clearer, menu-driven console output for a better player experience

This has been a helpful step in getting more comfortable with Python OOP and building small, interactive programs that go beyond simple scripts.
