# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        
        def merge(list1: List[Pair], list2: List[Pair]) -> List[Pair]:
            list3: List[Pair] = []
            
            i1, i2 = 0, 0
            while len(list1) > i1 and len(list2) > i2:
                if list1[i1].key <= list2[i2].key:
                    list3.append(list1[i1])
                    i1 += 1
                else:
                    list3.append(list2[i2])
                    i2 += 1

            while len(list1) > i1:
                list3.append(list1[i1])
                i1 += 1

            while len(list2) > i2:
                list3.append(list2[i2])
                i2 += 1

            return list3

            




        if not pairs or len(pairs) == 1:
            return pairs

        mid_idx = len(pairs) // 2
        
        return merge(self.mergeSort(pairs[:mid_idx]), self.mergeSort(pairs[mid_idx:]))








        
