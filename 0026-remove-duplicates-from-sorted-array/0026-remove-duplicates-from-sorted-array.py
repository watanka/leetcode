class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
    
        k = 1
        i = 1
        lastSeen = nums[0]
        
        while i < len(nums) :
            if nums[i] != lastSeen :
                nums[k] = nums[i]
                lastSeen = nums[i]
                k += 1

            i += 1
        
        change_idx = k 
        while change_idx < len(nums) :
            nums[change_idx] = '_'
            change_idx += 1

        return k
            