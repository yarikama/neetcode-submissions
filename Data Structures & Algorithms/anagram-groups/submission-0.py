class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        for string in strs:
            cummulative_ord = 1
            for c in string:
                cummulative_ord *= ord(c)
            hash[cummulative_ord].append(string)

        return list(hash.values())