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
            prod_s *= nums[i]
            suffix_prod.append(prod_s)
        
        print(prefix_prod)
        print(suffix_prod)

        ans = []
        for i in range(len(nums)):
            print(i, nums[i])
            print(i-1, prefix_prod[i])
            print(len(nums)-i-1, suffix_prod[len(nums)-i-1])
            prefix = prefix_prod[i-1] if i > 0 else 1
            suffix = prefix_prod[len(nums)-i-1]
            ans.append(prefix * suffix)

        return ans


