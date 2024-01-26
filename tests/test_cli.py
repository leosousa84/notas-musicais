#! /usr/bin/python3

from pytest import mark
from typer.testing import CliRunner

from notas_musicais.cli import app

runner = CliRunner()

def test_esacala_cli_deve_retornar_0_ao_stdout():
    result = runner.invoke(app)
    assert result.exit_code == 2

@mark.parametrize('nota', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
def test_escala_cli_deve_conter_as_notas_na_resposta(nota):
    result = runner.invoke(app)
    assert nota in result.stdout
