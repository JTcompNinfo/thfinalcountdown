# =====================================================
# Weapon Class
# Represents a weapon the player can equip
# =====================================================
class Weapon:
    def __init__(self, name, attack_bonus, price):
        # Name of the weapon (ex: "Iron Sword")
        self.name = name
        
        # How much extra attack damage this weapon adds
        self.attack_bonus = attack_bonus
        
        # Cost of the weapon in gold
        self.price = price

    def __str__(self):
        # Controls how the weapon is displayed when printed
        return f"{self.name} (+{self.attack_bonus} ATK) - {self.price} gold"


# =====================================================
# Armor Class
# Represents armor the player can equip
# =====================================================
class Armor:
    def __init__(self, name, defense_bonus, price):
        # Name of the armor (ex: "Steel Armor")
        self.name = name
        
        # How much extra defense this armor adds
        self.defense_bonus = defense_bonus
        
        # Cost of the armor in gold
        self.price = price

    def __str__(self):
        # Controls how armor is displayed when printed
        return f"{self.name} (+{self.defense_bonus} DEF) - {self.price} gold"


# =====================================================
# HealingItem Class
# Represents consumable healing items like potions
# =====================================================
class HealingItem:
    def __init__(self, name, heal_amount, price):
        # Name of the item (ex: "Health Potion")
        self.name = name
        
        # Amount of health this item restores
        self.heal_amount = heal_amount
        
        # Cost of the item in gold
        self.price = price

    def __str__(self):
        # Controls how healing items are displayed
        return f"{self.name} (Heals {self.heal_amount}) - {self.price} gold"
    


# =====================================================
# ALL ITEMS
# =====================================================

ALL_ITEMS = [
    Weapon("Razor Blade", 2, 20),
    Armor("Emo hoodie", 1, 15),
    HealingItem("Antidepressants", 10, 5),

    Weapon("Blury Purple Object", 5, 50),
    Armor("Latex suit", 3, 40),
    HealingItem("Cup of White Liquid", 20, 10),

    Weapon("Frozen Hotdog", 8, 80),
    Armor("Oversized clothes", 6, 70),
    HealingItem("Burger", 35, 20),

    Weapon("Sock Full of Coins", 12, 120),
    Armor("Business suit", 9, 100),
    HealingItem("Chocolate Coins", 50, 30),

    Weapon("Belt", 16, 180),
    Armor("Wife Beater", 18, 150),
    HealingItem("Beer", 70, 45),

    Weapon("Textbook", 22, 250),
    Armor("Lab Coat", 18, 220),
    HealingItem("Antibiotics", 100, 70),

    Weapon("Machete", 28, 320),
    Armor("Blood Covered Hocky Mask", 24, 300),
    HealingItem("Blood Bag", 150, 100),

    Weapon("Keyboard", 35, 400),
    Armor("Fedora", 30, 380),
    HealingItem("AI Slop", 200, 130),

    Weapon("Purse", 50, 600),
    Armor("White Girl Clothes", 45, 550),
    HealingItem("Needoh", 300, 200),
]

ITEM_DICT = {item.name: item for item in ALL_ITEMS}


# =====================================================
# POOLS
# =====================================================

ALL_POOLS = {
    1: ["Razor Blade", "Emo hoodie", "Antidepressants"],
    2: ["Blury Purple Object", "Latex suit", "Cup of White Liquid"],
    3: ["Frozen Hotdog", "Oversized clothes", "Burger"],
    4: ["Sock Full of Coins", "Business suit", "Chocolate Coins"],
    5: ["Belt", "Wife Beater", "Beer"],
    6: ["Textbook", "Lab Coat", "Antibiotics"],
    7: ["Machete", "Blood Covered Hocky Mask", "Blood Bag"],
    8: ["Keyboard", "Fedora", "AI Slop"],
    9: ["Purse", "White Girl Clothes", "Needoh"]
}