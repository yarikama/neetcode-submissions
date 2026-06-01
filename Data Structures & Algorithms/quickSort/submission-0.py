# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:
    def quickSort(
        self, 
        pairs: List[Pair]
    ) -> List[Pair]:
        return self._sort(
            pairs=pairs,
            start_index=0,
            end_index=len(pairs)-1,
        )

    def _sort(
        self,
        pairs: List[Pair],
        start_index: int,
        end_index: int,
    ) -> List[Pair]:
        # end condition
        if start_index >= end_index:
            return pairs

        # get the index of final swap
        stored_index = start_index

        # for index in start to end-1
        for index in range(start_index, end_index):
            # compare current item and the pivot item
            if(pairs[index].key < pairs[end_index].key):
                # swap and stored++
                pairs[index], pairs[stored_index] = pairs[stored_index], pairs[index]
                stored_index += 1

        # swap the final address
        pairs[end_index], pairs[stored_index] = pairs[stored_index], pairs[end_index]
        
        self._sort(
            pairs=pairs,
            start_index=start_index,
            end_index=stored_index-1,
        )
        self._sort(
            pairs=pairs,
            start_index=stored_index+1,
            end_index=end_index,
        )
        return pairs 
         
        