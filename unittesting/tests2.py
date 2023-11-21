"""
This is the parameterized version of the test run in test.py
"""

import unittest
import entertainment2


class EntertainmentSystemTests(unittest.TestCase):
    def test_movie_license(self):
        daily_movies = entertainment2.get_daily_movies()
        licensed_movies = entertainment2.get_licensed_movies()

        # Write your code below:
        for movie in daily_movies:
            print(movie)
            with self.subTest(movie):
                self.assertIn(movie, licensed_movies)


unittest.main()
