Building a Command Line Tool with Python
Python is a fantastic language for building all sorts of things, from small scripts to gigantic web applications. In this hands-on lab, we're going to build a robust command line application. By the time we've finished, we'll have gone through a complete process from starting a Python project to having an installable command line application.

The Scenario
We've been asked to create a tool that will export a system's user information into formats that various other departments can use. The tool will be able to export usernames, IDs, home directories, and shells in either JSON or CSV format. No information about system users themselves will be included in the files. By default, the Python tool will display the information as JSON to stdout, but the --format flag will allow a person to specify CSV as an alternative export type. Additionally, if we want the information going to a file instead of stdout, we can specify it by using the --path flag.

The Environment
Once we get into the lab, we're in our /home/user/ directory on a CentOS 7 machine that has Python 3.7 installed.

Objectives
We need to accomplish a few things before we can call them done. To finish them all, we'll be working from this list:

Create package
Implement CLI interface
Format user information
Write JSON and CSV
Wire the pieces together
Install the hr tool
Let's get to it!

Create the Package
We're in our home directory, /home/user/. If we do a quick ls, we'll see our home directory is empty. Let's start right off by making another directory and getting into it:

[user@$host]$ mkdir hr
[user@$host]$ cd hr
Then we'll make a spot for our code:

[user@$host hr]$ mkdir -p src/hr
[user@$host hr]$ touch src/hr/__init__.py
[user@$host hr]$ touch README.rst
We don't necessarily need to do all of this, but this is how to make a bonafide Python package we might share with other people.

Because we want to work on this in isolation, in case we have some dependencies that might differ from the installed environment, we're going to use pipenv, which creates a virtual environment. Fire that up with this:

[user@$host hr]$ pipenv --python python3.7
We'll see a bunch of output, ending with Creating a Pipfile for this project...

Now, in /home/user/hr/, if we run pipenv shell, we can actually activate the environment. The prompt will change, and now we'll see our virtualenv name preceding the rest of it:

(hr) [user@$host hr]$
The last part of getting set up is creating setup.py. Do this with whatever text editor you prefer. The example here uses Vim:

(hr) [user@$host hr]$ vim setup.py
This is the file with some comments:

# This will call the setuptools module, then import the setup and find_packages
# functions from it
from setuptools import setup, find_packages
# This will read the package description from our README.rst file
with open('README.rst', encoding='UTF-8') as f:
     readme = f.read()
# This will actually do the calling out to setup, and set some of the information
# about the package itself
setup(
    name='hr',
    version='1.0.0',
    description='Command line user export utility',
    long_description=readme,
    author='Your Name',
    author_email='youremail@example.com',
    # This will define where to look for the package itself. We're pointing find_packages
    # at the local src directory
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[]
)

This file is good to go. We can save and quit, and then move on.

Implement CLI Interface
Create the CLI Parser
We're going to use the argparse package in our CLI parser. Create and edit src/hr/cli.py (again, using any editor you like). Here is the finished file with comments:

import argparse
# This starts building up our own little parser that does what we want
def create_parser():
    parser = argparse.ArgumentParser()
    # These will add some arguments to the parser. First is the path to the export file.
    # Second is the format of the export file. The default will be JSON, with csv as another
    # option we can pick. The second argument also turns whatever we type (when prompted)
    # to lowercase letters. So if we type CSV or JSON, they'll make it in to the parser as
    # csv or json, respectively.
    parser.add_argument('--path', help='the path to the export file')
    parser.add_argument('--format', default='json', choices=['json', 'csv'], type=str.lower)
    return parser
We can leave this parser alone now and move on to the next task.

Format User Information
Regardless of the steps people take when they actually use the tool, we will always need to read in user information, so that we can put it into an exportable format. Let's create and edit src/hr/users.py, where we'll call in the pwd package. Here it is with some comments:

import pwd

# We're naming our function fetch_users
def fetch_users():
# We'll start with an empty user list
    users = []
    #  Now we're going to start a loop. Show ALL of the users...
    for user in pwd.getpwall():
    # ...and we'll figure out if this is a system user or not with a couple of tests.
    # If they have a UID of over 1000, and home is listed in the password directory  
        if user.pw_uid >= 1000 and 'home' in user.pw_dir:
        # If those are true, then we're going to run a user.append and create a
        # dictionary entry with four attributes: name, id, home, and shell.
            users.append({
                'name': user.pw_name,
                'id': user.pw_uid,
                'home': user.pw_dir,
                'shell': user.pw_shell,
            # Back out of our if and for loops
            })
    # And then end the function
    return users
Export to JSON and CSV
The last thing we need to do is set up export functionality. We need to figure out how we want to write out to JSON or CSV, both to stdout and to an actual file.

To get this done, we'll need to create and edit src/hr/export.py, again, using whichever editor you like best.

Here are the file contents with comments:


# First we need to import the packages we'll need from the standard library:
import json
import csv

# This section deals with exporting to JSON. First we'll create and define
# a function called to_json_file. It will take the user data from the fetch_users
# function

def to_json_file(export_file, users):

    # And then it will dump it out (it will look nice with the indent=4 we're specifying)
    json.dump(users, export_file, indent=4)

    # Then we'll close the export file
    export_file.close()

# This section deals with exporting to csv.
def to_csv_file(export_file, users):
    # With csv, we need a header (like column names)
    # We're specifying here what those names are.
    # Note the \n (newline) at the end of shell.
    # Once the line is done writing, we need to go
    # to the next line and start the actual exporting
    # of the data
    export_file.write('name,id,home,shell\n')

    # Now is where we're actually starting to use
    # the csv package. We'll create a writer that
    # will do the actual writing out of the data.
    writer = csv.writer(export_file)

    # We already wrote the header line to the file, and
    # since it ended with a newline character our rows
    # will all go below the header.
    rows = [[user['name'], user['id'], user['home'], user['shell']] for user in users]

    # This is going to actually write the data, rows
    writer.writerows(rows)

    #And this closes the file
    export_file.close()
Wire the Pieces Together
Add to cli.py
We've got all the smaller pieces built, and we're ready to tie them all together. Let's get back into the file (src/hr/cli.py), with whichever editor you like, and add to it. Our new edits won't be until after the return parser line. The comments that were in this file earlier in the guide are gone, just to save some scrolling.

import argparse
def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help='the path to the export file')
    parser.add_argument('--format', default='json', choices=['json', 'csv'], type=str.lower)
    return parser

# Inside here, we're going simply import some things.
# They'll only import though if someone runs the main
# function. If someone just runs the create_parser
# function on its own, then these will NOT be imported.
def main():

    import sys

    # Here, we want to import the export and users modules
    from hr import export, users

    # We're importing as u, because users is probably what
    # the list will be named.
    from hr import users as u

    # Here we're going to create a parser, and immediately
    # have it start parsing the args, so that we have access
    # to the args.
    args = create_parser().parse_args()

    # This reads in the user information (from the pwd module
    # that we used in users.py).
    users = u.fetch_users()

    # Now for some conditional logic, based on the path that's
    # passed in, to determine the file that we're using, and
    # and the format that's passed in, so that we know how to
    # export it

    # The first argument is going to be the path.
    if args.path:

        # If the path is present at all, we're going to open the file,
        # make sure it's writable, and set the newline to be an empty
        # string. We don't want any extra strings or characters in what
        # we're doing.
        file = open(args.path, 'w', newline='')

    # If we're NOT writing to a file, then the output is going to
    # be STDOUT
    else:
        file = sys.stdout

    # This is where the writing will actually happen. Our first part
    # if the if/else will be testing for whether we're dealing with
    # JSON or not. If it is (which is the default), then we'll call the
    # export module to_json_file and write users out to the file in
    # JSON format.
    if args.format == 'json':
        export.to_json_file(file, users)

    # And if it's not JSON, then we're planning on it being csv. We'll
    # call the export module to_csv_file and write out users to the
    # file in csv format.
    else:
        export.to_csv_file(file, users)

Since we wrote a batch of smaller separate modules that all do their respective jobs very well, we can now call them into this simple function that's fairly easy to follow.

Add to setup.py
We're going to add a bit more to setup.py after installrequires=[]. Just like with cli.py, previous comments in the file are gone. Let's make sure we don't forget the comma after installrequires=[]. It's easy to do, since we left the file for a bit and came back.


from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
     readme = f.read()

setup(
    name='hr',
    version='1.0.0',
    description='Command line user export utility',
    long_description=readme,
    author='Your Name',
    author_email='youremail@example.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[],

    # This is essentially saying:
    # When you are installed, create an executable named hr,
    # that will call the "main" method inside the "cli" module,
    # inside of the "hr" package.
    entry_points={
        'console_scripts': 'hr=hr.cli:main'
    }
)
Install the hr Tool
We're done, right? The tool's all built, and we can go home? Well, no. We'd better install it and test it.

Let's get out of the virtual environment. Once we type exit, we'll get dropped back into a regular command prompt.

(hr) [user@$host hr]$ exit
[user@$host hr]$
We need to install our application, and we're going to do it with pip.

[user@$host hr]$ pip3.7 install --user -e .
Let's dissect that command. pip 3.7 install is what installs a python package. --user is a flag that will just install this program locally for our user, rather than system-wide. The -e . is saying, "Install the package that's sitting right here in this environment."

Once we run that, there should be a bit of output (with Successfully installed hr near the end), and we'll be back at a command prompt.

Now, if we run the program hr, with no arguments, it should fetch us some user information in JSON format and spit it out to the screen:

[user@$host hr]$ hr
$ hr
[
  {
    "name": "cloud_user",
    "id": 1000,
    "home": "/home/cloud_user",
    "shell": "/bin/bash"
  },
  {
    "name": "centos",
    "id": 1001,
    "home": "/home/centos",
    "shell": "/bin/bash"
  },
  {
    "name": "ssm-user",
    "id": 1002,
    "home": "/home/ssm-user",
    "shell": "/bin/bash"
  }
][user@$host hr]$
Typing hr --help will give you a bit of information about hr usage, like valid arguments.

We can dump out CSV instead of JSON, if we want, with the --format argument.

[user@$host hr]$ hr --format=csv
name,id,home,shell
cloud_user,1000,/home/cloud_user,/bin/bash
centos,1001,/home/centos,/bin/bash
ssm-user,1002,/home/ssm-user,/bin/bash
These both outputted the data to the screen. Our programming is supposed to accommodate JSON and CSV files, remember? Let's give one of those a whirl with a --path argument.

[user@$host hr]$ hr --format=json --path=users.json
We won't see any output here — just another command prompt. But we should see a users.json sitting in the directory we're at (run a quick ls to check), and we can cat users.json to see it does, in fact, contain all our user data in JSON format.

We Did It!
Congratulations. Let's pat ourselves on the back here. We created a Python tool from scratch that does everything it's supposed to: It reads user data and exports it to either JSON or CSV, and it will export it either to stdout or a file. We are done.
