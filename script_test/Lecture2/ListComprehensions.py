lst = [i for i in range(10)]
print(lst)
lst1 = []
for num in range(0,10):
    lst1.append(num)
print (lst1)


lst = [i ** 2 for i in range(0, 10)]
print (lst)
lst1 = []
for num in range(0,10):
    lst1.append(pow(num,2))
print (lst1)


lst = [i ** 2 for i in range(0, 10) if i % 2 == 0]
print (lst)
lst1 = []
for num in range(0,10):
    if(num % 2) == 0: 
        lst1.append(pow(num,2))
print (lst1)


words = "This is a string"
info = [(w.upper(), w.lower(), len(w)) for w in words.split()]
print (info)
words = "This is a string"
lst = words.split()

info = []
print ("final", end="\n")

for elim in range(0,len(lst)):
    if info == None:
        info = [(lst[elim].upper(),lst[elim].lower())]
    else:
        info = info.append([(lst[elim].upper(),lst[elim].lower())])
   
print(info)
