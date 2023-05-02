#теорія декоратирів

def my_decorator_func(args): #3
    def wrapper():
        print("шото там")
        func()
        print("i tam shos")
    return wrapper


@my_decorator_func#2
def say_hello():#1
    print("hello!")
say_hello()


def delay_decorator(func):
    def wrapper(*args, **kwargs):
        time.sleep(3)
        return func(*args, **kwargs)
    return wrapper
@delay_decorator
def sleepy():
    print("ya splyu")
sleepy()