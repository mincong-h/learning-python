#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import unittest


class TestVariables(unittest.TestCase):

  def test_func(self):
    self.assertEqual(math.floor(18.7), 18)
    self.assertEqual(math.sqrt(81), 9)

  def test_func_as_var(self):
    f = math.sqrt
    self.assertEqual(f(9), 3.0)
    f = math.floor
    self.assertEqual(f(19.8), 19)


if __name__ == '__main__':
  unittest.main()
