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

#