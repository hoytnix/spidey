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

from web.admin.models import Keywords, Domains, word_json, domain_json

admin = Blueprint("admin", __name__)

@admin.route('/')
def _index():
    conf = {
        'title' : 'Search Engine',
        'slogan': 'Not Google.',
    }

    return render_template('admin/index.html', conf=conf)

@admin.route('/update_all_words')
def update_all_words():

    json = word_json()

    words = json[0]
    count = json[1]

    for word in words:
        k = Keywords(word=word, count=count[word])
        db.session.add(k)
        db.session.commit()

    return redirect('/admin')

@admin.route('/update_all_domains')
def update_all_domains():

    json = domain_json()
    words = word_json()[1]['domains']

    for domain in json:
        d =  json[domain]

        tld = d['tld']
        subdomains = ','.join([sd for sd in d['subdomains']])
        paths = ','.join([path for path in d['paths']])
        keys = ''
        if domain in words:
            keys = ','.join([word for word in words[domain]])

        d = Domains(name=domain,words=keys,tld=tld,pages=paths,subdomains=subdomains)
        db.session.add(d)
        db.session.commit()

    return redirect('/admin')