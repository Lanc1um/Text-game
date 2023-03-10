import Items
class Enemy:
    def __init__(self, name, type, hp, damage, *drop):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.drop = drop
        self.type = type
    def prnt(self):
        print(self.hp, self.damage, self.name)


slime = Enemy("Slime", "mob", 10, 1, Items.slime, Items.gold)
zombie = Enemy("Zombie", "mob", 50, 5, Items.brain, Items.gold)
bat = Enemy("Bat", "mob", 20, 2, Items.wing, Items.gold)
skeleton = Enemy("Skeleton", "mob", 30, 7, Items.bone, Items.gold)
boss_slime = Enemy("King slime", "boss", 100, 10, Items.slime, Items.gold)
troll = Enemy("Troll", "mob", 50, 10, Items.gold, Items.wooden_armor, Items.wooden_sword, Items.trolls_skin)
