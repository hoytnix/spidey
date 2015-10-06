# -*- coding: utf-8 -*-
"""
    web.app
    ~~~~~~~~~~~~~~~~~~~~

    manages the app creation and configuration process

    :copyright: (c) 2014 by Michael Hoyt.
    :license: MIT, see docs/license.md for more details.
"""
import os
import logging
import datetime
import time

from sqlalchemy import event
from sqlalchemy.engine import Engine

from flask import Flask, request

# Blueprints.
from web.index.views     import index
from web.stats.views     import stats
from web.admin.views     import admin

# extensions
from web.extensions import db, csrf

import braintree

braintree.Configuration.configure(
    braintree.Environment.Sandbox,
    '67tt3t7dy7zbqy4m',
    'mrx3j5sptd3y3fb3',
    'c4f011cc8e50802c455d9644efc574f2'
)

def create_app(config=None):
    """Creates the app."""

    # Initialize the app
    app = Flask(import_name = "web", 
        template_folder = '/www/search/templates')

    # Use the default config and override it afterwards
    app.config.from_object('web.configs.default.DefaultConfig')
    # Update the config
    #app.config.from_object(config)
    # try to update the config via the environment variable
    #app.config.from_envvar("web_SETTINGS", silent=True)

    configure_blueprints(app)
    configure_extensions(app)

    return app

def configure_blueprints(app):
    app.register_blueprint(index,     url_prefix='')
    app.register_blueprint(stats,     url_prefix='/stats')
    app.register_blueprint(admin,     url_prefix='/admin')

def configure_extensions(app):
    """Configures the extensions."""

    # Flask-WTF CSRF
    csrf.init_app(app)

    # Flask-SQLAlchemy
    db.init_app(app)