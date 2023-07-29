class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        numstack = []

        answer = None
        if len(tokens) == 1 :
            return int(tokens[0])

        for token in tokens :
            if token.replace('-', '').isnumeric() :
                numstack.append(token)
            else :
                x = numstack.pop()
                y = numstack.pop()
                
                answer = int(eval( f'({y}){token}({x})' ) )
                numstack.append(answer)
            
        
        return answer