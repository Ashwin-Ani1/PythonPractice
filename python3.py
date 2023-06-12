"""
The code below checks to see if an integer number is divisible by prime numbers less than 10 (2, 3, 5, and 7). Add additional if statements to see if the integer number is divisible by prime numbers less than 20 (11, 13, 17, and 19).

This should be fairly straightforward - try duplicating what the current lines do, but change the conditions in the if statements and the output in the print statements.
"""

number = int(input('Please enter an integer number.'))

if number % 2 == 0:
    print('That number is divisible by 2.')
if number % 3 == 0:
    print('That number is divisible by 3.')
if number % 5 == 0:
    print('That number is divisible by 5.')
if number % 7 == 0:
    print('That number is divisible by 7.')

# add your code.
if number % 11 == 0:
    print('That number is divisible by 11.')
if number % 13 == 0:
    print('That number is divisible by 13.')
if number % 17 == 0:
    print('That number is divisible by 17.')
if number % 19 == 0:
    print('That number is divisible by 19.')


"""
Try retrieving the user's input, evaluating it with an if statement, and telling the user if they guessed the number properly; give them a message telling them they guessed incorrectly if they don't guess 7. 

You can start by using `input()`, then an if statement to check the input from the user.
"""
guessed = input("Guess a number between 1 and 10.")
correct_number = 7
if guessed == correct_number:
  print("Thats the correct number!")
if guessed != correct_number:
  print("Thats not the correct number!")
  
"""
How would you write code that can tell a user if a number is odd or even? Look back in the lesson if you're not sure how to do this.
"""
# your code here

number = int(input('Enter a number.'))
if number % 2 == 0:
    print('That number is even.')
if number % 2 != 0:
    print('That number is odd.')

# your code here

"""
Output:
Please enter an integer number.4
That number is divisible by 2.
Guess a number between 1 and 10.3
Thats not the correct number!
Enter a number.45
That number is odd.
"""