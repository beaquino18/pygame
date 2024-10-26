import random

# Here i is defined and initialized by the for loop
for i in range(1,10):
    print(f"i: {i}")


print(i) # is i "visible" here?  

#the variable i defined in the for loop is visible outside of the loop. 
# After the loop finishes, i will hold the last value assigned to it, 
# which in this case will be 9. So, when you print i after the loop, it will output 

####################################


# Here a is defined and initialized inside the if and the else blocks
if random.random() < 0.5:
    a = 'Hello'
else:
    a = 'Goodbye'


print(a) # Is a visible outside of the if else block?
