#!/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from sliderepl import Deck

Deck.run()

### slide::

# the python regex module is available as re
import re

# it provides three (four) essential functions: search, match, findall
# (finditer)

# * search tries to match anywhere in the string
print re.search.__doc__

# * match tries to match at the beginning of the string
print re.match.__doc__

# * findall (finditer) returns a list (iterator) of all matches in the string
print re.findall.__doc__
print re.finditer.__doc__

### slide::

# search and match will return match objects or None

# * search
m = re.search(r'(bar)', 'foobar')
m.groups()

# * match
m = re.match(r'(bar)', 'foobar')
m is None

### slide::

# a little oddity with findall and finditer

# * findall return a tuple containing all matched groups
re.findall(r'(foo)(bar)', 'foobar')

# * finditer returns a match object
list(re.finditer(r'(foo)(bar)', 'foobar'))

### slide::

# other interesting functions in re

# * splitting a string
re.split(r'[,.!?]',
         'Hello World! How are you?'
         'This is a sample text, however nonsensical.')

# * replace a part of a string
re.sub('bar', 'baz', 'foobar')

### slide::

# compiling regex for repeated use
pattern = re.compile(r'(bar)')
pattern


# *the pattern object has the same functions that can be found in the re module
pattern.search('foobar')

# * compiling is useful if you use a lot of different regexes in your code,
#   the re module keeps a cache of up to 100 regular expressions
dict(list(re._cache)[:10])


### slide::

# now for some example regexs

# * two adolescent regex meet, says one to the other:
#   .*  (whatever)
re.search(r'(.*)',
          'any gibberish you might think of... !"!^"£&*!"&()').groups()

# non-trivial examples
# * [a-zA-Z], words with ascii letters, no Umlauts
re.findall(r'([a-zA-Z]+)', 'words with ascii letters, no Umlauts')

# * ma*x matches mx, max, maax, maaax, ...
re.search('(ma*x)', 'max').groups()

# * m(a|i)x matches mix and max
re.search('(m(i|a)x)', 'mix').groups()
re.search('(m(i|a)x)', 'max').groups()

# * m(?!au).*x does NOT match maux
re.search('m(?!au).*x', 'maux') is None

# * [\w_-]@[\w-]\.[a-zA-Z]{2,3} email adresses
re.search(r'([\w_-]+@[\w-]+.[a-zA-Z]{2,3})', 'mail_bar@host-foo1.de').groups()

### slide:: end
