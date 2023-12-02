class Solution:
    def maxPower(self, s: str) -> int:
        
        lastchar = None
        maxlength = 1
        
        for char in s :
            if not lastchar or lastchar != char :
                lastchar = char
                length = 1
            else :
                length += 1
                maxlength = max(maxlength, length)
        
        return maxlength
                