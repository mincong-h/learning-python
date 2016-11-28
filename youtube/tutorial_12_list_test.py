#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class TestList(unittest.TestCase):

  def test_list_func(self):
    numbers = [8, 1, 4, 17, 28, 165, 7]
    self.assertEqual(len(numbers), 7)
    self.assertEqual(max(numbers), 165)
    self.assertEqual(min(numbers), 1)
    self.assertEqual(list('bucky'), ['b', 'u', 'c', 'k', 'y'])
    numbers[3] = 77
    self.assertEqual(numbers, [8, 1, 4, 77, 28, 165, 7])
    del numbers[3]
    self.assertEqual(numbers, [8, 1, 4, 28, 165, 7])


if __name__ == '__main__':
    unittest.main()
