class TrieNode:
    def __init__(self):
        self.is_word = False
        self.chil = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _insert(self, word: str):
        curr = self.root
        for c in word:
            if c not in curr.chil:
                curr.chil[c] = TrieNode()
            curr = curr.chil[c]
        curr.is_word = True

    def insert_batch(self, words: List[str]):
        for w in words: self._insert(w)


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Create a trie
        trie = Trie()
        trie.insert_batch(words)

        n, m = len(board), len(board[0])
        res = []
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def dfs(r: int, c: int, parent: TrieNode, word: str):
            char = board[r][c]
            node = parent.chil[char]
            word += char

            if node.is_word:
                node.is_word = False
                res.append(word)

            board[r][c] = " "
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if min(nr, nc) < 0 or nr >= n or nc >= m or board[nr][nc] not in node.chil:
                    continue
                dfs(nr, nc, node, word)
            board[r][c] = char
                
            if not node.chil and not node.is_word:
                del parent.chil[char]

        # Check whether board[r][c] is in children
        for r in range(n):
            for c in range(m):
                if board[r][c] in trie.root.chil:
                    dfs(r, c, trie.root, "")

        return res




















