class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        distinct1 = set(nums1) - set(nums2)
        distinct2 = set(nums2) - set(nums1)

        return [list(distinct1), list(distinct2)]