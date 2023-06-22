class Solution:
    def trap(self, height: List[int]) -> int:
        # max height of left block and max height of right block

        upp, res = 0, 0

        l = 0 
        r = len(height) - 1

        while l < r :
            low = min(height[l], height[r])
            if height[l] < height[r] :
                l += 1
            else :
                r -= 1
            upp = max(upp, low)
            res += (upp - low)
        
        return res

