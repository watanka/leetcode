class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        # validate row-wise
        for col in range(9) : 
            num_set = [str(i) for i in range(1, 10)]
            for row in range(9) :
                if board[col][row] in num_set :
                    num_set.remove(board[col][row])
                elif board[col][row] == '.' :
                    continue
                else :
                    # print('row', board[col][row])
                    return False

        # validate column-wise
        for row in range(9) : 
            num_set = [str(i) for i in range(1, 10)]
            for col in range(9) :
                if board[col][row] in num_set :
                    num_set.remove(board[col][row])
                elif board[col][row] == '.' :
                    continue
                else :
                    # print('col', board[col][row])
                    return False
        
        # validate 3x3 sub-boxes
        for blck_row in range(3) :
            for blck_col in range(3) :
                num_set = [str(i) for i in range(1, 10)]
                for j in range(3) :
                    for k in range(3) :
                        
                        if board[blck_row * 3 + j][blck_col * 3 + k] in num_set :
                            num_set.remove(board[blck_row * 3 + j][blck_col * 3 + k])
                        elif board[blck_row * 3 + j][blck_col * 3 + k] == '.' :
                            continue
                        else :
                            # print('3x3', board[blck_row * 3 + j][blck_col * 3 + k])
                            return False

        return True

                