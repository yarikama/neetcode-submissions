class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = [[]]

        for num in nums:
            permutations_copy = []

            for permutation in permutations:
                for loc in range(len(permutation) + 1):
                    permutation_copy = permutation.copy()
                    permutation_copy.insert(loc, num)
                    permutations_copy.append(permutation_copy)

            permutations = permutations_copy

        return permutations

        