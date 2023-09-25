class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # input : [nums1, nums2], m, n <- 각 리스트의 길이
            # non-decreasing order, 
        # output : sorted([nums1 + nums2])
        # nums1에 Inplace 저장
        # nums1 <- (m+n). nums2 <- n길이. nums1에 nums2를 합침

        # [1,2,3,0,0,0] p1
        # [2,5,6]  p2 
        # if val(p1) <= val(p2) : skip as is. p1 += 1
        # elif val(p1) > val(p2) : nums2[p2]을 nums1의 p1 자리에 넣어줌. 어떻게?
        # p1 : 2, p2 : 0   : tmp = nums1[p1], nums2[p2]->nums1[p1], p1 += 1,  p2 += 1 

        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        while p1 >= 0 and p2 >= 0 :
            if nums1[p1] < nums2[p2] :
                nums1[p] = nums2[p2]
                p2 -= 1
            else :
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        nums1[:p2 + 1 ] = nums2[:p2 + 1]

