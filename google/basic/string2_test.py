#!/usr/bin/python -tt

import unittest
import string2 as s

class TestStringMethods(unittest.TestCase):

  def test_verbing(self):
    self.assertEqual(s.verbing('hail'), 'hailing')
    self.assertEqual(s.verbing('swiming'), 'swimingly')
    self.assertEqual(s.verbing('do'), 'do')

  def test_not_bad(self):
    self.assertEqual(s.not_bad('This movie is not so bad'), 'This movie is good')
    self.assertEqual(s.not_bad('This dinner is not that bad!'), 'This dinner is good!')
    self.assertEqual(s.not_bad('This tea is not hot'), 'This tea is not hot')
    self.assertEqual(s.not_bad("It's bad yet not"), "It's bad yet not")

  def test_front_back(self):
    self.assertEqual(s.front_back('abcd', 'xy'), 'abxcdy')
    self.assertEqual(s.front_back('abcde', 'xyz'), 'abcxydez')
    self.assertEqual(s.front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  unittest.main()
