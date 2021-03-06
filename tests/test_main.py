import tempfile

from click.testing import CliRunner

from gsrace.__main__ import main


def test_main():
    runner = CliRunner()
    tmp_dir = tempfile.TemporaryDirectory()
    # result = runner.invoke(main, ["l8WuQJgAAAAJ", f"-o {tmp_dir.name}"])
    result = runner.invoke(main, ["l8WuQJgAAAAJ", "-d 36", "-h 2", "-w 5"])
    tmp_dir.cleanup()
    assert result.exit_code == 0
