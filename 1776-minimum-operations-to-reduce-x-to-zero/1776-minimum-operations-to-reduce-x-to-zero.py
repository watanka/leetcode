class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        target = sum(nums) - x
        currSum = 0
        l = 0
        max_window_size = -1

        for r in range(len(nums)) :
            currSum += nums[r]

            while l <= r and currSum > target :
                currSum -= nums[l]
                l += 1

            if currSum == target :
                max_window_size = max(max_window_size, r - l + 1)
            
        return -1 if max_window_size == -1 else len(nums) - max_window_size
