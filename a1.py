

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
MY ORIGINAL AI PROMPT: I'm learning Python basics in a high school programming class. I have some experience with [mention your previous programming language if any, or say 'I'm new to programming']. Can you create 5-7 practice problems that cover:


Variables and basic data types
Conditionals (if/elif/else)
Loops (for and while)
Functions
Basic list operations
Make them progressively more challenging. Make sure each problem has clear instructions and example inputs/outputs.
[Paste the prompt you used to generate your problem set here]


Example: "I'm learning Python basics in a high school programming class.
I have some experience with Java. Can you create 5-7 practice problems that cover..."
"""


# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================


"""
PROBLEM 1: Problem 1: Temperature Converter (Variables & Basic Data Types)
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
temp_convert()


print("\nTesting Problem 2:")
# Add your tests here


print("\nTesting Problem 3:")
# Add your tests here


print("\nTesting Problem 4:")
# Add your tests here


print("\nTesting Problem 5:")
# Add your tests here




