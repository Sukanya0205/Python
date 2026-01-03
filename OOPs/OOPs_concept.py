class Dog:
    species = "Canis familiaris" 
 
    def _init_(self, name, breed) : 

     self.name = name  
       
     self.breed = breed 

    def bark(self): 
         
         print(f"{self.name} says Woof!")


my_dog = Dog("Buddy", "Golden Retriever")
another_dog = Dog("Lucy","Labrador") 
print(my_dog.name) 

print(another_dog.breed) 
my_dog.bark()
print(Dog.species) 