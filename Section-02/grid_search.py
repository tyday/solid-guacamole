# Given a 2D matrix of characters and a target word, write a function that 
# returns whether the word can be found in the matrix by going 
# left-to-right, or up-to-down.

# For example, given the following matrix:

# [['F', 'A', 'C', 'I'],
#   ['O', 'B', 'Q', 'P'],
#   ['A', 'N', 'O', 'B'],
#   ['M', 'A', 'S', 'S']]
# and the target word 'FOAM', you should return true, since it's the 
# leftmost column. Similarly, given the target word 'MASS', you should 
# return true, since it's the last row.

def contains_word(rows, word):
    for row in rows:
        if word in "".join(row):
            return True
    return False
def check_grid(grid,word):
    turnedlist = list(zip(*grid))
    if contains_word(grid,word):
        return True
    elif contains_word(turnedlist,word):
        return True
    else:
        return False

if __name__=="__main__":
    grid = [['F', 'A', 'C', 'I'],
            ['O', 'B', 'Q', 'P'],
            ['A', 'N', 'O', 'B'],
            ['M', 'A', 'S', 'S']]
    # print(contains_word(grid,'MASS'))
    # print(contains_word([['M', 'A', 'S', 'S'],[]], 'MASS'))
    print(check_grid(grid, 'FOAM'))