class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

    
        def backtracking(combinations, len_comb, remaining_num) :
            if len_comb == k :
                result.append(combinations)
                return
            
            if len_comb + (n - remaining_num) < k - 1 :
                return

            
            for j in range(remaining_num, n+ 1) :
                backtracking(combinations + [j], len_comb + 1, j + 1)
            return

        result = []
        backtracking([], 0,1)

        return result

        