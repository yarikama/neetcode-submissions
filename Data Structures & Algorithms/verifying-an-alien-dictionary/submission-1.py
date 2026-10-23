
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dictionary = {}
        for idx, char in enumerate(order):
            dictionary[char] = idx+1

        prev = float("-inf")
        for word in words:
            start = 5
            val = 0
            for char in word:
                alien_char = dictionary[char]
                val += (alien_char * (26 ** start))
                start -= 1

            if val < prev:
                return False

            prev = val

        return True




