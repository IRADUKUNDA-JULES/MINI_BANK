import random

def create_character():
    name = input("Enter your character's name: ")
    strength = int(input("Enter strength (1-10): "))
    intelligent = int(input("Enter intelligence (1-10): "))
    charisma = int(input("Enetr charisma (1-10): "))
    
    character = {
        "name":name,
        "strength":strength,
        "intelligent":intelligent,
        "charisma":charisma
        }
    
    print("\nCharacter created successfully")
    print(character)
    return character

def create_monster():
    monster_name = ["Goblin","orc","Troll","Dragon"]
    name = random.choice(monster_name)
    strength = random.randint(1,10)
    monster = {
        "name":name,
        "strength":strength
        }
    return monster

def battle(character, monster):
    print(f"\nA wild {monster['name']} appears!!")
    print(f"{monster['name']} strength: {monster['strength']}")
    print(f"{character['name']} strength: {character['strength']}")
    
    if character['strength'] >= monster['strength']:
        print(f"{character['name']} won the battle🎉🎉🎉")
    else:
        print(f"{character['name']} lost the battle 💀")

my_character = create_character()
for i in range(3):
    monster = create_monster()
    battle(my_character, monster)