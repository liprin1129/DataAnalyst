import sqlite3
import csv
import os
from tqdm import tqdm

os.chdir(r'/Users/pure/Private_Local_Data/Study/Udacity/DataAnalyst/HomeWork/P3_Data_Wrangling/Project3_DataWrangling/')

# Helper function
def create_sql_connection(db_name):
    try:
        sql_connection = sqlite3.connect(db_name)
        return sql_connection
    
    except Error:
        print Error
    
    return None

def create_table(sql_connection, sql_command):
    try:
        cursor = sql_connection.cursor()
        cursor.execute(sql_command)
    except ValueError:
        print "Error: ", ValueError

def insert_data_to_table(sql_connection, sql_command, data):
    cursor = sql_connection.cursor()
    cursor.execute(sql_command, data)

# Create connection
sql_connection = create_sql_connection("data/sql_db/street_data.db")

# nodes csv to sql db
if False:
    create_table(sql_connection, """
        CREATE TABLE node(
            id INTEGER PRIMARY_KEY,
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
        with open("data/csv/nodes.csv", "r") as node_csv:
            node_dict = csv.DictReader(node_csv)

            for row in tqdm(node_dict):
                sql_command = "INSERT INTO node(id, lat, lon, user, uid, version, changeset, timestamp) VALUES (?,?,?,?,?,?,?,?);"
                insert_data = (row["id"], row["lat"], row["lon"], row["user"].decode('utf8'), row["uid"], row["version"], row["changeset"], row["timestamp"])
                
                insert_data_to_table(sql_connection, sql_command, insert_data)

# nodes tag csv to sql db
if False:
    create_table(sql_connection, """
        CREATE TABLE node_tags(
        id INTEGER,
        key TEXT,
        value TEXT,
        type TEXT,
        FOREIGN KEY (id) REFERENCES nodes(id)
        );
        """)

    with sql_connection:
        with open("data/csv/nodes_tags.csv", "r") as node_csv:
            node_dict = csv.DictReader(node_csv)
            
            for row in tqdm(node_dict):
                sql_command = "INSERT INTO node_tags(id, key, value, type) VALUES (?,?,?,?);"
                insert_data = (row["id"], row["key"].decode('utf8'), row["value"].decode('utf8'), row["type"].decode('utf8'))
                
                insert_data_to_table(sql_connection, sql_command, insert_data)

# way csv to sql db
if False:
    create_table(sql_connection, """
        CREATE TABLE way(
        id INTEGER,
        user TEXT,
        uid INTEGER,
        version TEXT,
        timestamp TEXT,
        changeset INTEGER,
        PRIMARY KEY(id, uid)
        );
        """)

    with sql_connection:
        with open("data/csv/ways.csv", "r") as node_csv:
            node_dict = csv.DictReader(node_csv)
            
            for row in tqdm(node_dict):
                #print row

                sql_command = "INSERT INTO way(id, user, uid, version, timestamp, changeset) VALUES (?,?,?,?,?,?);"
                insert_data = (row["id"], row["user"].decode('utf8'), row["uid"], row["version"].decode('utf8'), row["timestamp"].decode('utf8'), row["changeset"])
                
                insert_data_to_table(sql_connection, sql_command, insert_data)

# way nodes csv to sql db
if False:
    create_table(sql_connection, """
        CREATE TABLE way_nodes(
        id INTEGER,
        node_id INTEGER,
        position INTEGER,
        FOREIGN KEY (id) REFERENCES ways(id)
        );
        """)
    
    with sql_connection:
        with open("data/csv/ways_nodes.csv", "r") as node_csv:
            node_dict = csv.DictReader(node_csv)
            
            for row in tqdm(node_dict):
                
                sql_command = "INSERT INTO way_nodes(id, node_id, position) VALUES (?,?,?);"
                insert_data = (row["id"], row["node_id"], row["position"])
                
                insert_data_to_table(sql_connection, sql_command, insert_data)

# way tags csv to sql db
if False:
    create_table(sql_connection, """
        CREATE TABLE way_tags(
        id INTEGER,
        key TEXT,
        type TEXT,
        value TEXT,
        FOREIGN KEY (id) REFERENCES ways(id)
        );
        """)
    
    with sql_connection:
        with open("data/csv/ways_tags.csv", "r") as node_csv:
            node_dict = csv.DictReader(node_csv)
            
            for row in tqdm(node_dict):
                
                sql_command = "INSERT INTO way_tags(id, key, type, value) VALUES (?,?,?,?);"
                insert_data = (row["id"], row["key"].decode('utf8'), row["type"].decode('utf8'), row["value"].decode('utf8'))
                
                insert_data_to_table(sql_connection, sql_command, insert_data)
