"""
You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

i.   Each row must contain the digits 1-9 without duplicates.
ii.  Each column must contain the digits 1-9 without duplicates.
iii. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.
"""

def isValidSudoku(board:list[list[str]]) -> bool:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    
    for i in range(9):
        for j in range(9):
            val = board[i][j]
            if val == ".":
                continue
            
            box_id = (i // 3)*3 + (j // 3)
            
            if val in rows[i] or val in cols[j] or val in boxes[box_id]:
                return False
            
            rows[i].add(val)
            cols[j].add(val)
            boxes[box_id].add(val)
        
    print(boxes)
    return True


isValidSudoku([["1","2",".",".","3",".",".",".","."],["4",".",".","5",".",".",".",".","."],[".","9","8",".",".",".",".",".","3"],["5",".",".",".","6",".",".",".","4"],[".",".",".","8",".","3",".",".","5"],["7",".",".",".","2",".",".",".","6"],[".",".",".",".",".",".","2",".","."],[".",".",".","4","1","9",".",".","8"],[".",".",".",".","8",".",".","7","9"]])