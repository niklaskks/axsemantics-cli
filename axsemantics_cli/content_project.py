import click
import json

import axsemantics


@click.group('content-project')
@click.pass_obj
def content_project(obj):
    """
    Content Project commands
    """
    pass


@content_project.command('list')
@click.option('--output-format', '-o', help='output format', default='json')
@click.pass_obj
def cp_list(obj, output_format):
    """
    list all Content Projects your user has access to
    """
    print(output_format)
    keys = {}
    for cp in axsemantics.ContentProjectList():
        if output_format == 'json':
            print(json.dumps(cp))
        elif output_format == 'csv':
            if not keys:
                keys = list(cp.keys())
                print('\t'.join(keys))

            for key in keys:
                print('{}\t'.format(cp.get(key, '')), end='')
        else:
            click.echo('output format must be either json or csv')


#@click.option('--id', help='content project id')
