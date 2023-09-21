class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str : 
      if len(strs) == 1 :
        return strs[0]
      
      strs.sort()
      result = ''
      end = min(len(strs[0]), len(strs[-1]))

      i = 0
      while i < end and strs[0][i] == strs[-1][i] :
        result += strs[0][i]
        i += 1

      return result
