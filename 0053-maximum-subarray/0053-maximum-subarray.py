class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxsums = [0 for _ in range(len(nums))]
        maxsums[0] = nums[0]
        

        
        for i in range(1, len(nums)) :
            maxsums[i] = max((nums[i] + maxsums[i-1]), nums[i])

           
        return max(maxsums)
            
        