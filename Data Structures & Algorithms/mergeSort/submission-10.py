# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs

        self.mergeSortHelper(pairs, 0, len(pairs)-1)

        return pairs

    def mergeSortHelper(
        self, pairs: List[Pair], start: int, end: int
    ) -> None:
        # Terminate Condition
        if start == end:
            return

        mid = (start + end) // 2

        # D&C
        self.mergeSortHelper(pairs, start, mid)
        self.mergeSortHelper(pairs, mid+1, end)
        self.merge(pairs, start, mid, end)

    def merge(self, pairs: List[pair], start: int, mid: int, end: int) -> None:
        arr1, arr2 = pairs[start:mid+1], pairs[mid+1:end+1] # copy here
        i, j, k = 0, 0, start

        while i < len(arr1) and j < len(arr2): # use the len of the copies instead manually calculated their boundries
            if arr1[i].key <= arr2[j].key: # <= to maintain the order of it
                pairs[k] = arr1[i]
                k += 1
                i += 1
            else:
                pairs[k] = arr2[j]
                k += 1
                j += 1
            
        while i < len(arr1):
            pairs[k] = arr1[i]
            k += 1
            i += 1      

        while j < len(arr2):
            pairs[k] = arr2[j]
            k += 1
            j += 1



            









