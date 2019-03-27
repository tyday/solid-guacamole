from grid_search import contains_word, check_grid
import pytest

grid = [['F', 'A', 'C', 'I'],
        ['O', 'B', 'Q', 'P'],
        ['A', 'N', 'O', 'B'],
        ['M', 'A', 'S', 'S']]

def test_contains_word():    
    assert contains_word(grid, 'MASS') == True
    assert contains_word(grid, 'MSS') == False
def test_check_grid():
    assert check_grid(grid, 'FOAM') == True
    assert check_grid(grid, 'foam') == False
    assert check_grid(grid, 'FOAL') == False

