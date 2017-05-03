#!/usr/bin/env python
# -*- coding: utf-8 -*-

import textwrap
import unittest

import fmt_props as fmt


class TestFormatLine(unittest.TestCase):
    def test_single_word_value(self):
        self.assertEqual('key=value', fmt.format_line('key= value'))
        self.assertEqual('key=value', fmt.format_line('key=  value'))
        self.assertEqual('key=value', fmt.format_line('key = value'))
        self.assertEqual('key=value', fmt.format_line('key =value'))
        self.assertEqual('key=value', fmt.format_line('key  =value'))

    def test_multi_word_value(self):
        self.assertEqual('key=my value', fmt.format_line('key = my value'))
        self.assertEqual('key=my value', fmt.format_line('key = my value '))
        self.assertEqual('key=v = 1', fmt.format_line('key=v = 1'), 'The 2nd "=" symbol is part of the value.')

    def test_without_key(self):
        # We don't handle multi-line value.
        self.assertEqual('2nd line of a multi-line value', fmt.format_line('2nd line of a multi-line value'))

    def test_empty_line(self):
        self.assertEqual('', fmt.format_line(''))

    def test_comment(self):
        self.assertEqual('#', fmt.format_line('#'))
        self.assertEqual('# key = value', fmt.format_line('# key = value'))


class TestFormatLines(unittest.TestCase):
    def test_format_lines(self):
        origin = textwrap.dedent('''\
        key1 = My value 1
        key2  =My value 2\
        is multi-line.

        key3= My value 3
        key4=My value 4

        # key5 = My value 5
        ''')
        expected = textwrap.dedent('''\
        key1=My value 1
        key2=My value 2\
        is multi-line.

        key3=My value 3
        key4=My value 4

        # key5 = My value 5
        ''')
        self.assertEquals(expected, fmt.format_content(origin))


if __name__ == '__main__':
    unittest.main()
