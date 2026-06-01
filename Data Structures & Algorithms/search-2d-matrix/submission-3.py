class Solution:
    def searchMatrix(
        self, 
        matrix: List[List[int]], 
        target: int
    ) -> bool:
        # extended_list = []
        # for every_list in matrix:
            # extended_list += every_list
        
        total_x = len(matrix[0])
        total_y = len(matrix)
        total_len = total_x * total_y 

        L, R = 0, total_len-1
        while(L <= R):
            M = (L + R)//2
            print(M)
            x = M % total_x
            y = M // total_y
            print(f"[{x}, {y}]")
            value = matrix[y][x]
            print(f"value: {value}")
            if target < value:
                R = M-1
            elif target > value:
                L = M+1
            elif target == value:
                return True
            
        return False