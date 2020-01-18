from unittest.mock import patch
import random

import pytest
from guess import get_random_number, Game

@patch.object(random, 'randint')
def test_get_random_number(m):
    m.return_value = 17
    assert get_random_number() == 17

@patch("builtins.input", side_effect=[11, '12', 'bob', 12,
                                       5, -1, 21, 7, None])
def test_game(inp):
    game = Game()
    # Good guesses
    assert game.guess() == 11
    assert game.guess() == 12
    # Not a number
    with pytest.raises(ValueError):
        game.guess()
    # Alread guessed 12
    with pytest.raises(ValueError):
        game.guess()
    # Good
    assert game.guess() == 5
    # Out of range values
    with pytest.raises(ValueError):
        game.guess()
    with pytest.raises(ValueError):
        game.guess()
    # Good
    assert game.guess() == 7
    # User hit enter
    with pytest.raises(ValueError):
        game.guess()

def test_validate_guess(capfd):
    game = Game()
    game._answer = 2

    assert not game._validate_guess(1)
    out, _ = capfd.readouterr()
    assert out.rstrip() == '1 is too low'

    assert not game._validate_guess(3)
    out, _ = capfd.readouterr()
    assert out.rstrip() == '3 is too high'

    assert game._validate_guess(2)
    out, _ = capfd.readouterr()
    assert out.rstrip() == '2 is correct!'

@patch("builtins.input", side_effect=[4, 22, 9, 4, 6])
def test_game_win(inp, capfd):
    game = Game()
    game._answer = 6

    game()
    assert game._win is True

    out = capfd.readouterr()[0]
    expected = ['4 is too low', 'Number not in range',
                '9 is too high', 'Already guessed',
                '6 is correct!', 'It took you 3 guesses']
    output = [line.strip() for line in out.split('\n') if line.strip()]
    for line, exp in zip(output, expected):
        assert line == exp

@patch("builtins.input", side_effect=[None, 5, 9, 14, 11, 12])
def test_game_lose(inp, capfd):
    game = Game()
    game._answer = 13

    game()
    assert game._win is False