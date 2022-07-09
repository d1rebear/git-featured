"""Docstring module"""
import typer

app = typer.Typer()


@app.command()
def merge():
    """Join development histories together"""
    # TODO: implement
    print('Merge')
