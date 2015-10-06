#!/usr/bin/env python

"""
    web.manage
    ~~~~~~~~~~~~~~~~~~~~

    This script provides some easy to use commands for
    creating the database with or without some sample content.
    You can also run the development server with it.
    Just type `python manage.py` to see the full list of commands.

    TODO: When Flask 1.0 is released, get rid of Flask-Script and use click.
          Then it's also possible to split the commands in "command groups"
          which would make the commands better seperated from each other
          and less confusing.

    :copyright: (c) 2014 by Michael Hoyt.
    :license: MIT, see docs/license.md for more details.
"""
from __future__ import print_function
import sys
import os
import subprocess

from flask import current_app
from werkzeug.utils import import_string
from sqlalchemy.exc import (IntegrityError, OperationalError)
from flask_script import (Manager, Shell, Server, prompt, prompt_pass,
                          prompt_bool)
from flask_migrate import (MigrateCommand, upgrade)

from web import create_app
from web.extensions import db

# Use the development configuration if available
try:
    from web.configs.development import DevelopmentConfig as Config
except ImportError:
    from web.configs.default import DefaultConfig as Config

app = create_app(Config)
manager = Manager(app)

# Used to get the plugin translations
#PLUGINS_FOLDER = os.path.join(app.root_path, "plugins")

# Run local server
manager.add_command("runserver", Server("0.0.0.0", port=53476, 
    use_debugger=True, 
    use_reloader=True))

# Migration commands
manager.add_command('db', MigrateCommand)


# Add interactive project shell
def make_shell_context():
    return dict(app=current_app, db=db)
manager.add_command("shell", Shell(make_context=make_shell_context))


@manager.command
def initdb():
    """Creates the database."""

    return None


@manager.command
def dropdb():
    """Deletes the database."""

    db.drop_all()

if __name__ == "__main__":
    manager.run()
