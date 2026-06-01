class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        bucket = [0] * 26
        bucket[ord(s[0]) - ord('A')] += 1

        max_length = 1
        L, R = 0, 0
        while R < len(s):
            length = R - L + 1
            if length - max(bucket) <= k:
                max_length = max(max_length, length)
                R += 1
                if R < len(s):
                    bucket[ord(s[R])-ord('A')] += 1
            else:
                bucket[ord(s[L])-ord('A')] -= 1
                L += 1
        return max_length
        