import os
import unittest
from routes_finder.parser import parse


class TestRouteFinder(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestRouteFinder, self).__init__(*args, **kwargs)
        self.locations_file = "data/locations.csv"
        self.trips_file = "data/trips.csv"
        self.results = 3
        self.input1 = "tests/input/input1.txt"
        self.input2 = "tests/input/input2.txt"
        self.input3 = "tests/input/input3.txt"
        self.input4 = "tests/input/input4.txt"
        self.output1 = "tests/output/output1.txt"
        self.output2 = "tests/output/output2.txt"
        self.output3 = "tests/output/output3.txt"
        self.output4 = "tests/output/output4.txt"

    def setUp(self) -> None:
        if os.path.exists(self.output1):
            os.remove(self.output1)
        if os.path.exists(self.output2):
            os.remove(self.output2)
        if os.path.exists(self.output3):
            os.remove(self.output3)
        if os.path.exists(self.output4):
            os.remove(self.output4)
        return super().setUp()

    def tearDown(self) -> None:
        if os.path.exists(self.output1):
            os.remove(self.output1)
        if os.path.exists(self.output2):
            os.remove(self.output2)
        if os.path.exists(self.output3):
            os.remove(self.output3)
        if os.path.exists(self.output4):
            os.remove(self.output4)
        return super().tearDown()

    def test_input1(self):
        parse(
            self.locations_file,
            self.trips_file,
            self.input1,
            self.output1,
            self.results,
        )
        with open("tests/expected/output1.txt", "r") as expected, open(
            self.output1, "r"
        ) as output:
            self.assertListEqual(list(expected), list(output))

    def test_input2(self):
        parse(
            self.locations_file,
            self.trips_file,
            self.input2,
            self.output2,
            self.results,
        )
        with open("tests/expected/output2.txt", "r") as expected, open(
            self.output2, "r"
        ) as output:
            self.assertListEqual(list(expected), list(output))

    def test_input3(self):
        parse(
            self.locations_file,
            self.trips_file,
            self.input3,
            self.output3,
            self.results,
        )
        with open("tests/expected/output3.txt", "r") as expected, open(
            self.output3, "r"
        ) as output:
            self.assertListEqual(list(expected), list(output))

    def test_input4(self):
        parse(
            self.locations_file,
            self.trips_file,
            self.input4,
            self.output4,
            self.results,
        )
        with open("tests/expected/output4.txt", "r") as expected, open(
            self.output4, "r"
        ) as output:
            self.assertListEqual(list(expected), list(output))


if __name__ == "__main__":
    unittest.main()
