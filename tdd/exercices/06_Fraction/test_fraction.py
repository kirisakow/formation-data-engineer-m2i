import pytest
import unittest
from fraction import parse_fraction


def test_us1():
    """US 1: si l'une des deux fractions a le dénominateur égal à 0 alors je veux que la fonction me renvoie une erreur."""
    with pytest.raises(ZeroDivisionError):
        parse_fraction('1/0 + 1/2')


def test_us2():
    """US 2: si les 2 fractions n'ont pas le même dénominateur alors je veux que la fonction me renvoie une erreur."""
    with pytest.raises(ValueError):
        parse_fraction('1/2 + 1/3', require_same_denominator=True)


def test_us3():
    """US 3: la fonction doit renvoyer le résultat de l'opération : par exemple '4/7 + 2/7' doit retourner '6/7'"""
    assert parse_fraction('4/7 + 2/7') == '6/7'
    assert parse_fraction('4/7 - 2/7') == '2/7'


def test_us4():
    """US 4: si le résultat est un entier, le retourner comme tel : par exemple '4/7 / 2/7' doit retourner '2'"""
    assert parse_fraction('4/7 / 2/7') == '2'


def test_going_further1():
    """
    Addition (pas même dénominateur) : 3/7 + 4/8 = 13/14
    """
    assert parse_fraction('3/7 + 4/8') == '13/14'


def test_going_further2():
    """
    Soustraction (pas même dénominateur) : 4/8 - 3/7 = 1/14
    """
    assert parse_fraction('4/8 - 3/7') == '1/14'


def test_going_further3():
    """
    Simplification (pas entier) : 120/200 -> 3/5
    """
    assert parse_fraction('120/200') == '3/5'


def test_going_further4():
    """
    Simplification (pas entier) : 140/200 -> 7/10
    """
    assert parse_fraction('140/200') == '7/10'


class TestFraction(unittest.TestCase):
    def test_us1(self):
        """US 1: si l'une des deux fractions a le dénominateur égal à 0 alors je veux que la fonction me renvoie une erreur."""
        self.assertRaises(ZeroDivisionError, parse_fraction, '1/0 + 1/2')

    def test_us2(self):
        """US 2: si les 2 fractions n'ont pas le même dénominateur alors je veux que la fonction me renvoie une erreur."""
        self.assertRaises(ValueError, parse_fraction, '1/2 + 1/3', require_same_denominator=True)

    def test_us3(self):
        """US 3: la fonction doit renvoyer le résultat de l'opération : par exemple '4/7 + 2/7' doit retourner '6/7'"""
        self.assertEqual(parse_fraction('4/7 + 2/7'), '6/7')
        self.assertEqual(parse_fraction('4/7 - 2/7'), '2/7')


    def test_us4(self):
        """US 4: si le résultat est un entier, le retourner comme tel : par exemple '4/7 / 2/7' doit retourner '2'"""
        self.assertEqual(parse_fraction('4/7 / 2/7'), '2')


    def test_going_further1(self):
        """
        Addition (pas méme dénominateur) : 3/7 + 4/8 = 13/14
        """
        self.assertEqual(parse_fraction('3/7 + 4/8'), '13/14')


    def test_going_further2(self):
        """
        Soustraction (pas méme dénominateur) : 4/8 - 3/7 = 1/14
        """
        self.assertEqual(parse_fraction('4/8 - 3/7'), '1/14')


    def test_going_further3(self):
        """
        Simplification (pas entier) : 120/200 -> 3/5
        """
        self.assertEqual(parse_fraction('120/200'), '3/5')


    def test_going_further4(self):
        """
        Simplification (pas entier) : 140/200 -> 7/10
        """
        self.assertEqual(parse_fraction('140/200'), '7/10')


if __name__ == '__main__':
    unittest.main()
