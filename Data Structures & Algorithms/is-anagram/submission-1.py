class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash = {}
        for c in s:
            if c not in hash:
                hash[c] = 0
            hash[c] += 1

        for c in t:
            if c not in hash:
                return False
            hash[c] -= 1
            if hash[c] == 0:
                del hash[c]

        if len(hash) > 0:
            return False

        return True
