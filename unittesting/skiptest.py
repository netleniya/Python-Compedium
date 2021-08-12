"""
Sometimes we have tests that should only run in a particular context. For example, we might have a group of tests that only runs on the Windows operating system but not Linux or macOS. For these situations, it’s helpful to be able to skip tests.

The unittest framework provides two different ways to skip tests:

1. The @unittest skip decorator
2. The skipTest() method

There are two decorator options:
1. @unittest.skipUnless(condition) - skips the test of the condition evaluates to False
2. @unittest.skipIf(condition) - skips the test of the condition evaluates to True

Below is a modified version of test.py. It is set to skip all tests on regional jets
"""

import entertainment
import unittest


class EntertainmentSystemChecks(unittest.TestCase):

    @unittest.skipIf(entertainment.regional_jet(), "Not avaiable on regional jets")
    def test_movie_license(self):
        daily_movie = entertainment.get_daily_movie()
        licensed_movies = entertainment.get_licensed_movies()
        self.assertIn(daily_movie, licensed_movies)

    @unittest.skipUnless(not entertainment.regional_jet(), "Not available on regional jets")
    def test_wifi_status(self):
        self.assertTrue(wifi_enabled := entertainment.get_wifi_status())

    def test_device_temperature(self):
        if entertainment.regional_jet():
            self.skipTest("Not avaiable on regional jets")
        self.assertLess(device_temp := entertainment.get_device_temp(), 35)

    def test_maximum_display_brightness(self):
        if entertainment.regional_jet():
            self.skipTest("Not available on regional jets")
        self.assertAlmostEqual(
            brightness := entertainment.get_maximum_display_brightness(), 400)


unittest.main()
