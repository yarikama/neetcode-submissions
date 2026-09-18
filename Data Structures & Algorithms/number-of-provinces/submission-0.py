class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        visited = set()

        res = 0

        def dfs(city: int) -> None:
            if city in visited:
                return 

            visited.add(city)

            for i in range(n):
                if isConnected[city][i] == 1:
                    dfs(i)

            return

        for city in range(n):
            if city not in visited:
                res += 1
                dfs(city)  

        return res