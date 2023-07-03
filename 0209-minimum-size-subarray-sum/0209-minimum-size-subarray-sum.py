import sys

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int: 
        if sum(nums) < target :
            return 0
        if sum(nums) == target :
            return len(nums)

        left, right, total = 0, 0, 0
        min_len = len(nums) + 1

        while right < len(nums) :
            total += nums[right]
            right += 1

            while total >= target :
                min_len = min(min_len, right - left)
                total -= nums[left]
                left += 1

                
        return min_len
        


        