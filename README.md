# axsemantics-cli

### How to install

Please work in a virtualenv.

    virtualenv -p /usr/bin/python3 axsemantics
    source axsemantics/bin/activate
    pip install axsemantics_cli

* requires: `python3`.

When you are done with your work with the client you can deactivate the virtualenv with the command `deactivate`.

### Usage

the client has verbose help output, just press enter in the middle of a command and it will tell you what
possible commands could follow the portion you typed so far, or you can use --help to get the help output

bash completion is also possible (needs documentation)

### Development

again a virtualenv is highly recommended for testing, making the binaries known to your virtualenv should be as simple as

    virtualenv -p /usr/bin/python3 axsemantics
    source axsemantics/bin/activate
    pip install --editable ../axsemantics-python  # (only if you want to work on both)
    pip install --editable .

now you can change your source and the "installed" package will directly incorporate your changes
