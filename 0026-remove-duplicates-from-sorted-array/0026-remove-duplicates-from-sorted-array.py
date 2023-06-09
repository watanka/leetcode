class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        idx = 0
        std = -101
        pos = 0
        total_length = len(nums)

        for idx in range(len(nums)) :
            if nums[pos] != nums[idx] :
                pos += 1
                nums[pos] = nums[idx]
            
        return pos + 1

