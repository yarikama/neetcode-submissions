class Solution:
    def isNStraightHand(
        self, 
        hand: List[int], 
        groupSize: int
    ) -> bool:
        if groupSize == 0:
            return False

        if not hand:
            return False

        if len(hand) % groupSize != 0:
            return False
        
        hand.sort()
        toDo = {}

        for num in hand:
            if num not in toDo:
                for i in range(1, groupSize):
                    if num+i in toDo:
                        toDo[num+i] += 1
                    else:
                        toDo[num+i] = 1
            if num in toDo:
                if toDo[num] == 1:
                    del toDo[num]
                else:
                    toDo[num] -= 1

        return True if not toDo else False

