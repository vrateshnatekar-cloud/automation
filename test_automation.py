from automation import run


def test_run_prints_greeting(capsys):
    run("Tester")
    assert "Hello, Tester!" in capsys.readouterr().out
