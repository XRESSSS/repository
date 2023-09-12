from typing import Callable
import functools


# print(print)
# print(id(print))
# print(type(print))
#
# print('*' * 50)
# not_print = print
# print(not_print)
# print(id(not_print))
#
# not_print(66666)

# def foo(foo_argument='Ale Ale'):
#     '''I print many 5-s'''
#     print('key 65765765')
#     print(f'from {foo_argument=}')

# print(foo)
#
# foo.age = 5
# print(foo.age)
#
# print(foo.__dict__)
# print(foo.__name__)
# print(foo.__doc__)
# foo()

# def func_eater(another_function: Callable):
#     another_function()
#
# func_eater(foo)
#
# ff = 'ggggggg'
# n = 9786


# print(add_log(foo))
# add_log(foo) ('ddddddddd')
# foo = decorate_as_float(foo)
# print(foo, 99999999)
# foo('chill')


def decorate_as_float(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # print(args)
        # print(*args)
        # print(kwargs)
        result = func(*args, **kwargs)
        result = float(result)
        return result
    # wrapper.__dict__ = func.__dict__
    # wrapper.__name__ = func.__name__
    # wrapper.__doc__ = func.__doc__
    return wrapper

def auth(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        name = input('Enter ur name:')
        password = input('Enter ur password:')
        if name == 'admin' and password == '1234':
            result = func(*args, **kwargs)
            return result
        print('Access not allowed')

    return wrapper

@auth
@decorate_as_float
def mul_two_args(value1: int, value2: int) -> int:
    return value1 * value2


@decorate_as_float
def convert_to_int(value: str) -> int:
    if value.isdigit():
        return int(value)
    return 0

res = mul_two_args(5, value2 = 2)
print(res)

res2 = convert_to_int('fdskjlh')
print(res2)


res3 = mul_two_args(5, value2 = 4)
print(res3)

print(convert_to_int.__doc__)
