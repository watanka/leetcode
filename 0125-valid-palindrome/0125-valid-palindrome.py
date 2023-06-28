import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        allowed = 'abcdefghijklmnopqrstuvwxyz0123456789'
        s = [letter.lower() for letter in s if letter.lower() in allowed]

        return s == s[::-1]

