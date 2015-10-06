# -*- coding: utf-8 -*-
"""
    web.index.views
    ~~~~~~~~~~~~~~~~~~~~

    Site-wide index! :0

    :copyright: (c) 2014 by Michael Hoyt.
    :license: MIT, see docs/license.md for more details.
"""
import datetime

from flask import (Blueprint, redirect, url_for, current_app,
                   request, flash, render_template)

from web.extensions import db
from web.utils.helpers import (randomizer)
from web.utils.helpers import (render_markup)
from web.index.models import  (posts, technologies, solutions, Randomizer)

index = Blueprint("index", __name__)

@index.route('/')
def _index():
    conf = {
        'title' : 'Search Engine',
        'slogan': 'Not Google.',

        'sidebar': True,
        'footer':  True,
        'rand': randomizer(),
        'user_level': 2,
    }

    markup = render_markup("""
# Chapter #

## Section ##

* Item 1
* Item 2
    """)

    return render_template('index/index.html', 
        conf = conf,
        solutions = solutions,
        technologies = technologies,
        posts = posts,
        m = markup,
        c = request.headers.get('CF-IPCountry'))

@index.route('/plans')
def plans():
    conf = {
        'title' : 'web',
        'slogan': 'The defining IT solution.',

        'sidebar': False,
        'footer':  False,
        'rand': None,
        'user_level': 5,
    }

    return render_template('index/plans.html', conf=conf)

@index.route('/spider')
def spider():
    conf = {
        'title' : 'web',
        'slogan': 'The defining IT solution.',

        'sidebar': False,
        'footer':  False,
        'rand': None,
        'user_level': 5,
    }

    return render_template('index/spider.html', conf=conf)