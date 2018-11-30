# sudoku-solver
A python program that solves sudoku puzzles.

I use simple set arithmetic to preprocess the puzzle and find possible candidates for each cell,
and I use backtracking to solve the puzzle.

Possible improvements:
  - Support variable sized boards (currently only 9x9)
  - Support variable sized boxes (currently only 3x3)
  - GUI (definitely not going to happen lol)
  
This is from LeetCode. https://leetcode.com/problems/sudoku-solver/
