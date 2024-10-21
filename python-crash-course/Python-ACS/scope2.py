name = "CS 1.1"

def welcome_class():
    # Is name a global var here? - global
    print(f'Welcome {name}!')

def dismiss_class():
    # Is name a global var here? - global
    print(f'Goodbye {name}!')

def print_name(name):
    # Is name a global var here? - global
    print(f'Class Name: {name}')

def change_name():
    # Is name a global var here? - local
    name = 'CS 1.0' 
    return name
    # print(f'New Name: {name}')


# Try uncommenting each line below and running the script

# welcome_class()
# dismiss_class()
# print_name("WEB2.0") 
# print(name)
# name = change_name()

# What do you think will print?

# print(name)

# Examine the code here figure out the scope of name
# Will the below code work? Why/Why not?
def add_year(): 
    # Is name a global var here? - local, but this would result to unboundlocalerror, so try adding variable name
    name = 'ACS 1111'
    name = name + ' 2024'
    print(f'New Name: {name}')

add_year()
