"""Docstring module"""
import typer

app = typer.Typer()


@app.callback(invoke_without_command=True)
def __list():
    """list of last commits"""
    # TODO: implement
    print("List")
