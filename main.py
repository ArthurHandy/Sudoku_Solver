import time
import sys
import numpy as np
import pyautogui as pg


class SudokuSolver:
    def __init__(self):
        # initialize grid with 9 rows and 9 columns all with zeros
        self.grid = np.array(np.zeros((9, 9), dtype=int))
        self.user_input()

    def user_input(self):
        """
        Takes input from the user to input 9 rows.
        """
        row_number = 1

        # Taking user input for 9 rows
        while True:
            row = list(input("Enter the row: "))
            ints = [int(n) for n in row if n.isdigit()]

            if len(ints) > 9 or len(ints) < 9:
                print("Your row is greater or less than 9 numbers. Row should only contain exactly 9 numbers.")
                continue

            for i in ints:
                self.grid[row_number - 1][ints.index(i)] = i
            print(f"Row {row_number} filled")

            # When row 9 is reached, print final matrix and break out of while loop
            if row_number == 9:
                print("All grids filled")
                print("Printing all 9 rows")
                print(np.matrix(self.grid))
                print("Click on the top left of sudoku puzzle grid to start solver")
                break
            row_number += 1

    def _fill(self, matrix):
        """
        Sudoku.com puzzle being filled in with numbers to complete the puzzle.

        :param matrix: int - Matrix of numbers.
        """
        # Appending matrix to final
        final = [matrix[i] for i in range(9)]

        # For each list in final and for each number in the list, append str_fin and convert to number
        string_final = [str(num) for lists in final for num in lists]

        counter = []

        # Move to the right 9 times
        for num in string_final:
            pg.press(num)
            pg.hotkey("right")
            counter.append(num)
            # When the length of counter is divisible by 9, go down 1
            if len(counter) % 9 == 0:
                pg.hotkey("down")
                # Move to the left 9 times
                for _ in range(9):
                    pg.hotkey("left")

    def _possible(self, row, column, number):
        """
        Checking row, column, and a 3x3 square if a number is possible.

        :param row: int - Row coordinate on the Sudoku board
        :param column: int - Column coordinate on the Sudoku board
        :param number: int - Number of a given coordinate

        :return: bool - Whether a number can be placed
        """
        # Checking row if a number exists
        for i in range(0, 9):
            if self.grid[row][i] == number and i != column:
                return False

        # Checking column if a number exists
        for i in range(0, 9):
            if self.grid[i][column] == number and i != row:
                return False

        # Where the square grid will start
        x0 = row - row % 3
        y0 = column - column % 3
        for i in range(0, 3):
            for j in range(0, 3):
                if self.grid[x0 + i][y0 + j] == number:
                    return False

        return True

    def solve(self):
        """
        Using backtracking algorithm to solve the sudoku puzzle.

        :return: bool - Determines whether the Sudoku puzzle can be solved.
        """
        for row in range(0, 9):
            for column in range(0, 9):
                # If number is zero, figure out what to replace 0 with
                if self.grid[row][column] == 0:
                    # Number will be between 1 - 9
                    for number in range(1, 10):
                        if self._possible(row, column, number):
                            self.grid[row][column] = number
                            # Backtracking
                            self.solve()
                            # Number is wrong, set it back to 0
                            self.grid[row][column] = 0
                    return

        self._fill(self.grid)
        print("Sudoku puzzle solved!")
        print(np.matrix(self.grid))
        sys.exit()

# Program start
if __name__ == "__main__":
    solver = SudokuSolver()
    # Gives 5 secs to click the first cell of sudoku puzzle
    time.sleep(5)
    print("Working on solution")
    solver.solve()

