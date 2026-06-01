# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:
    def mergeSort(
        self, 
        pairs: List[Pair]
    ) -> List[Pair]:
        # Base Case
        if not pairs or len(pairs) == 1:
            return pairs

        # Spilt
        mid = len(pairs)//2
        l1 = pairs[:mid]
        l2 = pairs[mid:]

        # Merge
        return self.merge(
            l1=self.mergeSort(l1),
            l2=self.mergeSort(l2),
        )

    def merge(
        self,
        l1: List[Pair],
        l2: List[Pair],
    ) -> List[Pair]:
        l3, i, j = [], 0, 0

        while(len(l1)-i > 0 and len(l2)-j > 0):
            if l1[i].key <= l2[j].key:
                l3.append(l1[i])
                i += 1
            else:
                l3.append(l2[j])
                j += 1

        if (len(l1) + len(l2) == i + j):
            pass
        elif(len(l1)-i == 0):
            l3.extend(l2[j:])
        else:
            l3.extend(l1[i:])

        return l3 











