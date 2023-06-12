"""
Now that you know some Python basics, how would you teach someone basic arithmetic in Python? Use the code block below to write and test a few examples.

* If sales tax is 6%, how much sales tax do you pay on a purchase of $7.98?
* What's the area of a triangle if its height is 8.2 and its base is 3.5?
* Assuming pi = 3.14, what's the circumference of a circle if its diameter is 19?
"""

tax = 0.06
purchase = 7.98

purchase += 7.98 * tax
print(purchase)

height = 8.2
base = 3.5
# the area of a triangle is one half its base times its height.

triangle = (height * base) / 2
print(triangle)

pi = 3.14
diameter = 19
# circumference is the diameter multiplied by pi.

circumference = pi * diameter
print(circumference)

"""
OUTPUT:
8.4588
14.349999999999998
59.660000000000004
"""