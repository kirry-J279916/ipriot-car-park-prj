from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

def main():
    """
    Simulate cars driving into car park.
    Sensors are triggered to calculate bay availability.
    Data is configured into json file
    """
    car_park = CarPark(location="moondalup", capacity=100, log_file="moondalup.txt")

    car_park_config_file = "moondalup.json"
    car_park.write_config(car_park_config_file)
    car_park = CarPark.from_config(car_park_config_file)

    entry_sensor = EntrySensor(1, car_park, is_on=True)
    exit_sensor = ExitSensor(2, car_park, is_on=True)

    display = Display(1, car_park, message="Welcome to Moondalup", is_on=True)

    car_park.register(entry_sensor)
    car_park.register(exit_sensor)
    car_park.register(display)

    temperature = 30

    for car in range(10):
        entry_sensor.car_park.update_displays(temperature)
        entry_sensor.detect_vehicle()

    for car in range(2):
        exit_sensor.detect_vehicle()


if __name__ == "__main__":
    main()