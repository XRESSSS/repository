import functools
import datetime
from pprint import pprint

# file = open('my.txt', mode='w')
# file.write('jihasdjih')
# file.close()
# '-5 ballow za etot staffchik'

# with open('my.txt', mode='a', encoding='utf-8') as file:
#     file.write('dasd')
#     print(file)


def logger(file_name='log_data1.txt'):
    def wrapper1(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(file_name, mode='a', encoding='utf-8') as file:
                file.write(f'{datetime.datetime.now()};{func.__name__};{result}\n')
            return result
        return wrapper
    return wrapper1

@logger()
def foo(arg):
    return arg * 2
foo(6)

@logger()
def foo2(arg):
    return arg * 2
foo(6)

with open('log_data.txt', mode='r', encoding='utf-8') as file:
    # print(file.read())
    # print(file.readline())
    # print(file.readline())
    # print(file.readlines())
    for line in file.readlines():
        data = line.split(';')

        if data[1] == 'foo2':
            print(data[0])
