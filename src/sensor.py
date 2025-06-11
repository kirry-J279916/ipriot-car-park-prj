class Sensor:
    """
    Create sensors to detect cars.
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


class EntrySensor(Sensor):
    ...


class ExitSensor(Sensor):
    ...