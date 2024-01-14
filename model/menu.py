#Zak Kannemeyer 22021286

from DataAccessObject import *



class Menu():
    def __init__(self):
        self.menu_items = []
        self.get_menu()

    def get_menu(self):
        con = getConn()
        c = getCursor()
        query = "SELECT * FROM menu ORDER BY CASE menuCategory WHEN 'STARTER' THEN 1 WHEN 'MAIN' THEN 2 WHEN 'SIDE' THEN 3 WHEN 'DESSERT' THEN 4 WHEN 'DRINK' THEN 5 ELSE 6 END;"
        c.execute(query)
        record = c.fetchall()
        #print(record)
        self.menu_items = record

    def get_prices(self, item_counter):
        con = getConn()
        c = getCursor()
        prices = {}
        keys = item_counter.keys()
        for key in keys:
            query = 'SELECT price FROM menu WHERE itemId = ?;'
            c.execute(query, (key,))
            record = c.fetchone()
            print(record)
            prices[key] = record[0]*item_counter[key]
        return prices
