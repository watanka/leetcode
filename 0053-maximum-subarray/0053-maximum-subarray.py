class Solution:
    def maxCSubArray(self, nums, mid) :
            s = 0
            ls = rs = float('-inf')
            for i in range(mid - 1, -1, -1) :
                s += nums[i]
                ls = max(ls, s)
            s = 0
            for i in range(mid, len(nums)) :
                s += nums[i]
                rs = max(rs, s)
            return ls + rs
            
    def maxSubArray(self, nums: List[int]) -> int:

        # 2nd approach. divide and conquer
        
        
        if len(nums) == 1 :
            return nums[0]
        if not nums :
            return 0
        mid = len(nums) // 2
        ls = self.maxSubArray(nums[:mid])
        rs = self.maxSubArray(nums[mid:])
        cs = self.maxCSubArray(nums, mid)
        return max(ls, rs, cs)


        # 1st. approach. dp
        # maxsums = [0 for _ in range(len(nums))]
        # maxsums[0] = nums[0]
        
        # for i in range(1, len(nums)) :
        #     maxsums[i] = max((nums[i] + maxsums[i-1]), nums[i])

           
        # return max(maxsums)
            
        