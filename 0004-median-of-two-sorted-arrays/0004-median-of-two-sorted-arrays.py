class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # median 값을 구하는 방법
        # 1. (median(nums1) + median(nums2)) // 2 -> X
        # 2. median(sorted(nums1 + nums2) ) ->
        

        # cases for continuous [1, 2, 3] 
        # mid = len(nums) // 2 
        # if len(nums) % 2 : -> mid 
        # if not len(nums) % 2 : [mid, mid + 1]

        # # 1. 
        # return (nums1[len(nums1) // 2] + nums2[len(nums2) // 2]) / 2 

        # 2.
        merged_nums = sorted(nums1 + nums2)
        # print(merged_nums)
        length = len(merged_nums)
        mid = length // 2
        # print(mid)
        if length % 2 : # odd
            return merged_nums[mid]

        else :
            return (merged_nums[mid - 1] + merged_nums[mid]) / 2