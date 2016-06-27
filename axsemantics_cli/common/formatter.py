import click


def heading(headline):
    click.secho(headline, bold=True)
    click.secho('='*len(headline), bold=True)
