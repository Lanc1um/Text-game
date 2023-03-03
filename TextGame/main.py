import random
import time

import Enemies
import Items
import Hero
import Shop
from Sort import sort

enemy_list = ["slime", "zombie", "bat", "skeleton"]


stage = 0


wooden_sword = Items.wooden_sword
wooden_armor = Items.wooden_armor


shop_inventory = [wooden_armor]
shop_char = Shop.Shop(0, shop_inventory)

inventory = [wooden_armor, wooden_sword]
character = Hero.Character(100, 5, 5, inventory)

slime = Enemies.slime
zombie = Enemies.zombie
bat = Enemies.bat
enemy_list = [slime, zombie, bat]


def hello():
    print("Welcome to the text rpg")
    lobby()


def death():
    character.hp = 100
    character.gold = 0


def lobby():
    print(f"Your hp: {character.hp}")
    print(f"Your damage: {character.damage}")
    print(f"Your gold: {character.gold}")
    path = input(f"Where would you like to go?\n1)shop\n2)check inventory\n3)dungeon\n")
    if path == "1":
        shop()
    elif path == "2":
        check_inventory()
    elif path == "3":
        dungeon()


def sell():
    print("For selling you have:\n")
    for i in range(0, len(inventory)):
        print(f"{i + 1}) {inventory[i].name} for {inventory[i].price} gold")
    selling = int(input("Print item number to sell it\n"))
    for i in range(0, len(inventory)):
        # print(i)
        if selling == i+1:
            answ = input(f"Are you sure you want to sell {inventory[i].name} for {inventory[i].price} gold\n Yes or No\n")
            if answ == "Yes" or answ == "yes":
                character.gold += inventory[i].price
                shop_char.inventory.append(inventory[i])
                inventory.pop(i)
            else:
                shop()


def buy():
    if len(shop_inventory) > 0:
        print("You can buy:")
        for i in range(0, len(shop_inventory)):
            print(f"{i+1}) {shop_inventory[i].name} for {shop_inventory[i].price} gold")
        buying = int(input("Print item number to buy it\n"))
        for i in range(0, len(shop_inventory)):
            print(i)
            if buying == i+1:
                if character.gold >= shop_inventory[i].price:
                    answ = input(f"Are you sure you want to buy {shop_inventory[i].name} for {shop_inventory[i].price} gold?\n")
                    if answ == "Yes" or answ == "yes":
                        inventory.append(shop_inventory[i])
                        character.gold -= shop_inventory[i].price
                        shop_inventory.pop(i)
                        sort(inventory)
                else:
                    print("You dont have enough gold")
                    shop()

    else:
        print("There is nothing you can buy")


def shop():
    print("What do you want to do?")
    shop_choose = input("1)buy\n2)sell\n3)goodbye\n")
    if shop_choose == "1":
        print("1")
        buy()
    if shop_choose == "2":
        for i in range(0, len(shop_char.inventory)):
            print(f"{i+1}) {shop_char.inventory[i].name} for {shop_char.inventory[i].price} gold")
        sell()
    if shop_choose == "3":
        lobby()


def check_inventory():
    global inventory
    print("2")
    print(f"In your inventory you have:\n")
    for i in range(0, len(inventory)):
        print(inventory[i].name)
    lobby()


def fight(mob, run):
    hp = mob.hp
    if run == True:
        while mob.hp > 0 and character.hp > 0:
            print(f"He hit you for {mob.damage} damage")
            character.hp -= mob.damage
            print(f"Your hp: {character.hp}")
            time.sleep(1)
            print(f"You hit him for {character.damage} damage")
            mob.hp -= character.damage
            print(f"His hp: {mob.hp}")
            time.sleep(1)
    elif run == False:
        while mob.hp > 0 and character.hp > 0:
            print(f"You hit him for {character.damage} damage")
            mob.hp -= character.damage
            print(f"His hp: {mob.hp}")
            time.sleep(1)
            print(f"He hit you for {mob.damage} damage")
            character.hp -= mob.damage
            print(f"Your hp: {character.hp}")
            time.sleep(1)
    if character.hp > 0 and mob.hp <= 0:
        mob.hp = hp
        drop(mob)


def dungeon():
    global stage
    stage += 1
    print("You go down to the dungeon")
    num = random.randint(0, len(enemy_list)-1)
    mob = enemy_list[num]
    mob.hp = mob.hp * ((stage * 5 + 100) / 100)
    mob.damage = mob.damage * ((stage * 5 + 100)/100)
    print(f"There you meet {mob.name}")
    print(f"His hp: {mob.hp}\nHis damage: {mob.damage}")
    answ = input("Would you like to fight or run?\n")
    if answ == "fight":
        fight(mob, False)
    elif answ == "run":
        if random.randint(1, 100) > 50:
            print("You've run away")
            lobby()
        else:
            print("You couldn't run, now you have to fight")
            fight(mob, True)


def drop(mob):
    drop = random.randint(0, 100)

    for i in range(0, len(mob.drop)):
        drop_item = mob.drop[i]

        if drop <= drop_item.rarity:
            print(f"{mob.name} dropped {drop_item.name}")
            if drop_item.name == "gold":
                character.gold += 1
            else:
                inventory.append(drop_item)
        else:
            print("pass")
    # for i in range(0, len(inventory)):
    #     print(inventory[i].name)
    # print(character.gold)
    dungeon()


while True:
    hello()
