import unittest
from sensor import EntrySensor, ExitSensor
from car_park import CarPark

class TestEntrySensor(unittest.TestCase):
    def test_sensor_initialized(self):
        carpark_test = CarPark("Location", 10)
        sensor = EntrySensor(123, carpark_test, is_on=True)

        self.assertEqual(sensor.id, 123)
        self.assertEqual(sensor.car_park, carpark_test)
        self.assertTrue(sensor.is_on)

    def test_detect_vehicle(self):
        carpark_test = CarPark("Location", 10)
        sensor = EntrySensor(123, carpark_test, is_on=True)

        self.assertEqual(len(carpark_test.plates), 0)  # before car enter
        sensor.detect_vehicle()  # car entry detected
        self.assertEqual(len(carpark_test.plates), 1)  # after car enter


class TestExitSensor(unittest.TestCase):
    def test_exit_sensor_initializes(self):
        carpark_test = CarPark("Location", 10)
        sensor = ExitSensor(123, carpark_test, is_on=True)

        self.assertEqual(sensor.id, 123)
        self.assertEqual(sensor.car_park, carpark_test)
        self.assertTrue(sensor.is_on)

    def test_detect_vehicle_removes_plate(self):
        carpark_test = CarPark("Location", 10)
        carpark_test.add_car("123")  # car 123 parked

        sensor = ExitSensor(123, carpark_test, is_on=True)

        self.assertIn("123", carpark_test.plates)
        sensor.detect_vehicle()  # car 123 exits
        self.assertEqual(len(carpark_test.plates), 0)


if __name__ == "__main__":
   unittest.main()