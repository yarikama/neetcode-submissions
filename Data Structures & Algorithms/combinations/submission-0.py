class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.get_combine(1, [], k, result)
        return result

    def get_combine(
        self, idx: int, combination: List[int], limit: int, result: List[List[int]],
    ) -> None:
        # Base Case
        if len(combination) == limit:
            result.append(combination)
            return

        if idx > k: # not >= cause we explore the case with idx + 1, not idx
            return

        for i in range(idx, n): # to n not n-1, starting from 1 not 0
            combination.append(idx)
            self.get_combine(idx+1, combination, limit, result)
            combination.pop()
            self.get_combine(idx+1, combination, limit, result)

        