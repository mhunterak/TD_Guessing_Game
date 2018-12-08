"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
by Maxwell Hunter
--------------------------------
"""

import os
import random


# function for clearing console
def clear_screen():
    os.system("clear")


# EXTRA CREDIT
# As a player of the game, after I guess correctly I should be prompted if I
# would like to play again.
# function for asking if the player wants to play another round.
# returns True if the user enters a y, Y, or a blank
# returns False if the user enters an n, or N
def play_again():
    # start with blank string
    play_again = ""
    # while they haven't  a valid string:
    while play_again == "":
        # prompt user to play again
        play_again = input("Would you like to play again? Y/N > ")
        try:
            # if they enter a y, Y, or a word that starts with one of those
            if play_again[0] in ['y', 'Y']:
                # return True
                return True
            # if they enter an N, n, or a word that starts with one of those
            elif play_again[0] in ['n', 'N']:
                clear_screen()
                # return False
                return False
        # an IndexError indicates a blank  string.
        # we're assuming this means they want to play again.
        except IndexError:
            return True


# get a random number between 1 and 10
def randomize():
    return random.randint(1, 10)


def start_game(LOW_SCORE=999):  # pragma: no cover (tested manually)
    # clear the screen for a new game
    clear_screen()
    # 1. Display an intro/welcome message to the player.
    print("Welcome to Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")

    # EXTRA CREDIT
    # As a player of the game, at the start of each game I should be shown the
    # current high score (least amount of points), so that I know what I am
    # supposed to beat.
    print("Can you beat the current low score of {}?".format(LOW_SCORE))
    # instantiate new Game
    game = Game()
    # randomize secrent number (make a new guess)
    game.secret = randomize()
    # while they haven't correctly guessed the number
    try:
        while game.test_guess_matches_secret(
            # print a guess prompt message
            input(("What number am I thinking of? > "))
                ) is False:
                    # print the number of guesses
                    print("You've made {} guesses so far.".format(
                        # increment the guess counter
                        game.increment_guess_counter()
                        ))
        # if that game set a new record, return the game score
        if game.guess_counter < LOW_SCORE:
            print("You got the new low score!")
            return game.guess_counter
        # otherwise, return the previous low score
        else:
            return LOW_SCORE
    except ValueError:
        pass


# the Game class will hold the secret number,
# and a counter for the number of guesses so far
class Game(object):
    # 2. Store a random number as the answer/solution.
    secret = randomize()
    # guess counter starts at 0
    guess_counter = 0

    # add 1 to the guess counter
    def increment_guess_counter(self):
        # increment counter
        self.guess_counter += 1
        # return the counter
        return self.guess_counter

    # test the supplied guess against the secret number
    def test_guess_matches_secret(
        # as a class method, import the instance for comparisons
        self,
        new_guess,  # type: string
            ):
        # clear screen
        clear_screen()

        # EXTRA CREDIT
        # As a player of the game, my guess should be within the number range.
        # If my guess is outside the guessing range
        # I should be told to try again.
        if int(new_guess) > 10 or int(new_guess) < 1:
            print("Your guess is outside the range I was thinking of. (1-10)")

        # if they guessed correctly,
        if self.secret == int(new_guess):
            # 4. Once the guess is correct, stop looping,
            # inform the user they "Got it"
            print("Got it, the secret number was {}!".format(
                # print the secret number
                self.secret
                ))
            # print the number of guesses
            print("it only took you {} tries.".format(
                self.increment_guess_counter()
                ))
            # The guess was correct, return True
            return True
        # if they guessed incorrectly,
        else:
            # display fail message
            print("Nope! {} is not the right number.".format(new_guess))
            # 3a. If the guess greater than the solution,
            if int(new_guess) > self.secret:
                # display to the player "It's lower than your guess".
                print("It's lower than {}.".format(new_guess))
            # 3b. If the guess is less than the solution,
            else:  # If it's not a correct guess and it's not lower
                # display to the player "It's higher than your guess".
                print("It's higher than {}.".format(new_guess))
            # The guess was not correct, return False
            return False


if __name__ == '__main__':  # pragma: no cover
    # Kick off the program by calling the start_game function.
    LOW_SCORE = start_game()
    # after the game is over, ask them if they want to play again
    while play_again():
        # instantiate new Game
        LOW_SCORE = start_game(LOW_SCORE)
    # 5. Let the player know the game is ending,
    # or something that indicates the game is over.
    print("Thanks for playing!")
