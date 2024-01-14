#Phoenix Burke Chang 21026891
#Zak Kannemeyer 22021286

from model.main import Model
from views.main import View
from views.login import LogInView
from views.home import HomeView
from views.select_table import SelectTableView 
from views.accountManage import AccountsView
from views.managerFunctions import ManagerFunctionsView
from views.reservation import ReservationView
from views.kitchen import KitchenView
from views.crudInventory import InventoryView

class HomeController:
    def __init__(self, controller, model: Model, view: View) -> None:
        self.maincontroller = controller
        self.model = model
        self.view = view
        self.frame = self.view._frames[HomeView]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.signout_btn.config(command=self.logout)
        self.frame.create_order_btn.config(command=self.create_order_btn)
        self.frame.admin_func_btn.config(command=self.admin_func_btn)
        self.frame.manager_func_btn.config(command=self.manager_func_btn)
        self.frame.reservation_btn.config(command=self.reservation_btn)
        self.frame.kitchen_btn.config(command=self.kitchen_btn)
        self.frame.inventory_btn.config(command=self.inventory_btn)

    def logout(self) -> None:
        self.model.auth.logout()
        self.view.switch(LogInView)

    def update_view(self) -> None:
        current_firstname = self.model.auth.current_firstname
        current_lastname = self.model.auth.current_lastname
        current_staffid = self.model.auth.current_staffid
        current_restaurantname = self.model.auth.current_restaurantname
        if current_staffid:
            firstname = current_firstname
            lastname = current_lastname
            staffid = current_staffid
            restaurantname = current_restaurantname
            self.frame.staffname_label.config(text=f"Operator: {firstname} {lastname}")
            self.frame.staffid_label.config(text=f"ID: {staffid}")
            self.frame.header.config(text=f"Horizon Restaurants: {restaurantname}")
            self.btn_access()
        else:
            self.frame.staffname_label.config(text=f"")
            self.frame.staffid_label.config(text=f"")
        
    def btn_access(self):
        current_stafftype = self.model.auth.current_stafftype
        print(f"Current Staff Type: {current_stafftype}")

        if current_stafftype == "Staff":
            self.frame.admin_func_btn.config(state="disabled")
            self.frame.manager_func_btn.config(state="disabled")
            self.frame.kitchen_btn.config(state="disabled")
        elif current_stafftype == "Chef":
            self.frame.admin_func_btn.config(state="disabled")
            self.frame.manager_func_btn.config(state="disabled")
        elif current_stafftype == "Manager":
            self.frame.admin_func_btn.config(state="disabled")
        else:
            self.frame.admin_func_btn.config(command=self.admin_func_btn)
            self.frame.manager_func_btn.config(command=self.manager_func_btn)
            self.frame.kitchen_btn.config(command=self.kitchen_btn)
    
    def create_order_btn(self):
        self.view.switch(SelectTableView)
        self.maincontroller.select_table_controller.update_view()

    def admin_func_btn(self):
        self.view.switch(AccountsView)
        self.maincontroller.accountManage_controller.update_view()

    def manager_func_btn(self):
        self.view.switch(ManagerFunctionsView)
        self.maincontroller.managerFunctions_controller.update_view()
        
    def reservation_btn(self):
        self.view.switch(ReservationView)
        self.maincontroller.reservation_controller.update_view()

    def kitchen_btn(self):
        self.view.switch(KitchenView)
        self.maincontroller.kitchen_controller.update_view()

    def inventory_btn(self):
        self.view.switch(InventoryView)
        self.maincontroller.inventory_controller.update_view()
        