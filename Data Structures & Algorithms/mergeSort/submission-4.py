# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
            
        mid = len(pairs) // 2
        return self.merge(
            self.mergeSort(pairs[:mid]), self.mergeSort(pairs[mid:]),
        ) 

    def merge(self, pair1: List[Pair], pair2: List[Pair]) -> List[Pair]:
        if not pair1:
            return pair2

        if not pair2:
            return pair1

        res = []
        i, j = 0, 0
        n, m = len(pair1), len(pair2) 
        while i < n and j < m:
            if pair1[i].key <= pair2[j].key:
                res.append(pair1[i])
                i += 1
            else:
                res.append(pair2[j])
                j += 1
        
        while i < n:
            res.append(pair1[i])
            i += 1
        
        while j < m:
            res.append(pair2[j])
            j += 1

        return res








        
