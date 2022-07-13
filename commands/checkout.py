"""Docstring module"""
import typer

app = typer.Typer()


@app.callback(invoke_without_command=True)
def __checkout():
    """updates files in the working tree to match the version  in the index
        or the specified tree"""
    # TODO:  implement
    print("Checkout")
