def sum(a,b):
    print("Hiii nice to meet you")
    c=a+b
    global z #please modify global z
    z= 6 #this will refer to global z and not create a local variable
    return c

print(sum(4,56))
z=3
print(z)