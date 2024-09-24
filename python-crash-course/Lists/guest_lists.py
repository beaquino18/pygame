guests =['Harry', 'Ron', 'Hermione']

for guest in guests:
    print(f"Hi {guest}! Would you like to have dinner with me?")

print(f"Unfortunately, {guests.pop(1)} can't make it.")
guests.insert(1, 'Luna')
print(f"Now, my guests are: {guests[0]}, {guests[1]}, {guests[2]}")