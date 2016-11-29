#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class TestContinue(unittest.TestCase):

  def test_continue(self):
    num_to_skip = [2, 5, 12, 13, 33, 17]
    for num in range(1, 20):
      if num in num_to_skip:
        continue
      self.assertTrue(num not in num_to_skip)


if __name__ == '__main__':
  unittest.main()
