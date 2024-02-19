class Solution:
    def align(self, long, short):
        total_length = len(long) + len(short)
        result = '' * total_length
        for idx in range(total_length):
            if idx % 2 == 0:
                result += long[idx // 2]
            else:
                result += short[(idx-1) // 2]
        return result

    
    def reformat(self, s: str) -> str:
        
        # print(sorted(s))

        alphabets, numbers = [], []
        # 알파벳, 숫자 구분짓고
        for chr in s:
            if chr.isalpha():
                alphabets.append(chr)
            else:
                numbers.append(chr)
        
        # 하나씩 배열
        len_alpha, len_nums = len(alphabets), len(numbers)

        num_diff = len_alpha - len_nums
        
        if abs(num_diff) > 1:
            return ''
        else:
            if num_diff >= 0:
                return self.align(alphabets, numbers)
            else:
                return self.align(numbers, alphabets)
            
        