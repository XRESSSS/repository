# data =[5, 6]
# set_data = {item for item in data}
# print(set_data)
#
# list_data = {item * 2 for item in data}
# print(list_data)
#
# dict_data = {item: item for item in data}
# print(dict_data)
#
# generator_data = (item for item in data)
# print(generator_data)


def our_generator():
    print(11111111)
    yield 55
    print(22222222)
    yield 58
    print(33333333)


generator_obj = our_generator()

print(next(generator_obj))
print(999999)
print(next(generator_obj))
