class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_p = 1
        prefix_prod = []
        for i in range(len(nums)):
            prod_p *= nums[i]
            prefix_prod.append(prod_p)

        prod_s = 1
        suffix_prod = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            prod_s *= nums[i]
            suffix_prod[i] = prod_s
        
        print(prefix_prod)
        print(suffix_prod)

        ans = []
        for i in range(len(nums)):
            l = prefix_prod[i-1] if i > 0 else 1
            r = suffix_prod[i+1] if i + 1 < len(nums) else 1
            ans.append(l*r)
            
        return ans


