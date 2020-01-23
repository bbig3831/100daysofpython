from functools import wraps
import time

def mydecorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return result
    return wrapper


@mydecorator
def my_function(args):
    pass


# def get_profile(name, active=True, *sports, **awards):
#     print('Positional arguments (required): ', name)
#     print(f'Keyword arguments (not required, default values): {active}')
#     print(f'Arbitrary argument list (sports): {sports}')
#     print(f'Arbitrary keyword argument dictionary (awards): {awards}')
#
# get_profile('julian')
# get_profile('julian', active=False)
# get_profile('julian', False, 'basketball', 'soccer')
# get_profile('julian', False, 'basketball', 'soccer',
#             pythonista='special honor of the community')

def show_args(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f'hi from decorator - args: {args}')
        result = function(*args, **kwargs)
        print(f'hi from decorator - kwargs: {kwargs}')
        return result
    return wrapper

@show_args
def get_profile(name, active=True, *sports, **awards):
    print('\n\thi from the get_profile function\n')

# timeit decorator
def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # before calling decorated function
        print('== starting timer')
        start = time.time()

        # call decorated function
        func(*args, **kwargs)

        # after calling decorated function
        end = time.time()
        print(f'== {func.__name__} took {int(end-start)} seconds to complete')

    return wrapper

@timeit
def generate_report():
    """Function to generate revenue report"""
    time.sleep(2)
    print('(actual function) Done, report links ...')

# Stacking decorator
def print_args(func):
    """Decorator"""

if __name__ == '__main__':
    get_profile('ben')
    get_profile('julian', False, 'basketball', 'soccer',
            pythonista='special honor of the community')

    generate_report()