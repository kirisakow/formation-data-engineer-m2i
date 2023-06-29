import pytest
import unittest
import thermometer


PLUS_DE_10000_PARAMS = list(range(10001))


def test_thermometer():
    assert thermometer.get_temp_closest_to_0([]) == 0


def test_thermometer5():
    assert thermometer.get_temp_closest_to_0([2, 9, 1]) == 1


def test_thermometer2():
    with pytest.raises(ValueError, match='Trop de paramètres'):
        thermometer.get_temp_closest_to_0(PLUS_DE_10000_PARAMS)


def test_thermometer3():
    assert thermometer.get_temp_closest_to_0([-19, 9, -5, 5]) == 5
    assert thermometer.get_temp_closest_to_0([-19, 9, 5, -5]) == 5


def test_thermometer4():
    assert thermometer.get_temp_closest_to_0([-19, 9, 5, -5, -1]) == -1


class TestThermometer(unittest.TestCase):
    def test_thermometer(self):
        self.assertEqual(thermometer.get_temp_closest_to_0([]), 0)

    def test_thermometer2(self):
        self.assertEqual(thermometer.get_temp_closest_to_0([2, 9, 1]), 1)

    def test_thermometer3(self):
        self.assertEqual(thermometer.get_temp_closest_to_0([-19, 9, 5, -5]), 5)
        self.assertEqual(thermometer.get_temp_closest_to_0([-19, 9, -5, 5]), 5)

    def test_thermometer4(self):
        self.assertEqual(thermometer.get_temp_closest_to_0([-19, 9, 5, -5, -1]), -1)

    def test_thermometer_err(self):
        self.assertRaisesRegex(ValueError,
                               'Trop de paramètres',
                               thermometer.get_temp_closest_to_0,
                               PLUS_DE_10000_PARAMS)


if __name__ == '__main__':
    unittest.main()
