from collections import defaultdict


class ReselloResponse(object):
    """
    The :class:`Response <Response>` object, contains a
    server's response to an HTTP request.
    """

    __attrs__ = [
        '_content',
        'status_code',
        'headers',
        'url',
        'history',
        'encoding',
        'reason',
        'cookies',
        'elapsed',
        'request',
        'status',
        'result',
        'has_errors',
        'errors'
    ]

    def __init__(self, response):
        self._response = response

        self.errors = defaultdict(list)

    def __getattr__(self, name):
        return self.result[name]

    def __repr__(self):
        return repr(self.result)

    def __nonzero__(self):
        return not self.has_errors

    def __len__(self):
        if self.has_errors:
            return 0

        return len(self.result)

    def __getitem__(self, index):
        return self.result[index]

    def __cmp__(self, other):
        if other is None or other is False:
            return self.has_errors
        return False

    @property
    def status_code(self):
        return self._response.status_code

    @property
    def status(self):
        try:
            return self._response.json()['status'] == 'success'
        except ValueError:
            return False

    @property
    def has_errors(self):
        """
        Checks if response contains errors
        """

        try:
            response = self._response.json()

        except ValueError:
            self.errors = {
                'code': 'json parse failed',
                'message': 'Can not decode JSON response.'
            }
            return True
        else:
            if not response['success']:
                self.errors = response['error']
                return True
        return False

    @property
    def result(self):
        if self.has_errors:
            return None

        try:
            return self._response.json()['result']
        except (ValueError, KeyError):
            return None
