class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        res = []

        idx = 0
        while idx < len(nums)-2:
            L, R = idx+1, len(nums)-1

            while L < R:
                print(f"nums[{idx}] = {nums[idx]}, nums[{L}] = {nums[L]}, nums[{R}]={nums[R]}, total={nums[L]+nums[R]+nums[idx]}")

                if nums[L] + nums[R] + nums[idx] == 0:
                    print('equal')
                    comb = [nums[idx], nums[L], nums[R]]
                    res.append(comb)
                    while L < len(nums)-1 and nums[L] == nums[L+1]:
                        L += 1
                    while R > 0 and nums[R] == nums[R-1]:
                        R -= 1
                    while idx < len(nums)-2 and nums[idx] == nums[idx+1]:
                        idx += 1
                    L += 1
                    R -= 1

                elif nums[L] + nums[R] + nums[idx] > 0:
                    print('bigger')
                    while R > 0 and nums[R] == nums[R-1]:
                        R -= 1
                    R -= 1

                else:
                    print('lower')
                    while L < len(nums)-1 and nums[L] == nums[L+1]:
                        L += 1
                    L += 1

            idx += 1

        return res
                

                
