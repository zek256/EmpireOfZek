import sys
import sqlite3
import hashlib
import os
from sqlite3 import Error
import time
import threading
import random

database = r"pythonsqlite.db"
name = 'random'
stop_combat = False

#---------------------DATABASE-------------------------
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

conn = create_connection(database)
cur = conn.cursor()

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        #not executing below statement properly
        c.execute(create_table_sql)
    except Error as e:
        print(e)
    
def create_player(conn, name, player_password_key, player_password_salt, player_class, location, health, max_health, mana, base_max_mana, max_mana, base_strength, strength, base_stamina, stamina, base_dexterity, dexterity, base_agility, agility, base_intelligence, intelligence, base_wisdom, wisdom, base_charisma, charisma, equipment_primary, equipment_secondary, equipment_head, equipment_body, equipment_feet, equipment_hands, equipment_legs, equipment_ring):
    """
    Create a Player
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql = """ INSERT INTO Player (
        name,
        player_password_key,
        player_password_salt,
        player_class,
        location,
        health,
        max_health,
        mana,
        base_max_mana,
        max_mana,
        base_strength,
        strength,
        base_stamina,
        stamina,
        base_dexterity,
        dexterity,
        base_agility,
        agility,
        base_intelligence,
        intelligence,
        base_wisdom,
        wisdom,
        base_charisma,
        charisma,
        equipment_primary, 
        equipment_secondary,
        equipment_head,
        equipment_body,
        equipment_feet,
        equipment_hands,
        equipment_legs,
        equipment_ring
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """
    #(id, name, location, totalexp, level, base_max_mana, base_strength, base_stamina, base_dexterity, base_agility, base_intelligence, base_wisdom, base_charisma, equipment_primary, equipment_secondary, equipment_head, equipment_body, equipment_feet, equipment_hands, gold, invetory_slot_1, invetory_slot_2, invetory_slot_3, invetory_slot_4, invetory_slot_5, invetory_slot_6, invetory_slot_7, invetory_slot_8, invetory_slot_9, invetory_slot_10, invetory_slot_11, invetory_slot_12, invetory_slot_13, invetory_slot_14, invetory_slot_15, invetory_slot_16, invetory_slot_17, invetory_slot_18, invetory_slot_19, invetory_slot_20)
    cur = conn.cursor()
    cur.execute(sql, (name, player_password_key, player_password_salt, player_class, location, health, max_health, mana, base_max_mana, max_mana, base_strength, strength, base_stamina, stamina, base_dexterity, dexterity, base_agility, agility, base_intelligence, intelligence, base_wisdom, wisdom, base_charisma, charisma, equipment_primary, equipment_secondary, equipment_head, equipment_body, equipment_feet, equipment_hands, equipment_legs, equipment_ring))
    conn.commit()
    
    Recalibrate_Stats()

def select_all_player(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Player")

    return cur.fetchall()

def Show_NPC(location):

    npc_list = []

    cur.execute("SELECT id FROM Npc WHERE room = ?", (location,))
    npc_id = cur.fetchall()
    cur.execute("SELECT name FROM Npc WHERE room = ?", (location,))
    npc_name = cur.fetchall()
    cur.execute("SELECT level FROM Npc WHERE room = ?", (location,))
    npc_level = cur.fetchall()
    cur.execute("SELECT alive FROM Npc WHERE room = ?", (location,))
    npc_alive = cur.fetchall()
    
    #Don't need all of this***********************************************************************************************************************************************************
    for i in range(0, len(npc_id)):
        npc_temp = []
        npc_temp.append(npc_id[i])
        npc_temp.append(npc_name[i])
        npc_temp.append(npc_level[i])
        npc_temp.append(npc_alive[i])
        npc_list.append(npc_temp)

    return(npc_list)
    
#The below two methods are activated at the beginning of the game, they look to see if there are any dead npcs(from when the player logs out with a dead npc), it then respawns them after 30 seconds. This must occur because the only other way an npc spawns is 30 seconds after its death. So if the player logs out right after kill an npc, there needs to be a way for it to respawn.
def Npc_Initial_Spawn_Helper():

    cur.execute("SELECT id FROM Npc WHERE alive = ?", (0,))
    npc_list = cur.fetchall()

    thread = threading.Thread(target = Npc_Initial_Spawn, args = (npc_list,))
    thread.daemon = True
    thread.start()

def Npc_Initial_Spawn(npc_list):
    
    conn = create_connection(database)
    cur = conn.cursor()

    time.sleep(30)

    for each in npc_list:
        sql = "UPDATE Npc SET alive = ? WHERE id = ?"
        cur.execute(sql, (1, each[0],))
        conn.commit()

def Look():
    cur.execute("SELECT location FROM Player WHERE name = ?", (name,))
    location = cur.fetchall()[0][0]
    cur.execute("SELECT description FROM Room WHERE location = ?", (location,))
    description = cur.fetchall()[0][0]

    print()
    print(description)

    npc_list = Show_NPC(location)

    for each in npc_list:
        if(each[3][0] == 1):
            print("-", end='')
            print(each[1][0], end='')
            print("[Lv. " + str(each[2][0]) + "]-")  

    print()

def Score():
    
    global name

    player_stat_name_list = ["level", "player_class", "totalexp", "rebirths", "health", "max_health", "mana", "max_mana", "base_strength", "base_stamina", "base_dexterity", "base_agility", "base_intelligence", "base_wisdom", "base_charisma", "strength", "stamina", "dexterity", "agility", "intelligence", "wisdom", "charisma"]
    player_stats = {}

    for player_stat_name in player_stat_name_list:
        cur.execute("SELECT " + player_stat_name + " FROM Player WHERE name = ?", (name,))
        player_stats[player_stat_name] = cur.fetchall()[0][0]        
    
    cur.execute("SELECT experience FROM Player_EXP_Table WHERE level = ?", (player_stats["level"] + 1,))
    exp_for_next_level = cur.fetchall()[0][0]
    to_next_level = exp_for_next_level - player_stats["totalexp"]

    dash = '-' * 64
    print()
    print(dash)
    print('{:2s}{:<5s}{:3s}{:<17}{:3}{:<17s}{:3}{:<12}{:3}'.format("| ", "Name", " : ", name, " | ", "Total Experience", " : ", player_stats["totalexp"], " | "))
    print('{:2s}{:<5s}{:3s}{:<17}{:3}{:<17s}{:3}{:<12}{:3}'.format("| ", "Level", " : ", player_stats["level"], " | ", "To Next Level", " : ", to_next_level, " | "))
    print('{:2s}{:<5s}{:3s}{:<17}{:3}{:<17s}{:3}{:<12}{:3}'.format("| ", "Class", " : ", player_stats["player_class"], " | ", "Rebirths", " : ", player_stats["rebirths"], " | "))
    print(dash)
    print('{:2s}{:<15s}{:>1s}{:>4}{:<1s}{:<4}{:3s}{:<32}{:3s}'.format("| ", "Health", ":", player_stats["health"], '/', player_stats["max_health"], " | ", " ", " | "))
    print('{:2s}{:<15s}{:>1s}{:>4}{:<1s}{:<4}{:3s}{:<32}{:3s}'.format("| ", "Mana", ":", player_stats["mana"], '/', player_stats["max_mana"], " | ", " ", " | "))
    print('{:2s}{:<15s}{:>1s}{:>4}{:<1s}{:<4}{:3s}{:<32}{:3s}'.format("| ", "Strength", ":", player_stats["base_strength"], '/', player_stats["strength"], " | ", " ", " | "))
    print('{:2s}{:<15s}{:>1s}{:>4}{:<1s}{:<4}{:3s}{:<32}{:3s}'.format("| ", "Stamina", ":", player_stats["base_stamina"], '/', player_stats["stamina"], " | ", " ", " | "))
    print('{:2s}{:<15s}{:>1s}{:>4}{:<1s}{:<4}{:3s}{:<32}{:3s}'.format("| ", "Dexterity", ":", player_stats["base_dexterity"], '/', player_stats["dexterity"], " | ", " ", " | "))
    print('{:2s}{:<15s}{:>1s}{:>4}{:<1s}{:<4}{:3s}{:<32}{:3s}'.format("| ", "Agility", ":", player_stats["base_agility"], '/', player_stats["agility"], " | ", " ", " | "))
    print('{:2s}{:<15s}{:>1s}{:>4}{:<1s}{:<4}{:3s}{:<32}{:3s}'.format("| ", "Intelligence", ":", player_stats["base_intelligence"], '/', player_stats["intelligence"], " | ", " ", " | "))
    print('{:2s}{:<15s}{:>1s}{:>4}{:<1s}{:<4}{:3s}{:<32}{:3s}'.format("| ", "Wisdom", ":", player_stats["base_wisdom"], '/', player_stats["wisdom"], " | ", " ", " | "))
    print('{:2s}{:<15s}{:>1s}{:>4}{:<1s}{:<4}{:3s}{:<32}{:3s}'.format("| ", "Charisma", ":", player_stats["base_charisma"], '/', player_stats["charisma"], " | ", " ", " | "))
    print(dash)

def Show_Equipment():

    slot_list = ["primary", "secondary", "head", "body", "feet", "hands", "legs", "ring"]
    equipment_id = {}
    equipment_name = {}

    #for i in range(0, 5):
    for each in slot_list:
        cur.execute("select equipment_" + each + " from player where name = ?", (name,))
        equipment_id[each] = cur.fetchall()[0][0]
        cur.execute("select name from Item where id = ?", (equipment_id[each],))
        equipment_name[each] = cur.fetchall()[0][0]

    dash = '-' * 64
    print()
    print(dash)
    for each in slot_list:
        print('{:2s}{:<9s}{:3s}{:<48s}{:2s}'.format("| ", each.capitalize(), " : ", equipment_name[each], " |"))
    
    print(dash)

def Show_Inventory():

    inventory_slot = {}
    inventory_slot_quantity = {}
    inventory_slot_name = {}

    #fetch item integers
    for i in range(1,21):
        cur.execute("SELECT inventory_slot_" + str(i) + " FROM Player WHERE name = ?", (name,))
        inventory_slot[i] = cur.fetchall()[0][0]
        cur.execute("SELECT inventory_slot_" + str(i) + "_quantity FROM Player WHERE name = ?", (name,))
        inventory_slot_quantity[i] = cur.fetchall()[0][0]
        cur.execute("SELECT name FROM Item WHERE id = ?", (inventory_slot[i],))
        inventory_slot_name[i] = cur.fetchall()[0][0]

    #inventory printing
    dash = '-' * 64
    print()
    print(dash)

    for i in range(1,21):
        if(inventory_slot[i] == 0):
            print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", str(i), " : ", inventory_slot_name[i], " |"))
        else:
            print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", str(i), " : ", inventory_slot_name[i] + " x " + str(inventory_slot_quantity[i]), " |"))
    print(dash)

def Show_Buffs():

    buff_id = {}
    buff_name = {}
    buff_timer = {}

    for i in range(1, 11):
        cur.execute("SELECT buff_slot_" + str(i) + " FROM Player WHERE name = ?", (name,))
        buff_id[i] = cur.fetchall()[0][0]
        cur.execute("SELECT name FROM Buff WHERE id = ?", (buff_id[i],))
        buff_name[i] = cur.fetchall()[0][0]
        cur.execute("SELECT buff_slot_" + str(i) + "_timer FROM Player WHERE name = ?", (name,))
        buff_timer[i] = cur.fetchall()[0][0]

    #buff printing
    dash = '-' * 120
    print()
    print(dash)
    print('{:2s}{:3s}{:113s}{:2s}'.format("| ", "", "Current Buffs", " |"))
    print(dash)
    print('{:2s}{:116s}{:2s}'.format("| ", "", " |"))

    #buff slot 1
    for i in range(1, 11):
        if(buff_id[i] > 0):
            print('{:2s}{:>4}{:1s}{:3s}{:<108s}{:2s}'.format("| ", buff_timer[i], "s", " : ", buff_name[i], " |"))

            buff_stat_list = ""
            cur.execute("SELECT max_health FROM Buff WHERE id = ?", (buff_id[i],))
            buff_max_health = cur.fetchall()[0][0]
            if(buff_max_health > 0):
                buff_stat_list = buff_stat_list + "+" + str(buff_max_health) + " Health "
            
            cur.execute("SELECT max_mana FROM Buff WHERE id = ?", (buff_id[i],))
            buff_max_mana = cur.fetchall()[0][0]
            if(buff_max_mana > 0):
                buff_stat_list = buff_stat_list + "+" + str(buff_max_mana) + " Mana "

            cur.execute("SELECT strength FROM Buff WHERE id = ?", (buff_id[i],))
            buff_strength = cur.fetchall()[0][0]
            if(buff_strength > 0):
                buff_stat_list = buff_stat_list + "+" + str(buff_strength) + " Strength "
            
            cur.execute("SELECT stamina FROM Buff WHERE id = ?", (buff_id[i],))
            buff_stamina = cur.fetchall()[0][0]
            if(buff_stamina > 0):
                buff_stat_list = buff_stat_list + "+" + str(buff_stamina) + " Stamina "
            
            cur.execute("SELECT dexterity FROM Buff WHERE id = ?", (buff_id[i],))
            buff_dexterity = cur.fetchall()[0][0]
            if(buff_dexterity > 0):
                buff_stat_list = buff_stat_list + "+" + str(buff_dexterity) + " Dexterity "

            cur.execute("SELECT agility FROM Buff WHERE id = ?", (buff_id[i],))
            buff_agility = cur.fetchall()[0][0]
            if(buff_agility > 0):
                buff_stat_list = buff_stat_list + "+" + str(buff_agility) + " Agility "
            
            cur.execute("SELECT intelligence FROM Buff WHERE id = ?", (buff_id[i],))
            buff_intelligence = cur.fetchall()[0][0]
            if(buff_intelligence > 0):
                buff_stat_list = buff_stat_list + "+" + str(buff_intelligence) + " Intelligence "

            cur.execute("SELECT charisma FROM Buff WHERE id = ?", (buff_id[i],))
            buff_charisma = cur.fetchall()[0][0]
            if(buff_charisma > 0):
                buff_stat_list = buff_stat_list + "+" + str(buff_charisma) + " Charisma"

            print('{:2s}{:8s}{:<108s}{:2s}'.format("| ", "", buff_stat_list, " |"))
            print('{:2s}{:116s}{:2s}'.format("| ", "", " |"))

    print(dash)

def Recalibrate_Stats():

    slot_list = ["primary", "secondary", "head", "body", "feet", "hands", "legs", "ring"]
    equipment = {}
    to_add = {"strength" : 0, "stamina" : 0, "dexterity" : 0, "agility" : 0, "intelligence" : 0, "wisdom" : 0, "charisma" : 0}

    #Iterate through equipment and add stats together
    for slot in slot_list:
        cur.execute("select equipment_" + slot + " from player where name = ?", (name,))
        equipment[slot] = cur.fetchall()[0][0]

        if(equipment[slot] != "0"):
            for stat in to_add:
                cur.execute("select modify_" + stat + " from Item where id = ?", (equipment[slot],))
                to_add[stat] += int(cur.fetchall()[0][0])

    base_stat = {}
    new_stat = {}
    #Get the base stats
    for stat in to_add:
        cur.execute("select base_" + stat + " from Player where name = ?", (name,))
        base_stat[stat] = int(cur.fetchall()[0][0])

    #Add new stats to the base stats
    for stat in to_add:
        new_stat[stat] = base_stat[stat] + to_add[stat]
        cur.execute("update Player set " + stat + " = " + str(new_stat[stat]) + " where name = ?", (name,))

    #HP recalibration with stamina
    max_health = new_stat["stamina"] * 10
    cur.execute("update Player set max_health = " + str(max_health) + " where name = ?", (name,))
    conn.commit()

def Move(direction):
    cur.execute("SELECT location FROM Player WHERE name = ?", (name,))
    location = cur.fetchall()[0][0]
    cur.execute("SELECT north FROM Room WHERE location = ?", (location,))
    north = cur.fetchall()[0][0]
    cur.execute("SELECT south FROM Room WHERE location = ?", (location,))
    south = cur.fetchall()[0][0]
    cur.execute("SELECT east FROM Room WHERE location = ?", (location,))
    east = cur.fetchall()[0][0]
    cur.execute("SELECT west FROM Room WHERE location = ?", (location,))
    west = cur.fetchall()[0][0]

    if(direction == 'north' or direction == 'n'):
        if(north == 0):
            print("You cannot go that way.")
        else:
            location += 100
            sql = "UPDATE Player SET location = ? WHERE name = ?"
            cur.execute(sql, (location, name,))
            conn.commit()
    elif(direction == 'south' or direction == 's'):
        if(south == 0):
            print()
            print("You cannot go that way.")
            print()
        else:
            location -= 100
            sql = "UPDATE Player SET location = ? WHERE name = ?"
            cur.execute(sql, (location, name,))
            conn.commit()
    elif(direction == 'east' or direction == 'e'):
        if(east == 0):
            print()
            print("You cannot go that way.")
            print()
        else:
            location += 1
            sql = "UPDATE Player SET location = ? WHERE name = ?"
            cur.execute(sql, (location, name,))
            conn.commit()
    elif(direction == 'west' or direction == 'w'):
        if(west == 0):
            print()
            print("You cannot go that way.")
            print()
        else:
            location -= 1
            sql = "UPDATE Player SET location = ? WHERE name = ?"
            cur.execute(sql, (location, name,))
            conn.commit()

    Look()
    
def Get_Health(stamina):
    return stamina * 10
    

def Level_Up():
    
    cur.execute("SELECT player_class FROM Player WHERE name = ?", (name,))
    player_class = cur.fetchall()[0][0]
    cur.execute("SELECT level FROM Player WHERE name = ?", (name,))
    level = cur.fetchall()[0][0]
    level += 1
    sql = "UPDATE Player SET level = ? WHERE name = ?"
    cur.execute(sql, (level, name,))
    conn.commit()

    player_base_stat_name_list = ["base_strength", "base_stamina", "base_dexterity", "base_agility", "base_intelligence", "base_wisdom", "base_charisma"]   
    player_base_stats = {}
    
    for player_base_stat_name in player_base_stat_name_list:
        cur.execute("SELECT " + player_base_stat_name + " FROM Player WHERE name = ?", (name,))
        player_base_stats[player_base_stat_name] = cur.fetchall()[0][0]

    if(player_class == "Warrior"):

        add_stats = {}
        for player_base_stat_name in player_base_stat_name_list:
            cur.execute("SELECT " + player_base_stat_name + " FROM Warrior_Level_Up WHERE level = ?", (level,))
            add_stats[player_base_stat_name] = cur.fetchall()[0][0]
            player_base_stats[player_base_stat_name] += add_stats[player_base_stat_name]
            cur.execute("UPDATE Player SET " + player_base_stat_name + " = ? WHERE name = ?", (player_base_stats[player_base_stat_name], name,))
        conn.commit()      

    Recalibrate_Stats()
    print("Welcome to level " + str(level) + "!!")
    for player_base_stat_name in player_base_stat_name_list:
        print(player_base_stat_name[5:].capitalize() + " has increased by " + str(add_stats[player_base_stat_name]) + " points.")


def Combat(npc_id):

    conn = create_connection(database)
    cur = conn.cursor()

    global stop_combat
    stop_combat = False
    win = False

    #-----------------------NPC_STATS----------------------------------
    npc_stat_list = ["name", "level", "health", "max_health", "mana", "max_mana", "dexterity", "agility", "intelligence", "wisdom", "charisma", "min_damage", "max_damage"]
    npc_stats = {}

    for npc_stat_name in npc_stat_list:
        cur.execute("SELECT " + npc_stat_name + " FROM Npc WHERE id = ?", (npc_id,))
        npc_stats[npc_stat_name] = cur.fetchall()[0][0]

    #-------------------------PLAYER_STATS-------------------------------------
    player_stat_list = ["level", "health", "max_health", "mana", "max_mana", "strength", "stamina", "dexterity", "agility", "intelligence", "wisdom", "charisma", "totalexp"]
    player_stats = {}

    for player_stat_name in player_stat_list:
        cur.execute("SELECT " + player_stat_name + " FROM Player WHERE name = ?", (name,))
        player_stats[player_stat_name] = cur.fetchall()[0][0]

    cur.execute("SELECT experience FROM Player_EXP_Table WHERE level = ?", (player_stats["level"],))
    current_level_exp = cur.fetchall()[0][0]
    cur.execute("SELECT experience FROM Player_EXP_Table WHERE level = ?", (player_stats["level"] + 1,))
    next_level_exp = cur.fetchall()[0][0]
        
    level_tnl = next_level_exp - current_level_exp
    player_exp_percent = round((player_stats["totalexp"] - current_level_exp) / level_tnl * 100, 5)
    
    #-------------------------PLAYER_EQUIPMENT---------------------------------
    cur.execute("SELECT equipment_primary FROM Player WHERE name = ?", (name,))
    equipment_primary = cur.fetchall()[0][0]
    cur.execute("SELECT equipment_secondary FROM Player WHERE name = ?", (name,))
    equipment_secondary = cur.fetchall()[0][0]

    if(equipment_primary > 0):
        cur.execute("SELECT damage_min FROM Item WHERE id = ?", (equipment_primary,))
        player_damage_min = cur.fetchall()[0][0]
        cur.execute("SELECT damage_max FROM Item WHERE id = ?", (equipment_primary,))
        player_damage_max = cur.fetchall()[0][0]
    else:
        player_damage_min = 1
        player_damage_max = 1

    player_damage_min += player_stats["strength"]
    player_damage_max += player_stats["strength"]

    #--------------------------HIT_CHANCE--------------------------------------
    player_hit_chance = round(player_stats["dexterity"] / npc_stats["agility"] * 80)
    npc_hit_chance = round(npc_stats["dexterity"] / player_stats["agility"] * 80)
    #print("NPC hit chance")
    #print(npc_hit_chance)

    while(True):
        if(stop_combat):
            break

        print()
        player_hit_roll = random.randrange(1, 100)
        #print("player hit chance: ", end='')
        #print(player_hit_chance)
        #print("player hit roll: ", end='')
        #print(player_hit_roll)
        if(player_hit_roll < player_hit_chance):
            player_damage = random.randrange(player_damage_min, player_damage_max + 1)
            print(name + " hits " + npc_stats["name"] + " for " + str(player_damage) + " points of damage.")
            npc_stats["health"] -= player_damage
            if(npc_stats["health"] < 0):
                npc_stats["health"] = 0
            sql = "UPDATE Npc SET health = ? WHERE id = ?"
            cur.execute(sql, (npc_stats["health"], npc_id,))
            conn.commit()
        else:
            print(name + " misses " + npc_stats["name"] + ".")

        npc_hit_roll = random.randrange(1, 100)
        #print("npc hit chance: ", end='')
        #print(npc_hit_chance)
        #print("npc hit roll: ", end='')
        #print(npc_hit_roll)
        if(npc_hit_roll < npc_hit_chance):
            npc_damage = random.randrange(npc_stats["min_damage"], npc_stats["max_damage"] + 1)
            print(npc_stats["name"] + " hits " + name + " for " + str(npc_damage) + " points of damage.")
            player_stats["health"] -= npc_damage
            if(player_stats["health"] < 0):
                player_stats["health"] = 0
            sql = "UPDATE Player SET health = ? WHERE name = ?"
            cur.execute(sql, (player_stats["health"], name,))
            conn.commit()
        else:
            print(npc_stats["name"] + " misses " + name + ".")
        print("[", end='')
        print(player_stats["health"], end='')
        print("/", end='')
        print(player_stats["max_health"], end=' ')
        print("(", end='')
        print("{:0.2f}".format(player_stats["health"] / player_stats["max_health"] * 100), end='')
        print("%) ", end='')
        print(player_stats["mana"], end='')
        print("/", end='')
        print(player_stats["max_mana"], end=' ')
        print("(", end='')
        print("{:0.2f}".format(player_stats["mana"] / player_stats["max_mana"] * 100), end='')
        print("%) ", end='')
        print("EXP: ", end='')
        print("{:0.2f}".format(player_exp_percent), end='')
        print("%", end='')
        print(" ENEMY: ", end='')
        print(npc_stats["health"], end='')
        print("/", end='')
        print(npc_stats["max_health"], end=' ')
        print("(", end='')
        print("{:0.2f}".format(npc_stats["health"] / npc_stats["max_health"] * 100), end='')
        print("%) ", end='')
        print("]", end='')
        #print(">", end='')
        print(">")
        time.sleep(3)

        if(player_stats["health"] <= 0):
            print("You have been slain by " + npc_stats["name"])
            stop_combat = True
            sql = "UPDATE Player SET location = ? WHERE name = ?"
            cur.execute(sql, (550, name,))
            conn.commit()
            break
        if(npc_stats["health"] <= 0):
            print()
            print(str(npc_stats["name"]) + " has been slain.")
            sql = "UPDATE Npc SET alive = ? WHERE id = ?"
            cur.execute(sql, (0, npc_id,))
            conn.commit()

            cur.execute("SELECT experience FROM NPC_EXP_Table WHERE level = ?", (npc_stats["level"],))
            exp_gain = cur.fetchall()[0][0]
            player_stats["totalexp"] += exp_gain
            sql = "UPDATE Player SET totalexp = ? WHERE name = ?"
            cur.execute(sql, (player_stats["totalexp"], name,))
            conn.commit()
            print("You have gained " + str(exp_gain) + " experience points.")
            stop_combat = True
            win = True
            thread = threading.Thread(target = Npc_Respawn, args = (npc_id,))
            thread.daemon = True
            thread.start()
            break


    #Awarding EXP
    if(win == True):
        #Award EXP directly
        pass



    conn.close()

def Precombat(choice):
    global stop_combat
    stop_combat = False
    npc_list = Show_NPC()
    found_fight = 0
    conn = create_connection(database)
    cur = conn.cursor()

    npc = choice.lower()[5:]

    for each in npc_list:
        if(found_fight == 0):
            if(npc == each[1][0] and each[3][0] == 1):
                found_fight = 1
                npc_id = each[0][0]

                conn = create_connection(database)
                cur = conn.cursor()
                conn.close()
                    
                thread = threading.Thread(target = Combat, args = (npc_id,))
                thread.daemon = True
                thread.start()

                while True:
                    choice = input("")
                    if(choice == 'flee'):
                        stop_combat = True
                        #thread.join()
                        time.sleep(2)
                        break
                    elif(stop_combat == True):
                        break
                    
                conn = create_connection(database)
                cur = conn.cursor()

    level = Get_Stat("level")
    
    cur.execute("SELECT experience FROM Player_EXP_Table WHERE level = ?", (level + 1,))
    exp_needed_to_level = cur.fetchall()[0][0]

    if(level < 50):
        if(Get_Stat("totalexp") >= exp_needed_to_level):
            Level_Up()

def Health_Regen():

    while(True):
    
        conn = create_connection(database)
        cur = conn.cursor()

        time.sleep(5)

        cur.execute("SELECT health FROM Player WHERE name = ?", (name,))
        health = cur.fetchall()[0][0]
        cur.execute("SELECT max_health FROM Player WHERE name = ?", (name,))
        max_health = cur.fetchall()[0][0]

        health += round(max_health * 0.1)

        if(health > max_health):
            health = max_health

        sql = "UPDATE Player SET health = ? WHERE name = ?"
        cur.execute(sql, (health, name,))
        conn.commit()
        conn.close()

def Health_Regen_Initiate():
    thread = threading.Thread(target = Health_Regen)
    thread.daemon = True
    thread.start()
    
#Respawns NPCs immediately after death
def Npc_Respawn(npc_id):
    conn = create_connection(database)
    cur = conn.cursor()

    time.sleep(30)

    cur.execute("UPDATE Npc SET alive = ? WHERE id = ?", (1, npc_id,))
    conn.commit()

    cur.execute("SELECT max_health FROM Npc WHERE id = ?", (npc_id,))
    max_health = cur.fetchall()[0][0]

    cur.execute("UPDATE Npc SET health = ? WHERE id = ?", (max_health, npc_id,))
    conn.commit()
    conn.close()

def Equip_Item(item):

    #Get the ID of item player is trying to equip
    item_id = Get_Item_Id(item)
    item_slot = Get_Item_Equip_Slot(item)
    item_level_requirement = Get_Item_Level_Requirement(item)
    player_level = Get_Stat("level")
    item_is_in_inventory = False
    inventory_slot_id_for_found_item = None

    #If item exists in general
    if(item_id != None and item_id != 0):
        if(item_slot != None):
            #Fetch player inventory from database
            for i in range(1, 21):
                cur.execute("SELECT inventory_slot_" + str(i) + " FROM Player WHERE name = ?", (name,))
                inventory_slot_id = cur.fetchall()[0][0]
                #Is the item in inventory?
                if(inventory_slot_id == item_id):
                    cur.execute("SELECT inventory_slot_" + str(i) + "_quantity FROM Player WHERE name = ?", (name,))
                    inventory_slot_quantity = cur.fetchall()[0][0]
                    item_is_in_inventory = True
                    inventory_slot_id_for_found_item = i
                    break
            if(item_is_in_inventory and inventory_slot_quantity > 0):
                if(player_level >= item_level_requirement):
                    Inventory_Swap(item_slot, item_id, inventory_slot_quantity, inventory_slot_id_for_found_item, item)
                else:
                    print("You are not powerful enough to equip this item.")
            else:
                print("You do not possess such item.")
        else:
            print("You cannot equip this item")
    else:
        print("The item you described does not exist in this universe.")
        
#Still need to account for dual wielding        
def Inventory_Swap(item_slot, item_id, inventory_slot_quantity, inventory_slot_id_for_found_item, item):
    global cur
    cur.execute("SELECT equipment_" + item_slot + " FROM Player WHERE name = ?", (name,))
    #Item ID of equipped item
    current_equipment = cur.fetchall()[0][0]
    if(current_equipment != item_id):
        previously_equipped_inventory_slot_quantity = 0
        for i in range(1, 21):
            cur.execute("SELECT inventory_slot_" + str(i) + " FROM Player WHERE name = ?", (name,))
            previously_equipped_inventory_slot_id = cur.fetchall()[0][0]
            if(previously_equipped_inventory_slot_id == current_equipment):
                cur.execute("SELECT inventory_slot_" + str(i) + "_quantity FROM Player WHERE name = ?", (name,))
                previously_equipped_inventory_slot_quantity = cur.fetchall()[0][0]
                previously_equipped_item_is_in_inventory = True
                previously_equipped_inventory_slot_id_for_found_item = i
                break                        

        #If the item in inventory has quantity of more than one and the previously equipped item also exists in inventory
        #In this case decrement the one to be equipped and increment the one being de-equipped
        if(inventory_slot_quantity > 1 and previously_equipped_inventory_slot_quantity > 0):
            #Reduce quantity in current inventory
            cur.execute("update Player set inventory_slot_" + str(inventory_slot_id_for_found_item) + "_quantity = ? WHERE name = ?", (inventory_slot_quantity - 1, name,))
            #Increase quantity of previously equipped item in inventory
            cur.execute("update Player set inventory_slot_" + str(previously_equipped_inventory_slot_id_for_found_item) + "_quantity = ? WHERE name = ?", (previously_equipped_inventory_slot_quantity + 1, name,))
            cur.execute("update Player set equipment_" + item_slot + " = ? WHERE name = ?", (item_id, name,))
        #If the item in inventory has quantity of more than one but the one already equipped doesn't exist in inventory
        #In this case decrement the one to be equipped and ensure there's an empty spot in inventory for the currently equipped item to go
        elif(inventory_slot_quantity > 1 and previously_equipped_inventory_slot_quantity == 0):
            #Is there an empty spot in the inventory for the currently equipped item to go?
            empty_inventory_slot = Is_There_Empty_Slot_In_Inventory()
            if(empty_inventory_slot):
                #Reduce quantity in current inventory
                cur.execute("update Player set inventory_slot_" + str(inventory_slot_id_for_found_item) + "_quantity = ? WHERE name = ?", (inventory_slot_quantity - 1, name,))                                    
                cur.execute("update Player set inventory_slot_" + str(empty_inventory_slot) + " = ? WHERE name = ?", (current_equipment, name,))
                cur.execute("update Player set inventory_slot_" + str(empty_inventory_slot) + "_quantity = ? WHERE name = ?", (1, name,))
                cur.execute("update Player set equipment_" + item_slot + " = ? WHERE name = ?", (item_id, name,))
            else:
                print("You don't have room in your inventory for the currently equipped item.")
        #If the item in inventory only has one but the item to be equipped also exists in inventory
        #In this case replace inventory item with item ID 0 (Nothing), and increment the quantity in inventory of item being de-equipped
        elif(inventory_slot_quantity == 1 and previously_equipped_inventory_slot_quantity > 0):
            #Increment currently equipped, set inventory to 0 (Nothing)
            #Increase quantity of previously equipped item in inventory
            cur.execute("update Player set inventory_slot_" + str(previously_equipped_inventory_slot_id_for_found_item) + "_quantity = ? WHERE name = ?", (previously_equipped_inventory_slot_quantity + 1, name,))                            
            #Update inventory id to 0 for the item to be equipped
            cur.execute("update Player set inventory_slot_" + str(inventory_slot_id_for_found_item) + " = ? WHERE name = ?", (0, name,))
            cur.execute("update Player set equipment_" + item_slot + " = ? WHERE name = ?", (item_id, name,))                                                         
        else:
            cur.execute("update Player set inventory_slot_" + str(inventory_slot_id_for_found_item) + " = ? WHERE name = ?", (current_equipment, name,))
            cur.execute("update Player set equipment_" + item_slot + " = ? WHERE name = ?", (item_id, name,))
        conn.commit()
        print("You are now using " + item + ".")
    else:
        print("You already have that equipped.")

    Recalibrate_Stats()

def Is_There_Empty_Slot_In_Inventory():
    empty_inventory_slot = None
    for i in range(1, 21):
        cur.execute("SELECT inventory_slot_" + str(i) + " FROM Player WHERE name = ?", (name,))
        temp_slot = cur.fetchall()[0][0]
        if(temp_slot == 0):
            empty_inventory_slot = i
            return empty_inventory_slot

def Is_Item_In_Inventory(item_id):
    item_exists_in_inventory_slot = None
    for i in range(1, 21):
        cur.execute("SELECT inventory_slot_" + str(i) + " FROM Player WHERE name = ?", (name,))
        temp_slot = cur.fetchall()[0][0]
        if(temp_slot == item_id):
            item_exists_in_inventory_slot = i
            return item_exists_in_inventory_slot

def Is_Item_Equipped(item_id):
    is_item_equipped = False
    #See if item is actually equipped
    slot_list = ["equipment_primary", "equipment_secondary", "equipment_head", "equipment_body", "equipment_feet", "equipment_hands", "equipment_legs", "equipment_ring"]
    for slot_name in slot_list:
        cur.execute("SELECT " + slot_name + " FROM Player WHERE name = ?", (name,))
        equipped_id = cur.fetchall()[0][0]
        if(item_id == equipped_id):
            is_item_equipped =  True
            return is_item_equipped
            
            #Clear the slot to Empty
            #cur.execute("update Player set " + slot_name + " = ? where name = ?", (0, name))


def Remove_Item(item_name):
    item_id = Get_Item_Id(item_name)
    item_slot = Get_Item_Equip_Slot(item_name)
    item_is_equipped = False

    #Is item already in inventory?
    is_item_in_inventory = Is_Item_In_Inventory(item_id)
    is_item_equipped = Is_Item_Equipped(item_id)
    if(not(is_item_equipped)):
        print("That item is not equipped.")
    elif(is_item_in_inventory and is_item_equipped):
        cur.execute("update Player set equipment_" + str(item_slot) + " = ? where name = ?", (0, name,))
        cur.execute("select inventory_slot_" + str(is_item_in_inventory) + "_quantity from Player where name = ?", (name,))
        previous_quantity = cur.fetchall()[0][0]
        cur.execute("update Player set inventory_slot_" + str(is_item_in_inventory) + "_quantity = ? where name = ?", (previous_quantity + 1, name))
        conn.commit()
        print("You remove " + item_name + ".")
    elif(not(is_item_in_inventory) and is_item_equipped):
        #Is there an empty spot in the inventory for the currently equipped item to go?
        empty_inventory_slot = Is_There_Empty_Slot_In_Inventory()
        if(empty_inventory_slot):
            cur.execute("update Player set equipment_" + str(item_slot) + " = ? where name = ?", ("0", name,))
            cur.execute("update Player set inventory_slot_" + str(empty_inventory_slot) + " = ? WHERE name = ?", (item_id, name,))
            cur.execute("update Player set inventory_slot_" + str(empty_inventory_slot) + "_quantity = ? WHERE name = ?", ("1", name,))
            conn.commit()
            print("You remove " + item_name + ".")
        else:
            print("You don't have room in your inventory for the currently equipped item.")
    Recalibrate_Stats()            




#Takes in the item name as a string
def Get_Item_Id(item_name):
    global cur
    cur.execute("select count(name) from Item where name = ?", (item_name,))
    count = cur.fetchall()[0][0]
    #If it has an ID (aka if it exists as an item in the world) then set item_id
    if(count > 0):
        cur.execute("select id from Item where name = ?", (item_name,))
        item_id = cur.fetchall()[0][0]
        return item_id
    else:
        return None

#Takes in the item name as a string    
def Get_Item_Equip_Slot(item_name):
    global cur
    cur.execute("select count(name) from Item where name = ?", (item_name,))
    count = cur.fetchall()[0][0]
    #If it has an ID (aka if it exists as an item in the world) then set item_slot
    if(count > 0):
        cur.execute("select slot from Item where name = ?", (item_name,))
        item_equipment_slot = cur.fetchall()[0][0]
        return item_equipment_slot
    else:
        return None

def Get_Item_Level_Requirement(item_name):
    global cur
    cur.execute("select count(name) from Item where name = ?", (item_name,))
    count = cur.fetchall()[0][0]
    #If it has an ID (aka if it exists as an item in the world) then set item_slot
    if(count > 0):
        cur.execute("select level_requirement from Item where name = ?", (item_name,))
        item_level_requirement = cur.fetchall()[0][0]
        return item_level_requirement
    else:
        return None     

def Get_Stat(stat):
    global cur
    global name
    cur.execute("select " + stat + " from Player where name = ?", (name,))
    value = cur.fetchall()[0][0]
    return value
    
def Command(choice):
    choice = choice.lower()
    if(choice == 'north' or choice == 'n' or choice == 'south' or choice == 's' or choice == 'east' or choice == 'e' or choice == 'west' or choice == 'w'):
        Move(choice)
    elif(choice == 'score' or choice == 'character'):
        Score()
    elif(choice == 'look' or choice == 'l'):
        Look()
    elif(choice == 'equipment'):
        Show_Equipment()
    elif(choice == 'inventory'):
        Show_Inventory()
    elif(choice == 'buffs'):
        Show_Buffs()
    elif(choice[0:4] == 'kill'):
        Precombat(choice)
    elif(choice == ''):
        pass
    elif(choice[0:5] == 'equip'):
        Equip_Item(choice[6:])
    elif(choice[0:6] == 'remove'):
        Remove_Item(choice[7:])
    elif(choice == 'quit' or choice == 'camp'):
        print("You have left the realm.")
        Login()
    else:
        print("That is not a valid command.")
        print()

def Login():
    global cur
    global name
    login_loop = True
    while(login_loop):

        print()
        print("New")
        print("Load")
        print("Delete")
        print("Quit")
        choice = input(">")
        choice = choice.lower()
    
    
        if(choice == "load"):
            login_loop = LoadCharacter()
        elif(choice == "new"):
            login_loop = CreateCharacter()                    
        elif(choice == "delete"):
            DeleteCharacter()
        elif(choice == "quit"):
            sys.exit()
    Look()

def LoadCharacter():
    global cur
    global name
    invalid = True
    while(invalid == True):
        tempString = select_all_player(conn)
        print()
        print("--------------------------------------------------------")
        for each in tempString:
            print(each[0])
        print("--------------------------------------------------------")
        print("Which name would you like to load?")
        name = input(">")
        name = name.lower().capitalize()

        cur.execute("SELECT count(*) FROM Player WHERE name = ?", (name,))
        if(cur.fetchall()[0][0] == 1):
            invalid = False
        else:
            print("That is not a valid character, please try again.")
    
    invalid = True
    while(invalid == True):
        print()
        print("Please enter your password.")
        password = input(">")

        #Verifying password
        cur.execute("SELECT player_password_salt FROM Player WHERE name = ?", (name,))
        player_password_salt = cur.fetchall()[0][0]
        cur.execute("SELECT player_password_key FROM Player WHERE name = ?", (name,))
        player_password_key = cur.fetchall()[0][0]

        new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), player_password_salt, 100000)

        if(player_password_key == new_key):
            invalid = False
        else:
            print()
            print("Your password was incorrect.")

    print("Welcome back ", end='')
    print(name, end='')
    print("!")
    login_loop = False
    
def CreateCharacter():
    global cur
    global name
    invalid = True
    while(invalid == True):
        print()
        print("What is your name?")
        name = input(">")
        name = name.lower().capitalize()

        cur = conn.cursor()
        cur.execute("SELECT count(*) FROM Player WHERE name = ?", (name,))
        if(len(name) >= 17):
            print()
            print("The name can't be longer than 17 characters.")
        elif(cur.fetchall()[0][0] == 0):
            invalid = False
        else:
            print()
            print("That character already exists, please try again.")

    invalid = True
    while(invalid == True):
        print()
        print("What would you like your password to be?")
        password1 = input(">")
        print()
        print("Please enter it in again")
        password2 = input(">")
        if(password1 == password2):
            invalid = False
            password = password1
        else:
            print()
            print("Your passwords did not match, please try again.")

        # Example generation
        player_password_salt = os.urandom(32)
        player_password_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), player_password_salt, 100000)

        # Store them as:
        final_password_hash = player_password_salt + player_password_key 

    invalid = True
    while(invalid == True):
        print()
        print("Which class will you choose?")
        print("Warrior")
        choice = input(">")
        print()
        if(choice.lower() == "warrior"):
            invalid = False
            player_class = "Warrior"
        else:
            print()
            print("Please select a valid class.")
    
    if(player_class == "Warrior"):
        location = 550
        mana = 1
        base_max_mana = 1
        max_mana = 1
        base_strength = 10
        strength = 10
        base_stamina = 3
        stamina = 3
        base_dexterity = 5
        dexterity = 5
        base_agility = 5
        agility = 5
        base_intelligence = 3
        intelligence = 3
        base_wisdom = 3
        wisdom = 3
        base_charisma = 5
        charisma = 5
        health = Get_Health(stamina)
        max_health = Get_Health(stamina)
        equipment_primary = 1
        equipment_secondary = 0
        equipment_head = 0
        equipment_body = 2000
        equipment_feet = 0
        equipment_hands = 0
        equipment_legs = 0
        equipment_ring = 0
        create_player(conn, name, final_password_hash[32:], final_password_hash[:32], player_class, location, health, max_health, mana, base_max_mana, max_mana, base_strength, strength, base_stamina, stamina, base_dexterity, dexterity, base_agility, agility, base_intelligence, intelligence, base_wisdom, wisdom, base_charisma, charisma, equipment_primary, equipment_secondary, equipment_head, equipment_body, equipment_feet, equipment_hands, equipment_legs, equipment_ring)
    
    print()
    print("Welcome, " + name + " to the Empire of Zek!")
    return False

def DeleteCharacter():
    global cur
    global name    
    invalid = True
    while(invalid == True):
        tempString = select_all_player(conn)
        print()
        for each in tempString:
            print(each[0])
        
        print()
        print("Which character would you like to delete?")
        name = input(">")
        name = name.lower().capitalize()

        cur = conn.cursor()
        cur.execute('SELECT count(*) FROM Player WHERE name = ?', (name,))
        if(cur.fetchall()[0][0] == 1):
            invalid = False
        else:
            print("That is not a valid character, please try again.")
    invalid = True
    while(invalid == True):
        print()
        print("Please enter your password.")
        password = input(">")

        #Verifying password
        cur.execute("SELECT player_password_salt FROM Player WHERE name = ?", (name,))
        player_password_salt = cur.fetchall()[0][0]
        cur.execute("SELECT player_password_key FROM Player WHERE name = ?", (name,))
        player_password_key = cur.fetchall()[0][0]

        new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), player_password_salt, 100000)

        if(player_password_key == new_key):
            invalid = False
            print(name, end ="")
            print(" has been removed from the Empire of Zek for eternity.")
            delete_player(conn, name)
        else:
            print()
            print("Your password was incorrect.")    

def Show_Prompt():
    
    stat_name_list = ["health", "max_health", "mana", "max_mana", "level", "totalexp"]
    stats = {}

    for stat_name in stat_name_list:
        stats[stat_name] = Get_Stat(stat_name)
    
    cur.execute("SELECT experience FROM Player_EXP_Table WHERE level = ?", (stats["level"],))
    stats["current_level_exp"] = cur.fetchall()[0][0]
    cur.execute("SELECT experience FROM Player_EXP_Table WHERE level = ?", (stats["level"] + 1,))
    stats["next_level_exp"] = cur.fetchall()[0][0]
    
    stats["level_tnl"] = stats["next_level_exp"] - stats["current_level_exp"]
    stats["exp_percent"] = round((stats["totalexp"] - stats["current_level_exp"]) / stats["level_tnl"] * 100, 5)
    print("[", end='')
    print(stats["health"], end='')
    print("/", end='')
    print(stats["max_health"], end=' ')
    print("(", end='')
    print("{:0.2f}".format(stats["health"] / stats["max_health"] * 100), end='')
    print("%) ", end='')
    print(stats["mana"], end='')
    print("/", end='')
    print(stats["max_mana"], end=' ')
    print("(", end='')
    print("{:0.2f}".format(stats["mana"] / stats["max_mana"] * 100), end='')
    print("%) ", end='')
    print("EXP: ", end='')
    print("{:0.2f}".format(stats["exp_percent"]), end='')
    print("%", end='')
    print("]", end='')
    print(">", end='')

def MainLoop():
    while(True):
        Show_Prompt()
        choice = input()
        Command(choice)

#------------------------MAIN--------------------------
def main():

    Login()
    Health_Regen_Initiate()
    Npc_Initial_Spawn_Helper()
    MainLoop()

main()