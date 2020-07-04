cmd = ""
while True:
    while True:
        cmd = input("Inner Command: ")
        if cmd == "exit":
            break
        else:
            print("Still going")
    print("Inner loop broken out of")
    cmd = input("Outer Command: ")
    if cmd == "quit":
        break
    else:
        print("Starting inner loop again")
print("Outer loop broken out of")