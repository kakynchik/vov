#1
def decorate(func):
    def wragger(*args, **wragger):
        result + func(*args, **wragger)
        return result + 10
    return wragger

@decorate
def my_func(x):
    return x

result = my_func(int(input("введіт число ")))
print(result)

