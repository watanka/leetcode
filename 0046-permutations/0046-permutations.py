class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        numLength = len(nums)

        result = []
        visited = [0 for _ in range(numLength)]
        def backtracking(perm, start_idx) :
            if len(perm) == numLength :
                result.append(perm[:])
                return

            for i in range(numLength) :
                if not visited[i] :
                    perm.append(nums[i]) 
                    visited[i] = 1
                    backtracking(perm, i + 1)
                    visited[i] = 0
                    perm.pop()

        backtracking([], 0)
        
        return result