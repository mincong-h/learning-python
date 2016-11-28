#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tutorial_5_class as tutorial
import unittest


class TestPerson(unittest.TestCase):

  def test_person(self):
    p = tutorial.Person('Mincong')
    self.assertEqual(p.name, 'Mincong')
    self.assertEqual(p.presentation(), "Hi, I'm Mincong!")


if __name__ == '__main__':
  unittest.main()
