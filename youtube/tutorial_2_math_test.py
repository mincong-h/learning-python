#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

class TestMath(unittest.TestCase):

  def test_math(self):
    self.assertEqual(2 + 3, 5)
    self.assertEqual(2 - 3, -1)
    self.assertEqual(2 * 3, 6)
    self.assertEqual(2 / 3, 0)
    self.assertEqual(3 / 2, 1)
    self.assertEqual(2 % 3, 2)
    self.assertEqual(2 ** 3, 8)

if __name__ == '__main__':
  unittest.main()
