def sum(a,b):
    #a and b are local variablesf
    
    c = a+b
    z=4 #it creates a local variable called z which is destroyed after this fun returns
    return c

def greet():
    z=34#local variable
    print("Hello")

z = 5
#z is the global variable
print(z)
print (sum(4,6))
print(z)