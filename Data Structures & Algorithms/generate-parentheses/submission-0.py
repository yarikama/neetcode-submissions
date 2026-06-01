class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []
        def dfs(left: int, right: int, parenthese: str) -> None:
            # Base Case: length equals 2 * n
            if len(parenthese) == 2*n:
                ans.append(parenthese) 

            # Base Case: no left or right left
            if left > 0:
                dfs(left - 1, right + 1,  parenthese + "(")
                
            if right > 0:
                dfs(left, right - 1,  parenthese + ")")
                

        dfs(n, 0, "")

        return ans