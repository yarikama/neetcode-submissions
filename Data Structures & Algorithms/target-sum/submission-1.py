class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        cache = {}
        for i in range(-total, total+1):
            cache[i] = 0
        cache[0] = 1
        print(cache)

        for num in nums:
            # for cap in cache:
                # if cap-num < -total or cap + num > total: continue
                # print(f"cache[{cap}] = {cache[cap]}, cache[{cap-num}] = {cache[cap-num]}, cache[{cap+num}] = {cache[cap+num]}")
                # 會污染
            new_cache = {}
            for i in range(-total, total+1):
                new_cache[i] = 0

            for cap in range(-total, total+1):
                if cap - num < -total: last_path = cache[cap+num]
                elif cap + num > total: last_path = cache[cap-num] 
                else: last_path = cache[cap-num] + cache[cap+num]
                new_cache[cap] = max(0, last_path) 
            cache = new_cache
            print(cache)

        return cache[target]
        