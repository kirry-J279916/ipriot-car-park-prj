import unittest
from car_park import CarPark
from pathlib import Path
from display import Display


class TestCarPark(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)
        self.log_file = Path("log.txt")
        self.config_file = Path("config.json")
        self.config_path = Path("test_config.json")
        self.log_path = Path("test_log.txt")
        self.display = Display(id=1, car_park=self.car_park, message="Welcome", is_on=True)

    def test_car_park_initialized_with_all_attributes(self):
        self.assertIsInstance(self.car_park, CarPark)
        self.assertEqual(self.car_park.location, "123 Example Street")
        self.assertEqual(self.car_park.capacity, 100)
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.displays, [])
        self.assertEqual(self.car_park.available_bays, 100)
        self.assertEqual(self.car_park.log_file, Path("log.txt"))

    def test_add_car(self):
         self.car_park.add_car("FAKE-001")
         self.assertEqual(self.car_park.plates, ["FAKE-001"])
         self.assertEqual(self.car_park.available_bays, 99)

    def test_remove_car(self):
         self.car_park.add_car("FAKE-001")
         self.car_park.remove_car("FAKE-001")
         self.assertEqual(self.car_park.plates, [])
         self.assertEqual(self.car_park.available_bays, 100)

    def test_overfill_the_car_park(self):
        for i in range(100):
            self.car_park.add_car(f"FAKE-{i}")
        self.assertEqual(self.car_park.available_bays, 0)
        self.car_park.add_car("FAKE-100")
        self.assertEqual(self.car_park.available_bays, 0)
        self.car_park.remove_car("FAKE-100")
        self.assertEqual(self.car_park.available_bays, 0)

    def test_removing_a_car_that_does_not_exist(self):
        with self.assertRaises(ValueError):
            self.car_park.remove_car("NO-1")

    def test_register_raises_type_error(self):
        car_park = CarPark("Test", 20)
        with self.assertRaises(TypeError):
            car_park.register("a string")

    def test_log_file_created(self):
        new_carpark = CarPark("123 Example Street", 100, self.log_file)
        self.assertTrue(self.log_file.exists())

    def tearDown(self):
        self.log_file.unlink(missing_ok=True)

    def test_car_logged_when_entering(self):
        new_carpark = CarPark("123 Example Street", 100, self.log_file)
        self.car_park.add_car("NEW-001")
        with self.car_park.log_file.open() as f:
            last_line = f.readlines()[-1]
        self.assertIn("NEW-001", last_line)
        self.assertIn("entered", last_line)
        self.assertIn("\n", last_line)

    def test_car_logged_when_exiting(self):
        new_carpark = CarPark("123 Example Street", 100, self.log_file)
        self.car_park.add_car("NEW-001")
        self.car_park.remove_car("NEW-001")
        with self.car_park.log_file.open() as f:
            last_line = f.readlines()[-1]
        self.assertIn("NEW-001", last_line)
        self.assertIn("exited", last_line,)
        self.assertIn("\n", last_line)

    def test_initialize_with_config(self):
        original = CarPark("TestLocation", 20, log_file=self.log_path, config_file=self.config_path)
        original.write_config()

        loaded = CarPark.from_config(self.config_path)

        self.assertEqual(loaded.location, original.location)
        self.assertEqual(loaded.capacity, original.capacity)
        self.assertEqual(str(loaded.log_file), str(original.log_file))

    def test_display_temperature_updated(self):
        test_data = {"available_bays": 1, "temperature": 30}

        self.display.update(test_data)
        self.assertEqual(self.display.temperature, 30)


if __name__ == "__main__":
   unittest.main()