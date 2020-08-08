import src.stdio.dialog as script

# How to test a function with input call?
# https://stackoverflow.com/a/36377194/4381330
def test_main_yes(capsys, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "y")
    script.main()
    captured = capsys.readouterr()
    assert "Welcome to Mincong's demo\nThanks for confirmation\n" == captured.out


def test_main_no(capsys, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "n")
    script.main()
    captured = capsys.readouterr()
    assert "Welcome to Mincong's demo\nSorry to see you go\n" == captured.out
