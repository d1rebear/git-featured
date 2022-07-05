"""See the file "LICENSE" for the full license governing this code."""
import typer
import commands
from commands import checkout, clone, list, merge, pull, push, show

app = typer.Typer()

app.add_typer(commands.checkout.app, name='checkout')
app.add_typer(commands.clone.app, name='clone')
app.add_typer(commands.list.app, name='list')
app.add_typer(commands.merge.app, name='merge')
app.add_typer(commands.pull.app, name='pull')
app.add_typer(commands.push.app, name='push')
app.add_typer(commands.show.app, name='show')


if __name__ == "__main__":
    app()
