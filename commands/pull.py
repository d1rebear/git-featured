"""Docstring module"""
import typer

app = typer.Typer()


@app.callback(invoke_without_command=True)
def __pull():
    """Fetches from and integrates another repository or a local branch"""
    # TODO: implement
    print('Pull')
