import requests, json, time

headers = {'host': 'api.linnworks.net', 'connection': 'keep-alive', 'accept': 'application/json, text/javascript, */*; q=0.01',
           'origin': 'https://linnworks.net', 'accept-language': 'en', 'user-agent': 'Chrome/42.0.2311.90',
           'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'referer': 'https://www.linnworks.net',
           'accept-encoding': 'gzip, deflate'}
payload = {'applicationId': '6c6edc81-5372-4309-bc72-aea610367d62', 'applicationSecret': 'b9c21192-f035-4d77-b967-4936cbcf5fc1',
           'token': 'ea37bff91d18d697849d045d31a4dd42'}

r = requests.post('https://api.linnworks.net//api/Auth/AuthorizeByApplication', headers=headers, params=payload)

# print json.dumps(r.json(), indent=4)
json_loads = json.loads(json.dumps(r.json()))  # json_loads is type dict

auth_token = json_loads["Token"]
print auth_token

item_price = requests.post('https://ext.linnworks.net//api/Inventory/GetInventoryItemPrices', headers={'Authorization': auth_token},
                           params={'inventoryItemId': '81a58e95-35ec-4402-99bd-8cae59e8c9d9'})

print json.dumps(item_price.json(), indent=4)

stock_item = {
        "Tag": 'null',
        "Source": "EBAY",
        "Price": 8.50,
        "SubSource": "EBAY0_US",
        "pkRowId": "e2065041-b0d5-4173-becf-fb5b99288bb9",
        "StockItemId": "81a58e95-35ec-4402-99bd-8cae59e8c9d9"
    }

#This uses the /Inventory/UpdateInventoryItemPrices to update prices for each SubSource
update_price = requests.post('https://ext.linnworks.net//api/Inventory/UpdateInventoryItemPrices',
              headers={'Authorization': auth_token},
              params={'inventoryItemPrices': "[{'Source': 'EBAY','Price': 15.50,'SubSource': 'EBAY0_US','StockItemId': '81a58e95-35ec-4402-99bd-8cae59e8c9d9'}]"})

update_retail_price = requests.post('https://ext.linnworks.net//api/Inventory/UpdateInventoryItem',
              headers={'Authorization': auth_token},
              params={'inventoryItem': "{'RetailPrice': 15.50,'StockItemId': '81a58e95-35ec-4402-99bd-8cae59e8c9d9', 'ItemTitle': 'TEST ITEM DO NO BID / BUY', 'ItemNumber': 'TEST'}"})

# print update_price.text
# print update_retail_price.text


def get_imports(token):
    import_list = requests.post('https://ext.linnworks.net//api/ImportExport/GetImports',
                                headers={'Authorization': token})
    print json.dumps(import_list.json(), indent=4)

get_imports(auth_token)


def run_import_now(token):
    run_import = requests.post('https://ext.linnworks.net//api/ImportExport/RunNowImport',
                               headers={'Authorization': token},
                               params={'importId': 26})


#run_import_now(auth_token)
