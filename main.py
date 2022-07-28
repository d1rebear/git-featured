"""See the file "LICENSE" for the full license governing this code."""
import typer
from commands import checkout, clone, list as __list, merge, pull, push, show
app = typer.Typer()

app.add_typer(checkout.app, name='checkout')
app.add_typer(clone.app, name='clone')
app.add_typer(__list.app, name='list')
app.add_typer(merge.app, name='merge')
app.add_typer(pull.app, name='pull')
app.add_typer(push.app, name='push')
app.add_typer(show.app, name='show')


if __name__ == "__main__":
    app()
