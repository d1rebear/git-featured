"""Docstring module"""
import typer

app = typer.Typer()


@app.command()
def checkout():
    """updates files in the working tree to match the version  in the index
        or the specified tree"""
    # TODO:  implement
    print(f'"Checkout"')
