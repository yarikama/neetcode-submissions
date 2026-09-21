from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Set up in_degress to trace the number of edges
        in_degree = [0] * numCourses
        adj_list = defaultdict(list)
        for c1, c2 in prerequisites:
            adj_list[c1].append(c2)
            in_degree[c2] += 1

        # Set up queue
        q = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)

        # Clean nodes with no in_degree
        while q:
            c = q.popleft()
            for nei in adj_list[c]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)

        return True if not sum(in_degree) else False

        

        