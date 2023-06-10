class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        replicates = nums + nums

        res = k % len(nums)

        idx = 0
        for i in range(len(nums) - res, len(nums) * 2 - res) :
            nums[idx] = replicates[i]
            idx += 1

        
            