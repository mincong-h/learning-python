#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


coloc = ['Mincong', 'Pape', 'Charline', 'Jinxing']


class TestSequenceAndList(unittest.TestCase):

  def test_sublist(self):
    self.assertEqual(coloc[0:1], ['Mincong'])
    self.assertEqual(coloc[1:3], ['Pape', 'Charline'])
    self.assertEqual(coloc[0:1] + coloc[1:3], ['Mincong', 'Pape', 'Charline'])
    self.assertEqual(coloc[1:], ['Pape', 'Charline', 'Jinxing'])
    self.assertEqual(coloc[-2:], ['Charline', 'Jinxing'])

  def test_list_elem(self):
    self.assertEqual(coloc[0], 'Mincong')
    self.assertEqual(coloc[1], 'Pape')
    self.assertEqual(coloc[2], 'Charline')
    self.assertEqual(coloc[-1], 'Jinxing') # negative index is OK
    self.assertEqual(coloc[-3], 'Pape')

  def test_list_out_of_range(self):
    # IndexError: list index out of range
    with self.assertRaises(IndexError):
      coloc[4]
    with self.assertRaises(IndexError):
      coloc[-5]

  def test_list_elem_char(self):
    self.assertEqual(coloc[0][2], 'Mincong'[2])
    self.assertEqual(coloc[0][2], 'n')
    self.assertEqual(coloc[0][-1], 'g')


if __name__ == '__main__':
  unittest.main()
