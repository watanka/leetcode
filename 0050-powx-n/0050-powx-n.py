class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        # x = 2, n = 10 => (2 ** 5) * (2 ** 5) => ((2 ** 2) * (2 ** 2) * 2) * ((2 ** 2) * (2 ** 2) * 2)

        # 10 // 2 = 5, 2 ** 2 = 4
        # 5 // 2 = 2, 4 ** 2 = 16
        # 3 // 2 = 1, 16 ** 2 = 256



        # x = 3, n = 5
        # 5 // 2 = 2, 3 ** 2 = 9
        # 3 // 2 = 1, 9 ** 2 = 81

        # 81 * 3 = 243

        neg = n < 0
        n = abs(n)

        ans = 1
        while n > 0 :
            if n % 2 == 0 :
                x = x * x
                n //= 2
            else :
                ans *= x
                n -= 1
        
        return 1 / ans if neg else ans