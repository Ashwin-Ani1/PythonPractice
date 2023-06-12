"""
In this Notebook file, we explore the use of **strings** and discuss 

---

how all of these different things are **data types**.

How would you show string manipulation in Python? Let's use Python to work out a few examples below.

* How can you make 'Spider-Man' into a sequel?
* How can you find the sum of three numbers reprented as strings?

"""

title = 'Spider-Man'
sequel = 3
# how can you make this Spider-Man 3?

title2 = title + ' ' + str(sequel)
print(title2)

value1 = '9'
value2 = '27'
value3 = '33'

sum = int(value1) + int(value2) + int(value3)
print(sum)
# what is the sum of these?

"""
OUTPUT:
Spider-Man 3
69
"""
