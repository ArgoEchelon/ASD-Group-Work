#Phoenix Burke Chang 21026891

from DataAccessObject import *
from tkinter import messagebox
from tkinter.messagebox import showerror, showinfo


class Inventory():
    def __init__(self):
        self.stockId = None
        self.stockNum = None
        self.stockPrice = None

    def add_record(self, stockId, stockNum, stockPrice, restaurantId):
        conn = sqlite3.connect('Database.db')
        c = conn.cursor()
        try:
            c.execute("INSERT INTO inventory VALUES (?, ?, ?, ?)",
                (stockId, stockNum, stockPrice, restaurantId))
            self.error_message = showinfo("Added!", "Your Record Has Been Added!")
        except:
            messagebox.showwarning("Duplicate Stock ID", "Stock ID already exists in the database.")
        conn.commit()
        conn.close()

    def delete_record(self, stock_id, restaurantId):
        conn = sqlite3.connect('Database.db')
        c = conn.cursor()
        c.execute("DELETE FROM inventory WHERE stockId=? AND restaurantId=?", (stock_id, restaurantId))
        conn.commit()
        conn.close()

    def query_database(self):
        conn = sqlite3.connect('Database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM inventory")
        records = c.fetchall()
        print("Fetchall:", records)
        conn.commit()
        conn.close()
        return records