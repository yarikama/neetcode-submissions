from collections import deque

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])

        hash_board = {}

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] not in hash_board:
                    hash_board[board[row][col]] = []
                hash_board[board[row][col]].append((row,col))

        ans = []
        for word in words:
            if self.findWord(board, word, hash_board):
                ans.append(word)

        return ans

    def findWord(self, board: List[List[str]], word: str, hash_board: dict) -> bool:
        if word[0] not in hash_board:
            return False

        locations = hash_board[word[0]]

        for r, c in locations:
            if self.bfs(board, r, c, word):
                return True

        return False

    def bfs(
        self, 
        board: List[List[str]], 
        r_start: int, 
        c_start: int, 
        word: str,
    ) -> bool:

        ROWS, COLS = len(board), len(board[0])
        loc = (r_start, c_start)

        visit = set()
        visit.add(loc)
        
        queue = deque()
        queue.append(loc)

        length = 1
        neighbors = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        while queue:
            for i in range(len(queue)):
                if length == len(word):
                    return True

                r, c = queue.popleft()

                for dr, dc in neighbors:
                    nr = dr + r
                    nc = dc + c

                    if (
                        nr < 0 
                        or nc < 0 
                        or nr == ROWS 
                        or nc == COLS
                        or (nr, nc) in visit
                        or board[nr][nc] != word[length] 
                    ):
                        continue

                    queue.append((nr, nc))
                    visit.add((nr, nc))
            length += 1

        return False
                





