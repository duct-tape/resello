import mock
import requests_mock
from unittest import TestCase

from resello import ReselloClient
from resello.managers.domain import DomainManager


class ReselloDomainManagerTestCase(TestCase):
    def setUp(self):
        self.client = ReselloClient(api_key='test', reseller_reference='test')
        self.client.BASE_PATH = 'mock://test'

    def test_if_domain_contacts_submanager_initiated(self):
        """
        DomainManager should have contacts submanager.
        """
        from resello.managers.domain_contacts import DomainContactsManager

        manager = DomainManager(mock.MagicMock())

        self.assertIsInstance(manager.contacts, DomainContactsManager)

    @requests_mock.mock()
    def test_if_tld_details_can_be_fetched(self, request_mock):
        """
        Domain manager can retrieve TLD details for any supported TLD.
        """
        expected_api_response = {'success': 'true', 'result': {'name': 'com'}}
        request_mock.get('mock://test/domain-tld/com',
                         json=expected_api_response)
        response = self.client.domain.tld(tld_name='com')

        self.assertEqual('com', response.name)
