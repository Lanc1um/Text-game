import random
import Enemies
import Items
import Hero
import Shop


enemy_list = ["slime", "zombie", "bat", "skeleton"]


stage = -1
max_stage = 0
mob_hp = 0


shop_inventory = [Items.wooden_armor]
shop_char = Shop.Shop(0, shop_inventory)

armor_inventory = [Items.wooden_armor, Items.wooden_sword]
inventory = []
character = Hero.Character(100, 5, 0, inventory)
equipped = [Items.wooden_sword]
amount = {Items.wooden_armor: 0,
          Items.wooden_sword: 0,
          Items.slime: 0,
          Items.brain: 0,
          Items.wing: 0,
          Items.bone: 0,
          Items.crown: 0,
          Items.trolls_skin: 0
          }

amount_equipped = {Items.wooden_armor: 1,
                   Items.wooden_sword: 1
                   }

slime = Enemies.slime
zombie = Enemies.zombie
bat = Enemies.bat
skeleton = Enemies.skeleton
bossSlime = Enemies.boss_slime

enemy_list = [slime, zombie, bat, skeleton]
boss_list = [bossSlime]


def hello():
    print("Welcome to the text rpg")
    lobby()


def equip(item):

    if len(equipped) > 0:
        for i in range(0, len(equipped)):
            if equipped[i].type == item.type:
                if equipped[i].type == "weapon":
                    character.damage -= equipped[i].damage
                armor_inventory.append(equipped[i])
                equipped.pop(i)
                equipped.append(item)
                if len(armor_inventory) > 0:
                    for i in range(0, len(armor_inventory)-1):
                        if armor_inventory[i] == item:
                            armor_inventory.pop(i)
                if item.type == "weapon":
                    character.damage += item.damage

    else:
        if len(armor_inventory) > 0:
            for i in range(0, len(armor_inventory) - 1):
                if armor_inventory[i] == item:
                    armor_inventory.pop(i)
        equipped.append(item)
        if item.type == "weapon":
            character.damage += item.damage



def unequip(item):
    global equipped
    armor_inventory.append(item)
    for i in range(0, len(equipped)):
        if equipped[i] == item:
            equipped[i].status = "unequipped"
            if equipped[i].type == "weapon":
                character.damage -= equipped[i].damage
            equipped.pop(i)


def death():
    character.hp = 100
    character.gold = 0
    lobby()


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
    if len(inventory) > 0:
        for i in range(0, len(inventory)):
            print(f"{i + 1}) {inventory[i].name} for {inventory[i].price} gold")
        for i in range(0, len(armor_inventory)):
            print(f"{len(inventory)+i}) {armor_inventory[i].name} for {armor_inventory[i].price} gold")
    else:
        if len(armor_inventory) > 0:
            for i in range(0, len(armor_inventory)):
                print(f"{i + 1}) {armor_inventory[i].name} for {armor_inventory[i].price} gold")
    selling = int(input("Print item number to sell it\n"))
    for i in range(0, len(inventory)):
        # print(i)
        if selling == i+1:
            answ = input(f"Are you sure you want to sell {inventory[i].name} for {inventory[i].price} gold\n Yes or No\n")
            if answ == "Yes" or answ == "yes":
                character.gold += inventory[i].price
                shop_char.inventory.append(inventory[i])
                inventory.pop(i)
            elif answ == "No" or answ == "no":
                shop()


def buy():
    if len(shop_inventory) > 0:
        print("You can buy:")
        for i in range(0, len(shop_inventory)):
            print(f"{i+1}) {shop_inventory[i].name} for {shop_inventory[i].price} gold")
        buying = int(input("Print item number to buy it\n"))
        for i in range(0, len(shop_inventory)):
            if buying == i+1:
                if character.gold >= shop_inventory[i].price:
                    answ = input(f"Are you sure you want to buy {shop_inventory[i].name} for {shop_inventory[i].price} gold?\n")
                    if answ == "Yes" or answ == "yes":
                        if shop_inventory[i].type == "armor" or shop_inventory[i].type == "weapon":
                            armor_inventory.append(shop_inventory[i])
                        else:
                            inventory.append(shop_inventory[i])
                        character.gold -= shop_inventory[i].price
                        shop_inventory.pop(i)
                    elif answ == "No" or answ == "no":
                        shop()
                else:
                    print("You dont have enough money")
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
    global inventory, armor_inventory
    print(f"In your inventory you have:\n")
    for i in range(0, len(inventory)):
        print(inventory[i].name)
    for i in range(0, len(armor_inventory)):
        print(armor_inventory[i].name)
    print("What do you want to do?")
    answ = input("1)equip/unequip armor/weapon\n2)leave\n")
    if answ == "2":
        lobby()
    elif answ == "1":
        answ = input("What do you want to do?\n1)Unequip\n2)Equip\n")
        if answ == "1":
            if len(equipped) > 0:
                for i in range(0, len(equipped)):
                    print(f"{i+1}){equipped[i].name}")
                answ = int(input("What do you want ot unequip?\n"))
                unequip(equipped[answ-1])
            elif len(equipped) <= 0:
                print("You dont wear anything right now")
                check_inventory()

        elif answ == "2":
            for i in range(0, len(armor_inventory)):
                print(f"{i+1}){armor_inventory[i].name}")
            answ = int(input("What do you want to equip?\n"))
            equip(armor_inventory[answ-1])
    lobby()


def dungeon():
    global stage, max_stage, mob_hp
    stage += 1
    print("You go down to the dungeon")
    if stage % 10 == 0 and stage != 0:
        num = random.randint(0, len(enemy_list) - 1)
        mob = boss_list[num]
        mob_hp = mob.hp
        mob.hp = mob.hp * ((stage * 5 + 100) / 100)
        mob.damage = mob.damage * ((stage * 5 + 100) / 100)
    else:
        num = random.randint(0, len(enemy_list)-1)
        mob = enemy_list[num]
        mob_hp = mob.hp
        mob.hp = mob.hp * ((stage * 5 + 100) / 100)
        mob.damage = mob.damage * ((stage * 5 + 100)/100)
    print(f"There you meet {mob.name}")
    print(f"His hp: {mob.hp}\nHis damage: {mob.damage}")
    answ = input("Would you like to fight or run?\n")
    if answ == "fight":
        fight_(mob)
    elif answ == "run":
        if random.randint(1, 100) > 50:
            print("You've run away")
            max_stage = stage
            stage = -1
            lobby()
        else:
            print("You couldn't run, now you have to fight")
            fight_(mob)


def drop(mob):
    global inventory, armor_inventory
    drop = random.randint(0, 100)

    for i in range(0, len(mob.drop)):
        drop_item = mob.drop[i]

        if drop <= drop_item.rarity:
            print(f"{mob.name} dropped {drop_item.name}")
            if drop_item.name == "gold":
                character.gold += 1
            else:
                if drop_item.type == "armor" or drop_item.type == "weapon":
                    armor_inventory.append(drop_item)
                else:
                    inventory.append(drop_item)
        else:
            print("pass")
    answ = input("Do you want to leave? Yes or No")
    if answ == "yes" or answ == "Yes":
        lobby()
    elif answ == "no" or answ == "No":
        dungeon()


def fight_(mob, tockens=3):
    global mob_hp
    character_attack = 0
    character_def = 0
    character_hold = 0
    mob_attack = 0
    mob_def = 0
    mob_hold = 0
    character_tockens_max = tockens
    mob_tockens = 3

    while character.hp > 0 and mob.hp > 0:
        character_tockens = character_tockens_max
        character_def = 0
        character_attack = 0
        character_hold = 0
        print(f"You have {character_tockens_max} tockens")
        character_attack = int(input("Print your attack tockens "))
        character_tockens -= character_attack
        if character_tockens > 0:
            character_def = int(input("Print your def tockens "))
            character_tockens -= character_def
        if character_attack + character_def > character_tockens_max:
            print(character_attack + character_def + character_hold, character_tockens_max)
            print("Not enough tockens")
            return fight_(mob, tockens=character_tockens_max)
        if character_tockens > 0:
            character_hold = character_tockens
            character_tockens = 0
        mob_attack = random.randint(0, mob_tockens)
        if mob_attack < mob_tockens:
            mob_def = random.randint(0, mob_tockens - mob_attack)
        if mob_def + mob_attack < mob_tockens:
            mob_hold = mob_tockens - (mob_def + mob_attack)
        print(f"mob attack {mob_attack}, mob def {mob_def}, mob hold {mob_hold}")

        if character_attack > mob_def:
            attack = (character_attack - mob_def) * character.damage
            print(f"You attacked him for {attack} hp")
            mob.hp -= attack
            print(f"His hp {mob.hp}")
        elif mob_attack > character_def:
            attack = (mob_attack - character_def) * mob.damage
            print(f"He attacked you for {attack} hp")
            character.hp -= attack
            print(f"Your hp {character.hp}")
        elif character_attack == mob_def or mob_attack == character_def:
            pass
        character_tockens_max = 0
        character_tockens_max += 1
        character_tockens_max += character_hold
        mob_tockens += 1
    mob.hp = mob_hp
    drop(mob)


while True:
    for i in range(0, len(equipped)):
        if equipped[i].type == "weapon":
            character.damage += equipped[i].damage
    hello()
