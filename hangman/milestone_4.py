import random

class Hangman:
    """
    Hangman(word_list : list)

    This class is used to represent the Hangman game

    Attributes:
        word (str): a randomly chosen word from the list given when the class is initialised
        word_guessed (list): initialised to be a list containing the same number of underscores as the length of the word
        num_letters (int): the number of unique letters in the word that haven't been guessed yet
        num_lives (int): the number of lives a player gets at the start of the game, default value = 5
        word_list (list): a list of words
        list_of_guesses (list): a list of guesses that have already been tried
    """

    def __init__(self, word_list, num_lives=5):
        """ See help(Hangman) for accurate information"""
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len([a for a in self.word if a not in self.word_guessed])
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []


    def check_guess(self,guess):
        """
        This function is used to check if the user guess is in the word or not

        Args:
            guess (str): The user input to be compared with the characters in the word

        """
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for w in self.word:
                if guess == w:
                    i = self.word.find(guess)
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word")
            print(f"You have {self.num_lives} lives left")
            

    def ask_for_input(self):
        """
        This function asks the user to guess a letter
        """
        valid = True
        while valid:
            guess = input("Guess a letter: ")
            if guess.isalpha() != True or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)


hman = Hangman(["apple", "banana", "watch"])
hman.ask_for_input()
