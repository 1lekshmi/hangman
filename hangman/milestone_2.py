import random

# list of fruits
word_list = ["watermelon", "lychee", "mango", "apple", "pomegranate"]
print(word_list)

# random word from the list
word = random.choice(word_list)
print(word)

# asking the user for a guess
guess = input("Enter a letter: ")

# conditions to validate the "guess" input
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")