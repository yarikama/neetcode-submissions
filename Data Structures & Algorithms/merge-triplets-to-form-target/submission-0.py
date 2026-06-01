class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        start = [0, 0, 0]

        for triplet in triplets:
            oneBigger = False
            for a, b in zip(triplet, target):
                if b < a:
                    oneBigger = True
            
            if oneBigger:
                continue

            for i in range(3):
                start[i] = max(start[i], triplet[i])


        if target != start:
            return False

        return True

                
            

        