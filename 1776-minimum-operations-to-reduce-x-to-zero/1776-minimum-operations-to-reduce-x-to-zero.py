class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # totalSum = sum(nums)
        # target = totalSum - targetSum

        # if target < 0 :
        #     return -1
        # if target == 0 :
        #     return len(nums)

        # n = len(nums)
        # minOp = float('inf')
        # currentSum = 0
        # leftIndex = 0
        # rightIndex = 0

        # while rightIndex < n :
        #     currentSum += nums[rightIndex]
        #     rightIndex += 1

        #     while currentSum > target and leftIndex < n :
        #         currentSum -= nums[leftIndex]
        #         leftIndex += 1

        #     if currentSum == target :
        #         minOps = min(minOps, n - (rightIndex - leftIndex))

        # return -1 if minOps == float('inf') else minOps

        target = sum(nums) - x
        currSum = 0
        l = 0
        max_window_size = -1

        for r in range(len(nums)) :
            currSum += nums[r]

            while l <= r and currSum > target :
                currSum -= nums[l]
                l += 1

            if currSum == target :
                max_window_size = max(max_window_size, r - l + 1)
            
        return -1 if max_window_size == -1 else len(nums) - max_window_size
