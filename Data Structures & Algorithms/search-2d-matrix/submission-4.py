class Solution:
    def searchMatrix(
        self, 
        matrix: List[List[int]], 
        target: int
    ) -> bool:
        # extended_list = []
        # for every_list in matrix:
            # extended_list += every_list
        self.matrix = matrix
        self.total_x = len(matrix[0])
        self.total_y = len(matrix)
        self.total_len = self.total_x * self.total_y 

        L, R = 0, self.total_len-1
        while(L <= R):
            M = (L + R)//2
            value = self.get_value(M)
            if target < value:
                R = M-1
            elif target > value:
                L = M+1
            elif target == value:
                return True
            
        return False

    def get_value(
        self,
        line_number: int,
    ) -> int:
        m = line_number // self.total_x
        n = line_number % self.total_x
        return self.matrix[m][n] 

    