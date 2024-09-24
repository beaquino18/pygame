motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)


#adding new element to the list
motorcycles.append('ducati')
print(motorcycles)

#motorcycles[0] = 'ducati' #change first element in the list

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

#inserting elements into a list insert method opens a space at position 0
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

#remove elements from a list, removes ducati
del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)

#pop() method removes the last item in a list, but it lets you work with that item after removing it
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles) #outputs 'suzuki'

#remove items in the list using pop indexes
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}")

#remove() method for removing specific value in the list
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)