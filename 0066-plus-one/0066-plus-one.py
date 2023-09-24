class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # naive approach. [1, 2, 3]  -> 123 -> 123 + 1 = 124 -> [1,2,4]
        
        # 2nd approach
        # list[-1] + 1 => 10 이상인 경우, 또는 10 이하인 경우
        # 10이상인 경우 list[-2] += 1, list[-1] += 1 => # [9] -> [1,0]
        # 10이하인 경우 => list[-1] += 1

        # [9, 9, 9] => expected [1, 0, 0, 0] 
        # 
        up = 0
        result = [0 for _ in range(len(digits))]
        for i in range(len(digits) - 1, -1, -1) :
            if i == len(digits) - 1 :
                num = digits[i] + 1
            else :
                num = digits[i]
            if up :
                num += up
            new_num, up = num % 10, num // 10
            result[i] = new_num
        if up :
            result = [up] + result

        return result



