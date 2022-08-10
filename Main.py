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

#-----------------------GET_STAT-----------------------
#cur.execute('SELECT name FROM Player WHERE pid = ?', (pid,))
#print(cur.fetchall())

#-----------------------SET_STAT-----------------------
#sql = "UPDATE Player SET base_strength = '5' WHERE pid = ?"
#cur = conn.cursor()
#cur.execute(sql, (pid,))
#conn.commit()

#Location_Dictionary_Description = {550:"You are at the town square inside of the Great Citadel. \nObvious exits:\nnorth - The Tavern\nsouth - The Main Road\nwest - The Gilded Greatsword\neast - The Cathedral"}

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
    
def create_player(conn, name, player_password_key, player_password_salt, player_class, health, max_health, mana, base_max_mana, max_mana, base_strength, strength, base_stamina, stamina, base_dexterity, dexterity, base_agility, agility, base_intelligence, intelligence, base_wisdom, wisdom, base_charisma, charisma, equipment_primary, equipment_secondary, equipment_head, equipment_body, equipment_feet, equipment_hands, equipment_legs, equipment_ring):
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
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """
    #(id, name, location, totalexp, level, base_max_mana, base_strength, base_stamina, base_dexterity, base_agility, base_intelligence, base_wisdom, base_charisma, equipment_primary, equipment_secondary, equipment_head, equipment_body, equipment_feet, equipment_hands, gold, invetory_slot_1, invetory_slot_2, invetory_slot_3, invetory_slot_4, invetory_slot_5, invetory_slot_6, invetory_slot_7, invetory_slot_8, invetory_slot_9, invetory_slot_10, invetory_slot_11, invetory_slot_12, invetory_slot_13, invetory_slot_14, invetory_slot_15, invetory_slot_16, invetory_slot_17, invetory_slot_18, invetory_slot_19, invetory_slot_20)
    cur = conn.cursor()
    cur.execute(sql, (name, player_password_key, player_password_salt, player_class, health, max_health, mana, base_max_mana, max_mana, base_strength, strength, base_stamina, stamina, base_dexterity, dexterity, base_agility, agility, base_intelligence, intelligence, base_wisdom, wisdom, base_charisma, charisma, equipment_primary, equipment_secondary, equipment_head, equipment_body, equipment_feet, equipment_hands, equipment_legs, equipment_ring))
    conn.commit()

def create_room(conn, location, description, npc1, npc1_existence, npc2, npc2_existence, npc3, npc3_existence, npc4, npc4_existence, npc5, npc5_existence, npc6, npc6_existence, npc7, npc7_existence, npc8, npc8_existence, npc9, npc9_existence, npc10, npc10_existence, npc11, npc11_existence, npc12, npc12_existence, npc13, npc13_existence, npc14, npc14_existence, npc15, npc15_existence, npc16, npc16_existence, npc17, npc17_existence, npc18, npc18_existence, npc19, npc19_existence, npc20, npc20_existence):
    """
    Create a Room
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql = """ INSERT INTO Room (
        location,
        description,
        npc1,
        npc1_existence,
        npc2,
        npc2_existence,
        npc3,
        npc3_existence,
        npc4,
        npc4_existence,
        npc5,
        npc5_existence,
        npc6,
        npc6_existence,
        npc7,
        npc7_existence,
        npc8,
        npc8_existence,
        npc9,
        npc9_existence,
        npc10,
        npc10_existence,
        npc11,
        npc11_existence,
        npc12,
        npc12_existence,
        npc13,
        npc13_existence,
        npc14,
        npc14_existence,
        npc15,
        npc15_existence,
        npc16,
        npc16_existence,
        npc17,
        npc17_existence,
        npc18,
        npc18_existence,
        npc19,
        npc19_existence,
        npc20,
        npc20_existence
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """
    #(id, name, location, totalexp, level, base_max_mana, base_strength, base_stamina, base_dexterity, base_agility, base_intelligence, base_wisdom, base_charisma, equipment_primary, equipment_secondary, equipment_head, equipment_body, equipment_feet, equipment_hands, gold, invetory_slot_1, invetory_slot_2, invetory_slot_3, invetory_slot_4, invetory_slot_5, invetory_slot_6, invetory_slot_7, invetory_slot_8, invetory_slot_9, invetory_slot_10, invetory_slot_11, invetory_slot_12, invetory_slot_13, invetory_slot_14, invetory_slot_15, invetory_slot_16, invetory_slot_17, invetory_slot_18, invetory_slot_19, invetory_slot_20)
    cur = conn.cursor()
    cur.execute(sql, (location, description, npc1, npc1_existence, npc2, npc2_existence, npc3, npc3_existence, npc4, npc4_existence, npc5, npc5_existence, npc6, npc6_existence, npc7, npc7_existence, npc8, npc8_existence, npc9, npc9_existence, npc10, npc10_existence, npc11, npc11_existence, npc12, npc12_existence, npc13, npc13_existence, npc14, npc14_existence, npc15, npc15_existence, npc16, npc16_existence, npc17, npc17_existence, npc18, npc18_existence, npc19, npc19_existence, npc20, npc20_existence))
    conn.commit()

def select_all_player(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Player")

    return cur.fetchall()

def select_player(conn, name):

    cur = conn.cursor()
    cur.execute('SELECT * FROM Player WHERE name = ?', (name,))

    return cur.fetchall()

def delete_player(conn, name):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql = 'DELETE FROM Player WHERE name=?'
    cur = conn.cursor()
    cur.execute(sql, (name,))
    conn.commit()

def delete_all_player(conn):
    """
    Delete all rows in the tasks table
    :param conn: Connection to the SQLite database
    :return:
    """
    sql = 'DELETE FROM Player'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def count_player(conn):

    sql = 'SELECT COUNT(*) FROM Player'
    cur = conn.cursor()
    cur.execute(sql)

    count = cur.fetchall()

    return count

def Show_NPC():

    npc_list = []

    cur.execute("SELECT location FROM Player WHERE name = ?", (name,))
    location = cur.fetchall()[0][0]

    cur.execute("SELECT id FROM Npc WHERE room = ?", (location,))
    npc_id = cur.fetchall()
    cur.execute("SELECT name FROM Npc WHERE room = ?", (location,))
    npc_name = cur.fetchall()
    cur.execute("SELECT level FROM Npc WHERE room = ?", (location,))
    npc_level = cur.fetchall()
    cur.execute("SELECT alive FROM Npc WHERE room = ?", (location,))
    npc_alive = cur.fetchall()
    
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
    cur = conn.cursor()
    cur.execute("SELECT location FROM Player WHERE name = ?", (name,))
    location = cur.fetchall()[0][0]
    cur.execute("SELECT description FROM Room WHERE location = ?", (location,))
    description = cur.fetchall()[0][0]

    print()
    print(description)

    npc_list = Show_NPC()

    for each in npc_list:
        if(each[3][0] == 1):
            print("-", end='')
            print(each[1][0], end='')
            print("[Lv. " + str(each[2][0]) + "]-")  

    print()

def Score():
    
    global name
    cur.execute("SELECT level FROM Player WHERE name = ?", (name,))
    level = cur.fetchall()[0][0]
    cur.execute("SELECT player_class FROM Player WHERE name = ?", (name,))
    player_class = cur.fetchall()[0][0]
    cur.execute("SELECT totalexp FROM Player WHERE name = ?", (name,))
    totalexp = cur.fetchall()[0][0]
    cur.execute("SELECT experience FROM Player_EXP_Table WHERE level = ?", (level + 1,))
    exp_for_next_level = cur.fetchall()[0][0]
    to_next_level = exp_for_next_level - totalexp
    cur.execute("SELECT rebirths FROM Player WHERE name = ?", (name,))
    rebirths = cur.fetchall()[0][0]

    cur.execute("SELECT health FROM Player WHERE name = ?", (name,))
    current_health = cur.fetchall()[0][0]
    cur.execute("SELECT max_health FROM Player WHERE name = ?", (name,))
    max_health = cur.fetchall()[0][0]
    cur.execute("SELECT mana FROM Player WHERE name = ?", (name,))
    current_mana = cur.fetchall()[0][0]
    cur.execute("SELECT max_mana FROM Player WHERE name = ?", (name,))
    max_mana = cur.fetchall()[0][0]

    cur.execute("SELECT base_strength FROM Player WHERE name = ?", (name,))
    base_strength = cur.fetchall()[0][0]
    cur.execute("SELECT base_stamina FROM Player WHERE name = ?", (name,))
    base_stamina = cur.fetchall()[0][0]
    cur.execute("SELECT base_dexterity FROM Player WHERE name = ?", (name,))
    base_dexterity = cur.fetchall()[0][0]
    cur.execute("SELECT base_agility FROM Player WHERE name = ?", (name,))
    base_agility = cur.fetchall()[0][0]
    cur.execute("SELECT base_intelligence FROM Player WHERE name = ?", (name,))
    base_intelligence = cur.fetchall()[0][0]
    cur.execute("SELECT base_wisdom FROM Player WHERE name = ?", (name,))
    base_wisdom = cur.fetchall()[0][0]
    cur.execute("SELECT base_charisma FROM Player WHERE name = ?", (name,))
    base_charisma = cur.fetchall()[0][0]

    cur.execute("SELECT strength FROM Player WHERE name = ?", (name,))
    strength = cur.fetchall()[0][0]
    cur.execute("SELECT stamina FROM Player WHERE name = ?", (name,))
    stamina = cur.fetchall()[0][0]
    cur.execute("SELECT dexterity FROM Player WHERE name = ?", (name,))
    dexterity = cur.fetchall()[0][0]
    cur.execute("SELECT agility FROM Player WHERE name = ?", (name,))
    agility = cur.fetchall()[0][0]
    cur.execute("SELECT intelligence FROM Player WHERE name = ?", (name,))
    intelligence = cur.fetchall()[0][0]
    cur.execute("SELECT wisdom FROM Player WHERE name = ?", (name,))
    wisdom = cur.fetchall()[0][0]
    cur.execute("SELECT charisma FROM Player WHERE name = ?", (name,))
    charisma = cur.fetchall()[0][0]


    dash = '-' * 64
    print()
    print(dash)
    print('{:2s}{:<5s}{:3s}{:<17}{:3}{:<17s}{:3}{:<12}{:3}'.format("| ", "Name", " : ", name, " | ", "Total Experience", " : ", totalexp, " | "))
    print('{:2s}{:<5s}{:3s}{:<17}{:3}{:<17s}{:3}{:<12}{:3}'.format("| ", "Level", " : ", level, " | ", "To Next Level", " : ", to_next_level, " | "))
    print('{:2s}{:<5s}{:3s}{:<17}{:3}{:<17s}{:3}{:<12}{:3}'.format("| ", "Class", " : ", player_class, " | ", "Rebirths", " : ", rebirths, " | "))
    print(dash)
    print('{:2s}{:<15s}{:>1s}{:>4}{:<1s}{:<4}{:3s}{:<32}{:3s}'.format("| ", "Health", ":", current_health, '/', max_health, " | ", " ", " | "))
    print('{:2s}{:<15s}{:>1s}{:>4}{:<1s}{:<4}{:3s}{:<32}{:3s}'.format("| ", "Mana", ":", current_mana, '/', max_mana, " | ", " ", " | "))
    print('{:2s}{:<15s}{:>1s}{:>4}{:<1s}{:<4}{:3s}{:<32}{:3s}'.format("| ", "Strength", ":", base_strength, '/', strength, " | ", " ", " | "))
    print('{:2s}{:<15s}{:>1s}{:>4}{:<1s}{:<4}{:3s}{:<32}{:3s}'.format("| ", "Stamina", ":", base_stamina, '/', stamina, " | ", " ", " | "))
    print('{:2s}{:<15s}{:>1s}{:>4}{:<1s}{:<4}{:3s}{:<32}{:3s}'.format("| ", "Dexterity", ":", base_dexterity, '/', dexterity, " | ", " ", " | "))
    print('{:2s}{:<15s}{:>1s}{:>4}{:<1s}{:<4}{:3s}{:<32}{:3s}'.format("| ", "Agility", ":", base_agility, '/', agility, " | ", " ", " | "))
    print('{:2s}{:<15s}{:>1s}{:>4}{:<1s}{:<4}{:3s}{:<32}{:3s}'.format("| ", "Intelligence", ":", base_intelligence, '/', intelligence, " | ", " ", " | "))
    print('{:2s}{:<15s}{:>1s}{:>4}{:<1s}{:<4}{:3s}{:<32}{:3s}'.format("| ", "Wisdom", ":", base_wisdom, '/', wisdom, " | ", " ", " | "))
    print('{:2s}{:<15s}{:>1s}{:>4}{:<1s}{:<4}{:3s}{:<32}{:3s}'.format("| ", "Charisma", ":", base_charisma, '/', charisma, " | ", " ", " | "))
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

def RecalibrateStats():

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

    print(to_add)

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

    if(player_class == "Warrior"):

        cur.execute("SELECT base_strength FROM Player WHERE name = ?", (name,))
        base_strength = cur.fetchall()[0][0]
        cur.execute("SELECT base_stamina FROM Player WHERE name = ?", (name,))
        base_stamina = cur.fetchall()[0][0]
        cur.execute("SELECT base_dexterity FROM Player WHERE name = ?", (name,))
        base_dexterity = cur.fetchall()[0][0]
        cur.execute("SELECT base_agility FROM Player WHERE name = ?", (name,))
        base_agility = cur.fetchall()[0][0]
        cur.execute("SELECT base_intelligence FROM Player WHERE name = ?", (name,))
        base_intelligence = cur.fetchall()[0][0]
        cur.execute("SELECT base_wisdom FROM Player WHERE name = ?", (name,))
        base_wisdom = cur.fetchall()[0][0]
        cur.execute("SELECT base_charisma FROM Player WHERE name = ?", (name,))
        base_charisma = cur.fetchall()[0][0]

        cur.execute("SELECT strength FROM Player WHERE name = ?", (name,))
        strength = cur.fetchall()[0][0]
        cur.execute("SELECT stamina FROM Player WHERE name = ?", (name,))
        stamina = cur.fetchall()[0][0]
        cur.execute("SELECT dexterity FROM Player WHERE name = ?", (name,))
        dexterity = cur.fetchall()[0][0]
        cur.execute("SELECT agility FROM Player WHERE name = ?", (name,))
        agility = cur.fetchall()[0][0]
        cur.execute("SELECT intelligence FROM Player WHERE name = ?", (name,))
        intelligence = cur.fetchall()[0][0]
        cur.execute("SELECT wisdom FROM Player WHERE name = ?", (name,))
        wisdom = cur.fetchall()[0][0]
        cur.execute("SELECT charisma FROM Player WHERE name = ?", (name,))
        charisma = cur.fetchall()[0][0]

        temp_strength_buff = strength - base_strength
        temp_stamina_buff = stamina - base_stamina
        temp_dexterity_buff = dexterity - base_dexterity
        temp_agility_buff = agility - base_agility
        temp_intelligence_buff = intelligence - base_intelligence
        temp_wisdom_buff = wisdom - base_wisdom
        temp_charisma_buff = charisma - base_charisma

        cur.execute("SELECT base_strength FROM Warrior_Level_Up WHERE level = ?", (level,))
        base_strength_add = cur.fetchall()[0][0]
        cur.execute("SELECT base_stamina FROM Warrior_Level_Up WHERE level = ?", (level,))
        base_stamina_add = cur.fetchall()[0][0]
        cur.execute("SELECT base_dexterity FROM Warrior_Level_Up WHERE level = ?", (level,))
        base_dexterity_add = cur.fetchall()[0][0]
        cur.execute("SELECT base_agility FROM Warrior_Level_Up WHERE level = ?", (level,))
        base_agility_add = cur.fetchall()[0][0]
        cur.execute("SELECT base_intelligence FROM Warrior_Level_Up WHERE level = ?", (level,))
        base_intelligence_add = cur.fetchall()[0][0]
        cur.execute("SELECT base_wisdom FROM Warrior_Level_Up WHERE level = ?", (level,))
        base_wisdom_add = cur.fetchall()[0][0]
        cur.execute("SELECT base_charisma FROM Warrior_Level_Up WHERE level = ?", (level,))
        base_charisma_add = cur.fetchall()[0][0]

        base_strength += base_strength_add
        base_stamina += base_stamina_add
        base_dexterity += base_dexterity_add
        base_agility += base_agility_add
        base_intelligence += base_intelligence_add
        base_wisdom += base_wisdom_add
        base_charisma += base_charisma_add

        sql = "UPDATE Player SET base_strength = ? WHERE name = ?"
        cur.execute(sql, (base_strength, name,))
        conn.commit()
        sql = "UPDATE Player SET base_stamina = ? WHERE name = ?"
        cur.execute(sql, (base_stamina, name,))
        conn.commit()
        sql = "UPDATE Player SET base_dexterity = ? WHERE name = ?"
        cur.execute(sql, (base_dexterity, name,))
        conn.commit()
        sql = "UPDATE Player SET base_agility = ? WHERE name = ?"
        cur.execute(sql, (base_agility, name,))
        conn.commit()
        sql = "UPDATE Player SET base_intelligence = ? WHERE name = ?"
        cur.execute(sql, (base_intelligence, name,))
        conn.commit()
        sql = "UPDATE Player SET base_wisdom = ? WHERE name = ?"
        cur.execute(sql, (base_wisdom, name,))
        conn.commit()
        sql = "UPDATE Player SET base_charisma = ? WHERE name = ?"
        cur.execute(sql, (base_charisma, name,))
        conn.commit()

        sql = "UPDATE Player SET strength = ? WHERE name = ?"
        cur.execute(sql, (base_strength + temp_strength_buff, name,))
        conn.commit()
        sql = "UPDATE Player SET stamina = ? WHERE name = ?"
        cur.execute(sql, (base_stamina + temp_stamina_buff, name,))
        conn.commit()
        sql = "UPDATE Player SET dexterity = ? WHERE name = ?"
        cur.execute(sql, (base_dexterity + temp_dexterity_buff, name,))
        conn.commit()
        sql = "UPDATE Player SET agility = ? WHERE name = ?"
        cur.execute(sql, (base_agility + temp_agility_buff, name,))
        conn.commit()
        sql = "UPDATE Player SET intelligence = ? WHERE name = ?"
        cur.execute(sql, (base_intelligence + temp_intelligence_buff, name,))
        conn.commit()
        sql = "UPDATE Player SET wisdom = ? WHERE name = ?"
        cur.execute(sql, (base_wisdom + temp_wisdom_buff, name,))
        conn.commit()
        sql = "UPDATE Player SET charisma = ? WHERE name = ?"
        cur.execute(sql, (base_charisma + temp_charisma_buff, name,))
        conn.commit()
        
        #----------------------------Health--------------------------------------
        cur.execute("SELECT max_health FROM Player WHERE name = ?", (name,))
        max_health = cur.fetchall()[0][0]
        #new base_stamina
        cur.execute("SELECT base_stamina FROM Player WHERE name = ?", (name,))
        base_stamina = cur.fetchall()[0][0]

        max_health = stamina * 10
        sql = "UPDATE Player SET max_health = ? WHERE name = ?"
        cur.execute(sql, (max_health, name,))
        conn.commit()        

        """
        #saving difference in hp from buffs. Say base_max_health = 30 but max_health = 50 due to a 20 hp buff. We save the 20 hp in temp_health_buff, we increase base_max_health for levelup, say to 40 hp, then max_health + temp_health_buff = 60. Now we have new hp value with the buff still applied.
        temp_health_buff = max_health - base_max_health

        base_max_health = base_stamina * 10
        sql = "UPDATE Player SET base_max_health = ? WHERE name = ?"
        cur.execute(sql, (base_max_health, name,))
        conn.commit()
        sql = "UPDATE Player SET max_health = ? WHERE name = ?"
        cur.execute(sql, (base_max_health + temp_health_buff, name,))
        conn.commit()
        """

    
    RecalibrateStats()

def Combat(npc_id):

    conn = create_connection(database)
    cur = conn.cursor()

    global stop_combat
    stop_combat = False
    win = False

    #-----------------------NPC_STUFF----------------------------------
    cur.execute("SELECT name FROM Npc WHERE id = ?", (npc_id,))
    npc_name = cur.fetchall()[0][0]
    cur.execute("SELECT level FROM Npc WHERE id = ?", (npc_id,))
    npc_level = cur.fetchall()[0][0]
    cur.execute("SELECT health FROM Npc WHERE id = ?", (npc_id,))
    npc_health = cur.fetchall()[0][0]
    cur.execute("SELECT max_health FROM Npc WHERE id = ?", (npc_id,))
    npc_max_health = cur.fetchall()[0][0]
    cur.execute("SELECT mana FROM Npc WHERE id = ?", (npc_id,))
    npc_mana = cur.fetchall()[0][0]
    cur.execute("SELECT max_mana FROM Npc WHERE id = ?", (npc_id,))
    npc_max_mana = cur.fetchall()[0][0]
    cur.execute("SELECT dexterity FROM Npc WHERE id = ?", (npc_id,))
    npc_dexterity = cur.fetchall()[0][0]
    cur.execute("SELECT agility FROM Npc WHERE id = ?", (npc_id,))
    npc_agility = cur.fetchall()[0][0]
    cur.execute("SELECT intelligence FROM Npc WHERE id = ?", (npc_id,))
    npc_intelligence = cur.fetchall()[0][0]
    cur.execute("SELECT wisdom FROM Npc WHERE id = ?", (npc_id,))
    npc_wisdom = cur.fetchall()[0][0]
    cur.execute("SELECT charisma FROM Npc WHERE id = ?", (npc_id,))
    npc_charisma = cur.fetchall()[0][0]
    cur.execute("SELECT damage_min FROM Npc WHERE id = ?", (npc_id,))
    npc_damage_min = cur.fetchall()[0][0]
    cur.execute("SELECT damage_max FROM Npc WHERE id = ?", (npc_id,))
    npc_damage_max = cur.fetchall()[0][0]


    #-------------------------PLAYER_STATS-------------------------------------
    cur.execute("SELECT level FROM Player WHERE name = ?", (name,))
    player_level = cur.fetchall()[0][0]
    cur.execute("SELECT health FROM Player WHERE name = ?", (name,))
    player_health = cur.fetchall()[0][0]
    cur.execute("SELECT max_health FROM Player WHERE name = ?", (name,))
    player_max_health = cur.fetchall()[0][0]
    cur.execute("SELECT mana FROM Player WHERE name = ?", (name,))
    player_mana = cur.fetchall()[0][0]
    cur.execute("SELECT max_mana FROM Player WHERE name = ?", (name,))
    player_max_mana = cur.fetchall()[0][0]
    cur.execute("SELECT strength FROM Player WHERE name = ?", (name,))
    player_strength = cur.fetchall()[0][0]
    cur.execute("SELECT stamina FROM Player WHERE name = ?", (name,))
    player_stamina = cur.fetchall()[0][0]
    cur.execute("SELECT dexterity FROM Player WHERE name = ?", (name,))
    player_dexterity = cur.fetchall()[0][0]
    cur.execute("SELECT agility FROM Player WHERE name = ?", (name,))
    player_agility = cur.fetchall()[0][0]
    cur.execute("SELECT intelligence FROM Player WHERE name = ?", (name,))
    player_intelligence = cur.fetchall()[0][0]
    cur.execute("SELECT wisdom FROM Player WHERE name = ?", (name,))
    player_wisdom = cur.fetchall()[0][0]
    cur.execute("SELECT charisma FROM Player WHERE name = ?", (name,))
    player_charisma = cur.fetchall()[0][0]

    cur.execute("SELECT level FROM Player WHERE name = ?", (name,))
    player_level = cur.fetchall()[0][0]
    cur.execute("SELECT totalexp FROM Player WHERE name = ?", (name,))
    player_totalexp = cur.fetchall()[0][0]
    cur.execute("SELECT experience FROM Player_EXP_Table WHERE level = ?", (player_level,))
    current_level_exp = cur.fetchall()[0][0]
    cur.execute("SELECT experience FROM Player_EXP_Table WHERE level = ?", (player_level + 1,))
    next_level_exp = cur.fetchall()[0][0]
        
    level_tnl = next_level_exp - current_level_exp
    player_exp_percent = round((player_totalexp - current_level_exp) / level_tnl * 100, 5)
    

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

    player_damage_min += player_strength
    player_damage_max += player_strength

    player_hit_chance = round(player_dexterity / npc_agility * 100) #Raw percentage

    npc_hit_chance = round(npc_dexterity / player_agility * 100)
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
            print(name + " hits " + npc_name + " for " + str(player_damage) + " points of damage.")
            npc_health -= player_damage
            if(npc_health < 0):
                npc_health = 0
            sql = "UPDATE Npc SET health = ? WHERE id = ?"
            cur.execute(sql, (npc_health, npc_id,))
            conn.commit()
        else:
            print(name + " misses " + npc_name + ".")

        npc_hit_roll = random.randrange(1, 100)
        #print("npc hit chance: ", end='')
        #print(npc_hit_chance)
        #print("npc hit roll: ", end='')
        #print(npc_hit_roll)
        if(npc_hit_roll < npc_hit_chance):
            npc_damage = random.randrange(npc_damage_min, npc_damage_max + 1)
            print(npc_name + " hits " + name + " for " + str(npc_damage) + " points of damage.")
            player_health -= npc_damage
            if(player_health < 0):
                player_health = 0
            sql = "UPDATE Player SET health = ? WHERE name = ?"
            cur.execute(sql, (player_health, name,))
            conn.commit()
        else:
            print(npc_name + " misses " + name + ".")
        print("[", end='')
        print(player_health, end='')
        print("/", end='')
        print(player_max_health, end=' ')
        print("(", end='')
        print("{:0.2f}".format(player_health / player_max_health * 100), end='')
        print("%) ", end='')
        print(player_mana, end='')
        print("/", end='')
        print(player_max_mana, end=' ')
        print("(", end='')
        print("{:0.2f}".format(player_mana / player_max_mana * 100), end='')
        print("%) ", end='')
        print("EXP: ", end='')
        print("{:0.2f}".format(player_exp_percent), end='')
        print("%", end='')
        print(" ENEMY: ", end='')
        print(npc_health, end='')
        print("/", end='')
        print(npc_max_health, end=' ')
        print("(", end='')
        print("{:0.2f}".format(npc_health / npc_max_health * 100), end='')
        print("%) ", end='')
        print("]", end='')
        #print(">", end='')
        print(">")
        time.sleep(3)

        if(player_health <= 0):
            print("You have been slain by " + npc_name)
            stop_combat = True
            sql = "UPDATE Player SET location = ? WHERE name = ?"
            cur.execute(sql, (550, name,))
            conn.commit()
            break
        if(npc_health <= 0):
            print(str(npc_name) + " has been slain.")
            sql = "UPDATE Npc SET alive = ? WHERE id = ?"
            cur.execute(sql, (0, npc_id,))
            conn.commit()

            cur.execute("SELECT experience FROM NPC_EXP_Table WHERE level = ?", (npc_level,))
            exp_gain = cur.fetchall()[0][0]
            player_totalexp += exp_gain
            sql = "UPDATE Player SET totalexp = ? WHERE name = ?"
            cur.execute(sql, (player_totalexp, name,))
            conn.commit()
            print("You have gained " + str(exp_gain) + " experience points.")
            """
            cur.execute("SELECT experience FROM Player_EXP_Table WHERE level = ?", (player_level + 1,))
            exp_needed_to_level = cur.fetchall()[0][0]

            if(player_totalexp >= exp_needed_to_level):
                player_level += 1
                sql = "UPDATE Player SET level = ? WHERE name = ?"
                cur.execute(sql, (player_level, name,))
                conn.commit()
            """


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
    
    cur.execute("SELECT level FROM Player WHERE name = ?", (name,))
    level = cur.fetchall()[0][0]
    cur.execute("SELECT totalexp FROM Player WHERE name = ?", (name,))
    totalexp = cur.fetchall()[0][0]
    cur.execute("SELECT experience FROM Player_EXP_Table WHERE level = ?", (level + 1,))
    exp_needed_to_level = cur.fetchall()[0][0]

    if(totalexp >= exp_needed_to_level):
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

    sql = "UPDATE Npc SET alive = ? WHERE id = ?"
    cur.execute(sql, (1, npc_id,))
    conn.commit()

    cur.execute("SELECT max_health FROM Npc WHERE id = ?", (npc_id,))
    max_health = cur.fetchall()[0][0]

    sql = "UPDATE Npc SET health = ? WHERE id = ?"
    cur.execute(sql, (max_health, npc_id,))
    conn.commit()
    conn.close()

def Equip_Item(item):
    
    #Get the ID of item player is trying to equip
    item_id = Get_Item_Id(item)
    item_slot = Get_Item_Equip_Slot(item)
    item_level_requirement = Get_Item_Level_Requirement(item)
    player_level = Get_Player_Level()
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
            is_there_empty_inventory_slot = False
            for i in range(1, 21):
                cur.execute("SELECT inventory_slot_" + str(i) + " FROM Player WHERE name = ?", (name,))
                temp_slot = cur.fetchall()[0][0]
                if(temp_slot == 0):
                    is_there_empty_inventory_slot = True
                    empty_inventory_slot = i
                    break
            if(is_there_empty_inventory_slot):
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

    RecalibrateStats()

def Sql_Select(selecter, table, comparer_column, comparer_value):
    global name
    cur.execute("SELECT " + selecter + " FROM " + table + " WHERE name = ?", (name,))

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

def Get_Player_Level():
    global cur
    global name
    cur.execute("select level from Player where name = ?", (name,))
    player_level = cur.fetchall()[0][0]
    return player_level       
    

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

        cur = conn.cursor()
        cur.execute("SELECT count(*) FROM Player WHERE name = ?", (name,))
        if(cur.fetchall()[0][0] == 0):
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
        create_player(conn, name, final_password_hash[32:], final_password_hash[:32], player_class, health, max_health, mana, base_max_mana, max_mana, base_strength, strength, base_stamina, stamina, base_dexterity, dexterity, base_agility, agility, base_intelligence, intelligence, base_wisdom, wisdom, base_charisma, charisma, equipment_primary, equipment_secondary, equipment_head, equipment_body, equipment_feet, equipment_hands, equipment_legs, equipment_ring)
    
    RecalibrateStats()
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

def Show_Prompt(cur):
    
    cur.execute("SELECT health FROM Player WHERE name = ?", (name,))
    health = cur.fetchall()[0][0]
    cur.execute("SELECT max_health FROM Player WHERE name = ?", (name,))
    max_health = cur.fetchall()[0][0]
    cur.execute("SELECT mana FROM Player WHERE name = ?", (name,))
    mana = cur.fetchall()[0][0]
    cur.execute("SELECT max_mana FROM Player WHERE name = ?", (name,))
    max_mana = cur.fetchall()[0][0]
    
    cur.execute("SELECT level FROM Player WHERE name = ?", (name,))
    level = cur.fetchall()[0][0]
    cur.execute("SELECT totalexp FROM Player WHERE name = ?", (name,))
    totalexp = cur.fetchall()[0][0]
    cur.execute("SELECT experience FROM Player_EXP_Table WHERE level = ?", (level,))
    current_level_exp = cur.fetchall()[0][0]
    cur.execute("SELECT experience FROM Player_EXP_Table WHERE level = ?", (level + 1,))
    next_level_exp = cur.fetchall()[0][0]
    
    level_tnl = next_level_exp - current_level_exp
    exp_percent = round((totalexp - current_level_exp) / level_tnl * 100, 5)
    print("[", end='')
    print(health, end='')
    print("/", end='')
    print(max_health, end=' ')
    print("(", end='')
    #print(health / max_health * 100, end='')
    print("{:0.2f}".format(health / max_health * 100), end='')
    print("%) ", end='')
    print(mana, end='')
    print("/", end='')
    print(max_mana, end=' ')
    print("(", end='')
    #print(mana / max_mana * 100, end='')
    print("{:0.2f}".format(mana / max_mana * 100), end='')
    print("%) ", end='')
    print("EXP: ", end='')
    print("{:0.2f}".format(exp_percent), end='')
    print("%", end='')
    print("]", end='')
    print(">", end='')

def MainLoop():
    while(True):
        Show_Prompt(cur)
        choice = input()
        Command(choice)

#------------------------MAIN--------------------------
def main():

    Login()
    Health_Regen_Initiate()
    Npc_Initial_Spawn_Helper()
    MainLoop()

main()