from .generic import GenericManager

from .domain_contacts import DomainContactsManager
from .domain_price_list import DomainPriceListManager


class DomainManager(GenericManager):
    app_prefix = '/domain'

    def add_submanagers(self):
        self.contacts = DomainContactsManager(self.api)
        self.price_lists = DomainPriceListManager(self.api)

    def tld(self, tld_name):
        return self.get('-tld/{}'.format(tld_name))

    def all(self):
        return self.get('?embed=tld,reseller,contacts,hosts,redirects')

    def details(self, uuid):
        return self.get('/{}?extended=1&embed=tld,reseller,contacts,hosts,redirects'.format(uuid))

    def update(self, uuid, payload):
        return self.put('/{}'.format(uuid), payload)

    def create_domain(self, name, contacts, reference=None):
        payload = {
            'name': name,
            'contacts': contacts,
            'is_managed': True
        }
        if reference is not None:
            payload['client_reference'] = reference
        return self.post(path='', payload=payload)

