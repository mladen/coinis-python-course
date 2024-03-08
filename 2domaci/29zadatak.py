string = input("Enter a string: ")

if all(
    c in "01" for c in string
):  # all() returns True if all items in an iterable are true, otherwise it returns False.
    print("The string is binary.")
else:
    print("The string is not binary.")
