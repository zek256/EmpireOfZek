import sqlite3
from sqlite3 import Error
from Player import Player


#-----------------------GET_STAT-----------------------
#cur.execute('SELECT name FROM Player WHERE pid = ?', (pid,))
#print(cur.fetchall())

#-----------------------SET_STAT-----------------------
#sql = "UPDATE Player SET base_strength = '5' WHERE pid = ?"
#cur = conn.cursor()
#cur.execute(sql, (pid,))
#conn.commit()


pid = -1

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

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
    
def create_player(conn, pid, name, location, totalexp, level, base_max_health, base_max_mana, base_strength, base_stamina, base_dexterity, base_agility, base_intelligence, base_wisdom, base_charisma, equipment_primary, equipment_secondary, equipment_head, equipment_body, equipment_feet, equipment_hands, gold, inventory_slot_1, inventory_slot_2, inventory_slot_3, inventory_slot_4, inventory_slot_5, inventory_slot_6, inventory_slot_7, inventory_slot_8, inventory_slot_9, inventory_slot_10, inventory_slot_11, inventory_slot_12, inventory_slot_13, inventory_slot_14, inventory_slot_15, inventory_slot_16, inventory_slot_17, inventory_slot_18, inventory_slot_19, inventory_slot_20):
    """
    Create a Player
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql = """ INSERT INTO Player (
        pid,
        name,
        location,
        totalexp,
        level,
        base_max_health,
        base_max_mana,
        base_strength,
        base_stamina,
        base_dexterity,
        base_agility,
        base_intelligence,
        base_wisdom,
        base_charisma,
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
        inventory_slot_20
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """
    #(id, name, location, totalexp, level, base_max_health, base_max_mana, base_strength, base_stamina, base_dexterity, base_agility, base_intelligence, base_wisdom, base_charisma, equipment_primary, equipment_secondary, equipment_head, equipment_body, equipment_feet, equipment_hands, gold, invetory_slot_1, invetory_slot_2, invetory_slot_3, invetory_slot_4, invetory_slot_5, invetory_slot_6, invetory_slot_7, invetory_slot_8, invetory_slot_9, invetory_slot_10, invetory_slot_11, invetory_slot_12, invetory_slot_13, invetory_slot_14, invetory_slot_15, invetory_slot_16, invetory_slot_17, invetory_slot_18, invetory_slot_19, invetory_slot_20)
    cur = conn.cursor()
    cur.execute(sql, (pid, name, location, totalexp, level, base_max_health, base_max_mana, base_strength, base_stamina, base_dexterity, base_agility, base_intelligence, base_wisdom, base_charisma, equipment_primary, equipment_secondary, equipment_head, equipment_body, equipment_feet, equipment_hands, gold, inventory_slot_1, inventory_slot_2, inventory_slot_3, inventory_slot_4, inventory_slot_5, inventory_slot_6, inventory_slot_7, inventory_slot_8, inventory_slot_9, inventory_slot_10, inventory_slot_11, inventory_slot_12, inventory_slot_13, inventory_slot_14, inventory_slot_15, inventory_slot_16, inventory_slot_17, inventory_slot_18, inventory_slot_19, inventory_slot_20))
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

def select_player(conn, pid):

    cur = conn.cursor()
    cur.execute('SELECT * FROM Player WHERE pid = ?', (pid,))

    return cur.fetchall()


def delete_player(conn, pid):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql = 'DELETE FROM Player WHERE pid=?'
    cur = conn.cursor()
    cur.execute(sql, (pid,))
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


#------------------------MAIN--------------------------
def main():

    database = r"pythonsqlite.db"
    conn = create_connection(database)

    #If Player table needs to be dropped
    #cur = conn.cursor()
    #cur.execute("DROP TABLE Player")
    #conn.commit()

    sql_create_player_table = """ CREATE TABLE IF NOT EXISTS Player (
        pid integer PRIMARY KEY,
        name text NOT NULL,
        location integer,
        totalexp integer,
        level integer,
        base_max_health integer,
        base_max_mana integer,
        base_strength integer,
        base_stamina integer,
        base_dexterity integer,
        base_agility integer,
        base_intelligence integer,
        base_wisdom integer,
        base_charisma integer,
        equipment_primary integer,
        equipment_secondary integer,
        equipment_head integer,
        equipment_body integer,
        equipment_feet integer,
        equipment_hands integer,
        gold integer,
        inventory_slot_1 integer,
        inventory_slot_2 integer,
        inventory_slot_3 integer,
        inventory_slot_4 integer,
        inventory_slot_5 integer,
        inventory_slot_6 integer,
        inventory_slot_7 integer,
        inventory_slot_8 integer,
        inventory_slot_9 integer,
        inventory_slot_10 integer,
        inventory_slot_11 integer,
        inventory_slot_12 integer,
        inventory_slot_13 integer,
        inventory_slot_14 integer,
        inventory_slot_15 integer,
        inventory_slot_16 integer,
        inventory_slot_17 integer,
        inventory_slot_18 integer,
        inventory_slot_19 integer,
        inventory_slot_20 integer
        ); """

    if conn is not None:
        # create projects table
        create_table(conn, sql_create_player_table)

    else:
        print("Error! cannot create the database connection.")


    #create_player(conn, 1, "Jon", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    print(select_all_player(conn))
    #delete_all_Player(conn)
    print(count_player(conn)[0][0])


    








    print("New")
    print("Load")
    print("Delete")
    choice = input(">")

    if(choice == "Load"):
        tempString = select_all_player(conn)
        for each in tempString:
            print(each[0], end = "")
            print(" - ", end = "")
            print(each[1])
        
        print()
        print("Which number would you like to load?")
        choice = input(">")

        pid = choice

        sql = "UPDATE Player SET base_strength = '0' WHERE pid = ?"
        cur = conn.cursor()
        cur.execute(sql, (pid,))
        conn.commit()

        print(select_player(conn, pid))


    elif(choice == "New"):
        
        pid = count_player(conn)[0][0]
        
        print("What is your name?")
        name = input(">")

        create_player(conn, pid, name, 550, 0, 0, 25, 0, 15, 20, 10, 10, 5, 5, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        
        print("Welcome, " + name + " to the Empire of Zek!")
    
    elif(choice == "Delete"):
        
        tempString = select_all_player(conn)
        for each in tempString:
            print(each[0], end = "")
            print(" - ", end = "")
            print(each[1])
        
        print()
        print("Which number would you like to delete?")
        choice = input(">")
        
        cur = conn.cursor()
        cur.execute('SELECT name FROM Player WHERE pid = ?', (choice,))
        print(cur.fetchall()[0][0], end ="")
        print(" has been removed from the Empire of Zek for eternity.")

        delete_player(conn, choice)




main()



