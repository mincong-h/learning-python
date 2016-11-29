#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


def allowed_dating_age(my_age):
  girl_age = my_age / 2 + 7
  return girl_age

def get_gender(sex='?'):
  if sex is 'm':
    return 'Male'
  elif sex is 'f':
    return 'Female'
  else:
    return 'Unknown'


class TestFunc(unittest.TestCase):

  def test_dating_age_limit(self):
    self.assertEqual(allowed_dating_age(18), 16)
    self.assertEqual(allowed_dating_age(30), 22)

  def test_get_gender(self):
    self.assertEqual(get_gender('m'), 'Male')
    self.assertEqual(get_gender('f'), 'Female')
    self.assertEqual(get_gender(), 'Unknown')


if __name__ == '__main__':
  unittest.main()
