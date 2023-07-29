class Solution:
    def evalRPN(self, tokens: List[str]) -> int: 
        if len(tokens) == 1 :
            return int(tokens[0])
        
        numstack = []

        for token in tokens :
            if token in ['+', '-', '*', '/'] :
                x = numstack.pop()
                y = numstack.pop()
                
                # answer = int(eval( f'({y}){token}({x})' ) )
                if token == '+' :
                    answer = int(y) + int(x)
                elif token == '-' :
                    answer = int(y) - int(x)
                elif token == '*' :
                    answer = int(y) * int(x)
                elif token == '/' :
                    answer = int(int(y) / int(x))

                numstack.append(answer)
            
            else :
                numstack.append(token)
        
        return answer