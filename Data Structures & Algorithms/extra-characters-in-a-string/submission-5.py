class Node:
    def __init__(self):
        self.isWord = False
        self.chil = {}

class Trie:
    def __init__(self):
        self.root = Node()
        self.cache = {}

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.chil:
                curr.chil[c] = Node()
            curr = curr.chil[c]
        curr.isWord = True

    def insert_batch(self, words: List[str]) -> None:
        for w in words:
            self.insert(w)
        
    def search(self, start: int, word: str) -> int:
        if start >= len(word):
            return 0

        if start in self.cache:
            return self.cache[start]

        min_res = 1 + self.search(start + 1, word)
        curr = self.root
        for i in range(start, len(word)):
            if word[i] not in curr.chil: # move
                break
            if curr.chil[word[i]].isWord: # split
                min_res = min(min_res, self.search(i+1, word))

            curr = curr.chil[word[i]]
        self.cache[start] = min_res
        return min_res

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()
        trie.insert_batch(dictionary)
        return trie.search(0, s)

        