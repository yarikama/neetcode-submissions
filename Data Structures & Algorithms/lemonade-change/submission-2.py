class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        counter = [0, 0]
        for b in bills:
            if b == 5:
                counter[0] += 1
            elif b == 10:
                if counter[0] == 0:
                    return False
                counter[0] -= 1
                counter[1] += 1
            else:
                if counter[0] > 0 and counter[1] > 0:
                    counter[0] -= 1
                    counter[1] -= 1
                elif counter[0] > 2:
                    counter[0] -= 3
                else:
                    return False

        return True
