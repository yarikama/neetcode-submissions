from sortedcontainers import SortedDict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L, R = 0, 0
        SD = SortedDict()
        max_length = 0
        while R < len(s):
            if s[R] not in SD:
                SD[s[R]] = 1

            else:
                SD[s[R]] += 1

            sum_ = self.get_word_count(SD)

            while sum_ > k:
                print(sum_)
                SD[s[L]] -= 1
                L += 1
                sum_ = self.get_word_count(SD)

            max_length = max(max_length, R - L + 1)
            R += 1

        return max_length

    def get_word_count(self, SD: SortedDict) -> int:
        print('New')
        is_counted = False
        sum_ = 0
        for key, value in SD.items():
            print("value:", value)
            if is_counted:
                sum_ += value
            is_counted = True

        return sum_
