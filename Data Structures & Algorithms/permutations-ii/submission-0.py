class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        perms = [[]]

        for num in nums: 

            perms_cpy = []
            for perm in perms:
                for idx in range(len(perm) + 1):
                    if idx > 0 and perm[idx-1] == num:
                        continue
                    perm_cpy = perm.copy()
                    perm_cpy.insert(idx, num)
                    perms_cpy.append(perm_cpy)
            perms = perms_cpy

        return perms