#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


def build_msg(name='Mincong', action='runs', item='marathon') :
  return '{0} {1} {2}.'.format(name, action, item)


class TestArguments(unittest.TestCase):

  def test_build_msg(self):
    self.assertEqual(build_msg(), 'Mincong runs marathon.')
    self.assertEqual(build_msg('Sally', 'farts', 'gently'),
                     'Sally farts gently.')
    self.assertEqual(build_msg(action='hates'), 'Mincong hates marathon.')


if __name__ == '__main__':
  unittest.main()
