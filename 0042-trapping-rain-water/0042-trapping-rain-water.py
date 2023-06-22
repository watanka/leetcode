class Solution:
    def trap(self, height: List[int]) -> int:
        # max height of left block and max height of right block

        maxheight_left_list = [0 for _ in range(len(height))]
        maxheight_left = 0
        for i in range(len(height)) :
            maxheight_left = max(height[i], maxheight_left)
            maxheight_left_list[i] = maxheight_left

        maxheight_right_list = [0 for _ in range(len(height))]
        maxheight_right = 0
        for i in range(len(height)-1, -1, -1) :
            maxheight_right = max(height[i], maxheight_right)
            maxheight_right_list[i] = maxheight_right

        # print(maxheight_left_list)
        # print(maxheight_right_list)
        result = 0
        for i in range(len(height)) :
            result += max(0, min(maxheight_right_list[i], maxheight_left_list[i]) - height[i])      
        
        return result

        

        
