class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if s is '' :
            return True

        j = 0
        for i in range(len(t)) :
            if j < len(s) :
                if t[i] == s[j] :
                    j += 1
            else :
                break
                
        return j == len(s)