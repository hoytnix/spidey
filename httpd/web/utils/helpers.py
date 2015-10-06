# -*- coding: utf-8 -*-
"""
    flaskbb.utils.helpers
    ~~~~~~~~~~~~~~~~~~~~

    A few helpers that are used by flaskbb

    :copyright: (c) 2014 by the FlaskBB Team.
    :license: BSD, see LICENSE for more details.
"""
import re
import time
import itertools
import operator
import struct
from io import BytesIO
from datetime import datetime, timedelta

from flask import session, url_for, Markup
import markdown
import unidecode

from os import walk
from random import choice

def randomizer():

  n = choice([0,1])
  if n == 0:
    rand = choice([
      'A2LR33TdLtM', 'PDVWBi-hzzk', 'Vl2sUAtiWxo', '9tU2Dj8zb7I',
      'aDSBW8J08QA', 'DoDw_gOhZto', 'tm54OFKoyhc', 'PDVWBi-hzzk'
    ])
  else:
    rand_dir = '/www/web/static/img/random'
    f = []
    for (dirpath, dirnames, filenames) in walk(rand_dir):
        f.extend(filenames)
        break
    rand = choice(f)

  return (n, rand)

_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')


def slugify(text, delim=u'-'):
    """Generates an slightly worse ASCII-only slug.
    Taken from the Flask Snippets page.

   :param text: The text which should be slugified
   :param delim: Default "-". The delimeter for whitespace
    """
    text = unidecode.unidecode(text)
    result = []
    for word in _punct_re.split(text.lower()):
        if word:
            result.append(word)
    return text_type(delim.join(result))


def render_template(template, **context):  # pragma: no cover
    """A helper function that uses the `render_theme_template` function
    without needing to edit all the views
    """
    if current_user.is_authenticated() and current_user.theme:
        theme = current_user.theme
    else:
        theme = session.get('theme', flaskbb_config['DEFAULT_THEME'])
    return render_theme_template(theme, template, **context)


def crop_title(title, length=None, suffix="..."):
    """Crops the title to a specified length

    :param title: The title that should be cropped

    :param suffix: The suffix which should be appended at the
                   end of the title.
    """
    length = flaskbb_config['TITLE_LENGTH'] if length is None else length

    if len(title) <= length:
        return title

    return title[:length].rsplit(' ', 1)[0] + suffix


def render_markup(text):
    """Renders the given text as markdown

    :param text: The text that should be rendered as markdown
    """
    return Markup(markdown.markdown(text=text, output_format='html5', enable_attributes=False))


def time_diff():
    """Calculates the time difference between now and the ONLINE_LAST_MINUTES
    variable from the configuration.
    """
    now = datetime.utcnow()
    diff = now - timedelta(minutes=flaskbb_config['ONLINE_LAST_MINUTES'])
    return diff


def format_date(value, format='%Y-%m-%d'):
    """Returns a formatted time string

    :param value: The datetime object that should be formatted

    :param format: How the result should look like. A full list of available
                   directives is here: http://goo.gl/gNxMHE
    """
    return value.strftime(format)


def time_since(time):  # pragma: no cover
    """Returns a string representing time since e.g.
    3 days ago, 5 hours ago.

    :param time: A datetime object
    """
    delta = time - datetime.utcnow()

    locale = "en"
    if current_user.is_authenticated() and current_user.language is not None:
        locale = current_user.language

    return format_timedelta(delta, add_direction=True, locale=locale)


def get_image_info(url):
    """Returns the content-type, image size (kb), height and width of a image
    without fully downloading it. It will just download the first 1024 bytes.

    LICENSE: New BSD License (taken from the start page of the repository)
    https://code.google.com/p/bfg-pages/source/browse/trunk/pages/getimageinfo.py
    """
    r = requests.get(url, stream=True)
    image_size = r.headers.get("content-length")
    image_size = float(image_size) / 1000  # in kilobyte

    data = r.raw.read(1024)
    size = len(data)
    height = -1
    width = -1
    content_type = ''

    if size:
        size = int(size)

    # handle GIFs
    if (size >= 10) and data[:6] in (b'GIF87a', b'GIF89a'):
        # Check to see if content_type is correct
        content_type = 'image/gif'
        w, h = struct.unpack(b'<HH', data[6:10])
        width = int(w)
        height = int(h)

    # See PNG 2. Edition spec (http://www.w3.org/TR/PNG/)
    # Bytes 0-7 are below, 4-byte chunk length, then 'IHDR'
    # and finally the 4-byte width, height
    elif ((size >= 24) and data.startswith(b'\211PNG\r\n\032\n') and
            (data[12:16] == b'IHDR')):
        content_type = 'image/png'
        w, h = struct.unpack(b">LL", data[16:24])
        width = int(w)
        height = int(h)

    # Maybe this is for an older PNG version.
    elif (size >= 16) and data.startswith(b'\211PNG\r\n\032\n'):
        # Check to see if we have the right content type
        content_type = 'image/png'
        w, h = struct.unpack(b">LL", data[8:16])
        width = int(w)
        height = int(h)

    # handle JPEGs
    elif (size >= 2) and data.startswith(b'\377\330'):
        content_type = 'image/jpeg'
        jpeg = BytesIO(data)
        jpeg.read(2)
        b = jpeg.read(1)
        try:
            while (b and ord(b) != 0xDA):

                while (ord(b) != 0xFF):
                    b = jpeg.read(1)

                while (ord(b) == 0xFF):
                    b = jpeg.read(1)

                if (ord(b) >= 0xC0 and ord(b) <= 0xC3):
                    jpeg.read(3)
                    h, w = struct.unpack(b">HH", jpeg.read(4))
                    break
                else:
                    jpeg.read(int(struct.unpack(b">H", jpeg.read(2))[0])-2)
                b = jpeg.read(1)
            width = int(w)
            height = int(h)
        except struct.error:
            pass
        except ValueError:
            pass

    return {"content-type": content_type, "size": image_size,
            "width": width, "height": height}


def check_image(url):
    """A little wrapper for the :func:`get_image_info` function.
    If the image doesn't match the ``flaskbb_config`` settings it will
    return a tuple with a the first value is the custom error message and
    the second value ``False`` for not passing the check.
    If the check is successful, it will return ``None`` for the error message
    and ``True`` for the passed check.

    :param url: The image url to be checked.
    """
    img_info = get_image_info(url)
    error = None

    if not img_info["content-type"] in flaskbb_config["AVATAR_TYPES"]:
        error = "Image type is not allowed. Allowed types are: {}".format(
            ", ".join(flaskbb_config["AVATAR_TYPES"])
        )
        return error, False

    if img_info["width"] > flaskbb_config["AVATAR_WIDTH"]:
        error = "Image is too wide! {}px width is allowed.".format(
            flaskbb_config["AVATAR_WIDTH"]
        )
        return error, False

    if img_info["height"] > flaskbb_config["AVATAR_HEIGHT"]:
        error = "Image is too high! {}px height is allowed.".format(
            flaskbb_config["AVATAR_HEIGHT"]
        )
        return error, False

    if img_info["size"] > flaskbb_config["AVATAR_SIZE"]:
        error = "Image is too big! {}kb are allowed.".format(
            flaskbb_config["AVATAR_SIZE"]
        )
        return error, False

    return error, True
