class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        biggest = -1
        for i in range(len(arr)-1, -1, -1):
            if arr[i] < biggest:
                arr[i] = biggest
            else:
                arr[i], biggest = biggest, arr[i]

        return arr