#Zak Kannemeyer 22021286

from model.main import Model
from views.main import View
from views.create_order import CreateOrderView
from views.home import HomeView
from views.select_table import SelectTableView 

class SelectTableController:
    def __init__(self, controller, model: Model, view: View) -> None:
        self.maincontroller = controller
        self.model = model
        self.view = view
        self.frame = self.view._frames[SelectTableView]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.back_btn.config(command=self.back_btn)

    def update_view(self) -> None:
        current_firstname = self.model.auth.current_firstname
        current_lastname = self.model.auth.current_lastname
        current_staffid = self.model.auth.current_staffid
        if current_staffid:
            firstname = current_firstname
            lastname = current_lastname
            staffid = current_staffid
            self.frame.staffname_label.config(text=f"Operator: {firstname} {lastname}")
            self.frame.staffid_label.config(text=f"ID: {staffid}")
            self.frame.add_table_buttons(self.frame.tables_frame, self.model.tables.tables, self.table_selected)
        else:
            self.frame.staffname_label.config(text=f"")
            self.frame.staffid_label.config(text=f"")

    def table_selected(self, table_id):
        self.view.switch(CreateOrderView)
        self.maincontroller.create_order_controller.update_view(table_id)
        self.model.tables.current_table = table_id
    
    def back_btn(self):
        self.view.switch(HomeView)
        self.maincontroller.home_controller.update_view()