"""666"""
import typer

app = typer.Typer()


@app.command()
def push():
    """updates remote refs using local refs"""
    # TODO: implement
    print('Push')
