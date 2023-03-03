class Item:
    def __init__(self, name, type, price, rarity=0, damage=0):
        self.name = name
        self.type = type
        self.price = price
        self.damage = damage
        self.rarity = rarity

gold = Item("gold", "gold", 1, 100)
wooden_sword = Item("Wooden sword", "sword", 1, 5)
wooden_armor = Item("Wooden armor", "armor", 5)
slime = Item("Slime", "drop", 1, 40)
brain = Item("Brain", "drop", 5, 20)
wing = Item("Wing", "drop", 2, 30)
bone = Item("Bone", "drop", 3, 30)
