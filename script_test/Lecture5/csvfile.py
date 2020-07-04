import csv

with open('record.csv', 'r') as records:
    # Creates a csv reader from a file object
    csv_reader = csv.reader(records)
    
    # If the csv file has headers you'll want to do this
    # to skip over it (maybe even use it in your code) 
    headers = next(csv_reader)
    
    print("Headers: {}".format(headers))
    for row in csv_reader:
        name = row[0]
        age = int(row[1])
        p_num = row[2]
        print("Person({}, {}, {})".format(name, age, p_num))