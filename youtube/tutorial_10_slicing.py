#!/usr/bin/env python
# -*- conding: utf-8 -*-

import unittest


class TestSlicing(unittest.TestCase):

  def test_slicing(self):
    nums = [0, 1, 2, 3, 4, 5]
    self.assertEqual(nums[1:3], [1, 2])
    self.assertEqual(nums[1, 4], [1, 2, 3])
    self.assertEqual(nums[1:], [1, 2, 3, 4, 5])
    self.assertEqual(nums[:4], [0, 1, 2, 3])
    self.assertEqual(nums[:], [0, 1, 2, 3, 4, 5])
    self.assertEqual(nums[0:5:2], [0, 2, 4])
    self.assertEqual(nums[5:0:-2], [5, 3, 1])
    self.assertEqual(nums[::2], [0, 2, 4])
    self.assertEqual(nums[::-1], [5, 4, 3, 2, 1, 0])


if __name__ == '__main__':
  main()
