class Person:
    def __init__(self, name, age, phone_number):
        self.NAME = name
        self.AGE = int(age)
        self.PHONE_NUMBER = phone_number
    
    def __str__(self):
        return "Person({name}, {age}, {phone})".format(name = self.NAME,age  = self.AGE,phone= self.PHONE_NUMBER)

# Used to store the records in the flat file
people = []

# The flat file is just a .txt file.
with open("record.txt", 'r') as records:
    header = next(records) # column names
    for record in records:
        # Unpacks the contents of the list (name, age, phone#)
        #returned by split to 
        # the constructor, __init__, of the Person class.
        p = Person(*record.split(" "))
        people.append(p)

for person in people:
    print(person)
