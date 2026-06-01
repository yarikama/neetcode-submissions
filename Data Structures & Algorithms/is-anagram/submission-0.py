class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        SET = set()
        for c in s:
            SET.add(c)

        for c in t:
            if c not in SET:
                return False
            SET.remove(c)

        if len(SET) > 0:
            return False

        return True
