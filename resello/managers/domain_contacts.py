from .generic import GenericManager


class DomainContactsManager(GenericManager):
    app_prefix = '/domain-contact'

    def all(self):
        return self.get('')
