print((lambda x: x+3)(2))

middle_value = lambda a, b, c: min(max(a, b), max(a, c), max(b, c))
print(middle_value(1, 5, 3))