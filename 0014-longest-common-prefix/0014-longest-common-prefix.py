class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        result = ''

        length = min([len(s) for s in strs])

        for idx in range(length) :
          if len(set([s[idx] for s in strs])) == 1 :
            result += strs[0][idx]
          else :
            break
        return result