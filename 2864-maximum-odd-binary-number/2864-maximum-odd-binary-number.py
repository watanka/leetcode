class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # 맨 오른쪽 값은 항상 1이여야함
        cnt_one = s.count('1')
        
        return (cnt_one - 1) * '1' + (len(s) - cnt_one) * '0' + '1'