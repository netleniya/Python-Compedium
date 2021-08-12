"""
Perform unit tests on the entertainment system in aircraft 
"""

import entertainment
import unittest


class EntertainmentSystemTests(unittest.TestCase):

    def test_movie_license(self):
        daily_movie = entertainment.get_daily_movie()
        licensed_movies = entertainment.get_licensed_movies()

        self.assertIn(daily_movie, licensed_movies)

    def test_wifi_status(self):
        self.assertTrue(wifi_enabled := entertainment.get_wifi_status())

    def test_maximum_display_brightness(self):
        self.assertAlmostEqual(
            brightness := entertainment.get_maximum_display_brightness(), 400)

    def test_device_temperature(self):
        self.assertLess(device_temp := entertainment.get_device_temp(), 35)


unittest.main()
