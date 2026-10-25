class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        
        if a > 0:
            heapq.heappush_max(heap, [a, "a"])
        if b > 0:
            heapq.heappush_max(heap, [b, "b"])
        if c > 0:
            heapq.heappush_max(heap, [c, "c"])

        if not heap:
            return ""

        res = "d"
        count = 0
        while heap:
            num1, char1 = heapq.heappop_max(heap)

            if char1 == res[-1]:
                if count == 2:
                    if not heap:
                        return res[1:]
                    num2, char2 = heapq.heappop_max(heap)
                    res += char2
                    count = 1

                    num2 -= 1
                    if num2 > 0:
                        heapq.heappush_max(heap, [num2, char2])
                    
                    heapq.heappush_max(heap, [num1, char1])
                    continue
                else:
                    res += char1
                    count += 1
                    num1 -= 1
                    if num1 > 0:
                        heapq.heappush_max(heap, [num1, char1])
            else:
                res += char1
                count = 1
                num1 -= 1
                if num1 > 0:
                    heapq.heappush_max(heap, [num1, char1])

        return res[1:]


