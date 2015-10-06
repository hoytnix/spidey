# -*- coding: utf-8 -*-
"""
    web.extensions
    ~~~~~~~~~~~~~~~~~~~~

    The extensions that are used by web.

    :copyright: (c) 2014 by Michael Hoyt.
    :license: MIT, see docs/license.md for more details.
"""
#from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask.ext.wtf import CsrfProtect


# Database
db = SQLAlchemy()

# CSRF
csrf = CsrfProtect()

# Login
#login_manager = LoginManager()