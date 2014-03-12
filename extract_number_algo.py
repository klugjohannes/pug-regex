#!/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import string


def extract_data(data):
    u"""
    >>> testdata = u'''Max Muster  01235/9123647
    ... Eva Birne   034734/9349324
    ... Adam Apfel  +41(2352)3749237
    ... Otto Graf von Grünensfeld  +49(3249)334800
    ... '''
    >>> extract_data(testdata)
    01235/9123647
    034734/9349324
    +41(2352)3749237
    +49(3249)334800
    """
    data = data.splitlines()

    for dataset in data:
        for index, char in enumerate(dataset):
            if char in (string.digits + '+'):
                print(dataset[index:].strip())
                break


if __name__ == '__main__':
    import doctest
    doctest.testmod()
