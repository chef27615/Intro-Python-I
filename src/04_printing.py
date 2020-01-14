"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
d = round(y, 2)
c = "x is %s, y is %s, z is %s" % (x, d, z)
print(c)

# Use the 'format' string method to print the same thing
a = "x is {}, y is {}, z is {}".format(str(x), str(round(y, 2)), z)
print(a)
# Finally, print the same thing using an f-string
b = f"x is {x}, y is {round(y, 2)}, z is {z}"
print(b)