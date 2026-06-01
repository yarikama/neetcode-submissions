class Solution:
    def findMedianSortedArrays(
        self, 
        nums1: List[int], 
        nums2: List[int]
    ) -> float:
        nums3 = []

        if not nums2:
            nums3 = nums1
        elif not nums1:
            nums3 = nums2
        else:
            i, j = 0, 0
            while i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    nums3.append(nums1[i])
                    i += 1
                else:
                    nums3.append(nums2[j])
                    j += 1

                if i == len(nums1):
                    nums3 += nums2[j:]

                if j == len(nums2):
                    nums3 += nums1[i:] 

        if len(nums3) % 2 == 1:
            return nums3[len(nums3)//2]
        else:
            return (nums3[len(nums3)//2] + nums3[len(nums3)//2 - 1])/2
        