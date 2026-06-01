from itertools import cycle

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        R_start, C_start, R_end, C_end = 0, 0, len(matrix)-1, len(matrix[0])-1
        total = len(matrix) * len(matrix[0])

        c = cycle(range(4))
        ans = []
        
        while R_start <= R_end or C_start <= C_end:
            session = next(c)

            if session == 0:
                print(0)
                for i in range(C_start, C_end+1):
                    ans.append(matrix[R_start][i])
                R_start += 1
            
            elif session == 1:
                print(1)
                for i in range(R_start, R_end+1):
                    ans.append(matrix[i][C_end])
                C_end -= 1
            
            elif session == 2:
                print(2)
                for i in range(C_end, C_start-1, -1):
                    ans.append(matrix[R_end][i])
                R_end -= 1
            
            elif session == 3:
                print(3)
                for i in range(R_end, R_start-1, -1):
                    ans.append(matrix[i][C_start])
                C_start += 1

            if len(ans) == total:
                return ans


[1, 2, 3, 4]
[5, 6, 7, 8]
[9,10,11,12]
        