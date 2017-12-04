import sqlite3
import csv
import os
os.chdir(r'/Users/pure/Private_Local_Data/Study/Udacity/DataAnalyst/HomeWork/P3_Data_Wrangling/Project3_DataWrangling/')

"""
    Create a connection of database to the SQLite database
    """

def create_sql_connection(db_name):
    try:
        sql_connection = sqlite3.connect(db_name)
        return sql_connection
    
    except Error:
        print Error
    
    return None

def create_table(sql_connection, sql_command):
    """
        if conn:
        command = '''
        Create Table nodes(id INTEGER PRIMARY_KEY, lat REAL, lon REAL, user TEXT, uid INTEGER, version TEXT, changeset INTEGER, timestamp TEXT);
        '''
        """
    try:
        cursor = sql_connection.cursor()
        cursor.execute(sql_command)
    except Error:
        print "Error: ", Error

# conn.commit

def insert_data_to_table(sql_connection, sql_command, data):
    #print list(node_dict)
    #cursor.executemany("INSERT INTO nodes(id, lat, lon, user, uid, version, changeset, timestamp) VALUES (?,?,?,?,?,?,?,?);", node_dict.values())
    cursor = sql_connection.cursor()
    #if len(data) != 1:
    cursor.execute(sql_command, data)
#for i in node_dict:
#print i['id']

sql_connection = create_sql_connection("data/sql_db/street_data.db")
create_table(sql_connection, """
    CREATE TABLE nodes(
        id INTEGER,
        lat REAL,
        lon REAL,
        user TEXT,
        uid INTEGER PRIMARY_KEY,
        version TEXT,
        changeset INTEGER,
        timestamp TEXT
    );
    """)

with sql_connection:
    with open("data/csv/nodes.csv", "r", encoding = "utf-8") as node_csv:
        node_dict = csv.DictReader(node_csv)
        for row in tqdm(node_dict):
            sql_command = "INSERT INTO nodes(id, lat, lon, user, uid, version, changeset, timestamp) VALUES (?,?,?,?,?,?,?,?);"
            insert_data = (row["id"], row["lat"], row["lon"], row["user"], row["uid"], row["version"], row["changeset"], row["timestamp"])
            
            insert_data_to_table(sql_connection, sql_command, insert_data)

