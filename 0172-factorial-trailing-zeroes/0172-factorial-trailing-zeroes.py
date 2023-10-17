class Solution:
    def trailingZeroes(self, n: int) -> int:
        '''
        n = 0, 0! = 0         1
        n = 1, 1! = 1         0
        n = 2, 2! = 2         0
        n = 3, 3! = 6         0
        n = 4, 4! = 24        0
        n = 5, 5! = 120       1
        n = 6, 6! = 720       1
        n = 7, 7! = 5040      1
        n = 8, 8! = 40320     1
        n = 9, 9! = 362880    1
        n = 10, 10! = 3628800 2
        how many 10 in the value => there are enough of 2 compared to 5. => how many 5s?
        '''
        zeros = 0

        while n > 0 :
            n //= 5
            zeros += n
        return zeros