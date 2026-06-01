class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold *= k
        num = 0
        cur_sum = sum(arr[:min(k, len(arr))])
        if cur_sum >= threshold:
            num += 1

        for i in range(k, len(arr)):
            cur_sum -= arr[i - k]
            cur_sum += arr[i]

            if cur_sum >= threshold:
                num += 1
            
        return num
        