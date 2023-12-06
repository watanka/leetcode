class Solution:
    def areNumbersAscending(self, s: str) -> bool:

        is_increasing = True
        
        print([int(letter) for letter in s.split(' ') if not letter.isalpha()])
        prev_num = None
        for letter in s.split(' ') :
            if not letter.isalpha() :
                if not prev_num :
                    prev_num = int(letter)
                else :
                    if prev_num >= int(letter) :
                        return False
                    else :
                        prev_num = int(letter)

        return is_increasing

        
        