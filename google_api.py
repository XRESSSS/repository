import sys

import requests
import inspect

url = 'https://script.google.com/macros/s/AKfycbzZ7ofoaQy2pbc7u-IjT71TxscX2GUd5iv7H4EVbXIR6ml32HsBVcG5AXTRPk1rleqGXw/exec'

data = requests.get(url)

data_dict = data.json()

money = 0

names = []
# for person in data_dict['trip']:
#     if person['money']:
#         print(f'{person["name"]} -->> {person["money"]}')
#         money += person['money']
#
#     names.append(person["name"])
#
# print(money)

# money = [person["money"] for person in data_dict['trip']]
# money = sum([person["money"] for person in data_dict['trip'] if person['money']])
# print(money)
#
# names = {person for person in data_dict['trip']}
# print(names)
#
# names = [person for person in data_dict['trip']]
# print(names)
#
# names = {person["name"]: person for person in data_dict['trip']}
# print(names)

names = (person for person in data_dict['trip'])
print(names)
print(sys.getsizeof(names))


names = [person for person in data_dict['trip']]
print(names)
print(sys.getsizeof(names))
