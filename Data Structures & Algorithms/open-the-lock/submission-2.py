from typing import List
from collections import deque

class Solution:
    def neighbors(self, node: str) -> List[str]:
        ans = []
    
        for i in range(len(node)):
            changed_char = int(node[i])
            ans.append(node[:i] + str((changed_char + 1) % 10) + node[i+1:])
            ans.append(node[:i] + str((changed_char - 1) % 10) + node[i+1:])

        return ans

    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1

        queue = deque()
        visited = set()

        queue.append("0000")
        visited.add("0000")
        
        steps = 0
        while queue:
            for _ in range(len(queue)):
                top = queue.popleft()
                
                if top == target:
                    return steps
        
                for neighbor in self.neighbors(top):
                    if neighbor not in deadends and neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
                        
            steps += 1
        return -1