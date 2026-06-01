class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            s = set()
            for col in row:
                if col != '.' and col in s:
                    return False
                s.add(col)

        for i in range(9):
            s = set()
            for row in board:
                if row[i] != '.' and row[i] in s:
                    return False
                s.add(row[i])

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                s = set()
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        if board[k][l] != '.' and board[k][l] in s:
                            return False
                        s.add(board[k][l])
        
        return True
        