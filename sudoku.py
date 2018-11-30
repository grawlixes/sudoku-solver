def solveSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    from collections import deque

    nxt = deque()
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                nxt.append((i, j))

    if not nxt:
        return

    NUMS = []
    possibilities = {}

    inRows = {i:set(board[i][j] for j in range(9))-set(['.']) for i in range(9)}
    inCols = {j:set(board[i][j] for i in range(9))-set(['.']) for j in range(9)}
    inBoxes = {}
    for IT in range(0, 9, 3):
        for j in range(3):
            inBoxes[(IT//3, j)] = set()
        for IT2 in range(0, 9, 3):
            for i in range(IT, 3+IT):
                for j in range(IT2, 3+IT2):
                    if board[i][j] != '.':
                        inBoxes[(IT//3, IT2//3)].add(board[i][j])

    def backtrack(i, j):
        choices = set(str(el) for el in range(1, 10)) - \
                 (inRows[i] | inCols[j] | \
                  inBoxes[(i//3, j//3)])
        if not choices:
            return False

        for choice in choices:
            board[i][j] = choice
            inRows[i].add(choice)
            inCols[j].add(choice)
            inBoxes[(i//3, j//3)].add(choice)
            if not nxt:
                return True

            nxt_i, nxt_j = nxt.popleft()
            success = backtrack(nxt_i, nxt_j)
            if success:
                return True

            board[i][j] = '.'
            inRows[i].remove(choice)
            inCols[j].remove(choice)
            inBoxes[(i//3, j//3)].remove(choice)
            nxt.appendleft((nxt_i, nxt_j))

        return False

    start = nxt.popleft()
    backtrack(start[0], start[1])

puzzle = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print("original sudoku:")
print(puzzle)
solveSudoku(puzzle)
print("solved sudoku:")
print(puzzle)
