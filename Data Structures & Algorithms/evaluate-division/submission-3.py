class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(lambda: defaultdict(float))

        for equ, val in zip(equations, values):
            fro, to = equ
            adj[fro][to] = val
            adj[to][fro] = 1/val

        def dfs(fro: str, to: str, curr_val: float, s: Set[str]) -> float:
            s.add(fro)

            if fro == to and fro in adj and adj[fro]:
                return curr_val

            res = -1
            for key, val in adj[fro].items():
                if key not in s:
                    res = max(res, dfs(key, to, curr_val * val, s))

            return res

        return [dfs(fro, to, 1.0, set()) for fro, to in queries] 