#Phoenix Burke Chang 21026891

from model.main import Model
from views.main import View
from views.home import HomeView
from views.managerFunctions import ManagerFunctionsView
from views.crudMenu import CrudMenuView

class ManagerFunctionsController:
    def __init__(self, controller, model: Model, view: View) -> None:
        self.maincontroller = controller
        self.model = model
        self.view = view
        self.frame = self.view._frames[ManagerFunctionsView]
        self._bind()

    def _bind(self) -> None:
        self.frame.back_btn.config(command=self.back_btn)
        self.frame.crud_menu_btn.config(command=self.crud_menu_btn)

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
        else:
            self.frame.staffname_label.config(text=f"")
            self.frame.staffid_label.config(text=f"")
    
    def back_btn(self):
        self.view.switch(HomeView)
        self.maincontroller.home_controller.update_view()

    def crud_menu_btn(self):
        self.view.switch(CrudMenuView)
        self.maincontroller.crudMenu_controller.update_view()


        
        