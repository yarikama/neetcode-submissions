class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        counter = {5: 0, 10: 0, 20: 0}
        for b in bills:
            if b == 5:
                counter[5] += 1
            elif b == 10:
                if counter[5] == 0:
                    return False
                counter[5] -= 1
                counter[10] += 1
            else:
                if counter[5] > 0 and counter[10] > 0:
                    counter[10] -= 1
                    counter[5] -= 1
                elif counter[5] > 2:
                    counter[5] -= 3
                else:
                    return False

        return True
