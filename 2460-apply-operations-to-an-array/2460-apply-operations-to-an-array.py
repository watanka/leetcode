class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        for i in range(len(nums) - 1) :
            if nums[i] == nums[i+1] :
                nums[i] *= 2
                nums[i+1] = 0
        
        # 0을 오른쪽으로 다 옮기기
        # for left in range(len(nums)) :
        #     if nums[left] != 0 :
        #         continue
        #     for right in range(left+1, len(nums)) :
        #         if nums[right] != 0 :
        #             nums[right], nums[left] = nums[left], nums[right]
        #             break
        zero_cnt = 0
        new_list = []
        for i in range(len(nums)) :
            if nums[i] != 0 :
                new_list.append(nums[i])        
            else :
                zero_cnt += 1
            
        return new_list + [0] * zero_cnt
                

            

        return nums
                

                


        