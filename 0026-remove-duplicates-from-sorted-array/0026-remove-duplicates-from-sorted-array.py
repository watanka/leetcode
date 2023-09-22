class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
    
        k = 1
        i = 1
        while i < len(nums) :
            if nums[i] != nums[i-1] :
                nums[k] = nums[i]
                
                k += 1

            i += 1
        
        # change_idx = k 
        # while change_idx < len(nums) :
        #     nums[change_idx] = '_'
        #     change_idx += 1

        return k
            

    
        # count = 1
        # for i in range(1, len(nums)):
        #   if nums[i] != nums[i-1]:
        #     nums[count] = nums[i]
        #     count += 1
        # arr = [int(x) for x in set(nums)]
        # print(len(arr))
        # print(count)
        return len(arr)