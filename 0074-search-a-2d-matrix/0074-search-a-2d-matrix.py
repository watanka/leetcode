class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first select which row target would fit into..
        # check only first and last element of the row

        def binary_search(ls) :
            l, r = 0, len(ls) - 1
            while l <= r :
                mid = (l + r) // 2
                if ls[mid] > target :
                    r = mid - 1
                elif ls[mid] < target :
                    l = mid + 1
                else :
                    return True
            return False


        m, n = len(matrix), len(matrix[0])
        for row_idx in range(m) : 
            selected_row = matrix[row_idx]

            if selected_row[0] <= target <= selected_row[-1] :
                if binary_search(selected_row) :
                    return True
        return False