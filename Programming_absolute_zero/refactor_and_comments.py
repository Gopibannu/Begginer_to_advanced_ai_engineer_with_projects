#Refactor one of your earlier scripts adding docstrings and clear comments.

#Build a 'Mad Libs' generator using f-strings and string methods.
# A Mad Libs program in Python is a beginner coding project where the computer asks the user to input random words like nouns, verbs, or adjectives, and then places those words into a blank story template to create a funny result
adjective = input("Enter an adjective (describing word): ")
noun = input("Enter a noun (person, place, or thing): ")
verb = input("Enter a verb (action word): ")
place = input("Enter a place: ")

# 2. Combine the inputs into a story using an f-string
story = f"Once upon a time, a {adjective} {noun} decided to {verb} all the way to {place}."

# 3. Print the final result
print("\n--- Here is your Mad Libs Story! ---")
print(story)
