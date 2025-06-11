from display import Display
from sensor import Sensor


class CarPark:
    """
    Manages parking bays, cars and displays.
    """
    def __init__(self,
                 location,
                 capacity,
                 plates = None,
                 sensors = None,
                 displays = None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []


    def __str__(self):
        return f"Welcome to {self.location} car park"


    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")

        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)