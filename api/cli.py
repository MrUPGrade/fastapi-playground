import typer

from api.db import create_db_from_scheema
from api import models

cli = typer.Typer()

db = typer.Typer()


@db.command()
def reflect():
    create_db_from_scheema()


cli.add_typer(db, name="db")

if __name__ == "__main__":
    cli()
