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

        combinations = []
        for digit in digits :
          combinations.append(phone_dict[digit])

        
        result = []
        def dfs(stack) :
          if len(stack) == len(digits) :
            
            result.append(''.join(stack))
            return

          for letter in combinations[len(stack)] :
            stack.append(letter)
            dfs(stack)
            stack.pop()
            
        dfs([])

        return result

          

          
