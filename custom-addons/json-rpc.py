import json
import random
import urllib.request

host = 'localhost'
port = 8069
odoo_url = f'http://{host}:8069'

username = 'handsomeguy'
password = 'orangtampan123'
db = 'LearningOdoo'


def json_rpc(url, method, params):
    data = {
        'jsonrpc': '2.0',
        'method': method,
        'params': params,
        'id': random.randint(0, 1_000_000_000)
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    request = urllib.request.Request(url, data=json.dumps(data).encode(), headers=headers)
    response = json.loads(urllib.request.urlopen(request).read().decode("UTF-8"))

    if response.get('error'):
        raise Exception(response['error'])
    return response['result']


def call(url, service, method, *args):
    return json_rpc(f'{url}/jsonrpc', 'call', {'service': service, 'method': method, 'args': args})


user_id = call(odoo_url, 'common', 'login', db, username, password)
print(user_id)

vals = {
    'name': "Property from JSON-RPC",
    'sales_id': 6  # to Marc Demo
}

# property_create = call(odoo_url, 'object', 'execute', db, user_id, password,
#                        'estate.property', 'create', vals)
# print("create function ==> ", property_create)

property_read = call(odoo_url, 'object', 'execute', db, user_id, password,
                     'estate.property', 'read', [19])
print("read function ==>",property_read)