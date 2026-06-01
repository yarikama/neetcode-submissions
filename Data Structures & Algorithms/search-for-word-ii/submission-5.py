from typing import Set

class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False

    def add_word(self, word: str) -> None:
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_word = True
        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie_root = self.construct_trie(words)
        ROWS, COLS = len(board), len(board[0])
        visited, result = set(), set()

        def dfs(row: int, col: int, trie_node: TrieNode, word: str) -> None:
            loc = (row, col) 
            if (
                min(loc) < 0 
                or row >= ROWS or col >= COLS
                or loc in visited
                or board[row][col] not in trie_node.children
            ):
                return

            visited.add(loc)
            char = board[row][col]
            trie_node = trie_node.children[char]
            word += char

            if trie_node.is_word:
                result.add(word)

            dfs(row+1, col, trie_node, word)
            dfs(row-1, col, trie_node, word)
            dfs(row, col+1, trie_node, word)
            dfs(row, col-1, trie_node, word)

            visited.remove(loc)

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie_root, "")

        return list(result)



    def construct_trie(self, words: List[str]) -> TrieNode:
        root = TrieNode()
        for word in words:
            root.add_word(word)
        return root

        