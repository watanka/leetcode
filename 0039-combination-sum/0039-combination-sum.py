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
                
