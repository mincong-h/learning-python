#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class TestForLoop(unittest.TestCase):

  def test_for_loop(self):
    foods = ['bacon', 'tuna', 'ham', 'sausage', 'beef']
    for f in foods[1:] : # starts at index 1 'tuna'
      self.assertTrue(f is not 'bacon')
      self.assertTrue(f != 'bacon')


if __name__ == '__main__':
  unittest.main()
