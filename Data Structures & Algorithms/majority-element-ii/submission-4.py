from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1

            if len(counter) <= 2:
                continue

            # remove the ones are == 1
            new_counter = defaultdict(int)
            for val, cnt in counter.items():
                if cnt > 1:
                    new_counter[val] = cnt - 1
            counter = new_counter

        # verify
        for num in counter.keys():
            counter[num] = 0

        for num in nums:
            if num not in counter:
                continue
            counter[num] += 1
        
        res = []
        criteria = len(nums) // 3
        for num, cnt in counter.items():
            if cnt > criteria:
                res.append(num)

        return res


        # d = defaultdict(int)
        # criteria = len(nums) // 3
        # res = set()
        # for num in nums:
        #     d[num] += 1
        #     if d[num] > criteria:
        #         res.add(num)

        #     if len(res) == 2:
        #         return list(res)
        # return list(res)
