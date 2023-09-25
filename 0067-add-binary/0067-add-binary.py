class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        # approaches.
        # 1. bin -> decimal -> bin
        # 2. bin -> bin

        # 2. bin -> bin
        # up = 0
        # length = max(len(a), len(b))
        # 짧은 string의 값을 0으로 채움
        # for idx in range( length - 1, -1, -1 ))
        # up, val = binsum(letter_a, letter_b). up = 1 if letter_a = 1, letter_b = 1

        # def binsum(letterA : int, letterB : int, up : int) -> tuple[str, str] :
        #     sumVal = letterA + letterB + up
        #     if sumVal == 1 :
        #         return '1', '0' # val, up
        #     elif sumVal == 2 :
        #         return '0', '1'
        #     elif sumVal == 3 :
        #         return '1', '1'
        #     elif sumVal == 0: 
        #         return '0', '0'

        

        # length = max(len(a), len(b))
        # # a = '100', b = '1' => a = '100', b = '001'
        # if length - len(a) :
        #     a = '0' * (length - len(a)) + a 
        # else :
        #     b = '0' * (length - len(b)) + b

        # result = ''
        # up = '0'
        # for idx in range(length - 1, -1, -1 ) :
        #     val, up = binsum(int(a[idx]), int(b[idx]), int(up))
        #     result = val + result
        # if up == '1' : 
        #     result = up + result

        # return result

        return bin(int(a, base = 2) + int(b, base = 2))[2:]
