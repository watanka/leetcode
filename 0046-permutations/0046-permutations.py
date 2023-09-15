# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         numLength = len(nums)
#         if numLength == 1 :
#             return [nums]
#         result = []
#         visited = [0 for _ in range(numLength)]
#         def backtracking(perm, start_idx) :
#             if len(perm) == numLength :
#                 result.append(perm[:])
#                 return

#             for i in range(numLength) :
#                 if not visited[i] :
#                     visited[i] = 1
#                     backtracking(perm + [nums[i]], i + 1)
#                     visited[i] = 0

#         backtracking([], 0)
        
#         return result

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) == 1 :
            return [nums[:]]

        for i in range(len(nums)) :
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms :
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        
        return result
        