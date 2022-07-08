import typer


def main(name: str, years: int):
    typer.echo(f"Hello {name},\nYou are {years} years old.")


if __name__ == "__main__":
    typer.run(main)
