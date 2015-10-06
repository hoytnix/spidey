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


class Randomizer(db.Model):
    __tablename__ = "topicsread"

    vid = db.Column(db.String(11), primary_key=True)

    @property
    def url(self):
        return 'http://www.youtube.com/embed/%s' % self._url
    

    def __repr__(self):
        return "<{}>".format(self.__class__.__name__)


solutions = [
    {
        'title': 'Social Media Management',
        'url':  '/solutions/social-media',
        'path': 'social.png',
        'data': [
            ['Social profiles setup'],
            [
                'Facebook',
                'Twitter',
                'Google+'
            ],
            ['Community management.'],
            ['Website integration.']
        ],
    },
    {
        'title': 'Direct Advertising',
        'url':   '/solutions/direct-advertising',
        'path':  'print.png',
        'data': [
            ['Platforms:'],
            [
                'Radio.',
                'Newspaper.',
                'Brochures.',
                'Placemats.'
            ],
            ['AB Testing.'],
            ['Content development.'],
        ]
    },
    {
        'title': 'Website Optimization',
        'url':   '/solutions/web-optimization',
        'path':  'web.png',
        'data':  [
            ['Search engine optimization.'],
            ['Mobile-first.'],
            ['Transition to responsive design.'],
            ['Online menus and ordering.'],
            ['Reputation management:'],
            [
                'Google Maps.',
                'Yelp.',
                'TripAdvisor.',
            ],
            ['Lead conversion.']
        ]
    },
    {
        'title': 'Mobile Marketing',
        'url':   '/solutions/mobile',
        'path':  'mobile.png',
        'data': [
            ['Mobile app development.'],
            ['Mobile ad campaigns:'],
            [
                'Google PPC.',
                'Google AdSense mobile optimization.',
                'Google AdMob (Android) campaigns.',
            ],
            ['Mobile-search lead conversion.']
        ]
    },
    {
        'title': 'E-Commerce',
        'url':   '/solutions/ecommerce',
        'path':  'ecommerce.png',
        'data':  [
            ['End-to-end management.'],
            ['Growth & development.'],
            ['Platforms:'],
            [
                'CMS',
                'Google Shopping',
                'Amazon',
                'eBay',
                'Square',
                'Overstock.com'
            ],
            ['Dropshipping.'],
        ]
    },
    {
        'title': 'Content Development',
        'url':   '/solutions/content',
        'path':  'content.png',
        'data':  [
            ['Copywriting.'],
            ['Graphic adaptation.'],
            ['Video testimonials.'],
            ['Reviews.'],
            [
                'Yelp',
                'Amazon',
                'TripAdvisor'
            ],
            ['Comprehensive & on-going analysis:'],
            [
                'AB Testing.',
                'Analytics.',
                'Algorithm updates.'
            ]
        ]
    },
    {
        'title': 'Security',
        'url':   '/solutions/security',
        'path':  'security.png',
        'data': [
            ['24/7 hot-line & server staffing.'],
            ['Dedicated management:'],
            [
                'Dedicated server hosting.',
                'Brand protection.',
                'Domain renewal.',
                'Online reputation management.',
                'Identity protection.'
            ],
            ['Anti-hacker:'],
            [
                'DDoS Protection.',
                'SQL Injection & XSS testing.',
                'SSL Protection.',
                'Anti-virus.'
            ]
        ]
    },
    {
        'title': 'Administration & Moderation',
        'url':   '/solutions/admin',
        'path':  'admin.png',
        'data': [
            ['Passive-income.'],
            ['Online community management:'],
            [
                'We\'ll run everything for you.',
                'Guaranteed digital engagement.',
                'Customer support.',
                'Social media management.',
                'Professionals with 20+ years of experience.',
            ],
            ['Diversify your portfolio.'],
            ['Your personalized brand.']
        ]
    },
    {
        'title': 'Web Development',
        'url':   '/solutions/web-dev',
        'path':  'development.png',
        'data': [
            ['Online menu & ordering.'],
            ['Content management systems:'],
            ['Traffic platforms:'],
            ['DevOps:'],
            [
                'Process automation.',
                'Systems administration.',
                'Full-stack management.'
            ]
        ]
    },
]



technologies = [
    {
        'title': 'Google',
        'path':  'google.jpg',
        'url':   'https://google.com'
    },
    {
        'title': 'Amazon',
        'path':  'amazon.png',
        'url':   'https://amazon.com'
    },
    {
        'title': 'Google Apps for Business',
        'path':  'apps.jpg',
        'url':   'https://www.google.com/work/apps/business/'
    },       
    {
        'title': 'Facebook',
        'path':  'facebook.png',
        'url':   'https://facebook.com/'
    },          
    {
        'title': 'Twitter',
        'path':  'twitter.png',
        'url':   'https://twitter.com/'
    },    
    {
        'title': 'Google+',
        'path':  'g-plus.png',
        'url':   'https://plus.google.com/'
    },    
    {
        'title': 'Android',
        'path':  'android.jpg',
        'url':   'https://www.android.com/'
    },  
    {
        'title': 'Google AdSense',
        'path':  'adsense.png',
        'url':   'http://www.google.com/adsense'
    },  
    {
        'title': 'Google AdMob',
        'path':  'admob.jpg',
        'url':   'https://www.google.com/admob/'
    },  
    {
        'title': 'Hootsuite',
        'path':  'hootsuite.png',
        'url':   'https://hootsuite.com/'
    },  
    {
        'title': 'Yelp',
        'path':  'yelp.png',
        'url':   'http://www.yelp.com/about'
    },  
    {
        'title': 'TripAdvisor',
        'path':  'tripadvisor.png',
        'url':   'http://www.tripadvisor.com/PressCenter-c3-Awards.html'
    },  
    {
        'title': 'Namecheap',
        'path':  'namecheap.jpg',
        'url':   'https://www.namecheap.com/about.aspx'
    },  
    {
        'title': 'Ubuntu',
        'path':  'ubuntu.png',
        'url':   'http://partners.ubuntu.com/'
    },  
    {
        'title': 'Cloudflare',
        'path':  'cloudflare.jpg',
        'url':   'https://www.cloudflare.com/partners'
    },  
    {
        'title': 'Python',
        'path':  'python.png',
        'url':   'https://www.python.org/psf/'
    },  
    {
        'title': 'Sublime Text',
        'path':  'sublime.jpg',
        'url':   'http://www.sublimetext.com/'
    },  
    {
        'title': 'Ramnode',
        'path':  'ramnode.png',
        'url':   'http://www.ramnode.com/about.php'
    },  
]



posts = [
    {
        'title':  'First Test Post.',
        'author': 'Anon',
        'date':   'Jan. 1, 2015'
    },
    {
        'title':  'Second Test Post.',
        'author': 'Aadmin',
        'date':   'Jan. 15, 2015'            
    }
]