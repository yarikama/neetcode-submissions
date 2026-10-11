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
    
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()
        trie.insert_batch(dictionary)


        n = len(s)
        dp = [0] * (n + 1)

        for i in range(n-1, -1, -1):
            dp[i] = 1 + dp[i + 1]
            curr = trie.root
            for j in range(i, n):
                if s[j] not in curr.chil:
                    break
                curr = curr.chil[s[j]]
                if curr.isWord:
                    dp[i] = min(dp[i], dp[j+1])
        
        return dp[0]
