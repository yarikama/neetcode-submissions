class TrieNode:
    def __init__(self):
        self.word = False
        self.chil = {}


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.chil:
                cur.chil[char] = TrieNode()
            cur = cur.chil[char]
        cur.word = True

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char not in cur.chil:
                return False
            cur = cur.chil[char]
        return cur.word 
