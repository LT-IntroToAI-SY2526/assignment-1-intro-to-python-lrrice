

# Assignment 1: AI-Generated Python Problems
# Name: [Your Name Here]


"""
AI-Generated Problem Set


INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs


Remember: The goal is to LEARN, not just get working code!
"""


# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================


"""
MY ORIGINAL AI PROMPT: I'm learning Python basics in a high school programming class. I have some experience with python. Can you create 5-7 practice problems that cover:


Variables and basic data types
Conditionals (if/elif/else)
Loops (for and while)
Functions
Basic list operations
Make them progressively more challenging. Make sure each problem has clear instructions and example inputs/outputs.


Example: "I'm learning Python basics in a high school programming class.
I have some experience with Java. Can you create 5-7 practice problems that cover..."
"""


# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================


"""
PROBLEM 1: Temperature Converter (Variables & Basic Data Types)
Instructions:


Get temperature value from user (as a float)
Get conversion type from user ("C" for Celsius to Fahrenheit, "F" for Fahrenheit to Celsius)
Perform the conversion and display the result
Formulas: F = (C  9/5) + 32 and C = (F - 32)  5/9
"""


def temp_convert():
    print("temperture converter")
    original_temprature = float(input("enter temperature:"))
    units = str(input("enter unit (F or C):"))
    if units == "F":
        original_temprature = ((original_temprature * 9/5) +32)
    elif units == "C":
        original_temprature = ((original_temprature -32) * 5/9)
    print (original_temprature)


"""
PROBLEM 2: Grade Calculator (Conditionals & Basic Math)
Topics: Variables, conditionals (if/elif/else), basic operations
Create a program that calculates a student's letter grade based on their numerical score. The program should:
Ask for a numerical grade (0-100)
Determine the letter grade using this scale:

A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: Below 60

Display both the numerical and letter grade
"""

def grade_calculator(grade):
    score = "A"
    if grade >= 90:
        score = "A"
    elif grade >= 80:
        score = "B"
    elif grade >= 70:
        score = "C"
    elif grade >= 60:
        score = "D"
    else:
        score = "F"
    
    return score

"""
PROBLEM 3: Number Guessing Game (While Loops & Conditionals)
Topics: While loops, conditionals, variables
Create a number guessing game where:

The program generates a random number between 1 and 100
The user has to guess the number
After each guess, provide hints ("too high" or "too low")
Count the number of attempts
Continue until the user guesses correctly
"""

import random

def number_guesser():
    number = random.randint(1, 100)
    guesses = 0
    correct = False

    while not correct:
        guess = int(input("Guess the number:"))
        if guess == number:
            correct = True
            print ("you got it!")
        elif guess > number:
            print ("too high")
        elif guess < number:
            print ("too low")


"""
PROBLEM 4: Multiplication Table (Loops)
Topics: Loops (for loop), variables
Write a program that generates a multiplication table for a given number. The program should:

Ask the user for a number
Display the multiplication table from 1 to 10 for that number
Format the output neatly
"""

def mult_table(number):
    print("Multiplication table of " + str(number) + ":")
    for i in range(10):
        print(str(number) + " X " + str(i + 1) + " = " str(int(number * (i+1))))
# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================




"""
Test all your solutions with different inputs


Add asserts if you feel comfortable


Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""


print("Testing Problem 1:")
"""temp_convert()"""


print("\nTesting Problem 2:")
print (grade_calculator(64))


print("\nTesting Problem 3:")
"""number_guesser()"""


print("\nTesting Problem 4:")
mult_table(5)


print("\nTesting Problem 5:")
# Add your tests here




