# Learning Classes and Objects by Building a Sudoku Solver

class Board:
    """
    Stores methods and functons to solve Sudoku
    """
    def __init__(self, board):
        """
        Initializes the board for a object with a puzzle

        Args:
            :self: The current instance of the class automatically passed
            :board: 
        """
        self.board = board

    def __str__(self):
        """
        Changes the look of the sudoku objects into strings
        Args:
            :self: The current instance of the class automatically passed
        """
        # Storing the custom string representation to return
        board_str = ''
        # Iterating over rows in the beard
        for row in self.board:
            # Turns each item i in row into a string using list comprehension
            # Give a string only when item is not zero, give '*' otherwise
            row_str = ' '.join([str(i) if i != 0 else '*' for i in row])
            # Adding up all the string with a space inbetween using .join()
            board_str += ' '.join(row_str)
            board_str += '\n' # Adding a new line character

        return board_str

    def find_empty_cell(self):
        """
        Finding an empty cell(the ones with '0' placeholder)

        Args:
            :self: The current instance of the class automatically passed
        """
        for row, contents in enumerate(self.board):
            try:
                # Locating the empty cell, the one with '0' placeholder
                col = contents.index(0)
                # Retuning the row and column index of the empty cell as a tuple
                return row, col
            except ValueError: # If the value is not found
                # 'pass' statement keeps the code running
                pass
        # Returning 'None' in which no empty cell is found
        return None

    def valid_in_row(self, row, num):
        """
        Checks if a given number can be inserted into a specified row 
        of the sudoku board

        Args:
            :self: The current instance of the class automatically passed
            :row: Row Index
            :num: The number to be checked
        """
        # If num is not in row, expression evaluates to True, 
        # it means number is valid for insertion, else it evaluates to False,
        # insertion would violate the rules
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        """
        Checks if a given number can be inserted into a specified column
        of the sudoku board

        Args:
            :self: The current instance of the class automatically passed
            :col: Column Index
            :num: The number to be checked
        """
        # Generates a list of value representing whether the condition 
        # is True or False for all the elements in the specified column
        return all(self.board[row][col] != num for row in range(9))

    def valid_in_square(self, row, col, num):
        """
        Checks if a number can be inserted in a 3x3 square

        Args:
            :self: The current instance of the class automatically passed
            :row: Row Index
            :col: Column Index
            :num: The number to be checked
        """
        # Storing row index for each 3x3 square
        row_start = (row // 3) * 3
        # Storing column index for each 3x3 square
        col_start = (col // 3) * 3

        # Iterating over the rows and columns inside the 3x3 square
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                # Checking if number in the current cell of the sudoku board == num
                if self.board[row_no][col_no] == num:
                    return False
        return True

    def is_valid(self, empty, num):
        """
        Checks if a given number is valid choice for an empty cell
        in the sudoku board by validating its compatibility with the row

        Args:
            :self: The current instance of the class automatically passed
            :empty: Tuple representing the row and column indices of an empty cell
            :num: The number to be checked
        """
        # Unpacking the 'empty' tuple into row and col
        row, col = empty
        # Checking if the number is valid for inserting
        # in the specified row, column, 3x3 square
        valid_in_row = self.valid_in_row(row, num) # Calling the valid_in_row method
        valid_in_col = self.valid_in_col(col, num) # Calling the valid_in_col method
        valid_in_square = self.valid_in_square(row, col, num) # Calling the valid_in_square method

        # Returning the validations from all the checks
        return all([valid_in_row, valid_in_col, valid_in_square])

    def solver(self):
        """
        Attempts to solve the sudoku in-place.
        Modifies the existing sudoku board rather than creating a new one.

        Args:
            :self: The current instance of the class automatically passed
        """
        # Checking if there are no empty cells to fill in
        # Storing self.find_empty_cell() to next_empty
        if (next_empty := self.find_empty_cell()) is None:
            # If none, the board is already solved
            return True

        # Looping from 1 to 9 to check if any of the number to fill the empty cell
        for guess in range(1, 10):
            # Checks if the number is a valid choice for the current cell
            if self.is_valid(next_empty, guess):
                # Unpacking tuple next_empty into row, col
                row, col = next_empty
                # Modifying the cell on the board at given row & column
                self.board[row][col] = guess
                # Making a recursive call
                if self.solver():
                    # Sudoku board is completely solve
                    return True
                # If the number tested in the cell doesn't work, restore it 0
                self.board[row][col] = 0

        # Returns the default result
        return False

def solve_sudoku(board):
    """
    Relays message on the puzzle, lets you know whether
    the puzzle is solveable or not

    Args:
        :board: The puzzle entered to solve
    """
    gameboard = Board(board)
    print(f"Puzzle to solve:\n{gameboard}")
    if gameboard.solver():
        print(f"Solved puzzle:\n{gameboard}")
    else:
        print("The provided puzzle is unsolvable.")

    return gameboard


if __name__ == "__main__":
    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]
    solve_sudoku(puzzle)
