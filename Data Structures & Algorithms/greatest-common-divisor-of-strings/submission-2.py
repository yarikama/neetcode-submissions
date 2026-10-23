class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        while str2:
            if len(str1) < len(str2):
                str1, str2 = str2, str1
            if not str1.endswith(str2):
                return ""
            str1 = str1[:len(str1) - len(str2)]
            if not str1:
                return str2
        return str1

