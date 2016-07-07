# -*- coding: utf-8 -*-

"""
Resello REST API Client
~~~~~~~~~~~~~~~~~~~~~~~

Resello Reseller API Client written in Python.

Basic Usage:

    >>> import resello
    >>> client = resello.ReselloClient(reference='...', api_key='...')
    >>> response = client.domain.all()
    >>> response.status
    True
    >>> response.result
    [
        {
            'id': '32a4-....',
        }
    ]
"""

__title__ = 'resello'
__version__ = '0.0.1'
__build__ = 0x021000
__author__ = 'Nick Garanko'
__license__ = 'BSD 3.0'
__copyright__ = 'Copyright 2016 Nick Garanko'

from .api import ReselloClient
