from unittest import TestCase


class BasicImportsTestCase(TestCase):
    def test_if_resello_client_can_be_imported_from_top_level(self):
        """
        Library API docs say:
        >>> import resello
        >>> client = resello.ReselloClient(reference='...', api_key='...')

        This should be true.
        """
        import resello

        self.assertIn('ReselloClient', dir(resello))
