'''
For loop - doing the same action for every item on the list
For every magician in the list of magicians, print the magician's name
Program ends when there's the for loop reach end of the list
'''
magicians = ['harry', 'ron', 'hermione']

for magician in magicians:
    print(magician)

'''
output:
harry
ron
hermione
'''

# =======================================

# Adding more method inside for loop

for magician in magicians:
    print(f"{magician.tltle()}, that was a great trick!")
    print(f"I can wait to see your next trick, {magician.title()}")

'''
output:
Harry, that was a great trick!
I can't wait to see your next trick, Harry.

Ron, that was a great trick!
I can't wait to see your next trick, Ron.

Hermione, that was a great trick!
I can't wait to see your next trick, Hermione.
'''

# =======================================

# Doing something after a for loop - since the last line isn't indented,
# it's outside the for loop

for magician in magicians:
    print(f"{magician.tltle()}, that was a great trick!")
    print(f"I can wait to see your next trick, {magician.title()}")

print("Thank you, everyone. That was a great magic show!")

'''
output:
Harry, that was a great trick!
I can't wait to see your next trick, Harry.

Ron, that was a great trick!
I can't wait to see your next trick, Ron.

Hermione, that was a great trick!
I can't wait to see your next trick, Hermione.

Thank you, everyone. That was a great magic show!
'''

# =======================================

# Logical error due to forgetting indent additional lines - this would only
# print the last element in the list

for magician in magicians:
    print(f"{magician.tltle()}, that was a great trick!")
print(f"I can wait to see your next trick, {magician.title()}")

'''
output:
Harry, that was a great trick!
Ron, that was a great trick!
Hermione, that was a great trick!
I can't wait to see your next trick, Hermione.
'''
