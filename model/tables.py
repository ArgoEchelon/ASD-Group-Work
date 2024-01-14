#Zak Kannemeyer 22021286
#Jack Wemyss 22027196
from DataAccessObject import *
import datetime

class TableManagement():
    def __init__(self):
        
        self.tables = []
        self.get_tables()
        self.current_table = None
    
    def get_tables(self):
        con = getConn()
        c = getCursor()
        query = 'SELECT tableid,tablesize FROM tables;'
        c.execute(query)
        record = c.fetchall()
        for table in record:
            self.tables.append(Table(table[0],table[1]))

    def create_order(self, item_counter, prices, restaurantid):
        self.tables[self.current_table].create_order(item_counter, prices, restaurantid)

    def orders_paid(self):
        con = getConn()
        c = getCursor()
        query = "UPDATE orders SET orderStatus = 'Paid' WHERE tableId = ? AND orderStatus = 'Pending'"
        c.execute(query, (self.current_table,))


class Table():
    def __init__(self, tableid, capacity):
        self.table_id = tableid
        self.capacity = capacity
        #self.table_status = 'Inactive'


    def get_order_id(self):
        con = getConn()
        c = getCursor()
        query = 'Select MAX(orderid) from orders;'
        c.execute(query)
        record = c.fetchone()
        #print(record[0])
        #print(type(record[0]))
        if record[0] == None:
            order_id = 1
        else:
            order_id = record[0] + 1
        return order_id

    def create_order(self,item_counter, prices, restaurantid):
        con = getConn()
        c = getCursor()
        order_id = self.get_order_id()
        #print(prices)
        try:
            time = x = datetime.datetime.now()

            keys = item_counter.keys()
            for key in keys:
                c.execute('INSERT INTO orders (orderId, tableId, itemId, quantity, orderStatus,totalPrice, orderDate, restaurantId) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (order_id, self.table_id, key, int(item_counter.get(key)), 'Pending', prices[key], time, restaurantid ))
            con.commit()

            

        except Exception as e :
            print("ORDER: ERROR", e)
            conn.rollback()

    



    

