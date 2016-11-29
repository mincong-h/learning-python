#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class TestRangeAndWhile(unittest.TestCase):

  def test_for_and_range(self):
    for x in range(10, 30, 5):
      # 10
      # 15
      # 20
      # 25
      # 30
      self.assertTrue(x % 5 == 0)
      self.assertTrue(x <= 30)
      self.assertTrue(x >= 10)

  def test_while(self):
    val = 5
    while val < 10 :
      val += 1
    self.assertEqual(val, 10)


if __name__ == '__main__':
  unittest.main()
