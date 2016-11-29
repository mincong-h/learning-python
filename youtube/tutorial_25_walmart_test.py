#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class TestWalmart(unittest.TestCase):

  def test_dict(self):
    visitors = {'a', 'a', 'b', 'c'}
    msg = ''
    for visitor in visitors:
      msg += visitor
    # 'a' is shown only once
    self.assertTrue('a' in msg)
    self.assertTrue('b' in msg)
    self.assertTrue('c' in msg)
    self.assertTrue(len(msg) == 3)


if __name__ == '__main__':
  unittest.main()
