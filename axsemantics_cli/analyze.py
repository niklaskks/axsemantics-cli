import click
from collections import OrderedDict, defaultdict
import json
import os

@click.group()
@click.argument('input', type=click.File('r'))
@click.pass_obj
def analyze(obj, input):
    """
    analyze a directory of atml3 files
    """
    print(input.name)
    try:
        fcontents = json.load(input, encoding='utf-8',
                              object_hook=OrderedDict,
                              object_pairs_hook=OrderedDict)
        obj['input'] = fcontents
    except Exception as e:
        print(e)


@analyze.command()
@click.pass_obj
def show(obj):
    """
    merely print the contents of the dict
    """
    return
    print(json.dumps(obj['input'], indent=4))


@click.group(chain=True, invoke_without_command=True)
@click.argument('path', type=click.Path(exists=True))
@click.pass_context
def atml3file(ctx, path):
    ctx.obj = {}
    if not os.path.isdir(path):
        click.echo('{} is not a directory'.format(path), err=True)
        return
                    # click.echo('\n\n{}'.format(name))
                    # click.echo(json.dumps(fcontents, indent=4))


def atml3file_iter(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            if name[-6:].lower() == '.atml3':
                fname = os.path.join(root, name)
                try:
                    with open(fname, 'r') as f:
                        fcontents = json.load(f, encoding='utf-8',
                                              object_hook=OrderedDict,
                                              object_pairs_hook=OrderedDict)
                        item = {
                            'atml3': fcontents,
                            'filename': fname,
                        }
                        yield item
                except Exception as e:
                    item = {
                        'filename': fname,
                        'atml3': {},
                        'error': str(e),
                    }
                    yield item


@atml3file.resultcallback()
def process_commands(processors, path):
    def echo_name(iterator):
        for item in iterator:
            click.echo(item['filename'])
            yield item

    iterator = echo_name(atml3file_iter(path))
    for processor in processors:
        print(processor)
        iterator = processor(iterator)
    for item in iterator:
        pass


@atml3file.command('collect-errors')
def atml3_errors():
    def processor(iterator):
        counter = 0
        fails = 0
        errors = []
        for item in iterator:
            counter += 1
            if 'error' in item:
                fails += 1
                errors.append('{}: {}'.format(item['filename'], item['error']))
            yield item
        click.echo('\n\n{}/{} failed to validate:'.format(fails, counter))
        click.echo('\n'.join(errors))
    return processor

@atml3file.command('keys')
@click.pass_obj
def atml3_rootkeys(obj):
    obj['allkeys'] = set()
    obj['orderings'] = set()
    def processor(iterator):
        for item in iterator:
            for key in item['atml3'].keys():
                obj['allkeys'].add(key)
            orderstring = '", "'.join(item['atml3'].keys())
            obj['orderings'].add('"{}"'.format(orderstring))
            yield item
        click.echo('\n')
        click.echo('all keys:\n"{}"'.format('", "'.join(obj['allkeys'])))
        click.echo('all orderings:')
        #print(obj['orderings'])
        orderings = list(obj['orderings'])
        orderings.sort()
        for line in orderings:
            click.echo(line)

    return processor

@atml3file.command('reindent')
def atml3_reindent():
    def processor(iterator):
        for item in iterator:
            if item.get('atml3', '') and item.get('filename', ''):
                filename = item['filename']
                atml3 = item['atml3']
                click.echo('writing reindented file to {}'.format(filename))
                with open(filename, 'w') as f:
                    json.dump(atml3, f, indent=4)
            yield item
    return processor