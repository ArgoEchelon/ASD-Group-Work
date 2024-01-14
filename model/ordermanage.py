#Zak Kannemeyer 22021286
#Leo Gan 22007334
from DataAccessObject import *

con = getConn()
c = getCursor()

class OrderManagement():
    def __init__(self):
        self.current_order = None
    
    def get_orders(self, restaurantId):
        query = 'SELECT DISTINCT orderId FROM orders WHERE orderStatus = "Pending" AND restaurantId = ?;'
        c.execute(query, (restaurantId,))
        record = c.fetchall()
        orders = []
        for order in record:
            orders.append(Order(order[0]))
        return orders


    def get_table_orders(self, table_id):
        conn = getConn()
        c = getCursor()
        query2 = "SELECT orderId,itemName,quantity,totalPrice FROM orders JOIN menu USING (itemId) where tableId = ? AND orderStatus = 'Ready';"
        c.execute(query2, (table_id,))
        records = c.fetchall()
        print("Fetchall:", records)
        conn.commit()
        return records
    
    def get_order_details(self, selected_orderId, restaurantId):
        query3 = 'SELECT itemName, quantity FROM orders JOIN menu USING (itemId) WHERE orderId = ? AND orderStatus = "Pending" AND orders.restaurantId = ?;'
        c.execute(query3, (selected_orderId, restaurantId,))
        record3 = c.fetchall()
        orderDetailsList = []
        for orderDetail in record3:
            orderDetailsList.append(OrderDetails(orderDetail[0], orderDetail[1]))
        return orderDetailsList
    
    def mark_order(self, orderId):
        con = getConn()
        c = getCursor()
        query4 = "UPDATE orders SET orderStatus = 'Ready' WHERE orderId = ? AND orderStatus = 'Pending'"
        c.execute(query4, (orderId,))

class Order():
    def __init__(self, orderId):
        self.orderId = orderId

class OrderDetails():
    def __init__(self, itemName, quantity):
        self.itemName = itemName
        self.quantity = quantity
        
