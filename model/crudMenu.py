#Phoenix Burke Chang 21026891

from DataAccessObject import *
from tkinter import messagebox
from tkinter.messagebox import showerror, showinfo


class CrudMenu():
    def __init__(self):
        self.itemId = None
        self.itemName = None
        self.price = None
        self.menuCategory = None
        self.allergens = None

    def add_record(self, itemId, itemName, price, menuCategory, allergens, restaurantId):
        conn = sqlite3.connect('Database.db')
        c = conn.cursor()
        try:
            c.execute("INSERT INTO menu VALUES (?, ?, ?, ?, ?, ?)",
                (itemId, itemName, price, menuCategory, allergens, restaurantId))
            self.error_message = showinfo("Added!", "Your Record Has Been Added!")
        except:
            messagebox.showwarning("Duplicate Item ID", "Item ID already exists in the database.")
        print(itemId, itemName, price, menuCategory, allergens, restaurantId)
        conn.commit()
        conn.close()

    def delete_record(self, item_id, restaurantId):
        conn = sqlite3.connect('Database.db')
        c = conn.cursor()
        c.execute("DELETE FROM menu WHERE itemId=? AND restaurantId=?", (item_id, restaurantId))
        conn.commit()
        conn.close()

    def query_database(self):
        conn = sqlite3.connect('Database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM menu")
        records = c.fetchall()
        print("Fetchall:", records)
        conn.commit()
        conn.close()
        return records