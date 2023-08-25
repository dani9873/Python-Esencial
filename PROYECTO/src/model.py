""" models for app"""
from repository import JsonRepository


class InputDevice:
    """Input device class"""

    def __init__(self, name, brand):
        self.name = name
        self.brand = brand
        self.respository = JsonRepository()


class OutputDevice:
    """Output device class"""

    def __init__(self, name, brand):
        self.name = name
        self.brand = brand


class Mouse(InputDevice):
    """Mouse class"""

    def __init__(self, name, brand):
        super().__init__(name, brand)
        self.id = 0
        self.units = 0

    def save_mouse(self):
        # self.respository.add(self.__dict__)
        data = {
            "name": self.name,
            "brand": self.brand,
            "id": self.id,
            "units": self.units
        }
        return self.respository.write(data)

    def update_mouse(self, old_name, new_brand, new_units):
        # self.respository.update(self.__dict__,old_name)
        if old_name != self.name:
            return False  # Mouse name cannot be updated
        self.brand = new_brand
        self.units = new_units
        return True


class keyboard(InputDevice):
    """Keyboard class"""

    def __init__(self, number, brand):
        super().__init__(number, brand)
        self.id = 0
        self.units = 0

    def save_keyboard(self):
        # self.respository.add(self.__dict__)
        data = {
            "number": self.number,
            "brand": self.brand,
            "id": self.id,
            "units": self.units
        }
        return self.respository.write(data)

    def update_keyboard(self, old_number, new_brand, new_units):
        if old_number != self.number:
            return False  # Keyboard number cannot be updated
        self.brand = new_brand
        self.units = new_units
        return True


class Monitor(OutputDevice):
    """Monitor class"""

    def __init__(self, number, brand):
        super().__init__(number, brand)
        self.id = 0
        self.units = 0

    def save_monitor(self):
        # self.respository.add(self.__dict__)
        data = {
            "number": self.number,
            "brand": self.brand,
            "id": self.id,
            "units": self.units
        }
        return self.respository.write(data)

    def update_monitor(self, old_number, new_brand, new_units):
        if old_number != self.number:
            return False  # Monitor number cannot be updated
        self.brand = new_brand
        self.units = new_units
        return True


class Loudspeaker(OutputDevice):
    """Loudspeaker class"""

    def __init__(self, number, brand):
        super().__init__(number, brand)
        self.id = 0
        self.units = 0

    def save_loudspeaker(self):
        # self.respository.add(self.__dict__)
        data = {
            "number": self.number,
            "brand": self.brand,
            "id": self.id,
            "units": self.units
        }
        return self.respository.write(data)

    def update_loudspeaker(self, old_number, new_brand, new_units):
        if old_number != self.number:
            return False  # Loudspeaker number cannot be updated
        self.brand = new_brand
        self.units = new_units
        return True

class Computer:
    def __int__(self, name, brand, mouse, monitor, loudspeaker, unit):
        self.name = name
        self.brand = brand
        self.mouse = mouse
        self.monitor = monitor
        self.loudspeaker = loudspeaker
        self.unit = unit

    def save_computer(self):
        # self.respository.add(self.__dict__)
        data = {
            "name": self.name,
            "brand": self.brand,
            "mouse": self.mouse,
            "monitor": self.monitor,
            "loudspeaker": self.loudspeaker,
            "unit": self.unit
        }
        return self.respository.write(data)


class OrderBy(Computer):
    def __init__(self, computer, unit):
        self.computer = computer
        self.unit = unit

    def save_order(self):
        # self.respository.add(self.__dict__)
        data = {
            "computer": self.computer,
            "unit": self.unit
        }
        return self.respository.write(data)
    def update_computer(self, new_name, new_brand, new_mouse, new_monitor, new_loudspeaker, new_unit):
        self.name = new_name
        self.brand = new_brand
        self.mouse = new_mouse
        self.monitor = new_monitor
        self.loudspeaker = new_loudspeaker
        self.unit = new_unit

