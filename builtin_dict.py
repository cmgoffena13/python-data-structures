empty_dict = {}
empty_dict = dict()

my_dict = {"apple": 1, "banana": 2, "cherry": 3}
my_dict = dict({"apple": 1, "banana": 2, "cherry": 3})

print(my_dict)

# Perfect for "for each" loops
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Dict Comprehension (faster than a for loop)
squared_dict = {key: value**2 for key, value in my_dict.items()}
print(squared_dict)

# Get a value by key; KeyError if key is not found
print("Get a value by key; KeyError if key is not found")
print(my_dict["apple"])

# Get a value by key with a default value; Returns default value if key is not found
print("Get a value by key with a default value; Returns default value if key is not found")
print(my_dict.get("peach", 0))

# Set a value by key
print("Set a value by key")
my_dict["apple"] = 4
print(my_dict)

# Delete a key
print("Delete a key")
del my_dict["apple"]
print(my_dict)

# Delete a key and return the value
print("Delete a key and return the value")
print(my_dict.pop("banana"))
print(my_dict)

# Delete a key and return the value with a default value
print("Delete a key and return the value with a default value")
print(my_dict.pop("banana", 0))
print(my_dict)

# Clear the dictionary
print("Clear the dictionary")
my_dict.clear()
print(my_dict)

# Delete the dictionary
print("Delete the dictionary")
del my_dict