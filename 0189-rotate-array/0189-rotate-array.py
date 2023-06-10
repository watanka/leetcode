class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = k % len(nums)

        replicate = nums + nums

        nums[:] = replicate[len(nums) - res : len(replicate) - res]