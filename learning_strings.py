#Learning about strings and string manipulation

strings = "The language of 'Python' is named for Monty Python"
print(strings)

"""
The title method changes each word to title case
Where each word begins with a capital letter
The upper method converts the string to all uppercase
The lower method converts the string to all lowercase
"""
name = "cheddar the dog"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "kevin"
last_name = "holt"
full_name = f"{first_name} {last_name}"
greeting = f"Hello, {full_name.title()}!"
print(greeting)

