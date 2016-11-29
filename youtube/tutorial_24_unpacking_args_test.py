#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


def health_index(age, apples, cigarettes):
  return 100 - age + apples * 3.5 - cigarettes * 2

  
class TestUnpackingArguments(unittest.TestCase):

  def test_unpacking_args(self):
    mincong_data = [20, 20, 0]
    index1 = health_index(mincong_data[0], mincong_data[1], mincong_data[2])
    index2 = health_index(*mincong_data)
    self.assertEqual(index1, 150)
    self.assertEqual(index2, 150)


if __name__ == '__main__':
  unittest.main()
