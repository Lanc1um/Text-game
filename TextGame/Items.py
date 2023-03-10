class Item:
    def __init__(self, name, type, price, rarity=0, damage=0, defence=0, status="unequipped"):
        self.name = name
        self.type = type
        self.price = price
        self.damage = damage
        self.rarity = rarity
        self.defence = defence
        self.status = status

gold = Item("gold", "gold", price=1, rarity=100)
wooden_sword = Item("Wooden sword", "weapon", price=1, damage=5, rarity=5)
wooden_armor = Item("Wooden armor", "armor", price=5, defence=5, rarity=5)
slime = Item("Slime", "drop", price=1, rarity=50)
brain = Item("Brain", "drop", price=5, rarity=30)
wing = Item("Wing", "drop", price=2, rarity=30)
bone = Item("Bone", "drop", price=2, rarity=30)
crown = Item("Crown", "drop", price=20, rarity=10, defence=10)
trolls_skin = Item("Troll's skin", "drop", price=10, rarity=20)
