"""Docstring module"""
import typer

app = typer.Typer()


@app.callback(invoke_without_command=True)
def __clone():
    """creates a copy of a specific repository or branch within a repository"""
    # TODO: implement
    print('Clone')
