#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import list1 as impl


class TestList1(unittest.TestCase):

  def test_match_ends(self):
    self.assertEqual(impl.match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    self.assertEqual(impl.match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    self.assertEqual(impl.match_ends(['aaa', 'be', 'abc', 'hello']), 1)

  def test_front_x(self):
    self.assertEqual(impl.front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
                     ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    self.assertEqual(impl.front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
                     ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    self.assertEqual(impl.front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
                     ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

  def test_sort_last(self):
    self.assertEqual(impl.sort_last([(1, 3), (3, 2), (2, 1)]),
                     [(2, 1), (3, 2), (1, 3)])
    self.assertEqual(impl.sort_last([(2, 3), (1, 2), (3, 1)]),
                     [(3, 1), (1, 2), (2, 3)])
    self.assertEqual(impl.sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
                     [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
  unittest.main()
