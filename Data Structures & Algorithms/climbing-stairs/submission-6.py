import numpy as np 
class Solution:
    def climbStairs(
        self, 
        n: int
    ) -> int:
        # # Base Case
        if n <= 2:
            return n
        
        def matrix_power(matrix, power):
            res = np.eye(2)
            while power > 0:
                if power % 2 == 1:
                    res = res @ matrix
                matrix = matrix @ matrix   
                power //= 2
            return res

        # 爬樓梯的轉移矩陣
        # [f(n)  ] = [1 1] * [f(n-1)]
        # [f(n-1)]   [1 0]   [f(n-2)]
        T = np.array([[1, 1], [1, 0]])
        result_matrix = matrix_power(T, n)
        

        return int(result_matrix[0][0])