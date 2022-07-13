"""Docstring module"""
import typer

app = typer.Typer()


@app.callback(invoke_without_command=True)
def __show():
    """shows various types of objects"""
    # TODO: implement
    print('Show')
