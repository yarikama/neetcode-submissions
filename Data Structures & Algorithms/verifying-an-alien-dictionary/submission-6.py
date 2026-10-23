class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {c: i + 1 for i, c in enumerate(order)}
        prev = -1
        for word in words:
            val = 0
            for i in range(20):
                d = rank[word[i]] if i < len(word) else 0
                val = val * 27 + d # using 27 as base
            if val < prev:
                return False
            prev = val
        return True