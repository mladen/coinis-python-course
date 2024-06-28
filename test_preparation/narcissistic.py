# Return true or false depending if the input number is a narcissistic number. Input is a positive integer.
# A narcissistic number is a number that is the sum of its own digits each raised to the power of the number of digits.
# For example, 371 is a narcissistic number because 3^3 + 7^3 + 1^3 = 371.


def is_narcissistic(n):
    n_str = str(n)
    n_len = len(n_str)
    n_sum = 0
    for i in n_str:
        n_sum += int(i) ** n_len
    return n_sum == n


print(is_narcissistic(371))
