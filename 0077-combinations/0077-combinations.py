class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

    
        def backtracking(combinations, remaining_num) :
            if len(combinations) == k :
                result.append(combinations)
                return
            
            if len(combinations) + (n - remaining_num) < k - 1 :
                return

            
            for j in range(remaining_num, n+ 1) :
                backtracking(combinations[::] + [j], j + 1)

        result = []
        backtracking([],1)

        return result

        