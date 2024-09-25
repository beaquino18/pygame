# sort() arrange list alphabetically
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# sort(reverse=True) reverse-alphabetical order
cars.sort(reverse=True)
print(cars)

# ============
# sorted() method lists them temporarily
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('Here is the original list.')
print(cars)

print('\nHere is the sorted list:')
print(sorted(cars))

print('\nHere is the original list again:')
print(cars)

# ============
# reverse() reverse order of list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse() #prints subaru, toyota, audi, bmw
print(cars)

# ============
# len() finds the length of the list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
