#!/usr/bin/python3

import unittest
'''
Given an array of ints, return True if the sequence.. 1, 3, 4 .. appears in the
array somewhere.
'''


def array_has_134(array):
    for i in range(len(array)-2):
        if array[i] == 1 and array[i+1] == 3 and array[i+2] == 4:
            return True
    return False


class ArraySequenceTest(unittest.TestCase):
    def setup(self):
        pass

    def test_134_sequence_is_in_array(self):
        self.assertTrue(array_has_134([6, 2, 1, 3, 4, 7]))

    def test_134_sequence_is_not_in_array(self):
        self.assertFalse(array_has_134([1, 2, 3, 4, 9, 10]))


if __name__ == '__main__':
    unittest.main()
