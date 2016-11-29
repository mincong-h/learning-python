#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class TestSlicing(unittest.TestCase):

  def test_append(self):
    face = [21, 18, 30]
    face.append(45)
    self.assertEqual(face, [21, 18, 30, 45])

  def test_count(self):
    fruits = ['apples', 'apples', 'banana']
    self.assertEqual(fruits.count('apples'), 2)

  def test_extend(self):
    one = [1, 2]
    two = [3, 4]
    one.extend(two)
    self.assertEqual(one, [1, 2, 3, 4])
    two.extend(one)
    self.assertEqual(two, [3, 4, 1, 2, 3, 4])


if __name__ == '__main__':
  unittest.main()
