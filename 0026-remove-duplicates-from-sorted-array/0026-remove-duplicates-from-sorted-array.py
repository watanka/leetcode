class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pos = 0

        for idx in range(len(nums)) :
            if nums[pos] != nums[idx] :
                pos += 1
                nums[pos] = nums[idx]
            
        return pos + 1

