import pytest

import gs2
from gs2.problem1 import solution as problem1


"""
1) Wendy and Bob are playing a simple game. It's your job to predict the winner.

The game involves removing white 'w', or black 'b' game pieces from a line. We'll represent the line of pieces as a string. e.g. "wwbbbbwww".

Wendy will remove white pieces and Bob will remove the black pieces. Wendy will always go first.

A game piece can only be removed if there are two pieces of the same color on either side of it. e.g. Wendy could remove a piece from "wwwb" and "bbbwwww" but not "ww" or "wwbbbbw".

The last player who is able to remove a piece wins. Your function should return the name of the winner, either "Wendy" or "Bob".

This comes from my hackerrank assessment (round 1) for FactSet, this was the question I did in haskell.
"""


@pytest.fixture
def solution():
    solution = problem1.Solution(1, "Wendy and Bob game", "Easy")
    return solution


def test_bs_between_ws(solution):
    """
    ("wwwbbbbwww","Bob")
    """
    expected = "Bob"
    actual =  solution.winner("wwwbbbbwww")
    # print('actual:{0} '.format(actual))
    assert actual == expected

def test_bs_between_ws(solution):
    """
    ("www","Wendy")
    """
    expected = "Wendy"
    actual =  solution.winner("www")
    # print('actual:{0} '.format(actual))
    assert actual == expected    