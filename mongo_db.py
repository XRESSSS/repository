import pymongo
# from bson import Decimal128

from config_mongo import USER, PASSWORD

url = (f'mongodb+srv://{USER}:{PASSWORD}'
       '@cluster0.yuvicuz.mongodb.net/?retryWrites=true&w=majority')
client = pymongo.MongoClient(url)

db = client.testDB
mops_coll = db.mops
vacuum_cleaners_coll = db.vacuum_cleaners

# add single document ################
# mops_coll.insert_one(
#        {'title': 'Super mop', 'price': 15}
# )
#
# vacuum_cleaners_coll.insert_one(
#        {'title': 'Vacuum cleaner', 'price': 150,
#         'power': 2000}
# )

# mops_coll.insert_one(
#        {'_id': 2, 'title': 'Super mop', 'price': 15}
# )
# add many document ################

# mops = [
#        {'_id': 3, 'title': 'Super mop3', 'price': 18},
#        {'_id': 4, 'title': 'Super mop4', 'price': 22, 'power': 'v'}
# ]
# mops_coll.insert_many(mops)
# GET DATA ******&&&&&&&&&&&&&&&&****************************
# first
# result = mops_coll.find_one(
#        {'price': 22}
# )
# print(result)
# all data
# result = mops_coll.find()
# for doc in result:
#     print(doc)
# looking for the specific field
# query = {'price': 18}
# query = {'price': {'$gt': 15}}
# query = {'price': {'$lt': 15}}
# query = {'price': {'$gte': 15}}
# result = mops_coll.find(query)
# for doc in result:
#     print(doc)

# UPDATE
#  use &set
# current = {}
# new_data = {'$set': {'warranty': 3}}
# data = mops_coll.update_many(current, new_data)
# print(data.raw_result)


# multiplication
# query = {}
# # operation = {'$mul': {'price': 1.1}} # bed idea
# operation = {'$mul': {'price': Decimal128(str(1.1))}}  # nor idea
# data = mops_coll.update_many(query, operation)
# print(data.raw_result)

# increase
# query = {'price': {'$lt': 619}}
# operation = {'$inc': {'warranty': -1, 'price': 300}}
# data = mops_coll.update_many(query, operation)
# print(data.raw_result)


# # DELETE
# query = {'price': {'$lt': 618}}
# operation = {'$unset': {'warranty': 1}}
# data = mops_coll.delete_one(query)
# print(data.raw_result)

# query = {}
# data = mops_coll.delete_many(query)
# print(data.deleted_count)

# mops_coll.drop()
# vacuum_cleaners_coll.drop()
# db.drop_database('testDB')

