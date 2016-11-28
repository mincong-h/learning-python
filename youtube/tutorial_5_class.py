#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Person:

  def __init__(self, name):
    self.name = name

  def presentation(self):
    return "Hi, I'm " + self.name + "!"


def main():
  me = Person('Mincong')
  print me.presentation()


if __name__ == '__main__':
  main()
