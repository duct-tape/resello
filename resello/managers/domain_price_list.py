from .generic import GenericManager


class DomainPriceListManager(GenericManager):
    app_prefix = '/domain-price-list'

    def all(self):
        return self.get(path='')

    def details(self, uuid):
        return self.get('/{}?embed=tlds'.format(uuid))
