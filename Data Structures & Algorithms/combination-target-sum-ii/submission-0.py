class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        visited = set()
        candidates.sort()

        def dfs(i: int, target: int, collections: list[int]) -> None:
            if (i, target, *collections) in visited:
                return

            if target < 0:
                return

            if i > len(candidates) - 1:
                return

            # Skip
            dfs(i+1, target, collections)


            include = collections.copy()
            include.append(candidates[i])
            new_target = target - candidates[i]

            if new_target == 0:
                ans.append(include)
                visited.add((i, target, *collections))
                return

            dfs(i+1, new_target, include)

        dfs(0, target, [])

        return list(ans)



        