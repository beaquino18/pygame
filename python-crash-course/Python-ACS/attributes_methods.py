# Created the Dog class
class Dog:
    pass

# Instatiation
jess_dog = Dog()

# TODO: Create an instance of Dog and assign it to a variable


# Create attributes for jess_dog object, using dot notation.
# Like variables, if attribute did not exist, it is created when you first assign it a value.

jess_dog.name = "Tara"
jess_dog.age = 1
jess_dog.color = "brown"
jess_dog.cuteness_level = 10

# TODO: Add four attrbutes to your dog instance. Give each a value that describes your dog.


# Update attributes similar to how you would update a variable.

jess_dog.age += 1
print(f"My age is {jess_dog.age}")

# TODO: Update the some of the attributes of your dog instance. Assign a new value 
# to one of the existing attributes of your dog. 


# The name attribute 
print(f"My name is {jess_dog.name}")

# TODO: Print one or more of your dog's attributes:


# Delete a property from an object with del

del jess_dog.name
print(f"My name is {jess_dog.age}")

# TODO: Delete one of the attributes of your dog. 


# Rather than having to print all of the attributes one by one, we can use __dict__
print(jess_dog.__dict__)

# TODO: Check the attrbutes of your dog by printing yourdog.__dict__. This should 
# show you all of the attribues that exist on your dog. 


## Challenge 1


# TODO: We need to define a Dog class. All dogs will have the following 
# attributes. Define these on the class Dog below. 

     
# name
# breed 
# fave_snack

# By defining these attributes on the class all dog instances will have them. 
# Remember! attributes are initialized in the __init__ method! 

# Dog class
class Dog:
    def __init__(self, name, breed, fave_snack):
        self.name = name
        self.breed = breed
        self.snack = fave_snack
    
    def dogs_list(self, dogs):
        return [dog.name for dog in dogs]  # Changed self.name to dog.name
    
    

# TODO: Instantiate 3 objects of type Dog
dog_1 = Dog("Hachiko", "Japanese Akita", "Cookies")
dog_2 = Dog("Lasagna", "Poodle", "Lasagna")
dog_3 = Dog("Pizza", "Beagle", "Pizza")

# TODO: Using the instance variable names, create a list of Dog objects called dogs.

dogs = [dog_1, dog_2, dog_3]
dog_instance = Dog("Temp", "TempBreed", "TempSnack")
print(dog_instance.dogs_list(dogs))  


# TODO: Using the loop print the name of each dog

for dog in dogs:
    print(dog.name)

# TODO: Using a loop, delete breed attribute for all the dogs in the list dogs

for dog in dogs:
    del dog.breed

# TODO: Using a loop, add an attribute 'species' and assign it the value 'canine'

for dog in dogs:
    dog.species = "canine"

# TODO: Use the __dict__ attribute to print each dog and check it's attributes and values 
# use a loop to print __dict__ for each dog in your list. 

for dog in dogs:
    print(dog.__dict__)



## Challenge 2


# TODO: Each object should have the following attributes:
# name - name of the city you picked
# country - the country the city is located in
# temperature - the city's temperature in F. 
# latitude - city's latitude coordinate 
# longitude - city's longitude coordinate 

# Location class
class Location:
    pass

# TODO: Instantiate three locations. Instaniate each location with the correct values for 
# name, country, temperature, latitude, longitude. For the last three look up the correct 
# values! Use the current teperature and the actual latitude and longitude. 


# TODO: Using the object variable names, create a list of Location objects called bucketlist.


# TODO: Using the loop print the name of the city of each location in bucketlist. 


# TODO: Loop over your locations and print only locations above the equator. 
# Latitude represents how far above or below the equator a location is. Positive numbers 
# are above the equator negative numbers are below. 


# TODO: Using the loop, loop through the objects to find which location has the warmest weather




## Challenge 2.5


# Students Class
class Student:
    # class attributes are shared by all instances
    school = "Make School"
    location = "San Francisco"
    major = "Computer Science"


# TODO: Instantiate 2 object of type Student

jhene = Student()
kehlani = Student()

# TODO: Access class attributes using dot notation. Run this code and check the output

print(f"Jhene studies {jhene.major} at {jhene.school} in {jhene.location}.")
print(f"Kehlani studies {kehlani.major} at {kehlani.school} in {kehlani.location}.")

# TODO: Print the  __dict__ attribute to for each object to see a dictionary of all the attributes defined for the object itself.

print(jhene.__dict__)
print(kehlani.__dict__)

# TODO: Answer the question: Why is it blank? 


# TODO: Remove the comment on the line below: 

# print(Student.__dict__)

# TODO: Answer the questions: 
# What attributes do I see in the Student class object? 
# Is Student an instance of Student or is it something else?

# Imagine that Make School moves to San Rafael!
# We can update the class variable for all instances by:

# TODO: Uncomment the line below

# Student.location = "San Rafael"

# TODO: Uncomment the lines below and run your code.
# Here you are printing the location for each student again.

# print(f"Jhene studies in {jhene.location}.")
# print(f"Kehlani studies in {kehlani.location}.")


# TODO: Kehlani transfered , update her school to UCLA.
# Uncomment these lines:

# kehlani.school = "UCLA"
# print(kehlani.school)


# Do you think that the name of the school will change for Jhene too? Test it.
# TODO: Predict what you think will happen. Is jhene going to UCLA or are they
# still in San Rafael?

# print(jhene.school) 


# What happened?

# Print the __dict__ for kehlani



## Challenge 3


# Let's add instance attributes to the Students class:

class Student:
    # Class attributes
    school = 'Make School'
    location = 'San Francisco'
    major = 'Computer Science'

    def __init__(self, name, year, coach):
      # instance attributes
      self.name = name
      self.year = year
      self.coach = coach


# TODO: Add three instances with attributes:
student_1 = Student("Jeffrey", 2021, "Lui") 
student_2 = Student("Hector", 2022, "Amanda") 
student_3 = Student("Consuela", 2023, "Paul") 
student_4 = Student("Consuela", 2023, "Paul") 


# Using __dict__, print the name space of each Student object
print(student_1.__dict__)
print(student_2.__dict__)
print(student_3.__dict__)


# TODO: Add a class attribute called num_students, which will keep count 
# of the number of students created. Initialize it to 0


# TODO: In your __init__ method, increment the num_students class attribute by 1.


# TODO: Print the value of the Student.num_students below: 


# TODO: Add an instance method called say_hello. It should print
# the student's name and a greeting


# TODO: Create a new class named Course. This should have a name and 
# list of students as attributes. 


# TODO: Give the new Course class two instance methods: add_student
# and drop_student. These methods should take a student as an argument
# and add or remove that student from the student list. 


# TODO: Create a new course. 


# TODO: Add the four students above to your new course. 


# TODO: Add a new method to Course called introduction. It should 
# loop through all students and call the say_hello method on each. 



