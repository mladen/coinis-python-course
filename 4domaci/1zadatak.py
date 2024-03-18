from functools import reduce

stringovi = ["flower", "flow", "flight"]

print(reduce(lambda x, y: x if len(x) > len(y) else y, stringovi))
