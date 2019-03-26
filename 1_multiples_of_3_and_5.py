#!/usr/bin/python3

import unittest
'''
Problem 1: https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Correct answer: 233168
'''


def sum_3_or_5_multiples(lastNumber):
    sum = 0

    if(isinstance(lastNumber, int) and lastNumber > 0):
        for n in range(0, lastNumber):
            if (n % 3 == 0) or (n % 5 == 0):
                sum += n

    return sum

print("Sum: " + str(sum_3_or_5_multiples(1000)))


class Sum3Or5MultiplesTest(unittest.TestCase):
    def setup(self):
        pass

    def test_sum_of_3_and_5_multiples_below_10(self):
        self.assertEqual(sum_3_or_5_multiples(10), 23)

    def test_passed_number_is_negative(self):
        self.assertEqual(sum_3_or_5_multiples(-10), 0)

    def test_passed_number_is_string(self):
        self.assertFalse(sum_3_or_5_multiples('10'))

    def test_passed_number_is_float(self):
        self.assertFalse(sum_3_or_5_multiples(10.5))

    def test_passed_number_is_zero(self):
        self.assertFalse(sum_3_or_5_multiples(0))

if __name__ == '__main__':
    unittest.main()
