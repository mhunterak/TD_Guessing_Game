import guessing_game
import os
import unittest


class test_(unittest.TestCase):
    def test_play_again(self):
        __builtins__.raw_input = lambda _: 'Y'
        self.assertTrue(guessing_game.play_again())
        __builtins__.raw_input = lambda _: 'y'
        self.assertTrue(guessing_game.play_again())
        __builtins__.raw_input = lambda _: 'yes!'
        self.assertTrue(guessing_game.play_again())
        __builtins__.raw_input = lambda _: ''
        self.assertTrue(guessing_game.play_again())
        __builtins__.raw_input = lambda _: 'N'
        self.assertFalse(guessing_game.play_again())
        __builtins__.raw_input = lambda _: 'n'
        self.assertFalse(guessing_game.play_again())
        __builtins__.raw_input = lambda _: 'no'
        self.assertFalse(guessing_game.play_again())

    def test_randomize(self):
        self.assertTrue(guessing_game.randomize() > 0)
        self.assertTrue(guessing_game.randomize() < 11)

    def test_Game_class(self):
        game = guessing_game.Game()
        self.assertTrue(game.secret < 11)
        self.assertTrue(game.guess_counter == 1)
        self.assertTrue(game.increment_guess_counter() > 0)
        self.assertFalse(game.test_guess_matches_secret('35'))

    def test_Game_test_guess_matches_secret(self):
        game = guessing_game.Game()
        game.secret = 5
        self.assertFalse(game.test_guess_matches_secret('3'))
        self.assertFalse(game.test_guess_matches_secret('8'))
        self.assertTrue(game.test_guess_matches_secret('5'))


if __name__ == '__main__':
    os.system("clear")
    unittest.main(verbosity=2)
