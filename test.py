import requests
from requests_negotiate_sspi import HttpNegotiateAuth

_nego_auth = HttpNegotiateAuth()
r = requests.get('https://ishareteam4.na.xom.com/sites/Fusion/', verify=False, auth=_nego_auth)

print(_nego_auth._auth_token_info.scheme)
print(_nego_auth._auth_token_info.token)