import pytest
import unittest
from employee_report import EMPLOYEES, employee_report

EXPECTED_RESULT_US1 = [{'name': 'Sepp', 'age': 18},
                        {'name': 'Mike', 'age': 51}]
EXPECTED_RESULT_US2 = [{'name': 'Max', 'age': 17},
                        {'name': 'Mike', 'age': 51},
                        {'name': 'Nina', 'age': 15},
                        {'name': 'Sepp', 'age': 18}]
EXPECTED_RESULT_US3 = [e['name'].upper() for e in EMPLOYEES]
EXPECTED_RESULT_US4 = [{'name': 'Sepp', 'age': 18},
                        {'name': 'Nina', 'age': 15},
                        {'name': 'Mike', 'age': 51},
                        {'name': 'Max', 'age': 17}]


def test_us1():
    """US 1: afficher la liste de tous les employés âgés de plus de 18 ans"""
    assert employee_report(EMPLOYEES, min_age=18) == EXPECTED_RESULT_US1


def test_us2():
    """US 2: trier la liste des employés par nom"""
    assert employee_report(EMPLOYEES, sort_by='name') == EXPECTED_RESULT_US2


def test_us3():
    """US 3: la liste des employés doit être écrite en majuscules"""
    assert employee_report(EMPLOYEES, uppercase=True) == EXPECTED_RESULT_US3


def test_us4():
    """US 4: trier la liste des employés par nom dans l'ordre décroissant"""
    actual_result_us4 = employee_report(EMPLOYEES, sort_by='name', sort_desc=True)
    assert actual_result_us4 == EXPECTED_RESULT_US4


class TestEmployeeReport(unittest.TestCase):
    def test_us1(self):
        """US 1: afficher la liste de tous les employés âgés de plus de 18 ans"""
        self.assertEqual(employee_report(EMPLOYEES, min_age=18),
                        EXPECTED_RESULT_US1)

    def test_us2(self):
        """US 2: trier la liste des employés par nom"""
        self.assertEqual(employee_report(EMPLOYEES, sort_by='name'),
                        EXPECTED_RESULT_US2)


    def test_us3(self):
        """US 3: la liste des employés doit être écrite en majuscules"""
        actual_result_us3 = [e['name'].upper() for e in employee_report(EMPLOYEES)]
        self.assertEqual(employee_report(EMPLOYEES, uppercase=True),
                        EXPECTED_RESULT_US3)


    def test_us4(self):
        """US 4: trier la liste des employés par nom dans l'ordre décroissant"""
        actual_result_us4 = employee_report(EMPLOYEES, sort_by='name', sort_desc=True)
        self.assertEqual(actual_result_us4,
                        EXPECTED_RESULT_US4)

if __name__ == '__main__':
    unittest.main()
