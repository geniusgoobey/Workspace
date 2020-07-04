l = [1, 2, 3]

for i in range(len(l)):
    c = l[-1]
    c += 1
    l.append(c)

print(l) 