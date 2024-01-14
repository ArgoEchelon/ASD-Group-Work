#Zak Kannemeyer 22021286
#Leo Gan 22007334 
#Jack Wemyss 22027196
from model.main import Model
from views.main import View
from controller.main import Controller


def main():
    model = Model()
    view = View()
    controller = Controller(model, view)
    controller.start()


if __name__ == "__main__":
    main()