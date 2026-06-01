from enum import Enum

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        cur_sum, max_sum = 0, 1
        tmp_sign = '=' 

        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                tmp_sign = '='
                cur_sum = 1
            elif arr[i] > arr[i-1]:
                if tmp_sign != '>':
                    cur_sum += 1
                else:
                    cur_sum = 1
                tmp_sign = ">"
            else:
                if tmp_sign != '<':
                    cur_sum += 1
                else:
                    cur_sum = 1 
                tmp_sign = "<"
            
            max_sum = max(max_sum, cur_sum)

        
        return max_sum