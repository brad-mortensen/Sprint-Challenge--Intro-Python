# The following list comprehension exercises will make use of the
# defined Human class.
import math


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Human: {self.name}, {self.age}"


humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
a = [p.name for p in humans if p.name[0] == 'D']
print(f"Starts with D: {a}")

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".

b = [p.name for p in humans if p.name[-1] == 'e']
print(f"Ends with e: {e}")

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.

c = [p.name for p in humans if ord(
    p.name[0]) in range(ord('C'), ord('G') + 1)]
print(f"Name starts between C and G inclusive: {c}")

# Write a list comprehension that creates a list of all the ages plus 10.

d = [(p.age + 10) for p in humans]
print(f"Ages plus 10: {d}")

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.

e = [f'{p.name}-{p.age}' for p in humans]
print(f"Name hyphen age: {e}")

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.

f = [(p.name, p.age)for p in humans if p.age in range(27, 33)]
print(f"Names and ages 27-32: {f}")

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names capitalized and the ages with 5 added tothem.
# The "humans" list should be unmodified.

g = [Human(p.name.upper(), p.age + 5) for p in humans]
print(f"All names capitalized: {g}")

# Write a list comprehension that contains the square root of all the ages.

h = [math.sqrt(p.age) for p in humans]
print(f"Square root of ages: {h}")
