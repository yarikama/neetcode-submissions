from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        criteria = len(nums) // 3
        res = set()
        for num in nums:
            d[num] += 1
            if d[num] > criteria:
                res.add(num)

            if len(res) == 2:
                return list(res)
        return list(res)
