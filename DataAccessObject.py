#Zak Kannemeyer 22021286


import sqlite3
conn = sqlite3.connect('Database.db')

cur = conn.cursor()
if conn != None:
    print("Connection established")

def getCursor():
    return cur

def getConn():
    return conn