# Pointless to create an empty frozen set, not modifiable
empty_frozen_set = frozenset()

my_frozen_set = frozenset([1, 2, 3, 4, 5])

print(my_frozen_set)

if 3 in my_frozen_set:
    print("3 is in the set")

# Check if element is not in set
if 10 not in my_frozen_set:
    print("10 is not in the set")

# Practical example: fast membership checks
valid_ids = frozenset([100, 200, 300, 400, 500])
user_id = 200

if user_id in valid_ids:
    print(f"User {user_id} is valid")
else:
    print(f"User {user_id} is not valid")

# Frozen sets are immutable, so you cannot add elements to them
# You can create a new frozen set with the elements you want
new_frozen_set = my_frozen_set.union([6, 7, 8])
print(new_frozen_set)

# You can also create a new frozen set with the elements you want
new_frozen_set = my_frozen_set.intersection([2, 3, 4])
print(new_frozen_set)

# You can also create a new frozen set with the elements you want
new_frozen_set = my_frozen_set.difference([2, 3, 4])
print(new_frozen_set)

# You can also create a new frozen set with the elements you want
new_frozen_set = my_frozen_set.symmetric_difference([2, 3, 4])
print(new_frozen_set)