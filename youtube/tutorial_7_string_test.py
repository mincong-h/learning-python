#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tutorial_7_string as tutorial
import unittest


class TestStringOperations(unittest.TestCase):

  def test_concat_str_int(self):
    num = 18
    # TypeError: cannot concatenate 'str' and 'int' objects
    with self.assertRaises(TypeError):
      'num ' + num

  def test_concat_str_str(self):
    num = 18
    self.assertEqual('num ' + str(num), 'num 18')

  def test_repr(self):
    person = tutorial.Person('Tom')
    self.assertEqual(person.name, 'Tom')
    self.assertEqual(repr(person), 'Hi, my name is Tom!')
    # If __repr__ is overridden, __str__ is overridden too.
    # But not vice versa.
    self.assertEqual(str(person), 'Hi, my name is Tom!')


if __name__ == '__main__':
  unittest.main()
