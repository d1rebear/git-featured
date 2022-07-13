"""Docstring module"""
import typer

app = typer.Typer()


@app.callback(invoke_without_command=True)
def __push():
    """updates remote refs using local refs"""
    # TODO: implement
    print('Push')
