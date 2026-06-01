class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        nums.sort()
        for num in nums:
            new_perms = []
            for perm in perms:
                for i in range(len(perm)+1):
                    new_perm = perm.copy()
                    new_perm.insert(i, num)
                    new_perms.append(new_perm)
                    if i != len(perm) and perm[i] == num: # 只能差前面
                        break
            perms = new_perms

        return perms

            








