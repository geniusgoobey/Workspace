def gen(val):
    for i in range(val):
       print( "Before yielding")
    yield i
    print("After yielding")
    print("End of generator")

print(next(gen(10)))
