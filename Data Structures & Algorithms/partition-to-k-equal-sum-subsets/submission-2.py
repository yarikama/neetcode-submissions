class Solution:
    def canPartitionKSubsets(
        self, nums: List[int], k: int,
    ) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        each = total // k
        
        nums.sort(reverse=True)
        if nums[0] > each:
            return False

        res = [0] * k

        def helper(i: int) -> bool:
            if i == len(nums):
                return True

            seen = set()
            for j in range(k):
                if res[j] in seen or nums[i] + res[j] > each:
                    continue

                seen.add(res[j])

                res[j] += nums[i]
                if helper(i+1):
                    return True
                res[j] -= nums[i]

            return False

        return helper(0)