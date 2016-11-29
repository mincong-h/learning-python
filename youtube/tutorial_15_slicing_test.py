#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class TestSlicing(unittest.TestCase):

  def test_slicing(self):
    words = ['hey', 'now', 'brown', 'cow']
    self.assertEqual(words.index('brown'), 2)

    words.insert(2, 'hoss')
    self.assertEqual(words, ['hey', 'now', 'hoss', 'brown', 'cow'])

    self.assertEqual(words.pop(1), 'now')
    self.assertEqual(words, ['hey', 'hoss', 'brown', 'cow'])

    self.assertEqual(words.remove('brown'), None)
    self.assertEqual(words, ['hey', 'hoss', 'cow'])


if __name__ == '__main__':
  unittest.main()
