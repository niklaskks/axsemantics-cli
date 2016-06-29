import click

import axsemantics

from .main import cli
from .common.transfer import download_with_progressbar, upload_with_progressbar
from .common.formatter import pretty_print_object


@cli.group()
@click.pass_obj
def training(obj):
    pass


@training.command('list')
@click.pass_obj
def trainings_list(obj):
    for training in axsemantics.TrainingList():
        print('{}: {}'.format(training['id'], training['name']))


@training.group('get')
@click.argument('id')
@click.pass_obj
def trainings_get(obj, id):
    try:
        training = axsemantics.Training.retrieve(id)
    except:
        click.echo('Content Project {} not found or not readable by your user'.format(id))
    else:
        obj['training-id'] = id
        obj['training'] = training


@trainings_get.command('show')
@click.pass_obj
def trainings_get_show(obj):
    if 'training' in obj:
        training = obj['training']
        pretty_print_object(training, 'Training')


@training.command()
@click.pass_obj
def download_promoted(obj):
    if 'training' in obj:
        pass
