import pytest
import unittest
from leap_years import is_leap_year


def test_leap_years():
    assert is_leap_year(2008) == True


def test_leap_years_2():
    assert is_leap_year(1900) == False


def test_leap_years_3():
    assert is_leap_year(2400) == True


def test_leap_years_4():
    assert is_leap_year(1200) == False


class TestLeapYears(unittest.TestCase):
    def test_leap_years(self):
        self.assertEqual(is_leap_year(2008), True)

    def test_leap_years_2(self):
        self.assertEqual(is_leap_year(1900), False)

    def test_leap_years_3(self):
        self.assertEqual(is_leap_year(2400), True)

    def test_leap_years_4(self):
        self.assertEqual(is_leap_year(1200), False)


if __name__ == '__main__':
    unittest.main()
