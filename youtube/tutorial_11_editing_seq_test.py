#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class TestSequences(unittest.TestCase):

  def test_sequences(self):
    self.assertEqual([1, 2] + [3, 4], [1, 2, 3, 4])
    self.assertEqual('hi' + ' python', 'hi python')
    self.assertEqual('hi' * 3, 'hihihi')
    self.assertEqual(21 * 3, 63)
    self.assertEqual([21] * 3, [21, 21, 21])

  def test_in_string(self):
    name = 'mincong'
    self.assertTrue('i' in name)
    self.assertTrue('w' not in name)

  def test_in_array(self):
    coloc = ['pape', 'mincong', 'charline']
    self.assertTrue('pape' in coloc)
    self.assertTrue('mincong' in coloc)
    self.assertTrue('charline' in coloc)


if __name__ == '__main__':
  unittest.main()
