class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for i, n in enumerate(nums) :
            if n not in nums_dict :
                nums_dict[target - n] = i
            else :
                return [i, nums_dict[n]]
