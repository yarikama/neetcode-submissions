class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            to_cmp = strs[0][i]
            for s in strs:
                if i >= len(s) or to_cmp != s[i]:
                    return strs[0][:i]

        return strs[0]                
        