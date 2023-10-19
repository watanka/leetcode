class Solution:
    def rob(self, nums: List[int]) -> int:
        # 한 집에 대해서 터는 옵션과 털지 않는 옵션이 있음
        dp = [[0, 0] for _ in range(len(nums) + 1)]
        for i in range(1, len(nums) + 1) :

            # 턴다
            dp[i][1] = dp[i-1][0] + nums[i-1]
            # 털지 않는다.
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])

        return max(dp[-1])