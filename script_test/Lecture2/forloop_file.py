with open("sample.txt", "r") as file_h:
    for line in file_h:
        print(line)

with open("sample.txt", "r") as file_h:
    for line in file_h:
        print(repr(line))

with open("sample.txt", "r") as file_h:
    for line in file_h:
        print(line.strip())