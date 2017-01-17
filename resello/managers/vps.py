from .generic import GenericManager


class VPSManager(GenericManager):
    app_prefix = '/vps-'

    def instances(self):
        """
        Get list of available VPS instances
        """
        return self.get('instance')

    def create_instance(self, instance_details):
        """
        Creates VPS instance via API.
        """
        result = self.post('instance', instance_details)

        return result

    def start_instance(self, instance_id):
        """
        Starts instance via API.
        """
        result = self.post('instance/{}/command'.format(instance_id),
                           {'type': 'start'})

        return result['success']

    def stop_instance(self, instance_id):
        """
        Stops instance via API.
        """
        result = self.post('instance/{}/command'.format(instance_id),
                           {'type': 'stop'})

        return result['success']

    def delete_instance(self, instance_id):
        """
        Deletes instance via API.
        """
        result = self.delete('instance/{}'.format(instance_id))

        return result

    def get_access_url(self, instance_id):
        """
        Fetches VNC access url.
        """
        return self.post('instance/{}/access'.format(instance_id), {})

    def details(self, instance_id):
        """
        Fetch instance details
        """
        return self.get('instance/{id}'.format(id=instance_id))

    def control_panel(self, instance_id):
        """
        Fetch instance control panel url
        """
        return self.get('instance/{id}/control-panel'.format(id=instance_id))

    def images(self):
        """
        Fetch list of available images.
        """
        return self.get('image')

    def tiers(self):
        """
        Fetch list of available tiers.
        """
        return self.get('tier')

    def price_lists(self):
        """
        Fetch list of available tiers.
        """
        return self.get('price-list')

    def price_indications(self):
        """
        Fetch list of available prices.
        """
        return self.get('price-indication')
