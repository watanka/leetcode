class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxsums = [[0, 0] for _ in range(len(nums))]
        maxsums[0][0] = nums[0]
        maxsums[0][1] = nums[0]

        
        for i in range(1, len(nums)) :

            # continue
            maxsums[i][0] = nums[i] + max(maxsums[i-1])
            # new start
            maxsums[i][1] = nums[i]
           
        return max([max(sums) for sums in maxsums])
            
        