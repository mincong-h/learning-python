import sys

import src.stdio.hello as script


def test_main(capsys):
    sys.argv[1:] = ["Python"]
    script.main()
    captured = capsys.readouterr()
    assert "Hello, Python\n" == captured.out
