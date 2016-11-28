#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class TestVariables(unittest.TestCase):

  def test_variables(self):
    x = 18
    y = 54
    self.assertEqual(x + 15, 33)
    self.assertEqual(x ** 3, 5832)
    self.assertEqual(x + y, 72)


if __name__ == '__main__':
  unittest.main()
