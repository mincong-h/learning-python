#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class TestIf(unittest.TestCase):

  def test_int(self):
    age = 27
    msg = ''
    if age > 21:
      msg = 'No beer for you!'
    elif age < 15:
      msg = 'Beer for you!'
    else:
      msg = 'Hello world.'
    self.assertEqual(msg, 'No beer for you!')

  def test_str(self):
    name = 'Mincong'
    msg = ''
    if name is 'Mincong': 
      msg = 'Hey, Mincong.'
    elif name is 'Pape':
      msg = "What's up, Pape?"
    elif name is 'Charline':
      msg = 'My name is Charline'
    else:
      msg = "You're not in our house."
    self.assertEqual(msg, 'Hey, Mincong.')


if __name__ == '__main__':
  unittest.main()
