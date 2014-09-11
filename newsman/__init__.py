import sys

if sys.version_info < (3, 0, 0):
    from xmlrpclib import ServerProxy
else:
    from xmlrpc.client import ServerProxy

__all__ = ["Newsman"]

class Newsman:
    API_VERSION = "1.2"
    
    """
    Creates a Newsman Client.
    """
    def __init__(self, user_id, api_key, api_url = "https://ssl.newsman.ro/api"):
        self.user_id = user_id
        self.api_key = api_key
        self.api_url = api_url
        
        self.proxy = self.getProxy()
        
    """
    Returns a xmlrpclib ServerProxy preconfigured for this API version, user id and api key.
    """
    def getProxy(self):
        api_url = "%s/%s/xmlrpc/%s/%s" % (self.api_url, Newsman.API_VERSION, self.user_id, self.api_key)
        
        return ServerProxy(api_url, allow_none = True)
    
    def __getattr__(self, name):
        return getattr(self.proxy, name)
