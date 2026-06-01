class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_p = 1
        prefix_prod = []
        for i in range(len(nums)):
            prod_p *= nums[i]
            prefix_prod.append(prod_p)

        prod_s = 1
        suffix_prod = []
        for i in range(len(nums)-1, -1, -1):
            prod_p *= nums[i]
            suffix_prod.append(prod_p)
        
        print(prefix_prod)
        print(suffix_prod)

        return prefix_prod


