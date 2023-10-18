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
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

        print(f"The mistery word has {len(self.word)} characters")
        print(f"{self.word_guessed}")


    def check_guess(self,guess):
        """
        This function is used to check if the user guess is in the word or not

        Args:
            guess (str): The user input to be compared with the characters in the word

        """
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for j in range(len(self.word)):
                if self.word[j] == guess:
                    self.word_guessed[j] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word")
            print(f"You have {self.num_lives} lives left")
            

    def ask_for_input(self):
        """
        This function asks the user to guess a letter
        """
        while True:
            guess = input("Guess a letter: ")
            if guess.isalpha() == False or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
    
def play_games(word_list):
    game = Hangman(word_list,num_lives=5)

    while True:

        if game.num_lives == 0:
            print(f"You lost! The word was {game.word}")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break

if __name__ == "__main__":
    word_list = ["apple", "banana", "orange", "pear", "strawberry", "watermelon"]
    play_games(word_list)