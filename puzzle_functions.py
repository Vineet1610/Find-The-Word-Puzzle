""" Where's That Word? functions. """

# The constant describing the valid directions. These should be used
# in functions get_factor and check_guess.
UP = 'up'
DOWN = 'down'
FORWARD = 'forward'
BACKWARD = 'backward'

# The constants describing the multiplicative factor for finding a
# word in a particular direction.  This should be used in get_factor.
FORWARD_FACTOR = 1
DOWN_FACTOR = 2
BACKWARD_FACTOR = 3
UP_FACTOR = 4

# The constant describing the threshold for scoring. This should be
# used in get_points.
THRESHOLD = 5
BONUS = 12

# The constants describing two players and the result of the
# game. These should be used as return values in get_current_player
# and get_winner.
P1 = 'player one'
P2 = 'player two'
P1_WINS = 'player one wins'
P2_WINS = 'player two wins'
TIE = 'tie game'

# The constant describing which puzzle to play. Replace the 'puzzle1.txt' with
# any other puzzle file (e.g., 'puzzle2.txt') to play a different game.
PUZZLE_FILE = 'puzzle1.txt'


# Helper functions.  Do not modify these, although you are welcome to
# call them.

def get_column(puzzle: str, col_num: int) -> str:
    """Return column col_num of puzzle.

    Precondition: 0 <= col_num < number of columns in puzzle

    >>> get_column('abcd\nefgh\nijkl\n', 1)
    'bfj'
    """

    puzzle_list = puzzle.strip().split('\n')
    column = ''
    for row in puzzle_list:
        column += row[col_num]

    return column


def get_row_length(puzzle: str) -> int:
    """Return the length of a row in puzzle.

    >>> get_row_length('abcd\nefgh\nijkl\n')
    4
    """

    return len(puzzle.split('\n')[0])


def contains(text1: str, text2: str) -> bool:
    """Return whether text2 appears anywhere in text1.

    >>> contains('abc', 'bc')
    True
    >>> contains('abc', 'cb')
    False
    """

    return text2 in text1


# Implement the required functions below.

def get_current_player(player_one_turn: bool) -> str:
    """
    Return 'player one' iff player_one_turn is True; otherwise, return
    'player two'.
    
    Precondition: player_one_turn should be boolean value
    
    >>> get_current_player(True)
    'player one'
    >>> get_current_player(False)
    'player two'
    """
    
    if player_one_turn:
        return P1
    
    else:
        return P2
    
def get_winner(player1: int, player2: int) -> str:
    """ 
    Returns which player wins by comparing the scores of each player
    
    Precondition: player1 >= 0 and player2 >= 0
    
    >>> get_winner(30, 20)
    'player one wins'
    >>> get_winner(25, 45)
    'player two wins'
    >>> get_winner(25, 25)
    'tie game
    """
    
    if player1 > player2:
        return P1_WINS
    
    elif player1 == player2: 
        return TIE
    
    else:
        return P2_WINS
    
def reverse(reverse_of_string: str) -> str:
    """ 
    Reverse the string that is given
    
    Precondition: '' required for every string
    
    >>>reverse('vineet')
    teeniv
    """
    
    return reverse_of_string[-1::-1]

def get_row(puzzle: str, row_number: int) -> str:
    """ 
    The letters of the row, that is called, should be returned and
    the newline character should not be returned
    
    Precondition: 0 < row_number <= number of rows in puzzle
    
    >>>get_row('abcd\nefgh\nijkl\n', 1)
    efgh
    """
    
    rowlength = get_row_length(puzzle) #Gets the length of the row
    
    first = row_number * (rowlength + 1) #Gets the first letter of the row
    
    last = first + rowlength #Gets the last letter of the row
    
    return puzzle[first:last:1]
    
def get_factor(direction: str) -> int:
    """ 
    For the given direction of word, return the multiplcative
    factor of that given direction
    
    Precondition: direction = UP or DOWN or BACKWARDS or FORWORD
    
    >>>get_factor(UP)
    4
    """
    
    if direction == UP:
        return UP_FACTOR
    
    elif direction == DOWN:
        return DOWN_FACTOR
    
    elif direction == FORWARD:
        return FORWARD_FACTOR
    
    elif direction == BACKWARD:
        return BACKWARD_FACTOR
    
    else:
        return "INVALID INPUT"
    
def get_points(direction: str, words_left: int) -> int:
    """ 
    Return the points that the player has earned by selecting the 
    word in the direction
    
    Precondition: 0 < words_left <= total words
    
    >>>get_points(BACKWARD, 2)
    24
    """
    
    #It gives multiplicative factor of that direction
    direction_factor = get_factor(direction) 
    
    if THRESHOLD <= words_left:
        return THRESHOLD * direction_factor
    
    #Add Bonus when only 1 word is left
    elif words_left == 1:
        return (2 * THRESHOLD - words_left) * direction_factor + BONUS
    
    else:
        return (2 * THRESHOLD - words_left) * direction_factor
    
def check_guess(puzzle: str, direction: str, guessed_word: str, 
                row_column_number: int, words_left: int) -> int:
    """
    If the guessed word is found in the puzzle at the given row or column
    and in the given direction then return the points earned for that guess or 
    else Return 0
    
    Precondition: 0 < words_left <= total words, guessed_word should be from 
                  the list and 0 < row_column_number <= row number and 
                  0 < row_column_number <= column number
    
    >>>check_guess('abcd\nefgh\nijkl\n', FORWARD, 'abc', 0, 2)
    8
    """
    
    if direction == FORWARD or direction == BACKWARD:
        #Gets the whole row of the puzzle
        row = get_row(puzzle, row_column_number) 
                                                 
        #If the word is in backward direction then reverse the guessed word                                        
        if direction == BACKWARD:                
            guessed_word = reverse(guessed_word)
            
        if contains(row, guessed_word):
            points = get_points(direction, words_left)
            return points
        
        else:
            return 0
    
    elif direction == UP or direction == DOWN:
        #Gets the whole column of the puzzle
        column = get_column(puzzle, row_column_number)
        
        #If the word is in upward direction then reverse the guessed word
        if direction == UP:
            guessed_word = reverse(guessed_word)
            
        if contains(column, guessed_word):
            points = get_points(direction, words_left)
            return points
        
        else:
            return 0
        
    else:
        return 0