empty_set = set()

my_set = {1, 2, 3, 4, 5}  # similar to a dictionary, but without keys
my_set = set([1, 2, 3, 4, 5])

my_set.add(6)

print(my_set)

# Perfect for "for each" loops
for item in my_set:
    print(item)

# Set Comprehension (faster than a for loop)
doubled_set = {item * 2 for item in my_set}
print(doubled_set)

# Membership testing - O(1) average (fast!)
# Check if element is in set
if 3 in my_set:
    print("3 is in the set")

# Check if element is not in set
if 10 not in my_set:
    print("10 is not in the set")

# Practical example: fast membership checks
valid_ids = {100, 200, 300, 400, 500}
user_id = 200

if user_id in valid_ids:
    print(f"User {user_id} is valid")
else:
    print(f"User {user_id} is not valid")