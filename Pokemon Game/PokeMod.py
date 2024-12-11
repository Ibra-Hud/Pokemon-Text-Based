#import PokemonGame
import random

def Attack(poke, viet_poke):
    # Dealing Damage
    if poke[1].Atk - viet_poke[1].Def >= 10:
        ran_num = random.randint(14, 20)
        viet_poke[1].HP = viet_poke[1].HP - ran_num
        print(viet_poke[0] + "'s", "HP is now", viet_poke[1].HP)
    elif poke[1].Atk - viet_poke[1].Def < 10:
        ran_num = random.randint(5, 14)
        viet_poke[1].HP = viet_poke[1].HP - ran_num
        print(viet_poke[0] + "'s", "HP is now", viet_poke[1].HP)


def Defend(poke, viet_poke):
    # Defending against damage
    if poke[1].Def > viet_poke[1].Atk:
        ran_num = random.randint(0, 5)
        poke[1].HP = poke[1].HP - ran_num
        print(poke[0] + "'s HP is now", poke[1].HP)
    # Try for loop to loop until Poke[1].HP == 0
    elif poke[1].Def < viet_poke[1].Atk:
        ran_num = random.randint(5, 10)
        poke[1].HP = poke[1].HP - ran_num
        print(poke[0] + "'s HP is now", poke[1].HP)
    else:
        ran_num = random.randint(3, 8)
        poke[1].HP = poke[1].HP - ran_num
        print(poke[0] + "'s HP is now", poke[1].HP)

def Item(poke):
    potion_uses = 5
    potion_uses -= 1
    print("")
    poke[1].HP = poke[1].HP + 10
    print(poke[0] + "'s HP is now", poke[1].HP)


def enemy_Attack(poke, viet_poke):
    # Dealing Damage
    if viet_poke[1].Atk - poke[1].Def >= 10:
        ran_num = random.randint(14, 20)
        poke[1].HP = poke[1].HP - ran_num
        print(viet_poke[1] + 'retaliates!')
        print(poke[0] + "'s", "HP is now", poke[1].HP)
    elif viet_poke[1].Atk - poke[1].Def < 10:
        ran_num = random.randint(5, 14)
        poke[1].HP = poke[1].HP - ran_num
        print(viet_poke[0] + 'retaliates!')
        print(poke[0] + "'s", "HP is now", poke[1].HP)


# Adds a small amount of hp back to the pokemon so the next attack subtracts a smaller amount of damage
def enemy_Defend(poke, viet_poke):
    # Defending against damage
    if viet_poke[1].Def > poke[1].Atk:
        ran_num = random.randint(5, 10)
        viet_poke[1].HP = viet_poke[1].HP + ran_num
    # Try for loop to loop until Poke[1].HP == 0
    elif poke[1].Def < viet_poke[1].Atk:
        ran_num = random.randint(0, 5)
        viet_poke[1].HP = viet_poke[1].HP + ran_num