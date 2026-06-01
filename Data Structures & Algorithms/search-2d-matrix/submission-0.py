class Solution:
    def searchMatrix(
        self, 
        matrix: List[List[int]], 
        target: int
    ) -> bool:
        extended_list = []
        for every_list in matrix:
            extended_list += every_list

        L, R = 0, len(extended_list)
        while(L <= R):
            M = (L + R)//2
            if target < extended_list[M]:
                R = M-1
            elif target > extended_list[M]:
                L = M+1
            elif target == extended_list[M]:
                return True
            
        return False