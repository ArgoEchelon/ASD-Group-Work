#Phoenix Burke Chang 21026891
#Zak Kannemeyer 22021286
#Jack Wemyss 22027196
from DataAccessObject import *


class Auth():
    def __init__(self):
        self.is_logged_in = False
        self.current_staffid = None
        self.current_firstname = None
        self.current_lastname = None
        self.current_stafftype = None
        self.current_restaurantid = None
        self.current_restaurantname = None

    def login(self, staffId, password, restaurantId) -> None:
        con = getConn()
        c = getCursor()
        query = 'SELECT * FROM staff WHERE staffId = ? and password = ? and restaurantId = ?;'
        c.execute(query, (staffId, password, restaurantId))
        record = c.fetchone()
        print(record)
        #print(type(record))

        if record is None:
            return False
        elif len(record) > 0:
            self.is_logged_in = True
            self.current_staffid = record[0]
            self.current_firstname = record[2]
            self.current_lastname = record[3]
            self.current_stafftype = record[4]
            self.current_restaurantid = record[5]
            query = 'SELECT * FROM restaurant WHERE restaurantId = ?;'
            c.execute(query, (self.current_restaurantid,))
            restaurantrecord = c.fetchone()
            print(restaurantrecord)
            self.current_restaurantname = restaurantrecord[1]
            print(self.current_restaurantname)
            return True

    def logout(self) -> None:
        self.is_logged_in = False
        self.current_staffid = None
        self.current_firstname = None
        self.current_lastname = None
        self.current_stafftype = None
        self.current_restaurantid = None
        self.current_restaurantname = None
