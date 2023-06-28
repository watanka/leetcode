import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        allowed = 'abcdefghijklmnopqrstuvwxyz0123456789'
        s = [letter.lower() for letter in s if letter.lower() in allowed]

        num_iter = len(s) // 2

        start, end = 0, len(s) - 1

        for _ in range(num_iter) :
            if s[start] != s[end] :
                return False
            else :
                start += 1
                end -= 1

        return True


