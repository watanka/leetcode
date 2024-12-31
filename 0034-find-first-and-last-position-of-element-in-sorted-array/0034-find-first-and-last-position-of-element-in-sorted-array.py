class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]

        def binary_search_range(nums, target, is_searching_left):
            left, right = 0, len(nums)-1
            idx = -1

            while left <= right:
                mid = left + (right-left) // 2

                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    idx = mid
                    if is_searching_left:
                        right = mid - 1
                    else:
                        left = mid + 1

            return idx

        start = binary_search_range(nums, target, True)
        end = binary_search_range(nums, target, False)

        return [start, end]
            
        
        
 