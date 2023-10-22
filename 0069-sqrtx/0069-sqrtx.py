class Solution:
    def mySqrt(self, x: int) -> int:

        # 1 = 1
        # 2 = 4
        # 3 = 9
        # 4 = 16
        # 5 = 25
        # 6 = 36
        # 7 = 49
        # 8 = 64


        # 1 = {1, 2, 3} = #3 
        # 2 = {4, 5, 6, 7, 8} = #5
        # 3 = {9, 10, 11, 12, 13, 14, 15} = #7
        # 4 = {16, 17, 18, 19, 20, 21, 22, 23, 24} = #9


        sqrt = 0
        sub = 3
        while x > 0:
            x -= sub
            sub += 2
            sqrt += 1
        
        return sqrt