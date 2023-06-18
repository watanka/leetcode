class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = [1 for _ in range(length)]

        prefix = 1
        postfix = 1

        for i in range(length) :
            output[i] *= prefix
            prefix *= nums[i]
            output[length - i - 1] *= postfix 
            postfix *= nums[length - i - 1]

        return output

