class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        notValIdx = 0

        idx = 0
        while idx < len(nums) :
            if nums[idx] != val :
                nums[notValIdx] = nums[idx]
                notValIdx += 1
            idx += 1

        # k = notValIdx
        # while k < len(nums) :
        #     nums[k] = '-'
        #     k += 1
            

        return notValIdx
