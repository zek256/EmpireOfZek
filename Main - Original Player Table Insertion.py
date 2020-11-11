import sqlite3
import hashlib
import os
from sqlite3 import Error
from Player import Player

database = r"pythonsqlite.db"
name = 'random'


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
    
def create_player(conn, name, pkey, salt, pclass, location, totalexp, level, current_health, base_max_health, max_health, current_mana, base_max_mana, max_mana, base_strength, strength, base_stamina, stamina, base_dexterity, dexterity, base_agility, agility, base_intelligence, intelligence, base_wisdom, wisdom, base_charisma, charisma, equipment_primary, equipment_secondary, equipment_head, equipment_body, equipment_feet, equipment_hands, gold, inventory_slot_1, inventory_slot_2, inventory_slot_3, inventory_slot_4, inventory_slot_5, inventory_slot_6, inventory_slot_7, inventory_slot_8, inventory_slot_9, inventory_slot_10, inventory_slot_11, inventory_slot_12, inventory_slot_13, inventory_slot_14, inventory_slot_15, inventory_slot_16, inventory_slot_17, inventory_slot_18, inventory_slot_19, inventory_slot_20, buff_slot_1, buff_slot_1_timer, buff_slot_2, buff_slot_2_timer, buff_slot_3, buff_slot_3_timer, buff_slot_4, buff_slot_4_timer, buff_slot_5, buff_slot_5_timer, buff_slot_6, buff_slot_6_timer, buff_slot_7, buff_slot_7_timer, buff_slot_8, buff_slot_8_timer, buff_slot_9, buff_slot_9_timer, buff_slot_10, buff_slot_10_timer):
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
        location,
        totalexp,
        level,
        current_health,
        base_max_health,
        max_health,
        current_mana,
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
        gold,
        inventory_slot_1,
        inventory_slot_2,
        inventory_slot_3,
        inventory_slot_4,
        inventory_slot_5,
        inventory_slot_6,
        inventory_slot_7,
        inventory_slot_8,
        inventory_slot_9,
        inventory_slot_10,
        inventory_slot_11,
        inventory_slot_12,
        inventory_slot_13,
        inventory_slot_14,
        inventory_slot_15,
        inventory_slot_16,
        inventory_slot_17,
        inventory_slot_18,
        inventory_slot_19,
        inventory_slot_20,
        buff_slot_1,
        buff_slot_1_timer,
        buff_slot_2,
        buff_slot_2_timer,
        buff_slot_3,
        buff_slot_3_timer,
        buff_slot_4,
        buff_slot_4_timer,
        buff_slot_5,
        buff_slot_5_timer,
        buff_slot_6,
        buff_slot_6_timer,
        buff_slot_7,
        buff_slot_7_timer,
        buff_slot_8,
        buff_slot_8_timer,
        buff_slot_9,
        buff_slot_9_timer,
        buff_slot_10,
        buff_slot_10_timer
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """
    #(id, name, location, totalexp, level, base_max_health, base_max_mana, base_strength, base_stamina, base_dexterity, base_agility, base_intelligence, base_wisdom, base_charisma, equipment_primary, equipment_secondary, equipment_head, equipment_body, equipment_feet, equipment_hands, gold, invetory_slot_1, invetory_slot_2, invetory_slot_3, invetory_slot_4, invetory_slot_5, invetory_slot_6, invetory_slot_7, invetory_slot_8, invetory_slot_9, invetory_slot_10, invetory_slot_11, invetory_slot_12, invetory_slot_13, invetory_slot_14, invetory_slot_15, invetory_slot_16, invetory_slot_17, invetory_slot_18, invetory_slot_19, invetory_slot_20)
    cur = conn.cursor()
    cur.execute(sql, (name, pkey, salt, pclass, location, totalexp, level, current_health, base_max_health, max_health, current_mana, base_max_mana, max_mana, base_strength, strength, base_stamina, stamina, base_dexterity, dexterity, base_agility, agility, base_intelligence, intelligence, base_wisdom, wisdom, base_charisma, charisma, equipment_primary, equipment_secondary, equipment_head, equipment_body, equipment_feet, equipment_hands, gold, inventory_slot_1, inventory_slot_2, inventory_slot_3, inventory_slot_4, inventory_slot_5, inventory_slot_6, inventory_slot_7, inventory_slot_8, inventory_slot_9, inventory_slot_10, inventory_slot_11, inventory_slot_12, inventory_slot_13, inventory_slot_14, inventory_slot_15, inventory_slot_16, inventory_slot_17, inventory_slot_18, inventory_slot_19, inventory_slot_20, buff_slot_1, buff_slot_1_timer, buff_slot_2, buff_slot_2_timer, buff_slot_3, buff_slot_3_timer, buff_slot_4, buff_slot_4_timer, buff_slot_5, buff_slot_5_timer, buff_slot_6, buff_slot_6_timer, buff_slot_7, buff_slot_7_timer, buff_slot_8, buff_slot_8_timer, buff_slot_9, buff_slot_9_timer, buff_slot_10, buff_slot_10_timer))
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
        npc20_existence,
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

def Look():
    cur = conn.cursor()
    cur.execute("SELECT location FROM Player WHERE name = ?", (name,))
    location = cur.fetchall()[0][0]
    cur.execute("SELECT description FROM Room WHERE location = ?", (location,))
    description = cur.fetchall()[0][0]
    print(description)

def Score():
    
    global name
    cur.execute("SELECT level FROM Player WHERE name = ?", (name,))
    level = cur.fetchall()[0][0]
    cur.execute("SELECT pclass FROM Player WHERE name = ?", (name,))
    pclass = cur.fetchall()[0][0]
    
    cur.execute("SELECT totalexp FROM Player WHERE name = ?", (name,))
    totalexp = cur.fetchall()[0][0]

    cur.execute("SELECT current_health FROM Player WHERE name = ?", (name,))
    current_health = cur.fetchall()[0][0]
    cur.execute("SELECT max_health FROM Player WHERE name = ?", (name,))
    max_health = cur.fetchall()[0][0]
    cur.execute("SELECT current_mana FROM Player WHERE name = ?", (name,))
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
    print('{:2s}{:<5s}{:3s}{:<17}{:3}{:<17s}{:3}{:<12}{:3}'.format("| ", "Level", " : ", level, " | ", "Next Level", " : ", totalexp, " | "))
    print('{:2s}{:<5s}{:3s}{:<17}{:3}{:<17s}{:3}{:<12}{:3}'.format("| ", "Class", " : ", pclass, " | ", "Seraphim Level", " : ", totalexp, " | "))
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
    

def Command(choice):
    if(choice.lower() == 'score'):
        Score()
    elif(choice.lower() == 'look'):
        Look()


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
                print()
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
            print()
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
                create_player(conn, name, final_password_hash[32:], final_password_hash[:32], pclass, 550, 0, 1, 25, 25, 25, 1, 1, 1, 15, 15, 20, 20, 10, 10, 10, 10, 5, 5, 5, 5, 8, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            
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
        cur.execute("SELECT current_health FROM Player WHERE name = ?", (name,))
        health = cur.fetchall()[0][0]
        cur.execute("SELECT max_health FROM Player WHERE name = ?", (name,))
        max_health = cur.fetchall()[0][0]
        cur.execute("SELECT current_mana FROM Player WHERE name = ?", (name,))
        mana = cur.fetchall()[0][0]
        cur.execute("SELECT max_mana FROM Player WHERE name = ?", (name,))
        max_mana = cur.fetchall()[0][0]
        print()
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
        print("%)", end='')
        print("]", end='')
        print(">", end='')
        #-----------------------------------------------------------------------
        choice = input()

        Command(choice)




#------------------------MAIN--------------------------
def main():

    Login()
    MainLoop()


    
    

main()



