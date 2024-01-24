from typer.testing import CliRunner

from notas_musicais.cli import app

runner = CliRunner()

def test_esacala_cli_deve_retornar_0_ao_stdout():
    runner.invoke(app)