class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # naive approach. [1, 2, 3]  -> 123 -> 123 + 1 = 124 -> [1,2,4]
        
        # 2nd approach
        # list[-1] + 1 => 10 이상인 경우, 또는 10 이하인 경우
        # 10이상인 경우 list[-2] += 1, list[-1] += 1 => # [9] -> [1,0]
        # 10이하인 경우 => list[-1] += 1

        # [9, 9, 9] => expected [1, 0, 0, 0] 
        # 

        
        square = 0
        integer = 0
        for i in range(len(digits) - 1, -1, -1) :
            integer += digits[i] * (10 ** square)
            square += 1

        integer += 1

        return list(map(int, str(integer)))


