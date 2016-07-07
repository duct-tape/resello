class GenericManager(object):
    """
    Generic manager class.
    
    Managers are abstraction proxies meant to 
    simplify and structurize client interface.
    """

    def __init__(self, api):
        self.api = api

        self.add_submanagers()

    def add_submanagers(self):
        """
        Register sub managers here.
        """
        pass

    def get(self, path):
        return self.api.get(self.app_prefix, path)

    def post(self, path, payload):
        return self.api.post(self.app_prefix, path, payload)

    def put(self, path, payload):
        return self.api.put(self.app_prefix, path, payload)

    def delete(self, path):
        return self.api.delete(self.app_prefix, path)
