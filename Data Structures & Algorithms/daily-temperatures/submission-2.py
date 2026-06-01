class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)

        stack = []
        for i in range(len(temperatures)-1, -1, -1):
            index = 1
            while stack and stack[-1][0] <= temperatures[i]:
                index += stack.pop()[1]
                
            if stack:
                ans[i] = index
                stack.append((temperatures[i], index))
            else:
                stack.append((temperatures[i], 0))

        return ans


        