class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for num in nums:
            new_perms = []
            for perm in perms:
                for i in range(len(perm)+1):
                    if i != len(perm) and perm[i] == num:
                        continue
                    new_perm = perm.copy()
                    new_perm.insert(i, num)
                    new_perms.append(new_perm)
            perms = new_perms

        return perms

            








