import pytest
import unittest
from isbn_validator import IsbnValidator


def test_isbn_validator():
    assert IsbnValidator.verifier_isbn('1491926309')


def test_isbn_validator2():
    assert not IsbnValidator.verifier_isbn('1491926308')


def test_isbn_validator3():
    assert IsbnValidator.verifier_isbn('2100825208')


def test_isbn_validator4():
    assert IsbnValidator.verifier_isbn('043942089X')


def test_isbn_validator5():
    with pytest.raises(
        expected_exception=ValueError,
        match='^[Ll]ongueur incorrecte.+$'):
        IsbnValidator.verifier_isbn('043942089')


def test_isbn_validator6():
    with pytest.raises(
        expected_exception=ValueError,
        match='^[Cc]aractères invalides.+$'):
        IsbnValidator.verifier_isbn('043942089A')


class TestIsbnValidator(unittest.TestCase):
    def test_isbn_validator(self):
        self.assertTrue(IsbnValidator.verifier_isbn('1491926309'))

    def test_isbn_validator2(self):
        self.assertFalse(IsbnValidator.verifier_isbn('1491926308'))

    def test_isbn_validator3(self):
        self.assertTrue(IsbnValidator.verifier_isbn('2100825208'))

    def test_isbn_validator4(self):
        self.assertTrue(IsbnValidator.verifier_isbn('043942089X'))

    def test_isbn_validator5(self):
        self.assertRaisesRegex(ValueError,
                                '^[Ll]ongueur incorrecte.+$',
                                IsbnValidator.verifier_isbn,
                                '043942089')

    def test_isbn_validator6(self):
        self.assertRaisesRegex(ValueError,
                                '^[Cc]aractères invalides.+$',
                                IsbnValidator.verifier_isbn,
                                '043942089A')


if __name__ == "__main__":
    unittest.main()
