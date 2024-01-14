#Phoenix Burke Chang 21026891
#Zak Kannemeyer 22021286

from model.main import Model
from views.main import View
from tkinter.messagebox import showerror
from views.login import LogInView
from views.home import HomeView

class LogInController:
    def __init__(self, controller, model: Model, view: View) -> None:
        self.maincontroller = controller
        self.model = model
        self.view = view
        self.frame = self.view._frames[LogInView]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.login_btn.config(command=self.login)


    def login(self) -> None:
        username = self.frame.username_input.get()
        password = self.frame.password_input.get()
        restaurant = self.frame.restaurant_input.get()

        if self.model.auth.login(username, password, restaurant):
            data = {"username": username, "password": password}
            self.view.switch(HomeView)
            self.maincontroller.home_controller.update_view()

        else:
            self.view.error_message = showerror("Error", "Wrong credentials")
        self.frame.password_input.delete(0, last=len(password))
        self.frame.username_input.delete(0, last=len(username))
        self.frame.restaurant_input.delete(0, last=len(restaurant))
        self.view.error_message = None