class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 :
            return s

        i = 0
        result = ''

        numIter = numRows + numRows - 2 

        while i < len(s) :

            trg_idx = i % numIter

            if trg_idx % numIter < numRows :
                result += s[i]
                i += 1

            else : 
                for numSpace in range(numRows - 2, 0, -1) :
                    result += ' ' * numSpace + s[i] + ' ' * (numRows - numSpace - 1)
                    i += 1
                    if i >= len(s) :
                        break

        numCols = (len(result) // numRows) + (1 if len(result) % numRows else 0)
        
        str_list = [[''] * numCols for _ in range(numRows)]

        idx = 0
        for i in range(numCols) : 
            for j in range(numRows) :
                if idx >= len(result) :
                    break
                if result[idx] != ' ' :
                    str_list[j][i] = result[idx] 
                idx += 1
            if idx >= len(result) :
                    break

        return ''.join([''.join(strvalue) for strvalue in str_list])

