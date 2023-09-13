class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits) == 0 :
          return []
        phone_dict = {
                      '2' : 'abc', 
                      '3' : 'def', 
                      '4' : 'ghi',
                      '5' : 'jkl', 
                      '6' : 'mno', 
                      '7' : 'pqrs', 
                      '8' : 'tuv', 
                      '9' : 'wxyz'
                    }

        result = []

        def dfs(stack) :
          if len(stack) == len(digits) :    
            result.append(''.join(stack))
            return

          for letter in phone_dict[digits[len(stack)]] :
            stack.append(letter)
            dfs(stack)
            stack.pop()
            
        dfs([])

        return result

          

          
