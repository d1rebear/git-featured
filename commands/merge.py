"""Docstring module"""
import typer

app = typer.Typer()


@app.callback(invoke_without_command=True)
def __merge():
    """Join development histories together"""
    # TODO: implement
    print('Merge')
