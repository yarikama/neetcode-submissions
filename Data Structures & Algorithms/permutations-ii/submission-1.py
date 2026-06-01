# hash nums -> {num: count}
# for key in hash:
#   -> generate perms by key and count

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # get hash
        self.nums, self.hash = nums, defaultdict(int)
        for num in nums:
            self.hash[num] += 1 

        # insert element into permutations
        perms = [[]]
        for num, cnt in self.hash.items(): 
            perms = self.insert(num, cnt, perms)
        return perms

    def insert(self, num: int, cnt: int, perms: List[List[int]]) -> List[List[int]]:
        # if only an empty one [[]] -> [[1, 1]]
        if not perms[0]:
            return [[num] * cnt]


        new_perms = []

        for i in range(cnt//2 + 1):
            for perm in perms:
                to_insert1, to_insert2 = [num] * i, [num] * (cnt-i)
                if not to_insert1:
                    for idx in range(len(perm)+1):
                        new_perm = perm[:idx] + to_insert2 + perm[idx:]
                        new_perms.append(new_perm)
                    continue

                for idx in range(len(perm)+1):
                    new_perm = perm[:idx] + to_insert1 + perm[idx:]
                    for j in range(len(new_perm)+1):
                        if j in range(idx, idx+len(to_insert1)+1):
                            continue
                        new_perm = new_perm[:j] + to_insert2 + new_perm[j:]
                        new_perms.append(new_perm)
                print(new_perms)
        return new_perms

            








