from unittest import TestCase
import requests
import requests_mock

from resello.models import ReselloResponse


class BasicResponseTestCase(TestCase):
    """
    Tests response functionality.
    """

    response_ok = {
        "total": 0,
        "limit": 100,
        "result": [
            {"id": 12, "name": "Test 1"},
            {"id": 15, "name": "Test 2"},
        ],
        "success": True,
        "offset": 0
    }
    response_error = {
        "success": False,
        "error": {
            "message": {
                "contacts": {
                    "contact": [
                        {
                            "message": "error message.",
                            "code": "invalid_choice"
                        }
                    ]
                }
            },
            "code": "request_validation_failed"
        }
    }

    @requests_mock.mock()
    def test_successful_response_result_is_filled(self, request_mock):
        """
        Test if successful response.result contains all data.
        """
        request_mock.get('mock://test/', json=self.response_ok)

        response = ReselloResponse(requests.get('mock://test/'))

        self.assertEqual(self.response_ok['result'], response.result)

    @requests_mock.mock()
    def test_successful_response_is_iterator(self, request_mock):
        """
        Test if it is possible to iterate over successful response.
        """
        request_mock.get('mock://test/', json=self.response_ok)

        response = ReselloResponse(requests.get('mock://test/'))

        for index, item in enumerate(response):
            self.assertIn(item, self.response_ok['result'])
        self.assertEqual(1, index)

    @requests_mock.mock()
    def test_successful_response_can_be_counted(self, request_mock):
        """
        Test if it is possible to get count from successful response.
        """
        request_mock.get('mock://test/', json=self.response_ok)

        response = ReselloResponse(requests.get('mock://test/'))

        self.assertEqual(2, len(response))

    @requests_mock.mock()
    def test_successful_response_has_no_errorrs(self, request_mock):
        """
        Test if successful response has no errors.
        """
        request_mock.get('mock://test/', json=self.response_ok)

        response = ReselloResponse(requests.get('mock://test/'))

        self.assertFalse(response.has_errors)

    @requests_mock.mock()
    def test_successful_response_cmp_true_is_true(self, request_mock):
        """
        Test if successful response copmares to True as True.
        """
        request_mock.get('mock://test/', json=self.response_ok)

        response = ReselloResponse(requests.get('mock://test/'))

        self.assertTrue(response)

    @requests_mock.mock()
    def test_successful_response_cmp_none_is_false(self, request_mock):
        """
        Test if successful response copmares to None as False.
        """
        request_mock.get('mock://test/', json=self.response_ok)

        response = ReselloResponse(requests.get('mock://test/'))

        self.assertFalse(response is None)

    @requests_mock.mock()
    def test_error_in_response_and_response_errors_filled(self, request_mock):
        """
        Test if error in response means response.has_errors is True
         and response.errors contain error.
        """
        request_mock.get('mock://test/', json=self.response_error)

        response = ReselloResponse(requests.get('mock://test/'))

        self.assertTrue(response.has_errors)

        self.assertEqual(self.response_error['error'], response.errors)

    @requests_mock.mock()
    def test_error_in_response_cmp_true_is_false(self, request_mock):
        """
        Test if error in response compares to None as True.
        """
        request_mock.get('mock://test/', json=self.response_error)

        response = ReselloResponse(requests.get('mock://test/'))

        self.assertFalse(response)
