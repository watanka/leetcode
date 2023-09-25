class Solution:
    def climbStairs(self, n: int) -> int:
        # stairs to climb up. 1-2 steps at a time. How many ways can you climb?
        # 1. n = 2, expected = [1, 1], [2,] = 2
        # 2. n = 3, expected = [1, 1, 1], [1, 2], [2, 1] = 3

        # n개의 stairs => 가장 많은 steps수는 n. 무조건 하나씩 올라가기

        # 마지막부터 세기. 
        # step(1) = [1,1] = 1
        # step(2) = [1,1],[2] = 2
        # step(3) = [1,1,1], [1,2], [2,1] = 3
        # step(4) = [1,1,1,1], [2,1,1], [1,2,1], [1,1,2], [2,2] = 5
        # step(5) = [1,1,1,1,1], [2,1,1,1], ... = 8
        def step(nsteps) :
            if nsteps == 0 :
                return 0
            if nsteps == 1 :
                return 1
            if nsteps == 2 :
                return 2
            return step(nsteps - 1) + step(nsteps - 2)
        
        dp = [0 for _ in range(46)]
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2

        if n < 3 :
            return n
    
        for i in range(3, n+1) :
            dp[i] = dp[i - 1] + dp[i - 2]
            

        return dp[n]
        
        