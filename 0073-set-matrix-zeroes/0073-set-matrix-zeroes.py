class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        nrow, ncol = len(matrix), len(matrix[0])

        zeros = []
        for row in range(nrow) :
            for col in range(ncol) :
                if matrix[row][col] == 0 :
                    zeros.append((row, col))

        for row_idx, col_idx in zeros :
            matrix[row_idx] = [0 for _ in range(ncol)]
            for row in range(nrow) :
                matrix[row][col_idx] = 0

        
            
