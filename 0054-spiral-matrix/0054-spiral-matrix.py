class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        m = len(matrix)
        n = len(matrix[0])

        row_sign = 1
        col_sign = 1

        top = 0
        bottom = m - 1
        left = 0
        right = n - 1
        
        cur_row, cur_col = 0, 0

        answer = []
        while left <= right and bottom >= top :
            if row_sign == 1 :
                for idx in range(left, right + 1) :
                    answer.append(matrix[top][idx])
                top += 1
                row_sign *= -1

            elif row_sign == -1 :
                for idx in range(right, left - 1, -1) :
                    answer.append(matrix[bottom][idx])
                bottom -= 1
                row_sign *= -1
                
            if col_sign == 1 :
                for idx in range(top, bottom + 1) :
                    answer.append(matrix[idx][right])
                right -= 1
                col_sign *= -1 

            elif col_sign == -1 :
                for idx in range(bottom, top - 1, -1) :

                    answer.append(matrix[idx][left])
                left += 1
                col_sign *= -1
        return answer