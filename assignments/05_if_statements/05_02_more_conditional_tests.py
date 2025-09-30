fruit = 'apple'
print("Is fruit == 'apple'? I predict True.")
print(fruit == 'apple')

print("\nIs fruit != 'apple'? I predict False.")
print(fruit != 'apple')

# Tests using the lower() method
name = 'Alice'
print("\nIs name.lower() == 'alice'? I predict True.")
print(name.lower() == 'alice')

print("\nIs name.lower() == 'ALICE'? I predict False.")
print(name.lower() == 'ALICE')

# Numerical tests
number = 25
print("\nIs number == 25? I predict True.")
print(number == 25)

print("\nIs number != 25? I predict False.")
print(number != 25)

print("\nIs number > 20? I predict True.")
print(number > 20)

print("\nIs number < 20? I predict False.")
print(number < 20)

print("\nIs number >= 25? I predict True.")
print(number >= 25)

print("\nIs number <= 24? I predict False.")
print(number <= 24)

# Tests using 'and' keyword
age = 18
print("\nIs age >= 18 and age < 21? I predict True.")
print(age >= 18 and age < 21)

print("\nIs age > 18 and age < 21? I predict False.")
print(age > 18 and age < 21)

# Tests using 'or' keyword
print("\nIs age > 18 or age == 18? I predict True.")
print(age > 18 or age == 18)

print("\nIs age > 21 or age < 18? I predict False.")
print(age > 21 or age < 18)

# Test whether an item is in a list
colors = ['red', 'green', 'blue']
print("\nIs 'green' in colors? I predict True.")
print('green' in colors)

print("\nIs 'yellow' in colors? I predict False.")
print('yellow' in colors)

# Test whether an item is not in a list
print("\nIs 'purple' not in colors? I predict True.")
print('purple' not in colors)

print("\nIs 'red' not in colors? I predict False.")
print('red' not in colors)