def cube(base):
    result = base ** 3
    print(f'The cube of {base} is: {result}')


cube(3)

# What are the local variables of cube()?
# result

# What will happen if we try to access result? Why?
# print(result) -- it would print an error cause it's not local variable

# What happens and why?
# error, result is local to the func

# What will happen if we try to access base? Why?
# print(base), error too!
