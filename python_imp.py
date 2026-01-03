'''print("Hello","World", sep=", ", end="!\n")
print(10>5) 
print(10==5)

print(True and False) # Output: False
print(True or False) # Output: True
print(not True) # Output: False'''

'''age =17

if age <18:
  print("You are a minor.")
elif age ==18:
  print("You just became an adult!")
else:
  print("You are an adult.")'''

'''status = 404

match status:
     case 200:
          print("Success!")
     case 404:
        print("Not Found")
     case _ :
        print("Unknown Status")'''


'''fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
  print(fruit)'''

for i in range(10):
 if i == 5:
   break
print(i) 

for i in range(5):
 if i == 2:
  continue
print(i)

for i in range(5):
 if i == 3:
   pass 
print(i)
