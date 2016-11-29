#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


def sum(*args):
  total = 0
  for arg in args:
    total += arg
  return total


class TestSum(unittest.TestCase):

  def test_sum(self):
    self.assertEqual(sum(3), 3)
    self.assertEqual(sum(3, 5), 8)


if __name__ == '__main__':
  unittest.main()
