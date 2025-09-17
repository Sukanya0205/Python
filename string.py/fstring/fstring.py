# string formatting

template = "Dear {}, You are awesome . Take this {}$ bag"
a = "Sahil"
a1 = 10000
b = "Abhi"
b2 = "1000" 
c = "Januu"
c2 = 340

s1 = template.format(a , a1)
print(s1)

print(f"{b} you are awesome and take this {b2}$ bag")