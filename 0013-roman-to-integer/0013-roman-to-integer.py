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
        total = 0
        for i in range(len(s)) :
            if i+1 < len(s) and symbol_dict[s[i]] < symbol_dict[s[i+1]] : # num_now and num_next is a combination num_now - num_next
                total -= symbol_dict[s[i]]
            else :
                total += symbol_dict[s[i]]
        
        return total

        
            
