""" controller for the application"""
from model import Mouse


class MouseController:
    def __init__(self) -> None:
        pass


    def create_mouse(self, name, brand):
        mouse = Mouse(name, brand)
        mouse.save_mouse()
        return mouse