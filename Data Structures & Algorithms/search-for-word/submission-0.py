class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(wrd_idx: int, r: int, c: int) -> bool:
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or board[r][c] != word[wrd_idx]:
                return False

            if wrd_idx == len(word)-1:
                return True
            
            visited.add((r, c))

            flag: bool = (
                dfs(wrd_idx+1, r+1, c) or
                dfs(wrd_idx+1, r, c+1) or 
                dfs(wrd_idx+1, r-1, c) or
                dfs(wrd_idx+1, r, c-1)
            )

            visited.remove((r, c))

            return flag

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(0, r, c):
                    return True

        return False
        