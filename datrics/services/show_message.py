import click

def show_error(error):
    raise click.ClickException(error)


def show_message(message):
    print(message)