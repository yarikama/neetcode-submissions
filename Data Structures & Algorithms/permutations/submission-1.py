class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = [[]]

        # insert every num to every location in every permutation
        for num in nums: # every num 
            permutations_copy = []

            for permutation in permutations: # every permutation
                for loc in range(len(permutation) + 1): # every location
                    permutation_copy = permutation.copy()
                    permutation_copy.insert(loc, num)
                    permutations_copy.append(permutation_copy)

            permutations = permutations_copy

        return permutations

        