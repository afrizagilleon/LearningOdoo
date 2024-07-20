import xmlrpc.client

host = 'localhost'
port = 8069
url = f'http://{host}:8069'

username = 'handsomeguy'
password = 'orangtampan123'
db = 'LearningOdoo'

common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
print(common.version())
# output : {'server_version': '17.0', 'server_version_info': [17, 0, 0, 'final', 0, ''], 'server_serie': '17.0',
# 'protocol_version': 1}

user_id = common.authenticate(db, username, password, {})
print(user_id)

models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

# search function
property_ids = models.execute_kw(db, user_id, password, 'estate.property', 'search', [[]])
print('search function ==>', property_ids)

# count function
property_count = models.execute_kw(db, user_id, password, 'estate.property', 'search_count', [[]])
print('count function ==>', property_count)

# read function
property_read = models.execute_kw(db, user_id, password, 'estate.property', 'read', [property_ids],
                                  {'fields': ['name']})
print('read function ==>', property_read)

# search & read function
property_search_read = models.execute_kw(db, user_id, password, 'estate.property', 'search_read', [[]],
                                  {'fields': ['name']})
print('search + read function ==>', property_search_read)

# create function
# create_property_id = models.execute_kw(db, user_id, password, 'estate.property', 'create', [
#     {
#         'name': f'Property Created from RPC {property_count}',
#         'sales_id': user_id
#     }
# ])
# print('create function ==>', create_property_id)

# write function
# write_property_id = models.execute_kw(db, user_id, password, 'estate.property', 'write', [18,{
#     'name': 'Edited from RPC'
# }])
# read_name_get = models.execute_kw(db, user_id, password, 'estate.property', 'name_get', [[18]])
# print('update function ==>', write_property_id)
# print('updated name_get ==>', read_name_get)

# unlink function
# property_unlink = models.execute_kw(db, user_id, password, 'estate.property', 'unlink', [[18]])
# print('unlink function ==>', property_unlink)

# paginate function
property_paginate = models.execute_kw(db, user_id, password, 'estate.property', 'search', [[]], {
    'offset': 0,
    'limit': 1,
})
print('paginate function ==>', property_paginate)