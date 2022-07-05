import typer

app = typer.Typer()


@app.command()
def clone():
    """creates a copy of a specific repository or branch within a repository"""
    # TODO: implement
    print(f'Clone')
