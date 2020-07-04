class Bag():
    def __init__(self):        
        self.lstcontents = []    
      
    def put_in_bag(self,item):   
        if(isinstance(item,Bag)):  
            a = Bag()
            a = item
            values = a.__str__()
            for its in values:
                a.put_in_bag(its)
        else:
            self.lstcontents.append(item)

    def __str__ (self):      
        return str(self.lstcontents)




a = Bag()

bag1 = Bag()
bag2 = Bag()
bag1.put_in_bag("comb")
bag1.put_in_bag("candy bar")
bag2.put_in_bag("comb1")
bag2.put_in_bag("candy bar1")

bag1.put_in_bag(bag2)
print(bag1)
print(bag2)




