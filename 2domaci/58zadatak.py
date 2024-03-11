string = "Hi Mr. Rober53. How are you today? Today is 08.10.2019"
novi_string = ""

# Remove numeric characters from string
for i in range(len(string)):
    if not string[i].isnumeric():
        novi_string += string[i]

print(novi_string)
