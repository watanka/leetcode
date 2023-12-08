class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if len(nums) <= k :
            return k

        left = 0
        window_size = 0
        for right in range(len(nums)) :
            k -= 1 - nums[right] 

            if k < 0 :
                k += 1 - nums[left]
                left += 1

            window_size = max(window_size, right - left + 1)

        return window_size
