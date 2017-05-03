#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import textwrap


class BColors:
    def __init__(self):
        pass

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def format_props(filename):
    f = open(filename, 'r')
    formatted = format_content(f.read())
    f.close()

    f = open(filename, 'w')
    f.write(formatted)
    f.close()


def format_content(text):
    """
    Format the entire content of a properties file.

    :param text: Content of a properties file.
    :return: Formatted content of a properties file.
    """
    formatted = []
    for line in text.splitlines():
        formatted.append(format_line(line).lstrip())
        formatted.append('\n')

    return ''.join(formatted)


def format_line(text):
    """
    Format one line text by trimming spaces around the assignment symbol '='

    The following cases are ignored:
    - The given line is empty.
    - The assignment symbol is not found (part of a multi-line value).
    - The given line is a comment.

    :param text: One line text
    :return: Formatted one line text
    """
    if len(text) == 0 or text.startswith('#'):
        return text

    idx = text.find('=')
    if idx < 0:  # not found
        return text

    key = text[:idx]
    val = text[idx + 1:] if idx < len(text) - 1 else ''
    return '%s=%s' % (key.strip(), val.strip())


def find_props(dir_path):
    file_paths = []
    for root, dirs, files in os.walk(dir_path):
        for f in files:
            if f.endswith('.properties'):
                file_path = os.path.join(root, f)
                file_paths.append(file_path)

    return file_paths


def main(dir_path, verbose=False):
    file_paths = find_props(dir_path)

    for file_path in find_props(dir_path):
        format_props(file_path)
        if verbose:
            print 'Formatted file: ' + file_path

    print BColors.OKGREEN + '-----------------------------------' + BColors.ENDC
    print BColors.OKGREEN + 'Finished. Total %d files formatted.' % len(file_paths) + BColors.ENDC
    print BColors.OKGREEN + '-----------------------------------' + BColors.ENDC


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])

    elif len(sys.argv) == 3 and (sys.argv[1] == "-v" or sys.argv[1] == "--verbose"):
        main(sys.argv[2], verbose=True)

    else:
        print BColors.FAIL + textwrap.dedent('''\
            usage:

                    ./fmt_props.py [ -v | --verbose ] /path/to/repo
            ''') + BColors.ENDC
