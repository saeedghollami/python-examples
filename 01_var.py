# -------------------------------------
# Creating variables
# integer variable, int
x = 10
age = 31

# Floating-Point or Float (Number with decimal point)
f = 4.9
cost = 9.99

# String or str (called strs)
s = 'This is a String.'
message = "This is another string."

# ------------------------------------
# Find area and premiter of a rectangle
width = 10
height = 5

area = width * height
premiter = (width + height) * 2

# --------------------------------------------
# Get a name from user and say hello to her/his
name = input('What is your name? ')
print('Hello', name, 'Nice to meet you.')

# ------------------------------------------
# Find area of circle
PI = 3.14159
r = 5
area = PI * r ** 2

# ------------------------------------------
# Creating a food menu
print('1. Cheese Burger ', '$3.99')
print('2. Bacon Cheese Burger ', '$4.99')
print('3. Soda ', '$1.99')
print('4. Classic Fries ', '$2.99')

response = input('> ')

# ------------------------------------------
# Another way to create menu
menu = """
1. Cheese Burger $3.99
2. Bacon Cheese Burger $4.99
3. Soda $1.99
4. Classic Fries $2.99
"""
print(menu)
response = input('> ')

