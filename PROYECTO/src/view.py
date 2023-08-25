""" view application"""

from controller import MouseController

class IndexView:
    def __init__(self) -> None:
        self.mouse_ctl = MouseController()

    def new_order(self):
        new_mouse = self.mouse_ctl.create_mouse("mouse 3", "brand 3")
        print(new_mouse.name)


if __name__ == "__main__":
    index_view = IndexView()
    index_view.new_order()