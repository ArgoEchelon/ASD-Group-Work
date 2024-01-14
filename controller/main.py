#Phoenix Burke Chang 21026891
#Leo Gan 22007334
#Zak Kannemeyer 22021286
#Jack Wemyss 22027196

from model.main import Model
from views.main import View
from .home import HomeController
from .login import LogInController
from .create_order import CreateOrderController
from .accountManage import AccountManageController
from .crudMenu import CrudMenuController
from .managerFunctions import ManagerFunctionsController
from .select_table import SelectTableController
from .reservation import ReservationController
from .kitchen import KitchenController
from .payment import PaymentController
from .crudInventory import InventoryController



class Controller:
    def __init__(self, model: Model, view: View) -> None:
        self.view = view
        self.model = model
        self.login_controller = LogInController(self, model, view)
        self.home_controller = HomeController(self, model, view)
        self.create_order_controller = CreateOrderController(self, model, view)
        self.select_table_controller = SelectTableController(self, model, view)
        self.accountManage_controller = AccountManageController(self, model, view)
        self.managerFunctions_controller = ManagerFunctionsController(self, model, view)
        self.crudMenu_controller = CrudMenuController(self, model, view)
        self.reservation_controller = ReservationController(self, model, view)
        self.kitchen_controller = KitchenController(self, model, view)
        self.payment_controller = PaymentController(self, model, view)
        self.inventory_controller = InventoryController(self, model, view)

    def start(self) -> None:
        # Here, you can do operations required before launching the gui, for example,
        # self.model.auth.load_auth_state()
        #if self.model.auth.is_logged_in:
        #    self.view.switch("home")
        #else:
        #self.view.switch('LoginView')
        self.view.start_mainloop()