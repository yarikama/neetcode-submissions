class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            str2, str1 = str1, str2

        if str2 == "":
            return str1

        for i in range(1, len(str2)+1):
            if str1[-i] != str2[-i]:
                return ""

        return self.gcdOfStrings(str2, str1[:len(str1)-len(str2)])

        

