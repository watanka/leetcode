class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        x = abs(x)
        val = x

        length = 1
        num_ls = []
        while True :
            remainder = val % 10
            num_ls.append(remainder)
            val //= 10
            
            if val > 0 :
                length += 1
            else :
                break
        length = len(num_ls)
        print(length)
        for idx in range(length // 2) :
            # 양쪽 끝에서부터 빼기
            print('---')
            print(idx)
            leftval = x // (10 ** (length - 1 - idx))
            rightval = (x % (10 ** (idx+1))) // (10 ** idx)
            print(leftval)
            print(rightval )
        
            if leftval != rightval :
                return False
            
            x -= leftval * (10 ** (length - 1- idx))
            print('after minus leftval', x)
            x -= rightval * (10 ** idx)
            print('after minus rightval', x)
        
        return True
        