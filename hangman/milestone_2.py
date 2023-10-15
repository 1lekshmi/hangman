import random

word_list = ["watermelon", "lychee", "mango", "apple", "pomegranate"]
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Enter a letter: ")
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")