import io
import sys
import unittest
from unittest.mock import patch

import src.stdio.hello as script


class TestHello(unittest.TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_main(self, mock_stdout):
        sys.argv[1:] = ["Python"]
        script.main()
        self.assertEqual("Hello, Python\n", mock_stdout.getvalue())
