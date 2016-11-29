#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class TestSlicing(unittest.TestCase):

  def test_slicing(self):
    example = list('hello')
    self.assertEqual(example, ['h', 'e', 'l', 'l', 'o'])

    example[2:] = list('wow')
    self.assertEqual(example, ['h', 'e', 'w', 'o', 'w'])

    example[2:2] = list('llo')
    self.assertEqual(example, ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'w'])

    example[1:6] = []  # delete
    self.assertEqual(example, ['h', 'o', 'w'])


if __name__ == '__main__':
  unittest.main()
