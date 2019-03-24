#!/usr/bin/python3

import unittest

'''
Write a program which returns a pair of numbers from a given array that sum up
to a given number. Assume the list is sorted and it has integers.
'''


def solution(list, sum):
    low = 0
    high = len(list) - 1

    while low < high:
        current_sum = list[low] + list[high]
        if current_sum == sum:
            return [list[low], list[high]]
        elif current_sum < sum:
            low += 1
        elif current_sum > sum:
            high -= 1

    return -1


class SolutionTest(unittest.TestCase):
    def setup(self):
        pass

    def test_solution_when_it_is_not_possible(self):
        self.assertEqual(solution([2, 4, 7, 9], 8), -1)

    def test_solution_when_it_is_possible(self):
        self.assertEqual(solution([1, 3, 6, 9], 7), [1, 6])

if __name__ == "__main__":
    unittest.main()
