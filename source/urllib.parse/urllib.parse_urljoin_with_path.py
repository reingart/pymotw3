#!/usr/bin/env python3
"""Joining fragments into absolute URLs
"""
#end_pymotw_header

from urlparse import urljoin

print urljoin('http://www.example.com/path/',
              '/subpath/file.html')
print urljoin('http://www.example.com/path/',
              'subpath/file.html')
