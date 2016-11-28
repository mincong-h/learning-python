#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class TestStringOperations(unittest.TestCase):

  def test_concat(self):
    a = 'hello '
    b = 'world'
    self.assertEqual(a + b, 'hello world')

  def test_swap(self):
    a = 'hello'
    b = 'world'
    a, b = b, a
    self.assertEqual(a, 'world')
    self.assertEqual(b, 'hello')


if __name__ == '__main__':
  unittest.main()
