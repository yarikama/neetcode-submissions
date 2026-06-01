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

    def search(self, word: str, node: TrieNode | None = None) -> bool:
        cur = node or self.root
        for idx, char in enumerate(word):

            if char == '.':
                sub_word = word[idx+1:]
                for child_node in cur.chil:
                    if self.search(sub_word, cur.chil[child_node]):
                        return True
                return False

            elif char not in cur.chil:
                return False

            cur = cur.chil[char]

        return cur.word 
