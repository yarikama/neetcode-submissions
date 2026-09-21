from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for c1, c2 in prerequisites:
            adj_list[c1].append(c2)

        visited, checked = set(), set()

        def dfs(course: int) -> bool:
            if course in visited:
                return False

            if course in checked:
                return True

            visited.add(course)
            
            for nei in adj_list[course]:
                if not dfs(nei):
                    return False

            visited.remove(course)
            checked.add(course)

            return True
                
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
            
        