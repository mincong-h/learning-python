#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Person:

  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return 'Hi, my name is ' + self.name + '!'


def main():
  person = Person('Tom')
  print person

if __name__ == '__main__':
  main()
