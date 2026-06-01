# edge last element

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        L = 0
        cur_len1 = 0
        cur_len2 = 0
        max_len = 1

        for k in range(len(arr)-1):
            add_up = 1
            if k == len(arr)-2:
                add_up = 2
            if arr[k] % 2 == 1:
                if arr[k] < arr[k+1]:
                    cur_len1 += add_up
                    cur_len2 = 0
                else:
                    cur_len2 += add_up
                    cur_len1 = 0
            elif arr[k] % 2 == 0:
                if arr[k] > arr[k+1]:
                    cur_len1 += add_up
                    cur_len2 = 0
                else:
                    cur_len2 += add_up
                    cur_len1 = 0

            max_len = max(cur_len1, max_len, cur_len2)    
        
        return max_len