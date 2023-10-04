class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtracking(n_open, n_close, comb) : 
            if n_open == n_close == n :
               
                result.append(comb)
                return


            for pthsis in [0, 1] : # put write ( or ).[open, close]
                if pthsis == 0 and n_open < n :
                    backtracking(n_open + 1, n_close, comb + '(')
                elif pthsis == 1 and n_close < n_open :
                    backtracking(n_open, n_close + 1, comb + ')')

        backtracking(0, 0, '')

        return result