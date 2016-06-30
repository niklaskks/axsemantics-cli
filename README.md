# axsemantics-cli

### How to install

Please work in a virtualenv.

    virtualenv -p /usr/bin/python3 axsemantics
    source axsemantics/bin/activate
    pip install axsemantics_cli

* requires: `python3`.

When you are done with your work with the client you can deactivate the virtualenv with the command `deactivate`.

### Usage

the client has verbose help output, just use --help to get the list of possible subcommands for the command you typed so far

bash completion is also possible (needs documentation)

#### Quick command cheat sheet:

##### list all trainings you have access to

`axsemantics training list`

##### list all content projects you have access to

`axsemantics content-project list`

##### show details about content project 123

`axsemantics content-project get 123 show`

##### list all things belonging to content project 123

`axsemantics content-project get 123 things list`

##### show details about thing 123456 belonging to content project 123

`axsemantics content-project get 123 things get 123456 show`

##### as user janedoe, download the promoted atml for training 128 into mytraining.atml3

`axsemantics -l janedoe training get 128 promoted mytraining.atml3`
(this will ask for your password interactively)

##### as user janedoe with password verysecure, import the training from file mytraining.atml3 into the existing Training 128

`axsemantics -l janedoe -p verysecure training get 128 import mytraining.atml3`

##### use login information from environment variables

```
export AXSEMANTICS_LOGIN='janedoe'
export AXSEMANTICS_PASSWORD='verysecure'
axsemantics training list
```

### Development

again a virtualenv is highly recommended for testing, making the binaries known to your virtualenv should be as simple as

    virtualenv -p /usr/bin/python3 axsemantics
    source axsemantics/bin/activate
    pip install --editable ../axsemantics-python  # (only if you want to work on both)
    pip install --editable .

now you can change your source and the "installed" package will directly incorporate your changes
