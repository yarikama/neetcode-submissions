class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        def plus(digits: List[int], idx: int):
            if idx < 0:
                digits = [1] + digits 
                return digits

            elif digits[idx] == 9:
                digits[idx] = 0
                return plus(digits, idx-1)

            else:
                digits[idx] += 1
                return digits

        return plus(digits, len(digits)-1)