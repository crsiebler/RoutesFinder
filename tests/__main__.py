import os
import unittest


class TestRouteFinder(unittest.TestCase):
    def test_input1(self):
        with open("tests/expected/expected1.txt", "r") as expected, open(
            "tests/output/output1.txt", "r"
        ) as output:
            self.assertListEqual(list(expected), list(output))

    def test_input2(self):
        with open("tests/expected/expected2.txt", "r") as expected, open(
            "tests/output/output2.txt", "r"
        ) as output:
            self.assertListEqual(list(expected), list(output))

    def test_input4(self):
        with open("tests/expected/expected3.txt", "r") as expected, open(
            "tests/output/output3.txt", "r"
        ) as output:
            self.assertListEqual(list(expected), list(output))

    def test_input4(self):
        with open("tests/expected/expected4.txt", "r") as expected, open(
            "tests/output/output4.txt", "r"
        ) as output:
            self.assertListEqual(list(expected), list(output))


if __name__ == "__main__":
    unittest.main()
