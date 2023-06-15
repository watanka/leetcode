class Solution:
    def jump(self, nums: List[int]) -> int:

        if len(nums) <= 1 :
            return 0
        
        n = len(nums)
        dp = [0 for _ in range(len(nums))]
        dp[0] = 1
        # num_jump = 1
        for i in range(n-1) :
            if dp[i] :
                for j in range(i+1, min(n, i + nums[i] + 1)) :
                    if dp[j] :
                        dp[j] = min(dp[j], dp[i] + 1)
                    else :
                        dp[j] = dp[i] + 1
            # print(dp)
        return dp[-1] - 1