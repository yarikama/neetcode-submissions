from typing import Set
from collections import defaultdict, deque

class Solution:
    def canFinish(
        self, 
        numCourses: int, 
        prerequisites: List[List[int]]
    ) -> bool:
        # if there is no prerequisites
        if not prerequisites:
            return True

        # construct a graph and a indegree array for courses (this course needs to finish how many prerequites)
        adj, indegree = defaultdict(list), [0] * numCourses
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1

        # 0 means we can start from this course
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        count = 0


        while queue:
            curr_course = queue.popleft()
            count += 1 # at the same, see if how many courses we are able to finish

            # for every neighbor, reduce the indegree (means we finished it)
            for neighbor in adj[curr_course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    # if all the prerequisites are finished, we can start from this course
                    queue.append(neighbor)
        # compare it to our answer
        return count == numCourses

        

