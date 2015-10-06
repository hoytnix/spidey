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

from web.stats.models import domain_stats, word_stats, domains_with_word
from web.admin.models import Keywords, Domains

stats = Blueprint("stats", __name__)

@stats.route('/')
def _index():
    conf = {
        'title' : 'Search Engine',
        'slogan': 'Not Google.',
    }

    return render_template('stats/index.html', conf=conf)

@stats.route('/tlds')
def tlds():
    conf = {
        'title' : 'Search Engine',
        'slogan': 'Not Google.',
    }

    tlds = domain_stats()

    total = 0
    for tld in tlds:
        total += int(tld[1])

    return render_template('stats/tlds.html', conf=conf, tlds=tlds, total=total)

@stats.route('/tlds/<tld>')
def tld(tld):
    conf = {
        'title' : 'Search Engine',
        'slogan': 'Not Google.',
    }

    d = Domains.query.filter_by(tld=tld)

    return render_template('stats/tld.html', conf=conf, domains = d)

@stats.route('/words')
def words():
    conf = {
        'title' : 'Search Engine',
        'slogan': 'Not Google.',
    }

    k = Keywords.query.all()

    return render_template('stats/words.html', conf=conf, words=k)

@stats.route('/word/<word>')
def word(word):
    conf = {
        'title' : 'Search Engine',
        'slogan': 'Not Google.',
    }

    words = word_stats()[0]

    if word in words:
        
        domains = domains_with_word(word=word)

        return render_template('stats/word.html', conf=conf, word=word, domains=domains)
    else:
        return render_template('stats/word_not_found.html', conf=conf, word=word)

@stats.route('/domain/<domain>')
def domain(domain):
    conf = {
        'title': 'Search Engine',
        'slogan': 'Not Google.'
    }

    site = Domains.query.filter_by(name=domain).first()

    return render_template('stats/domain.html', conf=conf, domain=domain, site=site)