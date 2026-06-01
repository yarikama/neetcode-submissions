from collections import defaultdict

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        word_index = {}
        for idx, char in enumerate(s):
            word_index[char] = idx

        ans = []
        L = 0
        while L < len(s):
            init = L
            R = word_index[s[L]]
            
            while L <= R:
                R = max(R, word_index[s[L]])
                L += 1

            ans.append(R-init+1)    

        return ans