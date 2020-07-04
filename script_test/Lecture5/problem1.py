import csv

class Element:
    #Expectes a dictionary which will convert the keys
    #to instance variables and the values to the value
    #pointed at by the instance variables.
    def __init__(self, **kwargs):
        for (attribute, value) in kwargs.items():
            setattr(self, attribute, value)
    
    def __str__(self):
        res = []
        for (attribute, value) in self.__dict__.items():
            res.append(f"{attribute}: {value if value else 'N/A'}")
        return '|'.join(res)


def search(query, data):
    #Gets the specific attribute (instance variable) of 
    #each element in the data iterable to perform a check
    #on whether the query matches one of those values.
    for element in data:
        name = getattr(element, "Element").lower()
        symbol = getattr(element, "Symbol").lower()
        number = getattr(element, "Number")
        if query.lower() in (name, symbol, number):
            return element 
    return None 

def load_data():
    #The resulting information to be returned
    table = []
    with open('elements.csv') as elements_file:
        csv_reader = list(csv.reader(elements_file))

        #Retrieve the header as attribute names
        attribute_names = csv_reader[0]

        #Load the data for each piece in a dictionary 
        #so that creating the Element object is easily done
        for row in csv_reader:
            data = {
                attrib: value 
                for (attrib, value) in zip(attribute_names, row)
            }
            table.append(Element(**data))
    return table

#Main application that waits for a query from the user
#and then prints a result if one exists.
if __name__ == "__main__":
    periodic_table = load_data()
    while True:
        q = input("Query: ")
        res = search(q, periodic_table)
        if q.lower() == "exit":
            break
        if res:
            print()
            for (i, s) in enumerate(str(res).split("|")):
                print(f"\t{s}")
        else:
            print(f"{q} not found")
        print()
    print("Exitting...")