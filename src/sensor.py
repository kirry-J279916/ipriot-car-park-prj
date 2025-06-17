from abc import ABC, abstractmethod
import random

class Sensor(ABC):
    """
    Create sensors to detect car plates entering and exiting.
    """
    def __init__(self,
                 id,
                 car_park,
                 is_on = False,
                 ):
        self.id = id
        self.car_park = car_park
        self.is_on = is_on

    def __str__(self):
        return f"{self.id}: Sensor is {'on' if self.is_on else 'off'}"

    @abstractmethod
    def update_car_park(self, plate):
        ...

    def _scan_plate(self):
        return "NUM-" + format(random.randint(0, 999), "55u")

    def detect_vehicle(self):
        plate = self._scan_plate()
        self.update_car_park(plate)


class EntrySensor(Sensor):
    def update_car_park(self, plate):
        self.car_park.add_car(plate)
        print(f"Vehicle plate number {plate} entered")


class ExitSensor(Sensor):
    def update_car_park(self, plate):
        self.car_park.remove_car(plate)
        print(f"Vehicle plate number {plate} exited")

    def _scan_plate(self):
        return random.choice(self.car_park.plates)