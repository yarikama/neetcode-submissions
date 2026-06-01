class Solution:
    def twoSum(
        self, 
        nums: List[int], 
        target: int
    ) -> List[int]:
        hashmap = {}
        for idx, val in enumerate(nums):
            # if val in hashmap and target == 2 * hashmap[val]:
            if val in hashmap:
                print(val)
                # return [hashmap[val], idx]
                
            hashmap[val] = idx

        for idx, val in enumerate(nums):
            diff = target - val
            hashmap.pop(val)
            if diff in hashmap:
                return [idx, hashmap[diff]]
            

        