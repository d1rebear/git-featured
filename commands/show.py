"""Docstring module"""
import typer

app = typer.Typer()


@app.command()
def show():
    """shows various types of objects"""
    # TODO: implement
    print('Show')
