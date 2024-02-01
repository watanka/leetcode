class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1 :
            return [0]

        # original = [10, 4, 8, 3]
        # leftSum  = [0, 10, 10+4, 10+4+8]
        # rightSum = [4+8+3, 8+3, 3, 0]
        # |leftSum - rightSum| = [(0) - (4+8+3), (10) - (8+3), (10+4) - (3), (10+4+8) - 0]
        # [15, 1, 11, 22]

        answer = []
        rightSum = sum(nums)
        leftSum = 0
        
        for idx in range(len(nums)):
            rightSum -= nums[idx]
            answer.append(abs(leftSum - rightSum))
            leftSum += nums[idx]

        return answer

        # sumVal = 0
        # leftSum = [sumVal]
        # for i in range(len(nums)-1):
        #     sumVal += nums[i]
        #     leftSum.append(sumVal)

        # sumVal = 0
        # rightSum = [sumVal]
        # for i in range(len(nums)-1, 0, -1):
        #     sumVal += nums[i]
        #     rightSum.append(sumVal)
        # rightSum = rightSum[::-1]
        
        # answer = []
        # for idx in range(len(nums)):
        #     answer.append(abs(leftSum[idx] - rightSum[idx]))

        # return answer

