# Sudoku_Solver
- Are you having trouble solving a sudoku puzzle? Sudoku_Solver can help you when you're stuck. By typing in each filled and empty column and row, you are able to watch the magic happen.

- What is Sudoku? Sudoku is a popular puzzle game that is required to fill a 9 x 9 grid with numbers in each column and row. In each of the 9 x 9 grids there are subs grids of 3 x 3 that must contain a single copy of a number from 1 to 9. 

- Sudoku_Solver fills in each blank spot from left to right, until your sudoku puzzle is full of numbers. 

https://user-images.githubusercontent.com/71150400/228752518-1d57e9d2-34d7-47f2-acc8-5b308b56e34a.mp4

## Prerequisites
Make sure to keep up to date with Python latest version:
```
Python 3.10 or up
```

Have all correct packages downloaded:
```
pip install -r requirement.txt
```

## Installing
PyAutoGUI on Windows:
```
py -m pip install pyautogui
```

PyAutoGUI on macOS:
```
python3 -m pip install pyautogui
```

PyAutoGUI Linux:
```
python3 -m pip install pyautogui
```

Clone the repository:
```
git clone https://github.com/ArthurHandy/Sudoku_Solver.git
```

## Running Program
Run Sudoku_Solver:
```
python main.py
```

- Head over to [Sudoku.com](https://sudoku.com) and select a difficulty to solve.

- Then go to `Sudoku_Solver` and run the program. Type in each `column and row`. If a cell is empty, insert 0 and don't forget to leave a space between each number inputed to help visual the puzzle better. Only 9 numbers can be inputed, if more or less than 9 numbers, an error message will be displayed.

- When done, you have `5 seconds to left click the top left cell from [Sudoku.com](https://sudoku.com)`. Boom! You're done! Watch as each empty column and row is filled automatically.

- Below is a step by step process of running Sudoku_Solver.

https://user-images.githubusercontent.com/71150400/228759458-2671edd7-6fc0-4ab5-b343-8b61cb8fe30f.mp4

## Built With
- [Python](https://python.org) - Programming language used
- [PyAutoGUI](https://github.com/asweigart/pyautogui) - Cross-platform GUI automation Python module that is used to control the mouse and keyboard
- [NumPy](https://numpy.org/) - Python library used to help with large array of 9 columns and 9 rows
- [time](https://docs.python.org/3/library/time.html) - Python library used to give user time to click on first cell of sudoku puzzle
- [sys](https://docs.python.org/3/library/sys.html) - Python module used to exit the program
