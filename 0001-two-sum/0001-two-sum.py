class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for l in range(len(nums) - 1) :
            left = nums[l]
            for r in range(l+1, len(nums)) :
                right = nums[r]

                if left + right == target :
                    return [l, r]