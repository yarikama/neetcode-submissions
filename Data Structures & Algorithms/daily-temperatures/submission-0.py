class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []
        for i in range(len(temperatures)):
            noBiggerOne = True
            for j in range(i, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    ans.append(j-i)
                    noBiggerOne = False
                    break
            if noBiggerOne:
                ans.append(0)
            
        return ans

        