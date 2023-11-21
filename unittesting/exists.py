# Short demonstration of the unittest module's capabilities
import unittest


def get_nearest_exit(row_number):
    if row_number < 15:
        return "front"
    elif row_number < 30:
        return "middle"
    else:
        return "back"


# Unit test the function above by creating a class that inherits from unittest.TestCase


class NearestExitTest(unittest.TestCase):
    def test_row_1(self):
        self.assertEqual(
            get_nearest_exit(1), "front", "The nearest exit to row 1 is in the front"
        )

    def test_row_20(self):
        self.assertEqual(get_nearest_exit(20), "middle", "Nearest exit is middle")

    def test_row_40(self):
        self.assertEqual(get_nearest_exit(40), "back", "Nearest exit is back")


# Run the unittest by calling unittest.main()
unittest.main()
