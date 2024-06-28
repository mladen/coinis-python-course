# def decorator1(func):
#     print(f"Decorator 1 is executed, 'func' is {func.__name__}")
#     func()
#     return func


# def decorator2(func):
#     print(f"Decorator 2 is executed, 'func' is {func.__name__}")
#     func()
#     return func


# @decorator1
# @decorator2
# def my_function():
#     print("Inside my_function")


# my_function()


def my_decorator1(func):
    def wrapper1(*args, **kwargs):
        print(
            f"Decorator 1: Something is happening before the function is called. {func.__name__}"
        )
        func(*args, **kwargs)
        print(
            f"Decorator 1: Something is happening after the function is called. {func.__name__}"
        )

    return wrapper1


def my_decorator2(func):
    def wrapper2(*args, **kwargs):
        print(
            f"Decorator 2: Something is happening before the function is called. {func.__name__}"
        )
        func(*args, **kwargs)
        print(
            f"Decorator 2: Something is happening after the function is called. {func.__name__}"
        )

    return wrapper2


# @my_decorator1  # This is the same as my_function = my_decorator1(my_function)
# @my_decorator2  # This is the same as my_function = my_decorator1(my_decorator2(my_function))
def say_hello(name):
    print(f"Hello, {name}! I am {__name__} and I am a {say_hello.__name__} function.")


say_hello = my_decorator1(my_decorator2(say_hello))
# my_decorator2 returns wrapper2, which is passed to my_decorator1, which returns wrapper1 - that's the process of wrapping the function
# The function is wrapped in the order of the decorators, so the order of the decorators matters.
# Now when we execute the function, it will execute wrapper1, which will execute wrapper2, which will execute the original function
# The order of the decorators is important, because the function is wrapped in the order of the decorators.

say_hello("John")
# print(say_hello.__name__)
# print(say_hello)  # Prints the memory address of the 'wrapper' function
