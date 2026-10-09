class Solution:
    def romanToInt(self, s: str) -> int:

        total = 0
        i = 0

        table = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
        }


        while i < len(s):
            if s[i] == "I" and i + 1 < len(s) and (s[i+1] == "V" or s[i+1] == "X"):
                    total += table[s[i+1]] - table[s[i]]
                    i += 1

            elif s[i] == "X" and i + 1 < len(s) and (s[i+1] == "L" or s[i+1] == "C"):
                    total += table[s[i+1]] - table[s[i]]
                    i += 1

            elif s[i] == "C" and i + 1 < len(s) and (s[i+1] == "D" or s[i+1] == "M"):
                    total += table[s[i+1]] - table[s[i]]
                    i += 1
            
            else:
                total += table[s[i]]

            i += 1

        return total        