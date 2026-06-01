class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def dfs(i: int, target: int, collections: list[int]) -> None:
            if target < 0:
                return

            if i > len(candidates) - 1:
                return

            include = collections.copy()
            include.append(candidates[i])
            new_target = target - candidates[i]

            if new_target == 0:
                ans.append(include)
                return

            dfs(i+1, new_target, include)

            # Skip
            j = i
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1

            if j != i: dfs(j, target, collections)



        dfs(0, target, [])

        return list(ans)



        