from collections import defaultdict


class ReselloResponse(object):
    """
    The :class:`Response <Response>` object, which contains a
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
