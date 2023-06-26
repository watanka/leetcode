class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 :
            return s

        freq = numRows + numRows - 2

        num_segs = len(s) // freq + (1 if len(s) % freq else 0)

        segments = [ s[freq * i :  min(len(s), freq * (i + 1))] \
                                for i in range(num_segs)]

        zigzag = [''] * numRows

        for seg in segments :
            for i in range(len(seg)) : 
                
                if i % freq < numRows :
                    zigzag[i] += seg[i]
                else :
                    zigzag[freq - i] += seg[i]

        return ''.join(zigzag)
                