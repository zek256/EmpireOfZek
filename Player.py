import sqlite3
from sqlite3 import Error

class Player:

    pid = -1
    name = "name"
    location = 0
    totalexp = 0
    level = 1
    base_max_health = 0
    base_max_mana = 0

    #stats
    base_strength = 0
    base_stamina = 0
    base_dexterity = 0
    base_agility = 0
    base_intelligence = 0
    base_wisdom = 0
    base_charisma = 0

    #equipment
    equipment_primary = 0
    equipment_secondary = 0
    equipment_head = 0
    equipment_body = 0
    equipment_feet = 0
    equipment_hands = 0

    #inventory
    gold = 0
    invetory_slot_1 = 0
    invetory_slot_2 = 0
    invetory_slot_3 = 0
    invetory_slot_4 = 0
    invetory_slot_5 = 0
    invetory_slot_6 = 0
    invetory_slot_7 = 0
    invetory_slot_8 = 0
    invetory_slot_9 = 0
    invetory_slot_10 = 0
    invetory_slot_11 = 0
    invetory_slot_12 = 0
    invetory_slot_13 = 0
    invetory_slot_14 = 0
    invetory_slot_15 = 0
    invetory_slot_16 = 0
    invetory_slot_17 = 0
    invetory_slot_18 = 0
    invetory_slot_19 = 0
    invetory_slot_20 = 0

    def __init__(self, pid, name, base_max_health, base_max_mana, base_strength, base_stamina, base_dexterity, base_agility, base_intelligence, base_wisdom, base_charisma):
        self.pid = pid
        self.name = name
        self.base_max_health = base_max_health
        self.base_max_mana = base_max_mana
        self.base_strength = base_strength
        self.base_stamina = base_stamina
        self.base_dexterity = base_dexterity
        self.base_agility = base_agility
        self.base_intelligence = base_intelligence
        self.base_wisdom = base_wisdom
        self.base_charisma = base_charisma

    def save_char(self):
        save_list = []
        save_list.append(self.name)
        save_list.append(self.totalexp)
        save_list.append(self.level)
        save_list.append(self.base_max_health)
        save_list.append(self.base_max_mana)
        save_list.append(self.location)
        save_list.append(self.base_strength)
        save_list.append(self.base_dexterity)
        save_list.append(self.base_agility)
        save_list.append(self.base_intelligence)
        save_list.append(self.base_wisdom)
        save_list.append(self.base_charisma)

        



