#Phoenix Burke Chang 21026891
#Zak Kannemeyer 22021286
#Leo Gan 22007334 
#Jack Wemyss 22027196
from .root import Root
from .login import LogInView
from .home import HomeView
from .create_order import CreateOrderView
from .select_table import SelectTableView
from .accountManage import AccountsView
from .reservation import ReservationView
from .managerFunctions import ManagerFunctionsView
from .crudMenu import CrudMenuView
from .kitchen import KitchenView
from .payment import PaymentView
from .crudInventory import InventoryView

class View:
    def __init__(self):
        self.root = Root()
        self._current_frame = None
        # create instances of views
        self.login_view = LogInView()
        self.home_view = HomeView()
        self.create_order_view = CreateOrderView()
        self.accounts_view = AccountsView()
        self.select_table_view = SelectTableView()
        self.reservation_view = ReservationView()
        self.manager_functions_view = ManagerFunctionsView()
        self.crud_menu_view = CrudMenuView()
        self.kitchen_view = KitchenView()
        self.payment_view = PaymentView()
        self.inventory_view = InventoryView()

        # save those views in a dictionary
        self._frames = {
            LogInView: self.login_view,
            HomeView: self.home_view,
            CreateOrderView: self.create_order_view,
            AccountsView: self.accounts_view,
            SelectTableView: self.select_table_view,
            ReservationView: self.reservation_view,
            ManagerFunctionsView: self.manager_functions_view,
            CrudMenuView: self.crud_menu_view,
            KitchenView: self.kitchen_view,
            PaymentView: self.payment_view,
            InventoryView: self.inventory_view
        }
        self.switch(LogInView)

    def switch(self, frame_class):
        if self._current_frame:
            # hide current frame
            self._current_frame.grid_forget()
        # show target frame
        self._current_frame = self._frames[frame_class]
        self._current_frame.grid(row=0, column=0, sticky="nsew")

    def start_mainloop(self):
        self.root.mainloop()