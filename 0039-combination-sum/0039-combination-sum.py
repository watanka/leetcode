class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        totalLength = len(candidates)

        def backtracking(val, comb, i) :
            if val < 0 :
                return
            if val == 0 :
                result.append(comb)
                return
            
            for idx in range(i, totalLength) :
                backtracking(val - candidates[idx], comb + [candidates[idx]], idx)

        
        result = []
        backtracking(target, [], 0)
        
        return result
                

        # dp = [[] for _ in range(target+1)]
        # for c in candidates:
        #     if c <= target:
        #         dp[c].append([c])
        #     for i in range(c+1, target+1):
        #         for comb in dp[i-c]:
        #             dp[i].append(comb + [c])
        # return dp[-1]
