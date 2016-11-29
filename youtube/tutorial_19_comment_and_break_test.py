#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class TestBreak(unittest.TestCase):

  def test_break(self):
    '''
    This is a long comment. And we're going to test `break`.
    '''
    magicNumber = 26
    msg = 'magic number not found'

    for n in range(101): # 0 - 100
      if n is magicNumber:
        msg = '{0} is the magic number!'.format(n)
        break

    self.assertEqual(msg, '26 is the magic number!')


if __name__ == '__main__':
  unittest.main()
