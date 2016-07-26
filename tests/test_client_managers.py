from unittest import TestCase

from resello import ReselloClient


class ReselloClientManagersTestCase(TestCase):
    def test_if_reseller_manager_initiated(self):
        """
        ReselloClient should have .reseller = ResellerManager instance.
        """
        from resello.managers.reseller import ResellerManager
        client = ReselloClient(api_key='test', reseller_reference='test')

        self.assertIsInstance(client.reseller, ResellerManager)

    def test_if_domain_manager_initiated(self):
        """
        ReselloClient should have .domain = DomainManager instance.
        """
        from resello.managers.domain import DomainManager
        client = ReselloClient(api_key='test', reseller_reference='test')

        self.assertIsInstance(client.domain, DomainManager)

    def test_if_vps_manager_initiated(self):
        """
        ReselloClient should have .vps = VPSManager instance.
        """
        from resello.managers.vps import VPSManager
        client = ReselloClient(api_key='test', reseller_reference='test')

        self.assertIsInstance(client.vps, VPSManager)
