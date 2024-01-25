class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        initSum = sum(nums[:k])
        maxVal = initSum
        for i in range(k, len(nums)):
            initSum += nums[i] - nums[i-k]
            maxVal = max(maxVal, initSum)

        maxVal /= k

        return maxVal