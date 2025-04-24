# Maze Solver

This Python project generates and solves mazes using a graphical interface built with Tkinter.

## Features

* **Maze Generation:** Implements a randomized depth-first search algorithm to create unique and solvable mazes.
* **Customizable Maze Size:** Easily configure the number of rows and columns for the maze.
* **Visual Generation:** The maze generation process is visualized step-by-step.
* **Entrance and Exit:** Clearly defines the entrance at the top-left and the exit at the bottom-right of the maze.
* **Maze Solving:** Employs a recursive depth-first search algorithm to find a path from the entrance to the exit.
* **Visual Solving:** The maze-solving process is visualized, showing the path being explored and backtracking when necessary.
* **Consistent Randomness (Optional):** Provides an option to seed the random number generator for consistent maze generation during development and debugging.

## Getting Started

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/GitOutlaw/maze_solver.git](https://github.com/GitOutlaw/maze_solver.git)
    cd maze_solver
    ```

2.  **Ensure you have Python 3 installed.**

3.  **Run the `main.py` file:**
    ```bash
    python main.py
    ```
    This will open a window displaying the generated maze and the solver in action.

## Project Structure


maze_solver/
├── cell.py       # Defines the Cell class representing individual cells in the maze.
├── graphics.py   # Contains the Window, Point, and Line classes for the graphical interface.
├── maze.py       # Implements the Maze class with maze generation and solving logic.
├── main.py       # The main entry point to run the maze generator and solver.
├── tests.py      # Unit tests for the Maze class.
└── README.md     # This file.


## Dependencies

* **Tkinter:** Used for creating the graphical user interface. This is usually included with standard Python installations.
* **random:** For random maze generation.
* **time:** To control the animation speed.
* **unittest:** For running unit tests.

## Usage

Modify the parameters in the `main()` function in `main.py` to customize the maze:

```python
def main():
    num_rows = 10
    num_cols = 10
    cell_size = 50
    win_width = 800
    win_height = 600
    start_x = 50
    start_y = 50

    win = Window(win_width, win_height)
    maze = Maze(start_x, start_y, num_rows, num_cols, cell_size, cell_size, win, seed=0) # Optional seed
    print("Maze Solved:", maze.solve())
    win.wait_for_close()

    num_rows: The number of rows in the maze.

    num_cols: The number of columns in the maze.

    cell_size: The size (width and height) of each cell in pixels.

    seed: An optional integer to seed the random number generator for consistent maze generation. Remove or set to None for fully random mazes.

Running Tests

To run the unit tests, navigate to the project directory in your terminal and execute:

python tests.py

This will run the tests defined in tests.py to ensure the Maze class is functioning correctly.
Ideas for Extending the Project

    Add other solving algorithms, like breadth-first search or A*

    Make the visuals prettier, change the colors, etc

    Mess with the animation settings to make it faster/slower. Maybe make backtracking slow and blazing new paths faster?

    Add configurations in the app itself using Tkinter buttons and inputs to allow users to change maze size, speed, etc

    Make much larger mazes to solve

    Make it a game where the user chooses directions

    If you made it a game, allow the user to race an algorithm

    Make it 3 dimensional

    Time the various algorithms and see which ones are the fastest

Contributing

Contributions to this project are welcome. Feel free to open issues for bug reports or feature requests, or submit pull requests with your changes.
License

This project is open source and available under the MIT License. (Add a `LICENSE