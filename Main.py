import sys
import sqlite3
import hashlib
import os
from sqlite3 import Error
from Player import Player
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
    
def create_player(conn, name, pkey, salt, pclass, health, base_max_health, max_health, mana, base_max_mana, max_mana, base_strength, strength, base_stamina, stamina, base_dexterity, dexterity, base_agility, agility, base_intelligence, intelligence, base_wisdom, wisdom, base_charisma, charisma, equipment_primary, equipment_secondary, equipment_head, equipment_body, equipment_feet, equipment_hands):
    """
    Create a Player
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql = """ INSERT INTO Player (
        name,
        pkey,
        salt,
        pclass,
        health,
        base_max_health,
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
        equipment_hands
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """
    #(id, name, location, totalexp, level, base_max_health, base_max_mana, base_strength, base_stamina, base_dexterity, base_agility, base_intelligence, base_wisdom, base_charisma, equipment_primary, equipment_secondary, equipment_head, equipment_body, equipment_feet, equipment_hands, gold, invetory_slot_1, invetory_slot_2, invetory_slot_3, invetory_slot_4, invetory_slot_5, invetory_slot_6, invetory_slot_7, invetory_slot_8, invetory_slot_9, invetory_slot_10, invetory_slot_11, invetory_slot_12, invetory_slot_13, invetory_slot_14, invetory_slot_15, invetory_slot_16, invetory_slot_17, invetory_slot_18, invetory_slot_19, invetory_slot_20)
    cur = conn.cursor()
    cur.execute(sql, (name, pkey, salt, pclass, health, base_max_health, max_health, mana, base_max_mana, max_mana, base_strength, strength, base_stamina, stamina, base_dexterity, dexterity, base_agility, agility, base_intelligence, intelligence, base_wisdom, wisdom, base_charisma, charisma, equipment_primary, equipment_secondary, equipment_head, equipment_body, equipment_feet, equipment_hands))
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
    #(id, name, location, totalexp, level, base_max_health, base_max_mana, base_strength, base_stamina, base_dexterity, base_agility, base_intelligence, base_wisdom, base_charisma, equipment_primary, equipment_secondary, equipment_head, equipment_body, equipment_feet, equipment_hands, gold, invetory_slot_1, invetory_slot_2, invetory_slot_3, invetory_slot_4, invetory_slot_5, invetory_slot_6, invetory_slot_7, invetory_slot_8, invetory_slot_9, invetory_slot_10, invetory_slot_11, invetory_slot_12, invetory_slot_13, invetory_slot_14, invetory_slot_15, invetory_slot_16, invetory_slot_17, invetory_slot_18, invetory_slot_19, invetory_slot_20)
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

    cur.execute("SELECT npc_1_existence FROM Room WHERE location = ?", (location,))
    npc_1_existence = cur.fetchall()[0][0]
    cur.execute("SELECT npc_2_existence FROM Room WHERE location = ?", (location,))
    npc_2_existence = cur.fetchall()[0][0]
    cur.execute("SELECT npc_3_existence FROM Room WHERE location = ?", (location,))
    npc_3_existence = cur.fetchall()[0][0]
    cur.execute("SELECT npc_4_existence FROM Room WHERE location = ?", (location,))
    npc_4_existence = cur.fetchall()[0][0]
    cur.execute("SELECT npc_5_existence FROM Room WHERE location = ?", (location,))
    npc_5_existence = cur.fetchall()[0][0]
    cur.execute("SELECT npc_6_existence FROM Room WHERE location = ?", (location,))
    npc_6_existence = cur.fetchall()[0][0]
    cur.execute("SELECT npc_7_existence FROM Room WHERE location = ?", (location,))
    npc_7_existence = cur.fetchall()[0][0]
    cur.execute("SELECT npc_8_existence FROM Room WHERE location = ?", (location,))
    npc_8_existence = cur.fetchall()[0][0]
    cur.execute("SELECT npc_9_existence FROM Room WHERE location = ?", (location,))
    npc_9_existence = cur.fetchall()[0][0]
    cur.execute("SELECT npc_10_existence FROM Room WHERE location = ?", (location,))
    npc_10_existence = cur.fetchall()[0][0]
    cur.execute("SELECT npc_11_existence FROM Room WHERE location = ?", (location,))
    npc_11_existence = cur.fetchall()[0][0]
    cur.execute("SELECT npc_12_existence FROM Room WHERE location = ?", (location,))
    npc_12_existence = cur.fetchall()[0][0]
    cur.execute("SELECT npc_13_existence FROM Room WHERE location = ?", (location,))
    npc_13_existence = cur.fetchall()[0][0]
    cur.execute("SELECT npc_14_existence FROM Room WHERE location = ?", (location,))
    npc_14_existence = cur.fetchall()[0][0]
    cur.execute("SELECT npc_15_existence FROM Room WHERE location = ?", (location,))
    npc_15_existence = cur.fetchall()[0][0]
    cur.execute("SELECT npc_16_existence FROM Room WHERE location = ?", (location,))
    npc_16_existence = cur.fetchall()[0][0]
    cur.execute("SELECT npc_17_existence FROM Room WHERE location = ?", (location,))
    npc_17_existence = cur.fetchall()[0][0]
    cur.execute("SELECT npc_18_existence FROM Room WHERE location = ?", (location,))
    npc_18_existence = cur.fetchall()[0][0]
    cur.execute("SELECT npc_19_existence FROM Room WHERE location = ?", (location,))
    npc_19_existence = cur.fetchall()[0][0]
    cur.execute("SELECT npc_20_existence FROM Room WHERE location = ?", (location,))
    npc_20_existence = cur.fetchall()[0][0]

    if(npc_1_existence == 1):
        cur.execute("SELECT npc_1 FROM Room WHERE location = ?", (location,))
        npc_1 = cur.fetchall()[0][0]
        cur.execute("SELECT name FROM Npc WHERE id = ?", (npc_1,))
        npc_name = cur.fetchall()[0][0]
        cur.execute("SELECT level FROM Npc WHERE id = ?", (npc_1,))
        npc_level = cur.fetchall()[0][0]
        temp_list = []
        temp_list.append("1")
        temp_list.append(npc_1)
        temp_list.append(npc_name)
        temp_list.append(npc_level)
        npc_list.append(temp_list)

    if(npc_2_existence == 1):
        cur.execute("SELECT npc_2 FROM Room WHERE location = ?", (location,))
        npc_2 = cur.fetchall()[0][0]
        cur.execute("SELECT name FROM Npc WHERE id = ?", (npc_2,))
        npc_name = cur.fetchall()[0][0]
        cur.execute("SELECT level FROM Npc WHERE id = ?", (npc_2,))
        npc_level = cur.fetchall()[0][0]
        temp_list = []
        temp_list.append("2")
        temp_list.append(npc_2)
        temp_list.append(npc_name)
        temp_list.append(npc_level)
        npc_list.append(temp_list)

    if(npc_3_existence == 1):
        cur.execute("SELECT npc_3 FROM Room WHERE location = ?", (location,))
        npc_3 = cur.fetchall()[0][0]
        cur.execute("SELECT name FROM Npc WHERE id = ?", (npc_3,))
        npc_name = cur.fetchall()[0][0]
        cur.execute("SELECT level FROM Npc WHERE id = ?", (npc_3,))
        npc_level = cur.fetchall()[0][0]
        temp_list = []
        temp_list.append("3")
        temp_list.append(npc_3)
        temp_list.append(npc_name)
        temp_list.append(npc_level)
        npc_list.append(temp_list)

    if(npc_4_existence == 1):
        cur.execute("SELECT npc_4 FROM Room WHERE location = ?", (location,))
        npc_4 = cur.fetchall()[0][0]
        cur.execute("SELECT name FROM Npc WHERE id = ?", (npc_4,))
        npc_name = cur.fetchall()[0][0]
        cur.execute("SELECT level FROM Npc WHERE id = ?", (npc_4,))
        npc_level = cur.fetchall()[0][0]
        temp_list = []
        temp_list.append("4")
        temp_list.append(npc_4)
        temp_list.append(npc_name)
        temp_list.append(npc_level)
        npc_list.append(temp_list)

    if(npc_5_existence == 1):
        cur.execute("SELECT npc_5 FROM Room WHERE location = ?", (location,))
        npc_5 = cur.fetchall()[0][0]
        cur.execute("SELECT name FROM Npc WHERE id = ?", (npc_5,))
        npc_name = cur.fetchall()[0][0]
        cur.execute("SELECT level FROM Npc WHERE id = ?", (npc_5,))
        npc_level = cur.fetchall()[0][0]
        temp_list = []
        temp_list.append("5")
        temp_list.append(npc_5)
        temp_list.append(npc_name)
        temp_list.append(npc_level)
        npc_list.append(temp_list)

    if(npc_6_existence == 1):
        cur.execute("SELECT npc_6 FROM Room WHERE location = ?", (location,))
        npc_6 = cur.fetchall()[0][0]
        cur.execute("SELECT name FROM Npc WHERE id = ?", (npc_6,))
        npc_name = cur.fetchall()[0][0]
        cur.execute("SELECT level FROM Npc WHERE id = ?", (npc_6,))
        npc_level = cur.fetchall()[0][0]
        temp_list = []
        temp_list.append("6")
        temp_list.append(npc_6)
        temp_list.append(npc_name)
        temp_list.append(npc_level)
        npc_list.append(temp_list)

    if(npc_7_existence == 1):
        cur.execute("SELECT npc_7 FROM Room WHERE location = ?", (location,))
        npc_7 = cur.fetchall()[0][0]
        cur.execute("SELECT name FROM Npc WHERE id = ?", (npc_7,))
        npc_name = cur.fetchall()[0][0]
        cur.execute("SELECT level FROM Npc WHERE id = ?", (npc_7,))
        npc_level = cur.fetchall()[0][0]
        temp_list = []
        temp_list.append("7")
        temp_list.append(npc_7)
        temp_list.append(npc_name)
        temp_list.append(npc_level)
        npc_list.append(temp_list)

    if(npc_8_existence == 1):
        cur.execute("SELECT npc_8 FROM Room WHERE location = ?", (location,))
        npc_8 = cur.fetchall()[0][0]
        cur.execute("SELECT name FROM Npc WHERE id = ?", (npc_8,))
        npc_name = cur.fetchall()[0][0]
        cur.execute("SELECT level FROM Npc WHERE id = ?", (npc_8,))
        npc_level = cur.fetchall()[0][0]
        temp_list = []
        temp_list.append("8")
        temp_list.append(npc_8)
        temp_list.append(npc_name)
        temp_list.append(npc_level)
        npc_list.append(temp_list)

    if(npc_9_existence == 1):
        cur.execute("SELECT npc_9 FROM Room WHERE location = ?", (location,))
        npc_9 = cur.fetchall()[0][0]
        cur.execute("SELECT name FROM Npc WHERE id = ?", (npc_9,))
        npc_name = cur.fetchall()[0][0]
        cur.execute("SELECT level FROM Npc WHERE id = ?", (npc_9,))
        npc_level = cur.fetchall()[0][0]
        temp_list = []
        temp_list.append("9")
        temp_list.append(npc_9)
        temp_list.append(npc_name)
        temp_list.append(npc_level)
        npc_list.append(temp_list)

    if(npc_10_existence == 1):
        cur.execute("SELECT npc_10 FROM Room WHERE location = ?", (location,))
        npc_10 = cur.fetchall()[0][0]
        cur.execute("SELECT name FROM Npc WHERE id = ?", (npc_10,))
        npc_name = cur.fetchall()[0][0]
        cur.execute("SELECT level FROM Npc WHERE id = ?", (npc_10,))
        npc_level = cur.fetchall()[0][0]
        temp_list = []
        temp_list.append("10")
        temp_list.append(npc_10)
        temp_list.append(npc_name)
        temp_list.append(npc_level)
        npc_list.append(temp_list)

    if(npc_11_existence == 1):
        cur.execute("SELECT npc_11 FROM Room WHERE location = ?", (location,))
        npc_11 = cur.fetchall()[0][0]
        cur.execute("SELECT name FROM Npc WHERE id = ?", (npc_11,))
        npc_name = cur.fetchall()[0][0]
        cur.execute("SELECT level FROM Npc WHERE id = ?", (npc_11,))
        npc_level = cur.fetchall()[0][0]
        temp_list = []
        temp_list.append("11")
        temp_list.append(npc_11)
        temp_list.append(npc_name)
        temp_list.append(npc_level)
        npc_list.append(temp_list)

    if(npc_12_existence == 1):
        cur.execute("SELECT npc_12 FROM Room WHERE location = ?", (location,))
        npc_12 = cur.fetchall()[0][0]
        cur.execute("SELECT name FROM Npc WHERE id = ?", (npc_12,))
        npc_name = cur.fetchall()[0][0]
        cur.execute("SELECT level FROM Npc WHERE id = ?", (npc_12,))
        npc_level = cur.fetchall()[0][0]
        temp_list = []
        temp_list.append("12")
        temp_list.append(npc_12)
        temp_list.append(npc_name)
        temp_list.append(npc_level)
        npc_list.append(temp_list)

    if(npc_13_existence == 1):
        cur.execute("SELECT npc_13 FROM Room WHERE location = ?", (location,))
        npc_13 = cur.fetchall()[0][0]
        cur.execute("SELECT name FROM Npc WHERE id = ?", (npc_13,))
        npc_name = cur.fetchall()[0][0]
        cur.execute("SELECT level FROM Npc WHERE id = ?", (npc_13,))
        npc_level = cur.fetchall()[0][0]
        temp_list = []
        temp_list.append("13")
        temp_list.append(npc_13)
        temp_list.append(npc_name)
        temp_list.append(npc_level)
        npc_list.append(temp_list)

    if(npc_14_existence == 1):
        cur.execute("SELECT npc_14 FROM Room WHERE location = ?", (location,))
        npc_14 = cur.fetchall()[0][0]
        cur.execute("SELECT name FROM Npc WHERE id = ?", (npc_14,))
        npc_name = cur.fetchall()[0][0]
        cur.execute("SELECT level FROM Npc WHERE id = ?", (npc_14,))
        npc_level = cur.fetchall()[0][0]
        temp_list = []
        temp_list.append("14")
        temp_list.append(npc_14)
        temp_list.append(npc_name)
        temp_list.append(npc_level)
        npc_list.append(temp_list)

    if(npc_15_existence == 1):
        cur.execute("SELECT npc_15 FROM Room WHERE location = ?", (location,))
        npc_15 = cur.fetchall()[0][0]
        cur.execute("SELECT name FROM Npc WHERE id = ?", (npc_15,))
        npc_name = cur.fetchall()[0][0]
        cur.execute("SELECT level FROM Npc WHERE id = ?", (npc_15,))
        npc_level = cur.fetchall()[0][0]
        temp_list = []
        temp_list.append("15")
        temp_list.append(npc_15)
        temp_list.append(npc_name)
        temp_list.append(npc_level)
        npc_list.append(temp_list)

    if(npc_16_existence == 1):
        cur.execute("SELECT npc_16 FROM Room WHERE location = ?", (location,))
        npc_16 = cur.fetchall()[0][0]
        cur.execute("SELECT name FROM Npc WHERE id = ?", (npc_16,))
        npc_name = cur.fetchall()[0][0]
        cur.execute("SELECT level FROM Npc WHERE id = ?", (npc_16,))
        npc_level = cur.fetchall()[0][0]
        temp_list = []
        temp_list.append("16")
        temp_list.append(npc_16)
        temp_list.append(npc_name)
        temp_list.append(npc_level)
        npc_list.append(temp_list)

    if(npc_17_existence == 1):
        cur.execute("SELECT npc_17 FROM Room WHERE location = ?", (location,))
        npc_17 = cur.fetchall()[0][0]
        cur.execute("SELECT name FROM Npc WHERE id = ?", (npc_17,))
        npc_name = cur.fetchall()[0][0]
        cur.execute("SELECT level FROM Npc WHERE id = ?", (npc_17,))
        npc_level = cur.fetchall()[0][0]
        temp_list = []
        temp_list.append("17")
        temp_list.append(npc_17)
        temp_list.append(npc_name)
        temp_list.append(npc_level)
        npc_list.append(temp_list)

    if(npc_18_existence == 1):
        cur.execute("SELECT npc_18 FROM Room WHERE location = ?", (location,))
        npc_18 = cur.fetchall()[0][0]
        cur.execute("SELECT name FROM Npc WHERE id = ?", (npc_18,))
        npc_name = cur.fetchall()[0][0]
        cur.execute("SELECT level FROM Npc WHERE id = ?", (npc_18,))
        npc_level = cur.fetchall()[0][0]
        temp_list = []
        temp_list.append("18")
        temp_list.append(npc_18)
        temp_list.append(npc_name)
        temp_list.append(npc_level)
        npc_list.append(temp_list)

    if(npc_19_existence == 1):
        cur.execute("SELECT npc_19 FROM Room WHERE location = ?", (location,))
        npc_19 = cur.fetchall()[0][0]
        cur.execute("SELECT name FROM Npc WHERE id = ?", (npc_19,))
        npc_name = cur.fetchall()[0][0]
        cur.execute("SELECT level FROM Npc WHERE id = ?", (npc_19,))
        npc_level = cur.fetchall()[0][0]
        temp_list = []
        temp_list.append("19")
        temp_list.append(npc_19)
        temp_list.append(npc_name)
        temp_list.append(npc_level)
        npc_list.append(temp_list)

    if(npc_20_existence == 1):
        cur.execute("SELECT npc_20 FROM Room WHERE location = ?", (location,))
        npc_20 = cur.fetchall()[0][0]
        cur.execute("SELECT name FROM Npc WHERE id = ?", (npc_20,))
        npc_name = cur.fetchall()[0][0]
        cur.execute("SELECT level FROM Npc WHERE id = ?", (npc_20,))
        npc_level = cur.fetchall()[0][0]
        temp_list = []
        temp_list.append("20")
        temp_list.append(npc_20)
        temp_list.append(npc_name)
        temp_list.append(npc_level)
        npc_list.append(temp_list)
    
    return(npc_list)

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
        print("-", end='')
        print(each[2], end='')
        print("[Lv. " + str(each[3]) + "]-")  
    
    print()

def Score():
    
    global name
    cur.execute("SELECT level FROM Player WHERE name = ?", (name,))
    level = cur.fetchall()[0][0]
    cur.execute("SELECT pclass FROM Player WHERE name = ?", (name,))
    pclass = cur.fetchall()[0][0]
    cur.execute("SELECT totalexp FROM Player WHERE name = ?", (name,))
    totalexp = cur.fetchall()[0][0]
    cur.execute("SELECT experience FROM Player_EXP_Table WHERE level = ?", (level + 1,))
    to_next_level = cur.fetchall()[0][0] - totalexp
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
    print('{:2s}{:<5s}{:3s}{:<17}{:3}{:<17s}{:3}{:<12}{:3}'.format("| ", "Level", " : ", level, " | ", "Next Level", " : ", to_next_level, " | "))
    print('{:2s}{:<5s}{:3s}{:<17}{:3}{:<17s}{:3}{:<12}{:3}'.format("| ", "Class", " : ", pclass, " | ", "Rebirths", " : ", rebirths, " | "))
    print(dash)
    print('{:2s}{:<15s}{:>1s}{:>4}{:<1s}{:<4}{:3s}{:<32}{:3s}'.format("| ", "Health", ":", current_health, '/', max_health, " | ", " ", " | "))
    print('{:2s}{:<15s}{:>1s}{:>4}{:<1s}{:<4}{:3s}{:<32}{:3s}'.format("| ", "Mana", ":", current_mana, '/', max_mana, " | ", " ", " | "))
    print('{:2s}{:<15s}{:>1s}{:>4}{:<1s}{:<4}{:3s}{:<32}{:3s}'.format("| ", "Strength", ":", strength, '/', base_strength, " | ", " ", " | "))
    print('{:2s}{:<15s}{:>1s}{:>4}{:<1s}{:<4}{:3s}{:<32}{:3s}'.format("| ", "Stamina", ":", stamina, '/', base_stamina, " | ", " ", " | "))
    print('{:2s}{:<15s}{:>1s}{:>4}{:<1s}{:<4}{:3s}{:<32}{:3s}'.format("| ", "Dexterity", ":", dexterity, '/', base_dexterity, " | ", " ", " | "))
    print('{:2s}{:<15s}{:>1s}{:>4}{:<1s}{:<4}{:3s}{:<32}{:3s}'.format("| ", "Agility", ":", agility, '/', base_agility, " | ", " ", " | "))
    print('{:2s}{:<15s}{:>1s}{:>4}{:<1s}{:<4}{:3s}{:<32}{:3s}'.format("| ", "Intelligence", ":", intelligence, '/', base_intelligence, " | ", " ", " | "))
    print('{:2s}{:<15s}{:>1s}{:>4}{:<1s}{:<4}{:3s}{:<32}{:3s}'.format("| ", "Wisdom", ":", wisdom, '/', base_wisdom, " | ", " ", " | "))
    print('{:2s}{:<15s}{:>1s}{:>4}{:<1s}{:<4}{:3s}{:<32}{:3s}'.format("| ", "Charisma", ":", charisma, '/', base_charisma, " | ", " ", " | "))
    print(dash)

def Show_Equipment():

    #Fetch equipment integers
    cur.execute("SELECT equipment_primary FROM Player WHERE name = ?", (name,))
    equipment_primary = cur.fetchall()[0][0]
    cur.execute("SELECT equipment_secondary FROM Player WHERE name = ?", (name,))
    equipment_secondary = cur.fetchall()[0][0]
    cur.execute("SELECT equipment_head FROM Player WHERE name = ?", (name,))
    equipment_head = cur.fetchall()[0][0]
    cur.execute("SELECT equipment_body FROM Player WHERE name = ?", (name,))
    equipment_body = cur.fetchall()[0][0]
    cur.execute("SELECT equipment_feet FROM Player WHERE name = ?", (name,))
    equipment_feet = cur.fetchall()[0][0]
    cur.execute("SELECT equipment_hands FROM Player WHERE name = ?", (name,))
    equipment_hands = cur.fetchall()[0][0]

    #fetch equipment names, from integers
    cur.execute("SELECT name FROM Item WHERE id = ?", (equipment_primary,))
    equipment_primary_name = cur.fetchall()[0][0]
    cur.execute("SELECT name FROM Item WHERE id = ?", (equipment_secondary,))
    equipment_secondary_name = cur.fetchall()[0][0]
    cur.execute("SELECT name FROM Item WHERE id = ?", (equipment_head,))
    equipment_head_name = cur.fetchall()[0][0]
    cur.execute("SELECT name FROM Item WHERE id = ?", (equipment_body,))
    equipment_body_name = cur.fetchall()[0][0]
    cur.execute("SELECT name FROM Item WHERE id = ?", (equipment_feet,))
    equipment_feet_name = cur.fetchall()[0][0]
    cur.execute("SELECT name FROM Item WHERE id = ?", (equipment_hands,))
    equipment_hands_name = cur.fetchall()[0][0]

    dash = '-' * 64
    print()
    print(dash)
    print('{:2s}{:<9s}{:3s}{:<48s}{:2s}'.format("| ", "Primary", " : ", equipment_primary_name, " |"))
    print('{:2s}{:<9s}{:3s}{:<48s}{:2s}'.format("| ", "Secondary", " : ", equipment_secondary_name, " |"))
    print('{:2s}{:<9s}{:3s}{:<48s}{:2s}'.format("| ", "Head", " : ", equipment_head_name, " |"))
    print('{:2s}{:<9s}{:3s}{:<48s}{:2s}'.format("| ", "Body", " : ", equipment_body_name, " |"))
    print('{:2s}{:<9s}{:3s}{:<48s}{:2s}'.format("| ", "Hands", " : ", equipment_hands_name, " |"))
    print('{:2s}{:<9s}{:3s}{:<48s}{:2s}'.format("| ", "Feet", " : ", equipment_feet_name, " |"))
    print(dash)

def Show_Inventory():

    #fetch item integers
    cur.execute("SELECT inventory_slot_1 FROM Player WHERE name = ?", (name,))
    inventory_slot_1 = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_1_quantity FROM Player WHERE name = ?", (name,))
    inventory_slot_1_quantity = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_2 FROM Player WHERE name = ?", (name,))
    inventory_slot_2 = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_2_quantity FROM Player WHERE name = ?", (name,))
    inventory_slot_2_quantity = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_3 FROM Player WHERE name = ?", (name,))
    inventory_slot_3 = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_3_quantity FROM Player WHERE name = ?", (name,))
    inventory_slot_3_quantity = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_4 FROM Player WHERE name = ?", (name,))
    inventory_slot_4 = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_4_quantity FROM Player WHERE name = ?", (name,))
    inventory_slot_4_quantity = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_5 FROM Player WHERE name = ?", (name,))
    inventory_slot_5 = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_5_quantity FROM Player WHERE name = ?", (name,))
    inventory_slot_5_quantity = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_6 FROM Player WHERE name = ?", (name,))
    inventory_slot_6 = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_6_quantity FROM Player WHERE name = ?", (name,))
    inventory_slot_6_quantity = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_7 FROM Player WHERE name = ?", (name,))
    inventory_slot_7 = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_7_quantity FROM Player WHERE name = ?", (name,))
    inventory_slot_7_quantity = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_8 FROM Player WHERE name = ?", (name,))
    inventory_slot_8 = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_8_quantity FROM Player WHERE name = ?", (name,))
    inventory_slot_8_quantity = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_9 FROM Player WHERE name = ?", (name,))
    inventory_slot_9 = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_9_quantity FROM Player WHERE name = ?", (name,))
    inventory_slot_9_quantity = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_10 FROM Player WHERE name = ?", (name,))
    inventory_slot_10 = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_10_quantity FROM Player WHERE name = ?", (name,))
    inventory_slot_10_quantity = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_11 FROM Player WHERE name = ?", (name,))
    inventory_slot_11 = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_11_quantity FROM Player WHERE name = ?", (name,))
    inventory_slot_11_quantity = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_12 FROM Player WHERE name = ?", (name,))
    inventory_slot_12 = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_12_quantity FROM Player WHERE name = ?", (name,))
    inventory_slot_12_quantity = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_13 FROM Player WHERE name = ?", (name,))
    inventory_slot_13 = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_13_quantity FROM Player WHERE name = ?", (name,))
    inventory_slot_13_quantity = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_14 FROM Player WHERE name = ?", (name,))
    inventory_slot_14 = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_14_quantity FROM Player WHERE name = ?", (name,))
    inventory_slot_14_quantity = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_15 FROM Player WHERE name = ?", (name,))
    inventory_slot_15 = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_15_quantity FROM Player WHERE name = ?", (name,))
    inventory_slot_15_quantity = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_16 FROM Player WHERE name = ?", (name,))
    inventory_slot_16 = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_16_quantity FROM Player WHERE name = ?", (name,))
    inventory_slot_16_quantity = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_17 FROM Player WHERE name = ?", (name,))
    inventory_slot_17 = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_17_quantity FROM Player WHERE name = ?", (name,))
    inventory_slot_17_quantity = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_18 FROM Player WHERE name = ?", (name,))
    inventory_slot_18 = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_18_quantity FROM Player WHERE name = ?", (name,))
    inventory_slot_18_quantity = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_19 FROM Player WHERE name = ?", (name,))
    inventory_slot_19 = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_19_quantity FROM Player WHERE name = ?", (name,))
    inventory_slot_19_quantity = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_20 FROM Player WHERE name = ?", (name,))
    inventory_slot_20 = cur.fetchall()[0][0]
    cur.execute("SELECT inventory_slot_20_quantity FROM Player WHERE name = ?", (name,))
    inventory_slot_20_quantity = cur.fetchall()[0][0]

    #fetch item names, from integers
    cur.execute("SELECT name FROM Item WHERE id = ?", (inventory_slot_1,))
    inventory_slot_1_name = cur.fetchall()[0][0]
    cur.execute("SELECT name FROM Item WHERE id = ?", (inventory_slot_2,))
    inventory_slot_2_name = cur.fetchall()[0][0]
    cur.execute("SELECT name FROM Item WHERE id = ?", (inventory_slot_3,))
    inventory_slot_3_name = cur.fetchall()[0][0]
    cur.execute("SELECT name FROM Item WHERE id = ?", (inventory_slot_3,))
    inventory_slot_3_name = cur.fetchall()[0][0]
    cur.execute("SELECT name FROM Item WHERE id = ?", (inventory_slot_4,))
    inventory_slot_4_name = cur.fetchall()[0][0]
    cur.execute("SELECT name FROM Item WHERE id = ?", (inventory_slot_5,))
    inventory_slot_5_name = cur.fetchall()[0][0]
    cur.execute("SELECT name FROM Item WHERE id = ?", (inventory_slot_6,))
    inventory_slot_6_name = cur.fetchall()[0][0]
    cur.execute("SELECT name FROM Item WHERE id = ?", (inventory_slot_7,))
    inventory_slot_7_name = cur.fetchall()[0][0]
    cur.execute("SELECT name FROM Item WHERE id = ?", (inventory_slot_8,))
    inventory_slot_8_name = cur.fetchall()[0][0]
    cur.execute("SELECT name FROM Item WHERE id = ?", (inventory_slot_9,))
    inventory_slot_9_name = cur.fetchall()[0][0]
    cur.execute("SELECT name FROM Item WHERE id = ?", (inventory_slot_10,))
    inventory_slot_10_name = cur.fetchall()[0][0]
    cur.execute("SELECT name FROM Item WHERE id = ?", (inventory_slot_11,))
    inventory_slot_11_name = cur.fetchall()[0][0]
    cur.execute("SELECT name FROM Item WHERE id = ?", (inventory_slot_12,))
    inventory_slot_12_name = cur.fetchall()[0][0]
    cur.execute("SELECT name FROM Item WHERE id = ?", (inventory_slot_13,))
    inventory_slot_13_name = cur.fetchall()[0][0]
    cur.execute("SELECT name FROM Item WHERE id = ?", (inventory_slot_14,))
    inventory_slot_14_name = cur.fetchall()[0][0]
    cur.execute("SELECT name FROM Item WHERE id = ?", (inventory_slot_15,))
    inventory_slot_15_name = cur.fetchall()[0][0]
    cur.execute("SELECT name FROM Item WHERE id = ?", (inventory_slot_16,))
    inventory_slot_16_name = cur.fetchall()[0][0]
    cur.execute("SELECT name FROM Item WHERE id = ?", (inventory_slot_17,))
    inventory_slot_17_name = cur.fetchall()[0][0]
    cur.execute("SELECT name FROM Item WHERE id = ?", (inventory_slot_18,))
    inventory_slot_18_name = cur.fetchall()[0][0]
    cur.execute("SELECT name FROM Item WHERE id = ?", (inventory_slot_19,))
    inventory_slot_19_name = cur.fetchall()[0][0]
    cur.execute("SELECT name FROM Item WHERE id = ?", (inventory_slot_20,))
    inventory_slot_20_name = cur.fetchall()[0][0]


    #inventory printing
    dash = '-' * 64
    print()
    print(dash)
    if(inventory_slot_1 == 0):
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "1", " : ", inventory_slot_1_name, " |"))
    else:
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "1", " : ", inventory_slot_1_name + " x " + str(inventory_slot_1_quantity), " |"))
    if(inventory_slot_2 == 0):
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "2", " : ", inventory_slot_2_name, " |"))
    else:
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "2", " : ", inventory_slot_2_name + " x " + str(inventory_slot_2_quantity), " |"))
    if(inventory_slot_3 == 0):
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "3", " : ", inventory_slot_3_name, " |"))
    else:
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "3", " : ", inventory_slot_3_name + " x " + str(inventory_slot_3_quantity), " |"))
    if(inventory_slot_4 == 0):
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "4", " : ", inventory_slot_4_name, " |"))
    else:
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "4", " : ", inventory_slot_4_name + " x " + str(inventory_slot_4_quantity), " |"))
    if(inventory_slot_5 == 0):
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "5", " : ", inventory_slot_5_name, " |"))
    else:
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "5", " : ", inventory_slot_5_name + " x " + str(inventory_slot_5_quantity), " |"))
    if(inventory_slot_6 == 0):
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "6", " : ", inventory_slot_6_name, " |"))
    else:
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "6", " : ", inventory_slot_6_name + " x " + str(inventory_slot_6_quantity), " |"))
    if(inventory_slot_7 == 0):
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "7", " : ", inventory_slot_7_name, " |"))
    else:
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "7", " : ", inventory_slot_7_name + " x " + str(inventory_slot_7_quantity), " |"))
    if(inventory_slot_8 == 0):
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "8", " : ", inventory_slot_8_name, " |"))
    else:
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "8", " : ", inventory_slot_8_name + " x " + str(inventory_slot_8_quantity), " |"))
    if(inventory_slot_9 == 0):
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "9", " : ", inventory_slot_9_name, " |"))
    else:
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "9", " : ", inventory_slot_9_name + " x " + str(inventory_slot_9_quantity), " |"))
    if(inventory_slot_10 == 0):
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "10", " : ", inventory_slot_10_name, " |"))
    else:
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "10", " : ", inventory_slot_10_name + " x " + str(inventory_slot_10_quantity), " |"))
    if(inventory_slot_11 == 0):
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "11", " : ", inventory_slot_11_name, " |"))
    else:
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "11", " : ", inventory_slot_11_name + " x " + str(inventory_slot_11_quantity), " |"))
    if(inventory_slot_12 == 0):
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "12", " : ", inventory_slot_12_name, " |"))
    else:
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "12", " : ", inventory_slot_12_name + " x " + str(inventory_slot_12_quantity), " |"))
    if(inventory_slot_13 == 0):
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "13", " : ", inventory_slot_13_name, " |"))
    else:
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "13", " : ", inventory_slot_13_name + " x " + str(inventory_slot_13_quantity), " |"))
    if(inventory_slot_14 == 0):
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "14", " : ", inventory_slot_14_name, " |"))
    else:
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "14", " : ", inventory_slot_14_name + " x " + str(inventory_slot_14_quantity), " |"))
    if(inventory_slot_15 == 0):
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "15", " : ", inventory_slot_15_name, " |"))
    else:
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "15", " : ", inventory_slot_15_name + " x " + str(inventory_slot_15_quantity), " |"))
    if(inventory_slot_16 == 0):
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "16", " : ", inventory_slot_16_name, " |"))
    else:
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "16", " : ", inventory_slot_16_name + " x " + str(inventory_slot_16_quantity), " |"))
    if(inventory_slot_17 == 0):
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "17", " : ", inventory_slot_17_name, " |"))
    else:
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "17", " : ", inventory_slot_17_name + " x " + str(inventory_slot_17_quantity), " |"))
    if(inventory_slot_18 == 0):
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "18", " : ", inventory_slot_18_name, " |"))
    else:
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "18", " : ", inventory_slot_18_name + " x " + str(inventory_slot_18_quantity), " |"))
    if(inventory_slot_19 == 0):
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "19", " : ", inventory_slot_19_name, " |"))
    else:
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "19", " : ", inventory_slot_19_name + " x " + str(inventory_slot_19_quantity), " |"))
    if(inventory_slot_20 == 0):
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "20", " : ", inventory_slot_20_name, " |"))
    else:
        print('{:2s}{:>2s}{:3s}{:<55s}{:2s}'.format("| ", "20", " : ", inventory_slot_20_name + " x " + str(inventory_slot_20_quantity), " |"))
    print(dash)

def Show_Buffs():

    #fetch buff integers
    cur.execute("SELECT buff_slot_1 FROM Player WHERE name = ?", (name,))
    buff_slot_1 = cur.fetchall()[0][0]
    cur.execute("SELECT buff_slot_2 FROM Player WHERE name = ?", (name,))
    buff_slot_2 = cur.fetchall()[0][0]
    cur.execute("SELECT buff_slot_3 FROM Player WHERE name = ?", (name,))
    buff_slot_3 = cur.fetchall()[0][0]
    cur.execute("SELECT buff_slot_4 FROM Player WHERE name = ?", (name,))
    buff_slot_4 = cur.fetchall()[0][0]
    cur.execute("SELECT buff_slot_5 FROM Player WHERE name = ?", (name,))
    buff_slot_5 = cur.fetchall()[0][0]
    cur.execute("SELECT buff_slot_6 FROM Player WHERE name = ?", (name,))
    buff_slot_6 = cur.fetchall()[0][0]
    cur.execute("SELECT buff_slot_7 FROM Player WHERE name = ?", (name,))
    buff_slot_7 = cur.fetchall()[0][0]
    cur.execute("SELECT buff_slot_8 FROM Player WHERE name = ?", (name,))
    buff_slot_8 = cur.fetchall()[0][0]
    cur.execute("SELECT buff_slot_9 FROM Player WHERE name = ?", (name,))
    buff_slot_9 = cur.fetchall()[0][0]
    cur.execute("SELECT buff_slot_10 FROM Player WHERE name = ?", (name,))
    buff_slot_10 = cur.fetchall()[0][0]

    #fetch buff names, from integers
    cur.execute("SELECT name FROM Buff WHERE id = ?", (buff_slot_1,))
    buff_slot_1_name = cur.fetchall()[0][0]
    cur.execute("SELECT name FROM Buff WHERE id = ?", (buff_slot_2,))
    buff_slot_2_name = cur.fetchall()[0][0]
    cur.execute("SELECT name FROM Buff WHERE id = ?", (buff_slot_3,))
    buff_slot_3_name = cur.fetchall()[0][0]
    cur.execute("SELECT name FROM Buff WHERE id = ?", (buff_slot_4,))
    buff_slot_4_name = cur.fetchall()[0][0]
    cur.execute("SELECT name FROM Buff WHERE id = ?", (buff_slot_5,))
    buff_slot_5_name = cur.fetchall()[0][0]
    cur.execute("SELECT name FROM Buff WHERE id = ?", (buff_slot_6,))
    buff_slot_6_name = cur.fetchall()[0][0]
    cur.execute("SELECT name FROM Buff WHERE id = ?", (buff_slot_7,))
    buff_slot_7_name = cur.fetchall()[0][0]
    cur.execute("SELECT name FROM Buff WHERE id = ?", (buff_slot_8,))
    buff_slot_8_name = cur.fetchall()[0][0]
    cur.execute("SELECT name FROM Buff WHERE id = ?", (buff_slot_9,))
    buff_slot_9_name = cur.fetchall()[0][0]
    cur.execute("SELECT name FROM Buff WHERE id = ?", (buff_slot_10,))
    buff_slot_10_name = cur.fetchall()[0][0]
    

    #fetch buff times, from integers
    cur.execute("SELECT buff_slot_1_timer FROM Player WHERE name = ?", (name,))
    buff_slot_1_timer = cur.fetchall()[0][0]
    cur.execute("SELECT buff_slot_2_timer FROM Player WHERE name = ?", (name,))
    buff_slot_2_timer = cur.fetchall()[0][0]
    cur.execute("SELECT buff_slot_3_timer FROM Player WHERE name = ?", (name,))
    buff_slot_3_timer = cur.fetchall()[0][0]
    cur.execute("SELECT buff_slot_4_timer FROM Player WHERE name = ?", (name,))
    buff_slot_4_timer = cur.fetchall()[0][0]
    cur.execute("SELECT buff_slot_5_timer FROM Player WHERE name = ?", (name,))
    buff_slot_5_timer = cur.fetchall()[0][0]
    cur.execute("SELECT buff_slot_6_timer FROM Player WHERE name = ?", (name,))
    buff_slot_6_timer = cur.fetchall()[0][0]
    cur.execute("SELECT buff_slot_7_timer FROM Player WHERE name = ?", (name,))
    buff_slot_7_timer = cur.fetchall()[0][0]
    cur.execute("SELECT buff_slot_8_timer FROM Player WHERE name = ?", (name,))
    buff_slot_8_timer = cur.fetchall()[0][0]
    cur.execute("SELECT buff_slot_9_timer FROM Player WHERE name = ?", (name,))
    buff_slot_9_timer = cur.fetchall()[0][0]
    cur.execute("SELECT buff_slot_10_timer FROM Player WHERE name = ?", (name,))
    buff_slot_10_timer = cur.fetchall()[0][0]

    #buff printing
    dash = '-' * 120
    print()
    print(dash)
    print('{:2s}{:3s}{:113s}{:2s}'.format("| ", "", "Current Buffs", " |"))
    print(dash)

    #buff slot 1
    if(buff_slot_1 > 0):
        print('{:2s}{:>4}{:1s}{:3s}{:<108s}{:2s}'.format("| ", buff_slot_1_timer, "s", " : ", buff_slot_1_name, " |"))

        buff_stat_list = ""
        cur.execute("SELECT max_health FROM Buff WHERE id = ?", (buff_slot_1,))
        buff_max_health = cur.fetchall()[0][0]
        if(buff_max_health > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_max_health) + " Health "
        
        cur.execute("SELECT max_mana FROM Buff WHERE id = ?", (buff_slot_1,))
        buff_max_mana = cur.fetchall()[0][0]
        if(buff_max_mana > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_max_mana) + " Mana "

        cur.execute("SELECT strength FROM Buff WHERE id = ?", (buff_slot_1,))
        buff_strength = cur.fetchall()[0][0]
        if(buff_strength > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_strength) + " Strength "
        
        cur.execute("SELECT stamina FROM Buff WHERE id = ?", (buff_slot_1,))
        buff_stamina = cur.fetchall()[0][0]
        if(buff_stamina > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_stamina) + " Stamina "
        
        cur.execute("SELECT dexterity FROM Buff WHERE id = ?", (buff_slot_1,))
        buff_dexterity = cur.fetchall()[0][0]
        if(buff_dexterity > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_dexterity) + " Dexterity "

        cur.execute("SELECT agility FROM Buff WHERE id = ?", (buff_slot_1,))
        buff_agility = cur.fetchall()[0][0]
        if(buff_agility > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_agility) + " Agility "
        
        cur.execute("SELECT intelligence FROM Buff WHERE id = ?", (buff_slot_1,))
        buff_intelligence = cur.fetchall()[0][0]
        if(buff_intelligence > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_intelligence) + " Intelligence "

        cur.execute("SELECT charisma FROM Buff WHERE id = ?", (buff_slot_1,))
        buff_charisma = cur.fetchall()[0][0]
        if(buff_charisma > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_charisma) + " Charisma"

        print('{:2s}{:8s}{:<108s}{:2s}'.format("| ", "", buff_stat_list, " |"))
        print('{:2s}{:116s}{:2s}'.format("| ", "", " |"))

    #buff slot 2
    if(buff_slot_2 > 0):
        print('{:2s}{:>4}{:1s}{:3s}{:<108s}{:2s}'.format("| ", buff_slot_2_timer, "s", " : ", buff_slot_2_name, " |"))
        
        buff_stat_list = ""
        cur.execute("SELECT max_health FROM Buff WHERE id = ?", (buff_slot_2,))
        buff_max_health = cur.fetchall()[0][0]
        if(buff_max_health > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_max_health) + " Health "
        
        cur.execute("SELECT max_mana FROM Buff WHERE id = ?", (buff_slot_2,))
        buff_max_mana = cur.fetchall()[0][0]
        if(buff_max_mana > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_max_mana) + " Mana "

        cur.execute("SELECT strength FROM Buff WHERE id = ?", (buff_slot_2,))
        buff_strength = cur.fetchall()[0][0]
        if(buff_strength > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_strength) + " Strength "
        
        cur.execute("SELECT stamina FROM Buff WHERE id = ?", (buff_slot_2,))
        buff_stamina = cur.fetchall()[0][0]
        if(buff_stamina > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_stamina) + " Stamina "
        
        cur.execute("SELECT dexterity FROM Buff WHERE id = ?", (buff_slot_2,))
        buff_dexterity = cur.fetchall()[0][0]
        if(buff_dexterity > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_dexterity) + " Dexterity "

        cur.execute("SELECT agility FROM Buff WHERE id = ?", (buff_slot_2,))
        buff_agility = cur.fetchall()[0][0]
        if(buff_agility > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_agility) + " Agility "
        
        cur.execute("SELECT intelligence FROM Buff WHERE id = ?", (buff_slot_2,))
        buff_intelligence = cur.fetchall()[0][0]
        if(buff_intelligence > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_intelligence) + " Intelligence "

        cur.execute("SELECT charisma FROM Buff WHERE id = ?", (buff_slot_2,))
        buff_charisma = cur.fetchall()[0][0]
        if(buff_charisma > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_charisma) + " Charisma"

        print('{:2s}{:8s}{:<108s}{:2s}'.format("| ", "", buff_stat_list, " |"))
        print('{:2s}{:116s}{:2s}'.format("| ", "", " |"))

    #buff slot 3
    if(buff_slot_3 > 0):
        print('{:2s}{:>4}{:1s}{:3s}{:<108s}{:2s}'.format("| ", buff_slot_3_timer, "s", " : ", buff_slot_3_name, " |"))

        buff_stat_list = ""
        cur.execute("SELECT max_health FROM Buff WHERE id = ?", (buff_slot_3,))
        buff_max_health = cur.fetchall()[0][0]
        if(buff_max_health > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_max_health) + " Health "
        
        cur.execute("SELECT max_mana FROM Buff WHERE id = ?", (buff_slot_3,))
        buff_max_mana = cur.fetchall()[0][0]
        if(buff_max_mana > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_max_mana) + " Mana "

        cur.execute("SELECT strength FROM Buff WHERE id = ?", (buff_slot_3,))
        buff_strength = cur.fetchall()[0][0]
        if(buff_strength > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_strength) + " Strength "
        
        cur.execute("SELECT stamina FROM Buff WHERE id = ?", (buff_slot_3,))
        buff_stamina = cur.fetchall()[0][0]
        if(buff_stamina > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_stamina) + " Stamina "
        
        cur.execute("SELECT dexterity FROM Buff WHERE id = ?", (buff_slot_3,))
        buff_dexterity = cur.fetchall()[0][0]
        if(buff_dexterity > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_dexterity) + " Dexterity "

        cur.execute("SELECT agility FROM Buff WHERE id = ?", (buff_slot_3,))
        buff_agility = cur.fetchall()[0][0]
        if(buff_agility > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_agility) + " Agility "
        
        cur.execute("SELECT intelligence FROM Buff WHERE id = ?", (buff_slot_3,))
        buff_intelligence = cur.fetchall()[0][0]
        if(buff_intelligence > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_intelligence) + " Intelligence "

        cur.execute("SELECT charisma FROM Buff WHERE id = ?", (buff_slot_3,))
        buff_charisma = cur.fetchall()[0][0]
        if(buff_charisma > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_charisma) + " Charisma"

        print('{:2s}{:8s}{:<108s}{:2s}'.format("| ", "", buff_stat_list, " |"))
        print('{:2s}{:116s}{:2s}'.format("| ", "", " |"))

    #buff slot 4
    if(buff_slot_4 > 0):
        print('{:2s}{:>4}{:1s}{:3s}{:<108s}{:2s}'.format("| ", buff_slot_4_timer, "s", " : ", buff_slot_4_name, " |"))

        buff_stat_list = ""
        cur.execute("SELECT max_health FROM Buff WHERE id = ?", (buff_slot_4,))
        buff_max_health = cur.fetchall()[0][0]
        if(buff_max_health > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_max_health) + " Health "
        
        cur.execute("SELECT max_mana FROM Buff WHERE id = ?", (buff_slot_4,))
        buff_max_mana = cur.fetchall()[0][0]
        if(buff_max_mana > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_max_mana) + " Mana "

        cur.execute("SELECT strength FROM Buff WHERE id = ?", (buff_slot_4,))
        buff_strength = cur.fetchall()[0][0]
        if(buff_strength > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_strength) + " Strength "
        
        cur.execute("SELECT stamina FROM Buff WHERE id = ?", (buff_slot_4,))
        buff_stamina = cur.fetchall()[0][0]
        if(buff_stamina > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_stamina) + " Stamina "
        
        cur.execute("SELECT dexterity FROM Buff WHERE id = ?", (buff_slot_4,))
        buff_dexterity = cur.fetchall()[0][0]
        if(buff_dexterity > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_dexterity) + " Dexterity "

        cur.execute("SELECT agility FROM Buff WHERE id = ?", (buff_slot_4,))
        buff_agility = cur.fetchall()[0][0]
        if(buff_agility > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_agility) + " Agility "
        
        cur.execute("SELECT intelligence FROM Buff WHERE id = ?", (buff_slot_4,))
        buff_intelligence = cur.fetchall()[0][0]
        if(buff_intelligence > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_intelligence) + " Intelligence "

        cur.execute("SELECT charisma FROM Buff WHERE id = ?", (buff_slot_4,))
        buff_charisma = cur.fetchall()[0][0]
        if(buff_charisma > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_charisma) + " Charisma"

        print('{:2s}{:8s}{:<108s}{:2s}'.format("| ", "", buff_stat_list, " |"))
        print('{:2s}{:116s}{:2s}'.format("| ", "", " |"))

    #buff slot 5
    if(buff_slot_5 > 0):
        print('{:2s}{:>4}{:1s}{:3s}{:<108s}{:2s}'.format("| ", buff_slot_5_timer, "s", " : ", buff_slot_5_name, " |"))

        buff_stat_list = ""
        cur.execute("SELECT max_health FROM Buff WHERE id = ?", (buff_slot_5,))
        buff_max_health = cur.fetchall()[0][0]
        if(buff_max_health > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_max_health) + " Health "
        
        cur.execute("SELECT max_mana FROM Buff WHERE id = ?", (buff_slot_5,))
        buff_max_mana = cur.fetchall()[0][0]
        if(buff_max_mana > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_max_mana) + " Mana "

        cur.execute("SELECT strength FROM Buff WHERE id = ?", (buff_slot_5,))
        buff_strength = cur.fetchall()[0][0]
        if(buff_strength > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_strength) + " Strength "
        
        cur.execute("SELECT stamina FROM Buff WHERE id = ?", (buff_slot_5,))
        buff_stamina = cur.fetchall()[0][0]
        if(buff_stamina > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_stamina) + " Stamina "
        
        cur.execute("SELECT dexterity FROM Buff WHERE id = ?", (buff_slot_5,))
        buff_dexterity = cur.fetchall()[0][0]
        if(buff_dexterity > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_dexterity) + " Dexterity "

        cur.execute("SELECT agility FROM Buff WHERE id = ?", (buff_slot_5,))
        buff_agility = cur.fetchall()[0][0]
        if(buff_agility > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_agility) + " Agility "
        
        cur.execute("SELECT intelligence FROM Buff WHERE id = ?", (buff_slot_5,))
        buff_intelligence = cur.fetchall()[0][0]
        if(buff_intelligence > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_intelligence) + " Intelligence "

        cur.execute("SELECT charisma FROM Buff WHERE id = ?", (buff_slot_5,))
        buff_charisma = cur.fetchall()[0][0]
        if(buff_charisma > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_charisma) + " Charisma"

        print('{:2s}{:8s}{:<108s}{:2s}'.format("| ", "", buff_stat_list, " |"))
        print('{:2s}{:116s}{:2s}'.format("| ", "", " |"))
    
    #buff slot 6
    if(buff_slot_6 > 0):
        print('{:2s}{:>4}{:1s}{:3s}{:<108s}{:2s}'.format("| ", buff_slot_6_timer, "s", " : ", buff_slot_6_name, " |"))

        buff_stat_list = ""
        cur.execute("SELECT max_health FROM Buff WHERE id = ?", (buff_slot_6,))
        buff_max_health = cur.fetchall()[0][0]
        if(buff_max_health > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_max_health) + " Health "
        
        cur.execute("SELECT max_mana FROM Buff WHERE id = ?", (buff_slot_6,))
        buff_max_mana = cur.fetchall()[0][0]
        if(buff_max_mana > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_max_mana) + " Mana "

        cur.execute("SELECT strength FROM Buff WHERE id = ?", (buff_slot_6,))
        buff_strength = cur.fetchall()[0][0]
        if(buff_strength > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_strength) + " Strength "
        
        cur.execute("SELECT stamina FROM Buff WHERE id = ?", (buff_slot_6,))
        buff_stamina = cur.fetchall()[0][0]
        if(buff_stamina > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_stamina) + " Stamina "
        
        cur.execute("SELECT dexterity FROM Buff WHERE id = ?", (buff_slot_6,))
        buff_dexterity = cur.fetchall()[0][0]
        if(buff_dexterity > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_dexterity) + " Dexterity "

        cur.execute("SELECT agility FROM Buff WHERE id = ?", (buff_slot_6,))
        buff_agility = cur.fetchall()[0][0]
        if(buff_agility > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_agility) + " Agility "
        
        cur.execute("SELECT intelligence FROM Buff WHERE id = ?", (buff_slot_6,))
        buff_intelligence = cur.fetchall()[0][0]
        if(buff_intelligence > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_intelligence) + " Intelligence "

        cur.execute("SELECT charisma FROM Buff WHERE id = ?", (buff_slot_6,))
        buff_charisma = cur.fetchall()[0][0]
        if(buff_charisma > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_charisma) + " Charisma"

        print('{:2s}{:8s}{:<108s}{:2s}'.format("| ", "", buff_stat_list, " |"))
        print('{:2s}{:116s}{:2s}'.format("| ", "", " |"))

    #buff slot 7
    if(buff_slot_7 > 0):
        print('{:2s}{:>4}{:1s}{:3s}{:<108s}{:2s}'.format("| ", buff_slot_7_timer, "s", " : ", buff_slot_7_name, " |"))

        buff_stat_list = ""
        cur.execute("SELECT max_health FROM Buff WHERE id = ?", (buff_slot_7,))
        buff_max_health = cur.fetchall()[0][0]
        if(buff_max_health > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_max_health) + " Health "
        
        cur.execute("SELECT max_mana FROM Buff WHERE id = ?", (buff_slot_7,))
        buff_max_mana = cur.fetchall()[0][0]
        if(buff_max_mana > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_max_mana) + " Mana "

        cur.execute("SELECT strength FROM Buff WHERE id = ?", (buff_slot_7,))
        buff_strength = cur.fetchall()[0][0]
        if(buff_strength > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_strength) + " Strength "
        
        cur.execute("SELECT stamina FROM Buff WHERE id = ?", (buff_slot_7,))
        buff_stamina = cur.fetchall()[0][0]
        if(buff_stamina > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_stamina) + " Stamina "
        
        cur.execute("SELECT dexterity FROM Buff WHERE id = ?", (buff_slot_7,))
        buff_dexterity = cur.fetchall()[0][0]
        if(buff_dexterity > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_dexterity) + " Dexterity "

        cur.execute("SELECT agility FROM Buff WHERE id = ?", (buff_slot_7,))
        buff_agility = cur.fetchall()[0][0]
        if(buff_agility > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_agility) + " Agility "
        
        cur.execute("SELECT intelligence FROM Buff WHERE id = ?", (buff_slot_7,))
        buff_intelligence = cur.fetchall()[0][0]
        if(buff_intelligence > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_intelligence) + " Intelligence "

        cur.execute("SELECT charisma FROM Buff WHERE id = ?", (buff_slot_7,))
        buff_charisma = cur.fetchall()[0][0]
        if(buff_charisma > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_charisma) + " Charisma"

        print('{:2s}{:8s}{:<108s}{:2s}'.format("| ", "", buff_stat_list, " |"))
        print('{:2s}{:116s}{:2s}'.format("| ", "", " |"))

    #buff slot 8
    if(buff_slot_8 > 0):
        print('{:2s}{:>4}{:1s}{:3s}{:<108s}{:2s}'.format("| ", buff_slot_8_timer, "s", " : ", buff_slot_8_name, " |"))

        buff_stat_list = ""
        cur.execute("SELECT max_health FROM Buff WHERE id = ?", (buff_slot_8,))
        buff_max_health = cur.fetchall()[0][0]
        if(buff_max_health > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_max_health) + " Health "
        
        cur.execute("SELECT max_mana FROM Buff WHERE id = ?", (buff_slot_8,))
        buff_max_mana = cur.fetchall()[0][0]
        if(buff_max_mana > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_max_mana) + " Mana "

        cur.execute("SELECT strength FROM Buff WHERE id = ?", (buff_slot_8,))
        buff_strength = cur.fetchall()[0][0]
        if(buff_strength > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_strength) + " Strength "
        
        cur.execute("SELECT stamina FROM Buff WHERE id = ?", (buff_slot_8,))
        buff_stamina = cur.fetchall()[0][0]
        if(buff_stamina > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_stamina) + " Stamina "
        
        cur.execute("SELECT dexterity FROM Buff WHERE id = ?", (buff_slot_8,))
        buff_dexterity = cur.fetchall()[0][0]
        if(buff_dexterity > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_dexterity) + " Dexterity "

        cur.execute("SELECT agility FROM Buff WHERE id = ?", (buff_slot_8,))
        buff_agility = cur.fetchall()[0][0]
        if(buff_agility > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_agility) + " Agility "
        
        cur.execute("SELECT intelligence FROM Buff WHERE id = ?", (buff_slot_8,))
        buff_intelligence = cur.fetchall()[0][0]
        if(buff_intelligence > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_intelligence) + " Intelligence "

        cur.execute("SELECT charisma FROM Buff WHERE id = ?", (buff_slot_8,))
        buff_charisma = cur.fetchall()[0][0]
        if(buff_charisma > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_charisma) + " Charisma"

        print('{:2s}{:8s}{:<108s}{:2s}'.format("| ", "", buff_stat_list, " |"))
        print('{:2s}{:116s}{:2s}'.format("| ", "", " |"))

    #buff slot 9
    if(buff_slot_9 > 0):
        print('{:2s}{:>4}{:1s}{:3s}{:<108s}{:2s}'.format("| ", buff_slot_9_timer, "s", " : ", buff_slot_9_name, " |"))

        buff_stat_list = ""
        cur.execute("SELECT max_health FROM Buff WHERE id = ?", (buff_slot_9,))
        buff_max_health = cur.fetchall()[0][0]
        if(buff_max_health > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_max_health) + " Health "
        
        cur.execute("SELECT max_mana FROM Buff WHERE id = ?", (buff_slot_9,))
        buff_max_mana = cur.fetchall()[0][0]
        if(buff_max_mana > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_max_mana) + " Mana "

        cur.execute("SELECT strength FROM Buff WHERE id = ?", (buff_slot_9,))
        buff_strength = cur.fetchall()[0][0]
        if(buff_strength > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_strength) + " Strength "
        
        cur.execute("SELECT stamina FROM Buff WHERE id = ?", (buff_slot_9,))
        buff_stamina = cur.fetchall()[0][0]
        if(buff_stamina > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_stamina) + " Stamina "
        
        cur.execute("SELECT dexterity FROM Buff WHERE id = ?", (buff_slot_9,))
        buff_dexterity = cur.fetchall()[0][0]
        if(buff_dexterity > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_dexterity) + " Dexterity "

        cur.execute("SELECT agility FROM Buff WHERE id = ?", (buff_slot_9,))
        buff_agility = cur.fetchall()[0][0]
        if(buff_agility > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_agility) + " Agility "
        
        cur.execute("SELECT intelligence FROM Buff WHERE id = ?", (buff_slot_9,))
        buff_intelligence = cur.fetchall()[0][0]
        if(buff_intelligence > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_intelligence) + " Intelligence "

        cur.execute("SELECT charisma FROM Buff WHERE id = ?", (buff_slot_9,))
        buff_charisma = cur.fetchall()[0][0]
        if(buff_charisma > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_charisma) + " Charisma"

        print('{:2s}{:8s}{:<108s}{:2s}'.format("| ", "", buff_stat_list, " |"))
        print('{:2s}{:116s}{:2s}'.format("| ", "", " |"))

    #buff slot 10
    if(buff_slot_10 > 0):
        print('{:2s}{:>4}{:1s}{:3s}{:<108s}{:2s}'.format("| ", buff_slot_10_timer, "s", " : ", buff_slot_10_name, " |"))

        buff_stat_list = ""
        cur.execute("SELECT max_health FROM Buff WHERE id = ?", (buff_slot_10,))
        buff_max_health = cur.fetchall()[0][0]
        if(buff_max_health > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_max_health) + " Health "
        
        cur.execute("SELECT max_mana FROM Buff WHERE id = ?", (buff_slot_10,))
        buff_max_mana = cur.fetchall()[0][0]
        if(buff_max_mana > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_max_mana) + " Mana "

        cur.execute("SELECT strength FROM Buff WHERE id = ?", (buff_slot_10,))
        buff_strength = cur.fetchall()[0][0]
        if(buff_strength > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_strength) + " Strength "
        
        cur.execute("SELECT stamina FROM Buff WHERE id = ?", (buff_slot_10,))
        buff_stamina = cur.fetchall()[0][0]
        if(buff_stamina > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_stamina) + " Stamina "
        
        cur.execute("SELECT dexterity FROM Buff WHERE id = ?", (buff_slot_10,))
        buff_dexterity = cur.fetchall()[0][0]
        if(buff_dexterity > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_dexterity) + " Dexterity "

        cur.execute("SELECT agility FROM Buff WHERE id = ?", (buff_slot_10,))
        buff_agility = cur.fetchall()[0][0]
        if(buff_agility > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_agility) + " Agility "
        
        cur.execute("SELECT intelligence FROM Buff WHERE id = ?", (buff_slot_10,))
        buff_intelligence = cur.fetchall()[0][0]
        if(buff_intelligence > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_intelligence) + " Intelligence "

        cur.execute("SELECT charisma FROM Buff WHERE id = ?", (buff_slot_10,))
        buff_charisma = cur.fetchall()[0][0]
        if(buff_charisma > 0):
            buff_stat_list = buff_stat_list + "+" + str(buff_charisma) + " Charisma"

        print('{:2s}{:8s}{:<108s}{:2s}'.format("| ", "", buff_stat_list, " |"))
        print('{:2s}{:116s}{:2s}'.format("| ", "", " |"))

    print(dash)

def Move(direction):

    #cur = conn.cursor()
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
    
def Combat(npc, npc_list):

    conn = create_connection(database)
    cur = conn.cursor()

    global stop_combat
    stop_combat = False
    win = False

    npc_slot = 0
    npc_id = 0
    npc_name = 0

    for each in npc_list:
        if(npc == each[2]):
            npc_slot = each[0]
            npc_id = each[1]
            npc_name = each[2]
            break

#-----------------------NPC_STUFF----------------------------------
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
    cur.execute("SELECT experience FROM Player_EXP_Table WHERE level = ?", (player_level + 1,))
    player_next_level_exp = cur.fetchall()[0][0]
    player_exp_percent =  round(player_totalexp / player_next_level_exp * 100, 5)

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


    player_damage_min += player_strength
    player_damage_max += player_strength

    player_hit_chance = round(player_dexterity / npc_agility * 100) #Raw percentage

    npc_hit_chance = round(npc_dexterity / player_agility * 100)
    print("NPC hit chance")
    print(npc_hit_chance)





    while(True):
        if(stop_combat):
            break

        print()
        player_hit_roll = random.randrange(1, 100)
        print("player hit chance: ", end='')
        print(player_hit_chance)
        print("player hit roll: ", end='')
        print(player_hit_roll)
        if(player_hit_roll < player_hit_chance):
            player_damage = random.randrange(player_damage_min, player_damage_max)
            print(name + " hits " + npc_name + " for " + str(player_damage) + " points of damage.")
        else:
            print(name + " misses " + npc_name + ".")

        print("[", end='')
        print(player_health, end='')
        print("/", end='')
        print(player_max_health, end=' ')
        print("(", end='')
        print(player_health / player_max_health * 100, end='')
        print("%) ", end='')
        print(player_mana, end='')
        print("/", end='')
        print(player_max_mana, end=' ')
        print("(", end='')
        print(player_mana / player_max_mana * 100, end='')
        print("%) ", end='')
        print("EXP: ", end='')
        print("{:0.2f}".format(player_exp_percent), end='')
        print("%", end='')
        print("]", end='')
        #print(">", end='')
        print(">")
        time.sleep(1.5)
        
        print()
        npc_hit_roll = random.randrange(1, 100)
        print("npc hit chance: ", end='')
        print(npc_hit_chance)
        print("npc hit roll: ", end='')
        print(npc_hit_roll)
        if(npc_hit_roll < npc_hit_chance):
            npc_damage = random.randrange(npc_damage_min, npc_damage_max)
            print(npc_name + " hits " + name + " for " + str(npc_damage) + " points of damage.")
        else:
            print(npc_name + " misses " + name + ".")
        print("[", end='')
        print(player_health, end='')
        print("/", end='')
        print(player_max_health, end=' ')
        print("(", end='')
        print(player_health / player_max_health * 100, end='')
        print("%) ", end='')
        print(player_mana, end='')
        print("/", end='')
        print(player_max_mana, end=' ')
        print("(", end='')
        print(player_mana / player_max_mana * 100, end='')
        print("%) ", end='')
        print("EXP: ", end='')
        print("{:0.2f}".format(player_exp_percent), end='')
        print("%", end='')
        print("]", end='')
        #print(">", end='')
        print(">")
        time.sleep(1.5)

        if(player_health <= 0):
            print("You died.")
            break
        if(npc_health <= 0):
            print(str(npc_name) + " has been slain.")
            win = True
            break


    #Awarding EXP
    if(win == True):
        #Award EXP directly
        pass



    conn.close()

def Command(choice):
    if(choice.lower() == 'north' or choice.lower() == 'n' or choice.lower() == 'south' or choice.lower() == 's' or choice.lower() == 'east' or choice.lower() == 'e' or choice.lower() == 'west' or choice.lower() == 'w'):
        Move(choice.lower())

    elif(choice.lower() == 'score' or choice.lower() == 'character'):
        Score()

    elif(choice.lower() == 'look' or choice.lower() == 'l'):
        Look()

    elif(choice.lower() == 'equipment'):
        Show_Equipment()

    elif(choice.lower() == 'inventory'):
        Show_Inventory()

    elif(choice.lower() == 'buffs'):
        Show_Buffs()

    elif(choice.lower()[0:4] == 'kill'):
        global stop_combat
        #stop_combat = False
        npc_list = Show_NPC()

        conn = create_connection(database)
        cur = conn.cursor()
        conn.close()
        
        thread = threading.Thread(target = Combat, args = (choice.lower()[5:], npc_list))
        thread.daemon = True
        thread.start()

        while True:
            choice = input("")
            if choice == 'flee':
                stop_combat = True
                #thread.join()
                time.sleep(2)
                break

        
        conn = create_connection(database)
        cur = conn.cursor()
        
    else:
        print("That is not a valid command.")
        print()


def Login():
    global cur
    global name
    delete_char_flag = 0
    while(delete_char_flag == 0):

        print()
        print("New")
        print("Load")
        print("Delete")
        choice = input(">")
        choice = choice.lower()
    
    
        if(choice == "load"):
            
            invalid = 1
            while(invalid == 1):
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
                    invalid = 0
                else:
                    print("That is not a valid character, please try again.")
            
            invalid = 1
            while(invalid == 1):
                print()
                print("Please enter your password.")
                password = input(">")

                #Verifying password
                cur.execute("SELECT salt FROM Player WHERE name = ?", (name,))
                salt = cur.fetchall()[0][0]
                cur.execute("SELECT pkey FROM Player WHERE name = ?", (name,))
                pkey = cur.fetchall()[0][0]

                new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

                if(pkey == new_key):
                    invalid = 0
                else:
                    print()
                    print("Your password was incorrect.")

            print("Welcome back ", end='')
            print(name, end='')
            print("!")
            delete_char_flag = 1
        


        elif(choice == "new"):
            
            invalid = 1
            while(invalid == 1):
                print()
                print("What is your name?")
                name = input(">")

                cur = conn.cursor()
                cur.execute("SELECT count(*) FROM Player WHERE name = ?", (name,))
                if(cur.fetchall()[0][0] == 0):
                    invalid = 0
                else:
                    print()
                    print("That character already exists, please try again.")

            invalid = 1
            while(invalid == 1):

                print()
                print("What would you like your password to be?")
                password1 = input(">")
                print()
                print("Please enter it in again")
                password2 = input(">")
                if(password1 == password2):
                    invalid = 0
                    password = password1
                else:
                    print()
                    print("Your passwords did not match, please try again.")

                # Example generation
                salt = os.urandom(32)
                pkey = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

                # Store them as:
                final_password_hash = salt + pkey 

            invalid = 1
            while(invalid == 1):
                print()
                print("Which class will you choose?")
                print("Warrior")
                choice = input(">")
                print()
                if(choice.lower() == "warrior"):
                    invalid = 0
                    pclass = "Warrior"
                else:
                    print()
                    print("Please select a valid class.")
            
            if(pclass == "Warrior"):
                health = 25
                base_max_health = 25
                max_health = 25
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
                equipment_primary = 0
                equipment_secondary = 0
                equipment_head = 0
                equipment_body = 0
                equipment_feet = 0
                equipment_hands = 0
                create_player(conn, name, final_password_hash[32:], final_password_hash[:32], pclass, health, base_max_health, max_health, mana, base_max_mana, max_mana, base_strength, strength, base_stamina, stamina, base_dexterity, dexterity, base_agility, agility, base_intelligence, intelligence, base_wisdom, wisdom, base_charisma, charisma, equipment_primary, equipment_secondary, equipment_head, equipment_body, equipment_feet, equipment_hands)
            
            print()
            print("Welcome, " + name + " to the Empire of Zek!")
            delete_char_flag = 1
        
        elif(choice == "delete"):
            invalid = 1
            while(invalid == 1):
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
                    invalid = 0
                else:
                    print("That is not a valid character, please try again.")
            invalid = 1
            while(invalid == 1):
                print()
                print("Please enter your password.")
                password = input(">")

                #Verifying password
                cur.execute("SELECT salt FROM Player WHERE name = ?", (name,))
                salt = cur.fetchall()[0][0]
                cur.execute("SELECT pkey FROM Player WHERE name = ?", (name,))
                pkey = cur.fetchall()[0][0]

                new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

                if(pkey == new_key):
                    invalid = 0
                    print(name, end ="")
                    print(" has been removed from the Empire of Zek for eternity.")
                    delete_player(conn, name)
                else:
                    print()
                    print("Your password was incorrect.")
    Look()

def MainLoop():

    while(True):
        #-------------------------------PROMPT----------------------------------
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
        cur.execute("SELECT experience FROM Player_EXP_Table WHERE level = ?", (level + 1,))
        next_level_exp = cur.fetchall()[0][0]
        exp_percent =  round(totalexp / next_level_exp * 100, 5)

        #print()
        #print("HP: ", end='')
        print("[", end='')
        print(health, end='')
        print("/", end='')
        print(max_health, end=' ')
        print("(", end='')
        print(health / max_health * 100, end='')
        print("%) ", end='')
        print(mana, end='')
        print("/", end='')
        print(max_mana, end=' ')
        print("(", end='')
        print(mana / max_mana * 100, end='')
        print("%) ", end='')
        print("EXP: ", end='')
        print("{:0.2f}".format(exp_percent), end='')
        print("%", end='')
        print("]", end='')
        print(">", end='')
        #-----------------------------------------------------------------------
        choice = input()

        if(choice.lower() == 'quit'):
            print("You have left the realm.")
            break

        Command(choice)




#------------------------MAIN--------------------------
def main():

    Login()
    MainLoop()

main()