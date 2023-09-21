class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False

        originalnum = x
        revnum = 0

        while x > 0 :
            revnum = revnum * 10 + x % 10
            x //= 10

        return originalnum == revnum