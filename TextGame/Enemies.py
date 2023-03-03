import Items
class Enemy:
    def __init__(self, name, hp, damage, *drop):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.drop = drop
    def prnt(self):
        print(self.hp, self.damage, self.name)


slime = Enemy("slime", 10, 1, Items.slime, Items.gold)
zombie = Enemy("zombie", 50, 5, Items.brain, Items.gold)
bat = Enemy("bat", 20, 2, Items.wing, Items.gold)
skeleton = Enemy("skeleton", 30, 7, Items.bone, Items.gold)
