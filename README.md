# Game of Life

This repository contains graphical way of dislpaying [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).

> **Used libraries**
> 
    - numpy
    - matplotlib
        - pyplot
        - animations
    - tkinter
    - os

It is possible to load predefined patterns from *sample_patterns* folder or create completly new boards by stating it's size
With the use of Tkinter, user inputs the name of file, or size of the randomly generated board in configuration window.

If you'd like to create new pattern, for dead cells use `.` and for live ones use `X`. Don't put new line at the end, because of the way this program calculates height of the board

It is advised **not to put commas in the name of your new patterns**, because it will not work and probably cause error.

<hr/>

> life.py
> 
    This is the main file, which includes code for creating configuration window, and animation process.
> calculations.py
> 
    This file handles the games logic, calculating number of cell's neighbours,
    and deciding which one lives of dies (or in this case changes from 1 to 0)
> start.py
> 
    This file is responsible for reading text files of predetermined 
    patterns and pseudo-randomly creating new ones
