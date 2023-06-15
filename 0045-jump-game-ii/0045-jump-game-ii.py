class Solution:
    def jump(self, nums: List[int]) -> int:
        idx = 0
        result = 0
        target = len(nums) - 1

        while idx < target :
            if nums[idx] + idx >= target :
                result += 1
                break

            greedy_idx, greedy_value = None, 0
            for i in range(idx + 1, min(idx + nums[idx] + 1, target)) :
                val = nums[i] + i

                if val > greedy_value :
                    greedy_value = val
                    greedy_idx = i

            idx = greedy_idx
            result += 1

        return result


            


            


        