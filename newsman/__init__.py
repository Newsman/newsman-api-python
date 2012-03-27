from xmlrpclib import ServerProxy

__all__ = ["Newsman"]

class Newsman:
    API_VERSION = "1.2"
    
    """
    Creates a Newsman Client.
    """
    def __init__(self, user_id, api_key, use_ssl = True):
        self.user_id = user_id
        self.api_key = api_key
        self.use_ssl = use_ssl
        
        self.proxy = self.getProxy()
        
    """
    Returns a xmlrpclib ServerProxy preconfigured for this API version, user id and api key.
    """
    def getProxy(self):
        if self.use_ssl:
            api_url = "https://ssl.newsman.ro/api"
        else:
            api_url = "http://api.newsman.ro/api"
        
        api_url = "%s/%s/xmlrpc/%s/%s" % (api_url, Newsman.API_VERSION, self.user_id, self.api_key)
        
        return ServerProxy(api_url)
    
    def __getattr__(self, name):
        return getattr(self.proxy, name)