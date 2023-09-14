class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtracking(curr, first) :
            if len(curr) == k :
                result.append(curr[:])
                return
            
            need = k - len(curr)
            remain = n - first + 1
            available = remain - need

            for num in range(first, first + available + 1) :
                curr.append(num)
                backtracking(curr, num + 1)
                curr.pop()
            return
            
        result = []
        backtracking([], 1)

        return result
