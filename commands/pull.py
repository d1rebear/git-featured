"""Docstring module"""
import typer

app = typer.Typer()


@app.command()
def pull():
    """Fetches from and integrates another repository or a local branch"""
    # TODO: implement
    print('Pull')
