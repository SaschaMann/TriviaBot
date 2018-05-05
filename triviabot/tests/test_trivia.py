from ..trivia import *


# TriviaGame tests
def test_trivia_game():
    test_game = TriviaGame()

    # default values
    assert not test_game.active
    assert test_game.question == test_game.answer == ''
    assert test_game.last_round == 0.0

    # question and answer
    test_game.question = 'What is the answer to the ultimate question of life, the universe, and everything?'
    test_game.answer = '42'
    assert not test_game.check_answer('43')
    assert test_game.check_answer('42')

    # reset
    test_game.reset()
    assert not test_game.active
    assert test_game.question == test_game.answer == ''
