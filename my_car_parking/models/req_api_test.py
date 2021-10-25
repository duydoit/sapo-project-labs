import xmlrpc.client
from operator import itemgetter

url = "http://192.168.25.73:8088"
db = "myodoo"
username = 'admin'
password = 'admin'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
common.version()

uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# Call list
cars_ids = models.execute_kw(db, uid, password, 'car.cars', 'search', [[['door_number', '!=', -1]]], {'limit': 20})
print("List Ids Car ...", cars_ids)

# Read cars list
cars_list = models.execute_kw(db, uid, password, 'car.cars', 'read', [cars_ids],
                              {'fields': ['name', 'door_number', 'horse_power']})

horse_max = 0
for cars in cars_list:
    if cars['horse_power'] > horse_max:
        horse_max = cars['horse_power']
print("Horse max ...", horse_max)

print("Three Horse max :")
# Lọc ra 3 car có house_pow cao nhất
new_list = sorted(cars_list, key=itemgetter('horse_power'), reverse=True)
num_check = 0
for cars in new_list:
    if num_check == 3:
        break
    print(cars)
    num_check += 1

