
from collections import Counter
from heapq import heappop, heapify, heappush

class Solution:
    def reorganizeString(self, s: str) -> str:
        if not s:
            return s

        n = len(s)
        new_str = ""    

        counter = Counter()
        for i in range(n):
            counter[s[i]] += 1
            if n % 2 == 1: # odd
                if counter[s[i]] > n // 2 + 1:
                    return new_str
            else:
                if counter[s[i]] > n // 2:
                    return new_str

        heap = [(-val, key) for key, val in counter.items()]
        heapify(heap)

        while len(heap) > 1:
            freq1, ch1 = heappop(heap)
            freq2, ch2 = heappop(heap)

            if new_str and ch1 == new_str[-1]:
                new_str += ch2
                new_str += ch1
            else:
                new_str += ch1
                new_str += ch2

            freq1 += 1
            freq2 += 1

            if freq1 < 0:
                heappush(heap, (freq1, ch1))

            if freq2 < 0:
                heappush(heap, (freq2, ch2))

        if heap:
            _, ch = heappop(heap)
            new_str += ch

        return new_str