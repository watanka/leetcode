class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxHeight=0

        gainHeight=0
        for g in gain:
            gainHeight += g
            maxHeight=max(maxHeight, gainHeight)

        return maxHeight