import requests
from .api_client import API_KEY,SECRET_KEY


url = 'https://aip.baidubce.com/oauth/2.0/token?'
payload = {
    'grant_type':'client_credentials',
    'client_id':API_KEY,
    'client_secret':SECRET_KEY
}
response = requests.post(url,data=payload)
if response:
    access_token = response.json()['access_token']
else:
    print('错误')