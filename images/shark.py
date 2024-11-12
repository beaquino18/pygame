'''
In the code below, we created a Shark class and a Clownfish class,
each of which will define methods for swim(), swim_backwards(),
and skeleton().

They share three methods in common with the same name. However,
each of the functionalities of these methods differ for each class.
'''


class Fish():
    # TODO: Define base class w/ common attributes and methods
    pass


class Shark():
    # TODO: Refactor to use Fish base class.
    def swim(self):
        print("The shark is swimming.")

    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards.")

    def skeleton(self):
        print("The shark's skeleton is made of cartilage.")


class Clownfish():
    # TODO: Refactor to use Fish base class.
    def swim(self):
        print("The clownfish is swimming.")

    def swim_backwards(self):
        print("The clownfish can swim backwards.")

    def skeleton(self):
        print("The clownfish's skeleton is made of bone.")


jaws = Shark()
nemo = Clownfish()
marlin = Clownfish()
marlin_jr = Clownfish()

# Now that we have two objects that make use of a common interface,
# we can use the two objects in the same way regardless of their
# individual types.

school_of_fish = [jaws, nemo, marlin, marlin_jr]

for fish in school_of_fish:
    fish.swim()
    fish.swim_backwards()
    fish.skeleton()

# Example from Digital Ocean 🐠
