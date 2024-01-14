#Phoenix Burke Chang 21026891
#Zak Kannemeyer 22021286
#Leo Gan 22007334 
#Jack Wemyss 22027196

from model.auth import Auth
from model.menu import Menu
from model.tables import TableManagement
from model.accountManage import AccountManage
from model.times import TimeManagement
from model.crudMenu import CrudMenu
from model.ordermanage import OrderManagement
from model.branches import BranchManagement
from model.crudInventory import Inventory


class Model():
    def __init__(self):
        self.auth = Auth()
        self.menu = Menu()
        self.tables = TableManagement()
        self.accountManage = AccountManage()
        self.crudMenu = CrudMenu()
        self.times = TimeManagement()
        self.branches= BranchManagement()
        self.crudMenu = CrudMenu()
        self.orderManage = OrderManagement()
        self.inventory = Inventory()

    
