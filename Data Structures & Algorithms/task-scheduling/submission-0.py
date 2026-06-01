from heapq import heappush, heappop

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # first order time
        # second order cnt
        cnts = defaultdict(int)
        for task in tasks:
            cnts[task] += 1
        
        pq = []
        for task, cnt in cnts.items():
            heappush(pq, (0, -cnt, task))


        if not pq:
            return 0

        length = 0
        while pq:
            start, cnt, task = heappop(pq)
            cnt *= -1
            cnt -= 1
            if cnt > 0:
                heappush(pq, (start+n+1, -cnt, task))

            length += (1 + max(0, start-length))


        return length
        

        
