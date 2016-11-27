#!/usr/bin/python -tt

import string1 as s
import unittest

class TestStringMethods(unittest.TestCase):

  def test_donuts(self):
    self.assertEqual(s.donuts(4), 'Number of donuts: 4')
    self.assertEqual(s.donuts(9), 'Number of donuts: 9')
    self.assertEqual(s.donuts(10), 'Number of donuts: many')
    self.assertEqual(s.donuts(99), 'Number of donuts: many')

  def test_both_ends(self):
    self.assertEqual(s.both_ends('spring'), 'spng')
    self.assertEqual(s.both_ends('Hello'), 'Helo')
    self.assertEqual(s.both_ends('a'), '')
    self.assertEqual(s.both_ends('xyz'), 'xyyz')

  def test_fix_start(self):
    self.assertEqual(s.fix_start('babble'), 'ba**le')
    self.assertEqual(s.fix_start('aardvark'), 'a*rdv*rk')
    self.assertEqual(s.fix_start('google'), 'goo*le')
    self.assertEqual(s.fix_start('donut'), 'donut')

  def test_mix_up(self):
    self.assertEqual(s.mix_up('mix', 'pod'), 'pox mid')
    self.assertEqual(s.mix_up('dog', 'dinner'), 'dig donner')
    self.assertEqual(s.mix_up('gnash', 'sport'), 'spash gnort')
    self.assertEqual(s.mix_up('pezzy', 'firm'), 'fizzy perm')

if __name__ == '__main__':
  unittest.main()
