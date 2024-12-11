import random
import PokeMod
import Pokemon
# Pokémon (pending on which Starter you get the others will join companions. Companions will have 4 Pokémon each.)

# Function, Loop, and Error component: Password

def pas(p_w):
    password = "HelloWorld123"
    if password == p_w:
        print("Welcome enjoy my demo!")
        return print(" ")

    else:
        print("WRONG PASSWORD!")
        return pas(input("Input the Password: "))


pas(input("Input the Password: "))
# Story
trainer = input("Enter Your Name: ")
print(f'\nWelcome Trainer", {trainer}! I am Professor Dew and this is the Script Region where Pokemon thrive in the air, '
      f'the sea, and everything in between! These Pokemon help trainers like you embark on your journey. Go forth and '
      f'add Pokemon to your party, gather your strength and test your resolve versus the gym leaders across the Script '
      f'Region!\n')

party = 0

# Creating Pokémon list for characters
poke = []
bonipurple_poke = []
zylith_poke = []
viet_poke = []


# Type hierarchy (pause until you create values for pokemon)

# Declaring your starter
class PokemonStarter:
    def __init__(self):
        self.starter_choice = input('Choose Your Starter Pokemon: Chimchar, Oshawatt, or Rowlet: ').capitalize()
        if self.starter_choice.startswith("O"):
            self.poke_type = Pokemon.Osh
            self.boni_type = Pokemon.Row
            self.viet_type = Pokemon.Chi
        elif self.starter_choice.startswith("R"):
            self.poke_type = Pokemon.Row
            self.boni_type = Pokemon.Chi
            self.viet_type = Pokemon.Osh
        else:
            self.poke_type = Pokemon.Chi
            self.boni_type = Pokemon.Osh
            self.viet_type = Pokemon.Row

        poke.append(self.poke_type.Name)
        poke.append(self.poke_type)
        bonipurple_poke.append(self.boni_type.Name)
        bonipurple_poke.append(self.boni_type)
        viet_poke.append(self.viet_type.Name)
        viet_poke.append(self.viet_type)

        # Showing Stats
        print(f'\nLevel: {self.poke_type.Level}')
        print(f'HP: {self.poke_type.HP}')
        print(f'Atk: {self.poke_type.Atk}')
        print(f'Def:  {self.poke_type.Def}')
        print(f'Sp. Atk: {self.poke_type.SpAtk}')
        print(f'Sp. Def: {self.poke_type.SpDef}')
        print(f'Speed: {self.poke_type.Speed}\n')

# Instantiate the class to choose a starter
starter = PokemonStarter()


# Adding party count and Pokémon to party
party += 1
print('Party Size: ', party)
print('Pokemon in Party:', poke[0])

# ---------------Second Part--------------

# Story
print("Now go forth, embark on a journey of a lifetime, before you go", trainer,
      "here is something to help you on your way...")
print(" ")
print("---YOU HAVE ACQUIRED 5 POTIONS---")
potion_uses = 5
print(" ")
print("Welcome to the Script Region", trainer)
print(" ")
# Narrator
print("As you travel through the Script region you meet your first companion and rival Viet....\n")
print("Three days later you have reached the first city Frostern. Your friend Viet approaches you...\n")
# Dialogue
print("Hey", trainer, "how is it embarking on a journey of a lifetime?")
print(" ")
input()
print(" ")
print("Im glad to here that", trainer + ". Look at the pokemon I got from Professor Dew!")
# Printing his poke list
print(viet_poke[0])
print(" ")
print("What do you think?!")
print(" ")
input(" ")
print(" ")
print("Oh really lets battle then! That way you can learn through the spirit of battle!")
print(" ")
# Battle!
print(trainer, "chooses", poke[0])
print('')
print("Veit chooses", viet_poke[0])
print('')


# Prints battling Pokémon and confirms Attack decision
# -------------------------
# Applies battle damage to stats with +10 diff, etc.
def Battle():
    print("Do you choose to Attack, Defend, or Item?")
    choice = input()

    if choice.capitalize().startswith("A"):
        print(poke[0], "Attacks", viet_poke[0] + "!")
        PokeMod.Attack(poke, viet_poke)

    elif choice.capitalize().startswith("D"):
        print(poke[0], 'defends against', viet_poke[0] + "'s attack.")
        PokeMod.Defend(poke, viet_poke)

    elif choice.capitalize().startswith("I"):
        print(trainer, "Uses a Potion!")
        PokeMod.Item(poke)

    def enemyMove():
            retaliate = random.randint(1, 3)
            # FIXME Create a A, D, I function for enemy.
            if retaliate == 1:
                PokeMod.enemy_Attack(poke, viet_poke)
                # Runs Attack function
            elif retaliate == 2:
                PokeMod.enemy_Defend(poke, viet_poke)
                # Runs Defend function
            else:
                pass
                # Runs Item function
    enemyMove()

# Continues the battle until either Pokémon dies
while poke[1].HP and viet_poke[1].HP >= 0:
    Battle()

poke[1].Exp = poke[1].Exp + viet_poke[1].HP

print("")
print("You Won! This concludes my demo, thank you for playing!")


def pas_2(p_w2):
    password = "Paradise Island"
    p_w2 = input("Input the Password: ")
    while password == p_w2:
        print("Give your heart!")
        return print(" ")

    while password != p_w2:
        print("WRONG PASSWORD!")
        return pas_2("lol")
