from collections import defaultdict

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        word_index = defaultdict(list)
        for idx, char in enumerate(s):
            word_index[char].append(idx)

        ans = []
        L = 0
        while L < len(s):
            init = L
            R = word_index[s[L]][-1]
            
            while L <= R:
                R = max(R, word_index[s[L]][-1])
                L += 1

            ans.append(R-init+1)    

        return ans