import requests

headers = {'host': 'api.linnworks.net', 'connection': 'keep-alive', 'accept': 'application/json, text/javascript, */*; q=0.01',
           'origin': 'https://linnworks.net', 'accept-language': 'en', 'user-agent': 'Chrome/42.0.2311.90',
           'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'referer': 'https://www.linnworks.net',
           'accept-encoding': 'gzip, deflate'}
payload = {'applicationId': '6c6edc81-5372-4309-bc72-aea610367d62', 'applicationSecret': 'b9c21192-f035-4d77-b967-4936cbcf5fc1'}

r = requests.post('https://api.linnworks.net//api/Auth/AuthorizeByApplication', headers=headers, params=payload)

print r.text
