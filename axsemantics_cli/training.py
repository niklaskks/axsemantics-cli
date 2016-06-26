import click
from main import cli
from .common.transfer import download_with_progressbar, upload_with_progressbar


@cli.group(chain=True)
@click.argument('training-id')
@pass_data
def training(data, training_id):
    data.training_id = training_id


@training.command()
@pass_data
def download_promoted(data):
    print(data.training_id)
    print(data.auth_token)
    # download_with_progressbar(data, )
