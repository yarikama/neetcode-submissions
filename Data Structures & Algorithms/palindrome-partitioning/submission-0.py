class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def dfs(i: int, palis: list[str], curr_str: str) -> None:
            if i == len(s):
                if self.isPali(curr_str):
                    palis.append(curr_str)
                    ans.append(palis)
                return


            new_curr_str = curr_str + s[i]
            if self.isPali(new_curr_str):
                # Include
                new_palis = palis.copy()
                new_palis.append(new_curr_str)
                dfs(i+1, new_palis, "")

            dfs(i+1, palis, new_curr_str)

        dfs(0, [], "")
        return ans


    def isPali(self, s: str) -> bool:
        if not s:
            return False
            
        L, R = 0, len(s)-1
        while L < R:
            if s[L] != s[R]:
                return False
            L += 1
            R -= 1
        return True

            