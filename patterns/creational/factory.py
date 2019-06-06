#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""*What is this pattern about?
A Factory is an object for creating other objects.

*What does this example do?
The code shows a way to localize words in two languages: English and
Chinese. "get_localizer" is the factory function that constructs a
localizer depending on the language chosen. The localizer object will
be an instance from a different class according to the language
localized. However, the main code does not have to worry about which
localizer will be instantiated, since the method "localize" will be called
in the same way independently of the language.

*Where can the pattern be used practically?
The Factory Method can be seen in the popular web framework Django:
http://django.wikispaces.asu.edu/*NEW*+Django+Design+Patterns For
example, in a contact form of a web page, the subject and the message
fields are created using the same form factory (CharField()), even
though they have different implementations according to their
purposes.

*References:
http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/

*TL;DR
Creates objects without having to specify the exact class.
"""

from __future__ import unicode_literals
from __future__ import print_function


class ChineseLocalizer(object):
    """A simple chinese localizer"""

    def localize(self, msg):
        return print('The message is translated to chinese.\n', msg)


class EnglishLocalizer(object):
    """A simple english localizer"""

    def localize(self, msg):
        return print('The message is translated to english.\n', msg)


def get_localizer(language="English"):
    """Factory"""
    localizers = {
        "English": EnglishLocalizer,
        "Chinese": ChineseLocalizer,
    }
    return localizers[language]()


def main():
    elocalizer = get_localizer(language="English")
    zlocalizer = get_localizer(language="Chinese")

    elocalizer.localize('Please localize to English.')
    zlocalizer.localize('Please localize to Chinese.')

if __name__ == "__main__":
    main()
