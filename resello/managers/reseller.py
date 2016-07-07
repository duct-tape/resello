from .generic import GenericManager


class ResellerManager(GenericManager):
    app_prefix = '/reseller'

    def product_configuration(self):
        return self.api.get(app_prefix='/product-reseller-configuration', path='')

    def create_reseller(self, name):
        return self.post(path='', payload={
            'name': name,
            'currency': 'EUR',
            'country': 'NL'
        })
