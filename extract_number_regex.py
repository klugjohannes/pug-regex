#!/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import re


def extract_data(data):
    u"""
    >>> testdata = u'''Max Muster  01235/9123647
    ... Eva Birne   034734/9349324
    ... Adam Apfel  +41(2352)3749237
    ... Otto Graf von Grünensfeld  +49(3249)334800
    ... '''
    >>> extract_data(testdata)
    (u'Max Muster', u'01235/9123647')
    (u'Eva Birne', u'034734/9349324')
    (u'Adam Apfel', u'+41(2352)3749237')
    (u'Otto Graf von Grünensfeld', u'+49(3249)334800')
    """
    data = data.splitlines()

    pattern = re.compile(r'(\d*)', re.UNICODE)

    for dataset in data:
        m = pattern.search(dataset)
        if m:
            print(m.groups())


if __name__ == '__main__':
    import doctest
    doctest.testmod()
