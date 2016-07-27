# The AX-API client

##Context
Some of our customers are using the API in a sophisticated manner by continually importing puredata json datasets via carefully crafted API calls. Their greater struggles are compensated, though, through advanced influence and control over the AX API and the underlying database. They are easily able to masterfully manipulate the data, stored in the MyAX platform, through careful and subtle operations, like redesigning a dataset on the fly or removing single objects from our database without touching the others.

There are however customers, not receptive to this ways, who prefer a more linear and thus straightforward approach to achieve their goals. These customers have basically a very firm grasp on the intended results but otherwise lack the understanding and technical expertise to achieve it with the aforementioned ways of direct API interaction. To provide them with a straightforward way of importing their data into their Contentprojects this API client was created by our team of software developers to empower them to do exactly that.

##The Excel Sheet
Most if not all of our customers are adept at using the notorious Excel for data related interactions and tasks. It is thus only natural to base our API client of the usage of this format as a solid base for further endeavours. So the requirements for the API client are simple: First you need an Excel sheet consisting of 2+x columns. The 2 mandatory columns are the UID of the dataset, mostly a series of numbers or letters, and the name of the dataset, a descriptive and prosaic description of the depicted dataset content.
The rest of the Excel sheet needs to be arranged in the traditional way of column headers in the first row and values in the rows below. The names of the columns should be conform to json format and should be void of special characters like !”§$%&/( etc.

Note: A List of Json Datasets packed into a single json-file is also possible to upload.

##Preparations:
If the data input is prepared we now can begin to configure our system for accommodating the API client.

###5 Actions
We need to take 5 steps before our first import:
- Choosing a folder/repository in our system. This repository should be easily accessible, for we need to place downloaded files there frequently, to upload them afterwards.
- Creating a virtual environment on our system. This virtual environment is then configured in a standardized way, for we need to equalize our systems to gain the same intended results on every computer and operating system alike.
- Installing the API client on your system
- Configuring the uploadscript for our specific import. This is a necessary step to customize the import to our liking, for we want to specify where our data shall be integrated into the MyAX system.
- Starting the import and push the Button, for every journey needs a first step.

###3 techniques
Before we undertake these five steps to achieve our goal, we shall familiarize ourself with 4 techniques necessary for our endeavour, which are:
- Navigating your systems folder- and file-structure through the commandlinetool of your choice.
- Creating and activating a virtual environment
- Installation and execute the upload script inside your virtual environment

##The MAC Way
###Your Folder Structure
Look at the folder structure of a typical OS X installation. Open a Finder window and click the icon for your hard drive (which is typically called Macintosh HD) in the Sidebar. You should see at least four folders: Applications, Library, System, and Users. Within the Users folder, each user has his own set of folders containing documents, preferences, and other information that belongs to that user and account.

When you open the Users folder, you see a folder for each person who has a user account on the Mac, as well as the Shared folder.
The Shared folder that you see inside the Users folder allows everyone who uses the Mac to use any files stored there. If you want other people who use your Mac to have access to a file or folder, the Shared folder is the proper place to stash it.

From the Users folder, you can drill down into the Home folder to see what’s inside. When the user logs on to this Mac, his Home folder appears whenever he clicks the Home icon in the Sidebar, chooses Go→Home, or uses the keyboard shortcut Shift+Command+H.
Your Home folder is the most important folder for you as a user — or at least the one where you stash most of your files. It is strongly recommend that you store all the files you create in subfolders within your Home folder — preferably, in subfolders in your Home/Documents folder.
When you open your Home folder, you see a Finder window with a little house icon and your short username in the title bar. Seeing your short username in the title bar tells you that you’re in your Home folder. Every user has a Home folder named after his or her short username.

If your Mac has more than one user, you can see the other users’ Home folders in your Users folder, but OS X prevents you from opening files from or saving files to them.
By default, your Home folder has several folders inside it created by OS X. The following four are the most important:
Desktop: If you put items (files, folders, applications, or aliases) on the Desktop, they’re actually stored in the Desktop folder.
Documents: This is the place to put all the documents (letters, spreadsheets, recipes, and novels) that you create.
Library: This Library folder is invisible in Mavericks. Rest assured that even though it’s hidden, it’s still one of the most important folders in your Home folder, containing Preferences, fonts available only to you, and other stuff that you expect to use.
Public: If others on your local area network use file sharing to connect with your Mac, they can’t see or use the files or folders in your Home folder, but they can share files you’ve stored in your Home folder’s Public folder.
You can create more folders, if you like. In fact, every folder that you ever create (at least every one you create on this particular hard drive or volume) should be within your Home folder.
 

###Command Line navigation
The navigation of the command line is a skill needed to operate the API client effectively. For a brief description of the most important commands pls resort to this site: http://ss64.com/osx/

Now, If you start your Command line tool “Terminal”, your starting folder is your user folder.

From their you should navigate through the different places in your system by using the two most important commands:
ls and cd
Ls, also known as the list command has the ability to list you the subdirectories of the folder where you are located right now. For example if you type “ls” as the first thing after opening your terminal directories shown are Applications, Documents, etc.
If you want to open one of these directories use the command cd, “change directory” + ”directory name” to open this directory. Your current directory is the displayed in the terminal as follows:
Administrators-Mac-mini:Desktop

If you want to switch back to a higher directory “cd ..” is the command you need.

###Creating and activating a virtual environment
A Virtual Environment is a tool to keep the dependencies required by different projects in separate places, by creating virtual Python environments for them. It solves the “Project X depends on version 1.x but, Project Y needs 4.x” dilemma, and keeps your global site-packages directory clean and manageable.
For example, you can work on a project which requires Django 1.3 while also maintaining a project which requires Django 1.0.

####Install virtual your environment
virtualenv is a tool to create isolated Python environments. virtualenv creates a folder which contains all the necessary executables to use the packages that a Python project would need.

Install virtualenv via pip:

*$pip install virtualenv*


####Create a virtual environment for a project:

*$cd my_project_folder*
*$virtualenv environment_name*


virtualenv environment_name will create a folder in the current directory which will contain the Python executable files, and a copy of the pip library which you can use to install other packages. The name of the virtual environment (in this case, it was environment_name) can be anything; omitting the name will place the files in the current directory instead.
This creates a copy of Python in whichever directory you ran the command in, placing it in a folder named environment_name.

You can also use a Python interpreter of your choice.
*$virtualenv -p /usr/bin/python3.5 environment_name*

This will use the Python interpreter in /usr/bin/python3.5
This interpreter is needed to use the API-client.

####Activating the virtual environment

*$source environment_name/bin/activate*

The name of the current virtual environment will now appear on the left of the terminal prompt (e.g. (environment_name)Your-Computer:your_project UserName$) to let you know that it’s active. From now on, any package that you install using pip will be placed in the environment_name folder, isolated from the global Python installation.
Install packages as usual, for example:

*$pip install ax-semantics-cli*

####Deactivating your virtual environment 
If you are done working in the virtual environment for the moment, you can deactivate it:

*$deactivate*

This puts you back to the system’s default Python interpreter with all its installed libraries.
To delete a virtual environment, just delete its folder. (In this case, it would be rm -rf venv.)
After a while, though, you might end up with a lot of virtual environments littered across your system, and its possible you’ll forget their names or where they were placed.


###The API-Client
####Installing the API client on your virtual environment
If your new virtual environment is activated you can proceed to install the packages required for the API client:

*$pip install axsemantics_cli*

After the installation is completed everything is set and ready to go. If you need information about the basic functions of the client, please use:

*$axsemantics --help*
 
Then you get a brief overview of the possible commands of the API client.

#####Importing files with the API-client
To import an Excel- or Json-File via the API client we first need to create the necessary import configuration inform of an import script:

*$axsemantics -l user_mail_adress create-importer -c CP_id configuration_file_name.py*

user_mail_adress is the email address you are using to login to the MyAX Plattform
CP_ID is the ID of the content project where you want to import your data into

As a result an import Script is created that contains a mapping, your API-Token and the targeted content project. Open and edit it with a texteditor of your choice.

The Mapping looks like this:
*MAPPING = {
        'MPID': uid,
        'Title English': 'name’
}*

As stated in the script the first element (before ‘:’) is the column name (excell) or key (json) from your data. The second Element (after ‘:’) is the datafield as needed by your trainings. As shown in the above mapping, the fields ‘uid’ and ‘name’ have to be mapped for the import script to work. The rest of the content of either the excel or the json file are written in the pure_data field as key-value-pairs. If the Data-field-names in your export are different than the ones your training needs to incorporate the information in the texts this mapping is the palace is where you can define a mapping yourself to compensate deviations.
    
After the Mapping is configured you can start your Importer by placing the file you want to import in the same directory where the import script is located.
After that step the import is started like this:

*./configuration_file_name.py data_file_name.json*

After the import started you can got to your content project in the MyAX and watch the data getting import into the specified content project.

####Displaying your MyAX resources with the API-client

Here are some more commands you can use to trigger additional functions and get additional information:

Quick command cheat sheet:
list all trainings you have access to
axsemantics training list
list all content projects you have access to
axsemantics content-project list
show details about content project 123
axsemantics content-project get 123 show
list all things belonging to content project 123
axsemantics content-project get 123 things list
show details about thing 123456 belonging to content project 123
axsemantics content-project get 123 things get 123456 show
as user janedoe, download the promoted atml for training 128 into mytraining.atml3
axsemantics -l janedoe training get 128 promoted mytraining.atml3 (this will ask for your password interactively)
as user janedoe with password verysecure, import the training from file mytraining.atml3 into the existing Training 128
axsemantics -l janedoe -p verysecure training get 128 import mytraining.atml3










### How to install on Linux

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
