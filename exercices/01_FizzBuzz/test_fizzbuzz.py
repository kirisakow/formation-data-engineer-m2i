import pytest
import unittest
import fizzbuzz

FIZZBUZZ_FROM_1_TO_100_EXPECTED = [
    '1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz', '16', '17', 'Fizz', '19', 'Buzz', 'Fizz', '22', '23', 'Fizz', 'Buzz', '26', 'Fizz', '28', '29', 'FizzBuzz', '31', '32', 'Fizz', '34', 'Buzz', 'Fizz', '37', '38', 'Fizz', 'Buzz', '41', 'Fizz', '43', '44', 'FizzBuzz', '46', '47', 'Fizz', '49', 'Buzz', 'Fizz', '52', '53', 'Fizz', 'Buzz', '56', 'Fizz', '58', '59', 'FizzBuzz', '61', '62', 'Fizz', '64', 'Buzz', 'Fizz', '67', '68', 'Fizz', 'Buzz', '71', 'Fizz', '73', '74', 'FizzBuzz', '76', '77', 'Fizz', '79', 'Buzz', 'Fizz', '82', '83', 'Fizz', 'Buzz', '86', 'Fizz', '88', '89', 'FizzBuzz', '91', '92', 'Fizz', '94', 'Buzz', 'Fizz', '97', '98', 'Fizz', 'Buzz']


def test_fizzbuzz():
    assert fizzbuzz.fizzbuzz(9) == 'Fizz'
    assert fizzbuzz.fizzbuzz(10) == 'Buzz'
    assert fizzbuzz.fizzbuzz(15) == 'FizzBuzz'
    assert fizzbuzz.fizzbuzz(2) == '2'
    fizzbuzz_from_1_to_100_actual = [
        fizzbuzz.fizzbuzz(i) for i in range(1, 101)]
    assert ''.join(FIZZBUZZ_FROM_1_TO_100_EXPECTED) == ''.join(
        fizzbuzz_from_1_to_100_actual)


class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz.fizzbuzz(9), 'Fizz')
        self.assertEqual(fizzbuzz.fizzbuzz(10), 'Buzz')
        self.assertEqual(fizzbuzz.fizzbuzz(15), 'FizzBuzz')
        self.assertEqual(fizzbuzz.fizzbuzz(2), '2')
        fizzbuzz_from_1_to_100_actual = ''.join(
            [fizzbuzz.fizzbuzz(i) for i in range(1, 101)]
        )
        self.assertEqual(''.join(FIZZBUZZ_FROM_1_TO_100_EXPECTED),
                         ''.join(fizzbuzz_from_1_to_100_actual))


if __name__ == '__main__':
    unittest.main()
