# sudoku-solver
A python program that solves sudoku puzzles.

I use simple set arithmetic to preprocess the puzzle and find possible candidates for each cell,
and I use backtracking to solve the puzzle. I also use a double-ended queue for traversal (DFS).

Possible improvements:
  - Support variable sized boards (currently only 9x9)
  - Support variable sized boxes (currently only 3x3)
  - GUI (definitely not going to happen lol)
  
This challenge is from LeetCode; the solution is my own. https://leetcode.com/problems/sudoku-solver/
