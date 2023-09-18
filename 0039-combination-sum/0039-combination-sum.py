class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtracking(val, comb) :
            if val < 0 :
                return
            if val == 0 :
                strKey = ''.join(map(str,sorted(comb)))

                if strKey not in result_dict :
                    result.append(comb)
                    result_dict[strKey] = 1
                return
            
            for cand in candidates :
                backtracking(val - cand, comb + [cand])
        result_dict = {}
        result = []
        backtracking(target, [])
        
        return result
                
