import time
from decimal import Decimal


def timer(func):
    def inner1(*args, **kwargs):
        # Store time before execution of the fucntion
        begin = time.time()

        func(*args, **kwargs)

        # Store time after execution of the function
        end = time.time()

        print("Total time taken to calculate factorial: ", end - begin)

    return inner1


@timer
def factorial(n):
    factorial = 1
    if n == 0:
        print("The factorial of 0 is", factorial)
    else:
        for i in range(1, n + 1):
            factorial *= i
        print(f"The factorial of {n} is {factorial}")


factorial(20)


@timer
def sum_of_natural_numbers(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    print(f"\nThe sum of first {n} natural numbers is {sum}")


sum_of_natural_numbers(20)
