class Test:
    class_variable = 3
        
t1 = Test()
t2 = Test()

print("T1 Class Variable:", t1.class_variable)
print("T2 Class Variable:", t2.class_variable)

Test.class_variable = 1000

print("New T1 Class Variable:", t1.class_variable)
print("New T2 Class Variable:", t2.class_variable)