import requests

from settings import cache


FACEBOOK_API = 'https://graph.facebook.com/%s'

def get_access_token():
    access_token = cache.get('facebook_access_token')
    if access_token:
        return access_token

    client_id = cache.get('facebook_client_id')
    client_secret = cache.get('facebook_client_secret')
    url = FACEBOOK_API % 'oauth/access_token'
    try:
        r = requests.get(url, params={
            'client_id': client_id,
            'client_secret': client_secret,
            'grant_type': 'client_credentials'})
        access_token = r.content.split('=')[1]
        cache.set('facebook_access_token', access_token)
        return access_token
    except:
        raise

def facebook_request(facebook_id):
    access_token = get_access_token()
    url = FACEBOOK_API % facebook_id
    try:
        return requests.get(url, params={'access_token': access_token})
    except:
        raise
