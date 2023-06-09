class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        idx = 0
        std = -101
        pos = 0
        total_length = len(nums)

        while idx < total_length :
            if std != nums[idx] :
                std = nums[idx]
                nums[pos] = std
                pos += 1

            idx += 1

        return pos

