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

class Keywords(db.Model):
  __tablename__ = 'keywords'
  
  word_id = db.Column(db.Integer(), primary_key=True)
  word    = db.Column(db.String(255))
  count   = db.Column(db.Integer())

  def __init__(self, word=None, count=0):
    self.word  = word
    self.count = count

class Domains(db.Model):
  __tablename__ = 'domains'

  domain_id  = db.Column(db.Integer(), primary_key=True)
  name       = db.Column(db.String(255))
  words      = db.Column(db.Text, nullable=True)
  tld        = db.Column(db.String(10), nullable=True)
  pages      = db.Column(db.Text, nullable=True)
  subdomains = db.Column(db.Text, nullable=True)

  def __init__(self, name=None, words=None, tld=None, pages=None, subdomains=None):
    self.name = name
    self.words = words
    self.tld = tld
    self.pages = pages
    self.subdomains = subdomains

def domain_json():
  j = Jsondb(f='/home/me/db_15-05-26.json')
  db = j.db

  return db

def word_json():
  j = Jsondb(f='/home/me/03.json')
  db = j.db

  return (sorted(db["words"]), db)