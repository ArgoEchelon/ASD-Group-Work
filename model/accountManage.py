#Phoenix Burke Chang 21026891

from DataAccessObject import *
from tkinter import messagebox
from tkinter.messagebox import showerror, showinfo

class AccountManage():
    def __init__(self):
        self.staffId = None
        self.password = None
        self.firstname = None
        self.lastname = None
        self.staffType = None

    def add_record(self, staffId, password, firstname, lastname, staffType, restaurantId):
        conn = sqlite3.connect('Database.db')
        c = conn.cursor()
        try:
            c.execute("INSERT INTO staff VALUES (?, ?, ?, ?, ?, ?)",
                (staffId, password, firstname, lastname, staffType, restaurantId))
            self.error_message = showinfo("Added!", "Your Record Has Been Added!")
        except:
            messagebox.showwarning("Duplicate Staff ID", "Staff ID already exists in the database.")
        conn.commit()
        conn.close()

    def delete_record(self, staff_id, restaurantId):
        conn = sqlite3.connect('Database.db')
        c = conn.cursor()
        c.execute("DELETE FROM staff WHERE staffId=? AND restaurantId=?", (staff_id, restaurantId))
        conn.commit()
        conn.close()

    def query_database(self):
        conn = sqlite3.connect('Database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM staff")
        records = c.fetchall()
        print("Fetchall:", records)
        conn.commit()
        conn.close()
        return records