class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, R = 0, 0
        word_set = set()
        longest_length = 0

        while R < len(s):
            print(word_set)

            if s[R] not in word_set:
                word_set.add(s[R])
                longest_length = max(longest_length, R - L + 1)
                R += 1
                continue

            while s[R] in word_set and L <= R:
                print(f"s[{L}] = {s[L]}")
                word_set.remove(s[L])
                L += 1

        return longest_length
