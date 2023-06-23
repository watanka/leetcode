class Solution:
    def romanToInt(self, s: str) -> int :
        
        symbol_dict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        if len(s) == 1 :
            return symbol_dict[s]

        total = 0 
        i = 0 
        while i < len(s) :
            num1, num2 = symbol_dict[s[i]], symbol_dict[s[i+1]]
            if num1 < num2 :
                total += (num2 - num1)
                i += 2
            else :
                total += num1
                i += 1
            if i == len(s)-1 :
                total += symbol_dict[s[i]]
                break
        
        return total

        
            
