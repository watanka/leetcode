class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        # x = 2, n = 10 => (2 ** 5) * (2 ** 5) => ((2 ** 2) * (2 ** 2) * 2) * ((2 ** 2) * (2 ** 2) * 2)


        # while n > 0 :
        #     x ** 2
        #     n //= 2

        return x ** n
        