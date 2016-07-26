[![Build Status](https://travis-ci.org/duct-tape/resello.svg?branch=master)](https://travis-ci.org/duct-tape/resello) [![Stories in Ready](https://badge.waffle.io/duct-tape/resello.png?label=ready&title=Ready)](https://waffle.io/duct-tape/resello)
# resello

Resello Reseller API Client written in Python.

Basic Usage:

```python
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
```
