class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, num in enumerate(nums) :
            if num not in num_dict :
                num_dict[num] = i
            else :
                # only one valid answer exists means there are maximum 2 same numbers.
                num_dict[num] = [num_dict[num], i]

        nums.sort()
        l, r = 0, len(nums) - 1


        while l < r :
            currSum = nums[l] + nums[r]
            if currSum == target :
                if nums[l] == nums[r] :
                    return num_dict[nums[l]]
                else :
                    return num_dict[nums[l]], num_dict[nums[r]]
            elif currSum < target :
                l += 1
            else : 
                r -= 1

        return 

        