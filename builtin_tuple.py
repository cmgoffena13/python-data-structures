# Pointless to create an empty tuple, not modifiable
empty_tuple = ()
empty_tuple = tuple()

my_tuple = (1, 2, 3, 4, 5)
my_tuple = tuple([1, 2, 3, 4, 5])

print(my_tuple)

# Tuples are immutable, so you cannot add elements to them
# You can create a new tuple with the elements you want
new_tuple = my_tuple + (6, 7, 8)
print(new_tuple)

# You can also create a new tuple with the elements you want
new_tuple = my_tuple * 2
print(new_tuple)

# Perfect for "for each" loops
for item in my_tuple:
    print(item)

# Tuple Comprehension does not exist because tuples are immutable
# Generator expression (creates a generator, not a tuple!)
generator = (item * 2 for item in my_tuple)
print(generator)  # Prints: <generator object <genexpr> at 0x...>

for item in generator:
    print(item)

# To create a tuple, wrap the generator expression in tuple()
doubled_tuple = tuple(item * 2 for item in my_tuple)
print(doubled_tuple)  # Prints: (2, 4, 6, 8, 10)

# Note: Python doesn't have "tuple comprehension" syntax
# Parentheses alone create a generator expression, not a tuple