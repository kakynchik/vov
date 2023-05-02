#1
def decorate(func):
    def wragger(*args, **wragger):
        result + func(*args, **wragger)
        return result + 10
    return wragger

@decorate
def my_func(x):

def cache(func):
    cache_dict = {}
    def wrapper(*args, **kwargs):
        if args in cache_dict:
            return cache_dict[args]
        else:
            result = func(*args)
            cache_dict[args] = result
            return result, cache_dict
        return wrapper

@cache
def my_func(x, y):
    return x * y
print(my_func(3, 10))
