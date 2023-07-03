import pytest
import unittest
from prime_factors import PrimeFactors


def test_prime_factors():
    assert PrimeFactors.factors_of(0) == []


def test_prime_factors2():
    assert PrimeFactors.factors_of(1) == []


def test_prime_factors3():
    assert PrimeFactors.factors_of(2) == [2]


def test_prime_factors4():
    assert PrimeFactors.factors_of(8) == [2, 2, 2]


def test_prime_factors5():
    assert PrimeFactors.factors_of(13) == [13]


class TestPrimeFactors(unittest.TestCase):
    def test_prime_factors(self):
        self.assertEqual(PrimeFactors.factors_of(0), [])

    def test_prime_factors2(self):
        self.assertEqual(PrimeFactors.factors_of(1), [])

    def test_prime_factors3(self):
        self.assertEqual(PrimeFactors.factors_of(2), [2])

    def test_prime_factors4(self):
        self.assertEqual(PrimeFactors.factors_of(8), [2, 2, 2])

    def test_prime_factors5(self):
        self.assertEqual(PrimeFactors.factors_of(13), [13])


if __name__ == '__main__':
    unittest.main()
