# Newsman Python API Client - version 1.2

This is the Newsman App Python API client for API version 1.2.

## Newsman - Smart Email Service Provider

[Newsman](http://www.newsmanapp.com "Smart Email Service Provider") is a Smart Email Service Provider. 
We send newsletters on behalf of our customers.

## About Newsman API - version 1.2

Our current API version is 1.2. API documentation can be found here:

* RO: http://kb.newsman.ro/api/
* EN: http://kb.newsmanapp.com/api/
* FR: http://kb.newsman.fr/api/
 
Our API requires an API KEY which you can generate in your Account and your Newsman user id.
The API exposes XML RPC and REST interfaces.

This Python Client will use only xmlrpclib python module.

### Install

```bash
easy_install https://github.com/Newsman/newsman-api-python/zipball/master
```

### Example Code

```python
import newsman

# you can get your api_key and user_id from My Account -> API
client = newsman.Newsman(user_id, api_key)
print client.API_VERSION
print client.list.all()
```