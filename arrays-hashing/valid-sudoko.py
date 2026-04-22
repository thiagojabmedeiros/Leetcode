def validSudoku(board):
    rows = [set() for i in range(9)]
    columns = [set() for i in range(9)]
    boxes = [set() for i in range(9)]
    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            b = ((r // 3) * 3) + (c // 3) 
            if board[r][c] in rows[r] or board[r][c] in columns[c] or board[r][c] in boxes[b]:
                return False
            rows[r].add(board[r][c])
            columns[c].add(board[r][c])
            boxes[b].add(board[r][c])
    return True

board = [["1","2",".",".","3",".",".",".","."],
         ["4",".",".","5",".",".",".",".","."],
         [".","9","8",".",".",".",".",".","3"],
         ["5",".",".",".","6",".",".",".","4"],
         [".",".",".","8",".","3",".",".","5"],
         ["7",".",".",".","2",".",".",".","6"],
         [".",".",".",".",".",".","2",".","."],
         [".",".",".","4","1","9",".",".","8"],
         [".",".",".",".","8",".",".","7","9"]]

validSudoku(board)