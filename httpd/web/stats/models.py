# -*- coding: utf-8 -*-
"""
    web.index.models
    ~~~~~~~~~~~~~~~~~~~~

    It provides the models for the index

    :copyright: (c) 2014 by Michael Hoyt.
    :license: MIT, see docs/license.md for more details.
"""
from datetime import datetime, timedelta

from flask import url_for, abort

from web.extensions import db
from web.utils.helpers import slugify
from web.utils.jsondb import Jsondb

import operator

def domains_with_word(word):
  j = Jsondb(f='/home/me/03.json')
  db = j.db

  _domains = db["domains"]

  keys = []
  for key in _domains:
    words = _domains[key]
    if word in words:
      _keys = ( key, words )
      keys.append(_keys)

  return keys

def word_stats():
  j = Jsondb(f='/home/me/03.json')
  db = j.db

  return (sorted(db["words"]), db["words"])

def domain_stats():
  j = Jsondb(f='/home/me/db_15-05-26.json')
  db = j.db

  stats = {}
  for line in db:
    tld = db[line]['tld']
    if tld in stats:
      stats[tld] += 1
    else:
      stats[tld] = 1

  sorted_x = sorted(stats.items(), key=operator.itemgetter(1))
  return sorted_x