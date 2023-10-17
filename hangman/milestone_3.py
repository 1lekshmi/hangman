from random_word import RandomWords

# function to ask for input
def ask_for_input():
    valid = True
    while valid:
        guess = input("Enter a letter: ")
        if guess.isalpha() and len(guess) == 1:
            valid = False
        else:
            print("Invalid letter. Please, enter a single alphabetcal character.")
    check_guess(guess)

# function to check the input
def check_guess(guess):
    # Generating random word using RandomWords function from an imported package 'random_word'
    r = RandomWords()
    r_word = r.get_random_word()

    # checks to see if the inputted guess is in the word
    guess = guess.lower()
    if guess in r_word:
        print(f"Good guess! {guess} is in the word")
    else:
        print(f"Sorry, {guess} is not in the word. Try again")



ask_for_input()

