# Python toolset for tests with only minor differences.
"""
Here, in our test method test_times_ten(), instead of writing individual test cases for each input of 0, 10, and 1000000, we can test a collection of inputs by using a loop followed by a with statement and our subTest context manager.

By using subTest, each iteration of our loop is treated as an individual test. Python will run the code inside of the context manager on each iteration, and if one fails, it will return the failure as a separate test case failure.

If we want to expand our test coverage, we can simply modify the list that our loop iterates over. We can test a range of thousands of inputs simply by using the context manager setup to achieve test parameterization.
"""
import unittest


# Function to be tested (it's deliberately set to return the wrong value)
def times_ten(num):
    '''Takes a number and returns the 10x that number'''
    return num * 100


# Create a test class
class TestTimesTen(unittest.TestCase):

    def test_times_ten(self):
        for num in [0, 1_000_000, -10]:
            with self.subTest(num):
                expected_result = num * 10
                message = f"Expected times_ten({num}) to return {expected_result}"
                self.assertEqual(times_ten(num), expected_result, message)


unittest.main()
