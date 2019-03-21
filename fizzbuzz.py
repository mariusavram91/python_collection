#!/usr/bin/python3

import unittest

'''
Write a program that: for multiples of three returns “Fizz” instead of the
number and for the multiples of five returns “Buzz”.
For numbers which are multiples of both three and five returns “FizzBuzz”.
For the rest it returns the number.
'''


def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
        return str(number)


class FizzBuzzTest(unittest.TestCase):
    def setup(self):
        pass

    def test_fizzbuzz_for_3(self):
        self.assertEqual(fizzbuzz(3), 'Fizz')

    def test_fizzbuzz_for_5(self):
        self.assertEqual(fizzbuzz(5), 'Buzz')

    def test_fizzbuzz_for_multiple_of_3(self):
        self.assertEqual(fizzbuzz(9), 'Fizz')

    def test_fizzbuzz_for_multiple_of_5(self):
        self.assertEqual(fizzbuzz(10), 'Buzz')

    def test_fizzbuzz_for_multiple_of_3_and_5(self):
        self.assertEqual(fizzbuzz(15), 'FizzBuzz')

    def test_fizzbuzz_for_other_number(self):
        self.assertEqual(fizzbuzz(7), '7')

if __name__ == '__main__':
    unittest.main()
